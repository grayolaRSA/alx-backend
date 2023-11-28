const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account'
};

const notificationJob = queue.create('push_notification_code', jobData);

notificationJob.on('enqueue', () => {
    console.log(`Notification job created: ${notificationJob.id}`);
});

// push_notification_code.process(JOB_ID, (err, push_notification_code) => {
//     if (err) {
//     console.error('Notification job failed');
//     } else {
//         console.log('Notification job completed');
//     }
// });

notificationJob.on('complete', () => {
    console.log('Notification job completed');
});

notificationJob.on('failed', () => {
    console.log('Notification job failed');
});

notificationJob.save();

// Exit gracefully when the job is completed or failed
queue.process('push_notification_code', (job, done) => {
    // Simulate a successful job completion
    // In a real scenario, you would perform the actual work here
    console.log(`Processing job ${job.id}`);
    done();
  });
  
  // Gracefully shut down the queue when the process is terminated
  process.on('SIGTERM', () => {
    queue.shutdown(5000, (err) => {
      console.log('Kue shutdown: ', err || '');
      process.exit(0);
    });
  });

  module.exports = notificationJob;