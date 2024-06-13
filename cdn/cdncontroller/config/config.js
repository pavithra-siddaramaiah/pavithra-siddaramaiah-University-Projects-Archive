'use strict'

let devConfig = {
    db: 'cdndb',
    websiteURL: 'https://localhost:3002',
    edgeServerLoc: [
        {zone: 'Mumbai', la: 19.07, lo: 72.877426, url: '../edgeservers/', bucket: 'e1-server'},
        {zone: 'London', la: 51.50, lo: -0.12, url: '../edgeservers/', bucket: 'e2-server'},
        {zone: 'Sao Paulo', la: -23.53, lo: -46.62, url: '../edgeservers/', bucket: 'e3-server'}
    ]
}

module.exports = devConfig;