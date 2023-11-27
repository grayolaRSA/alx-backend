const Redis = require('ioredis');
const redis = new Redis();

if (redis) {
    console.log('Redis client connected to the server');
} else {
    console.log('Redis client not connected to the server: ERROR_MESSAGE');
}

redis.quit();


module.exports = redis;