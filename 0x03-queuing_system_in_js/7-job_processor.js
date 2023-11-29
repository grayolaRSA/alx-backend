const kue = require('kue');
const queue = kue.createQueue();

const blackListed = ['4153518780', '4153518781'];


const sendNotification = (phoneNumber, message, job, done) => {

  // const jobProgress = queue.create('push_notification_code_2', {phoneNumber, message}).progress(0, 100);
  job.progress(0, 100);

  if (blackListed.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    // Fail the job with an error message
    done(new Error(errorMessage));
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    setTimeout(() => {
      job.progress(100, 100);
      done();
    }, 1000);
  }
}

 queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
  });