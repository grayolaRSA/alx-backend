const util = require('util');
const redis = require('redis');

const client = redis.createClient();

// Assuming you have a Redis client named 'client'
const asyncGet = util.promisify(client.get).bind(client);
const asyncSet = util.promisify(client.set).bind(client);


client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server: ERROR_MESSAGE');
});

// async function setNewSchool(schoolName, value) {
//     await asyncSet(schoolName, value);
//     console.log('values set for key-value pair!');
// }

async function setNewSchool(schoolName, value) {
    // client.set(`${schoolName}`, `${value}`, redis.print);
    // redis.print('key-value pair set!');
    try {
        asyncSet(schoolName, value).then(redis.print);
    } catch (error) {
        console.error(`Error: ${error}`)
    }
}

    
async function displaySchoolValue(schoolName) {    
    try {
        const value = await asyncGet(schoolName);
        console.log(`${value}`);
    } catch (error) {
        console.error(`Error retrieving value for ${schoolName}: ${error}`);
    }
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
client.quit();


// module.exports = redis;