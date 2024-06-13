'use strict'
let geoip = require('geoip-lite');
let cdnModel = require('../model/cdn.model');
let helper = require('../helper');
let config = require('../config/config');
let geolib = require('geolib');
const fs = require('fs');
let path = require('path');

let getNearestEdge = (lat, lon) => {
    let edgeServerLoc = config.edgeServerLoc;
    let min = edgeServerLoc[0];
    for(let i of edgeServerLoc){
        let dis = geolib.getPreciseDistance({latitude: i['la'], longitude: i['lo']}, {latitude: lat, longitude: lon});
        let mindis = geolib.getPreciseDistance({latitude: min['la'], longitude: min['lo']}, {latitude: lat, longitude: lon});
        if(dis < mindis){
            min = i;
        }
    }
    return min;
}

let getFileData = (nearestEdge, fileName) => {
    return new Promise(async (resolve, reject) => {
        let fileData = await cdnModel.findOne({zone: nearestEdge.zone, fileName: fileName});
        if(fileData){
            resolve(fileData);
        }
        else{
            resolve(null);
        }
    });
}

exports.checkContent = async (req, res, next) => {
    let fileName = req.url;
    fileName = fileName.slice(1);
    console.log(`Requested Content file ${fileName}`);
    // req.locals = {};
    let ip = (req.headers['x-forwarded-for'] || '').split(',').pop() || 
        req.connection.remoteAddress || 
        req.socket.remoteAddress || 
        req.connection.socket.remoteAddress;

        ip = '65.94.7.236'; // change this ip with any public IP India - 49.206.131.234 EU - 173.178.211.109

        console.log(`IP addess of client: ${ip}`);    
        if(ip){
        let geo;
        let nearestEdge;
        if(ip === '127.0.0.1'){
            nearestEdge = {zone: 'London', la: 51.50, lo: -0.12, url: '../edgeservers/', bucket: 'e2-server'};
        }
        else{
            // geo = geoip.lookup(ip);
            // nearestEdge = getNearestEdge(geo['ll'][0], geo['ll'][1]);
            nearestEdge = req.locals.nearestEdge;
            console.log(`nearestEdge ${nearestEdge}`)
        }
        console.log(`Edge Server as per round robin algo${nearestEdge.zone}`);
        let fileData = await getFileData(nearestEdge, fileName);
        if(fileData){
            if(!fileData.deleted){
                console.log('Requested file is available');
                req.locals.fileData = fileData;
                next();
            }
            else{
                console.log('Requested file is not available');
                console.log('res header1', res.headers)
                let uploadFile = await helper.storeFile(fileName, nearestEdge.bucket);
                if(uploadFile){
                    let fileData = await cdnModel.findOneAndUpdate({zone: nearestEdge.zone, fileName: fileName}, {deleted: false, updatedAt: new Date()}, {upsert: true, new: true});
                    req.locals.fileData = fileData;
                    console.log('File is fetched from server since it is deleted');
                    next();
                }   
                else{
                    res.status(500).jsonp({status: false, message: 'Internal Server Error'});
                }    
            }
        }
        else{
            console.log('File is fetched from server since it was not present');
            console.log(`nearestEdge.bucket ${nearestEdge.bucket}`)
            let uploadFile = await helper.storeFile(fileName, nearestEdge.bucket);
            if(uploadFile){
                let fileData = await cdnModel.create({website: config.websiteURL, zone: nearestEdge.zone, url: nearestEdge.url, fileName: fileName});
                req.locals.fileData = fileData;
                next();    
            }
            else{
                res.status(400).jsonp({status: false, message: 'Bad Request'});
            }    
        }
    }
    else{
        res.status(400).jsonp({status: false, message: 'Bad Request'});
    }
}

exports.getFile = (req, res) => {
    console.log(`${req.locals.fileData.fileName} is being served from ${req.locals.fileData.zone} edge server`);
    let fileName = req.locals.fileData.fileName;
    let contentType = helper.typeCheck(fileName)
    console.log(`fileName ${fileName}`)
    console.log(`contentType ${contentType}`)
    let url = req.locals.fileData.url;
    res.setHeader("Content-Type", contentType);
    res.headers = {"Content-Type": contentType}
    console.log(`res.headers ${JSON.stringify(res.headers)}`)
    setTimeout(() => {
        const bucket = helper.getEdgeServerBucket(req.locals.fileData.zone);
        const fileExt = fileName.split('/')[0];
        const serverDir = url + bucket + '/' + fileExt;
        const filePath = path.join(serverDir, fileName.split('/')[1]);
        const rs = fs.createReadStream(filePath);
        rs.pipe(res); 
    }, 2000);
}


exports.delete = (req, res, next) => {
    cdnModel.deleteMany({}, (err, data) => {
        if(err){
            console.log(`Error occurred while deleting all the cached data ${err}`);
            res.status(500).jsonp({message: 'Error occurred while deleting all the cached data', status: 'fail'});
        }
        else{
            console.log('Deleted all the cached data successfully');
            next();
        }
    });
}
