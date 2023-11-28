const kue = require('kue');
const queue = kue.createQueue();
// const notificationJob = require('./6-job_creator');

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// queue.on('job enqueue', (id, type) => {
//   for id === notificationJob.id;
//       if (type === 'notificationJob') {
//         sendNotification(notificationJob.phoneNumber, notificationJob.message);
//       }
//   }
// });

// Define a handler for processing jobs of type 'push_notification_code'
queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;
  
    // Call the sendNotification function with the phone number and message
    sendNotification(phoneNumber, message);
  
    // Mark the job as complete
    done();
  });
  
  // Gracefully shut down the queue when the process is terminated
  process.on('SIGTERM', () => {
    queue.shutdown(5000, (err) => {
      console.log('Kue shutdown: ', err || '');
      process.exit(0);
    });
  });