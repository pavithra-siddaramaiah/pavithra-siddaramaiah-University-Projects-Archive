'use strict';

let express = require('express');
let mongoose = require('mongoose');
let bodyParser = require('body-parser');
let cors = require('cors');
let cookieParser = require('cookie-parser');
let path = require('path');
let fs = require('fs');
let util = require('util');
const http2 = require("spdy")
const cron = require('node-cron');
const fse = require('fs-extra');

let commonsConfig = require('./config/config');
let cdnRoute = require('./routes/cdn.route');
let cdnController = require('./controller/cdn.controller');
let helper = require('./helper');
let dbPath = "mongodb://127.0.0.1/" + commonsConfig.db;
mongoose.connect(dbPath,{ useNewUrlParser: true, useUnifiedTopology: true });

let accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), {flags : 'a'});
let logStdout = process.stdout;
console.log = function(d) { 
    accessLogStream.write(util.format(d) + '\n');
    logStdout.write(util.format(d) + '\n');
};

let app = express();

app.use(cors());
app.use(cookieParser());
app.use(bodyParser.urlencoded({ extended: true, limit: '50mb' }));
app.use(bodyParser.json({ extended: true, limit: '50mb' }));

app.use('/', cdnRoute);

app.get('/reset',
    (req, res, next) => {
        fs.writeFileSync(path.join(__dirname, 'access.log'), '');
        next();
    },
    cdnController.delete,
    helper.deleteFiles
);

app.get('/fulllogs', 
    (req, res) => {
        let read = fs.createReadStream(path.join(__dirname, 'access.log'));
        read.pipe(res);
    }
);

cron.schedule('*/10 * * * * *', () =>  {
  const buckets = [commonsConfig.edgeServerLoc[0].bucket, commonsConfig.edgeServerLoc[1].bucket, commonsConfig.edgeServerLoc[2].bucket];
  const emptyDir = [];
  let src;
  for(let i=0; i<buckets.length; i++){
    if(isEmpty(buckets[i])){
      emptyDir.push(i);
    }
    else{
      src = i;
    }
  }
  for(let d of emptyDir) {
    let srcDir = path.join('../edgeservers/', buckets[src]);
    let destDir = path.join('../edgeservers/', buckets[d]);
    fse.copy(srcDir, destDir, {recursive: true} ,function (err) {
      if (err) return console.error(err)
    });
  }
});

http2.createServer(
    {
      key: fs.readFileSync("./server.key"),
      cert: fs.readFileSync("./server.crt")
    },
    app
  ).listen(3001, (err) => {
    if(err){
      throw new Error(err)
    }
    console.log("CDN controller running on port 3001")
})


function isEmpty(pathVal) {
  pathVal = path.join('../edgeservers/', pathVal);
  return fs.readdirSync(pathVal).length === 0;
}
  
