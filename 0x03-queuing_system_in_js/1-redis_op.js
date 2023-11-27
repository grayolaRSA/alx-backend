const Redis = require('ioredis');
const redis = new Redis();

if (redis) {
    console.log('Redis client connected to the server');
} else {
    console.log('Redis client not connected to the server: ERROR_MESSAGE');
}

export function setNewSchool(schoolName, value) {
    redis.set(`${schoolName}`, `${value}`).then(redis.print);
    // redis.print('key-value pair set!');
}
    
export function displaySchoolValue(schoolName) {
    redis.get(`${schoolName}`).then(value => {
        console.log(value);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

redis.quit();
// module.exports = redis;