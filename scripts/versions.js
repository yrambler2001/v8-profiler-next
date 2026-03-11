'use strict';

const os = require('os');

exports.os7u = [
  'node-v17.9.1',
];

if (os.platform() === 'darwin' && os.arch() === 'arm64') {
  exports.os7u = exports.os7u.slice(2);
}

exports.os8u = [
  'node-v18.19.0',
  'node-v19.9.0',
  'node-v20.10.0',
  'node-v21.5.0',
  'node-v22.12.0',
  'node-v24.14.0',
];
