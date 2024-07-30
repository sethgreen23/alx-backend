import { createClient } from 'redis';

// async function connectRedis() {
// 	const client = await createClient()
// .on('connect', () => console.log('Redis client connected to the server'))
// .on('error', (err) => console.log('Redis client not connected to the server: ' + err));
// }

// connectRedis();

const client = createClient()
.on('connect', () => console.log('Redis client connected to the server'))
.on('error', (err) => console.log('Redis client not connected to the server: ' + err));

