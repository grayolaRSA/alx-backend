const kue = require('kue');
const queues = kue.createQueue();

// const jobs = [];

const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    for (const job of jobs) {    

        queue = queues;
        const notificationCode = queue.create('push_notification_code_3', { phoneNumber: job.phoneNumber, message: job.message });

        notificationCode.on('enqueue', () => {
            console.log(`Notification job created: ${notificationCode.id}`);
        });

        notificationCode.on('complete', () => {
            console.log(`Notification job ${notificationCode.id} completed`);
        });

        notificationCode.on('failed', (error) => {
            console.log(`Notification job ${notificationCode.id} failed: ${error}`);
        });

        notificationCode.on('progress', (progress) => {
            console.log(`Notification job ${notificationCode.id} ${progress}% complete`);
        });

        // Save the job to the queue
        notificationCode.save();
    }
}

module.exports = createPushNotificationsJobs;
// createPushNotificationsJobs(jobs);
