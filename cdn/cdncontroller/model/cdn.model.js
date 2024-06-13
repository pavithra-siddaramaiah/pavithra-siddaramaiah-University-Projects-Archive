'use strict'

let mongoose = require('mongoose');
let Schema = mongoose.Schema;

let cdnSchema = new Schema({
    website: String,
    zone: String,
    url: String,
    fileName: String,
    deleted: {type: Boolean, default: false},
    createdAt: {type: Date, default: new Date()},
    updatedAt: Date
});

let cdns = mongoose.model('cdns', cdnSchema);

module.exports = cdns;