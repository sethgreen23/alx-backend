function createPushNotificationsJobs(jobs, queue) {
	if (!Array.isArray(jobs))
		throw new Error('Jobs must be an array');
	jobs.forEach((jobObject) => {
		let job = queue.create('push_notification_code_3', jobObject).save((err) => {
			if (!err) {
				console.log(`Notification job created: ${job.id}`);
			}
		});
		job.on('complete', (result) => {
			console.log(`Notification job ${job.id} completed`);
		}).on('failed', (err) => {
			console.log(`Notification job ${job.id} failed: ${err}`);
		}).on('progress', (progress, data) => {
			console.log(`Notification job ${job.id} ${progress}% complete`);
		})
	});
}

module.exports = createPushNotificationsJobs;
