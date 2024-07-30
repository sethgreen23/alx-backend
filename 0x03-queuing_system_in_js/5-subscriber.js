import { createClient } from 'redis';

const subscriber = createClient()
.on('connect', () => console.log('Redis client connected to the server'))
.on('error', (err) => console.log('Redis client not connected to the server: ' + err));

const chan = 'holberton school channel';
subscriber.subscribe(chan);
subscriber.on('message', (channel, message) =>{
	if (message === 'KILL_SERVER' && channel === chan) {
		console.log(message);
		subscriber.unsubscribe(chan);
		subscriber.quit();
	} else if(channel === chan) {
		console.log(message);
	}
});
