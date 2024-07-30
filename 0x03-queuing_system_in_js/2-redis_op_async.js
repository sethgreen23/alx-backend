import { createClient, print } from 'redis';
import { promisify } from 'util';


const client = createClient()
.on('connect', () => console.log('Redis client connected to the server'))
.on('error', (err) => console.log('Redis client not connected to the server: ' + err));

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
	const getAsync = promisify(client.get).bind(client);
	try{
		const reply = await getAsync(schoolName);
		console.log(reply);
	}catch(error){
		console.log(error);
	}
}

async function mainActions() {
	await displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	await displaySchoolValue('HolbertonSanFrancisco');
}

mainActions();
