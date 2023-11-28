const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

const kue = require('kue');
const queue = kue.createQueue();

let totalJobs = 0;
let completedJobs = 0;

function updatePercentage() {
    // Track the total number of jobs and the number of completed jobs
    const percentage = totalJobs > 0 ? ((completedJobs / totalJobs) * 100).toFixed(2) : 0;
}

function jobCreate(jobs) {

  
    for (const job of jobs) {
      const notificationJob = queue.create('push_notification_code_2', {phoneNumber: job.phoneNumber, message: job.message});
      notificationJob.on('enqueue', () => {
      console.log(`Notification job created: ${notificationJob.id}`);
      totalJobs++;
      updatePercentage();
      });
  
  // push_notification_code.process(JOB_ID, (err, push_notification_code) => {
  //     if (err) {
  //     console.error('Notification job failed');
  //     } else {
  //         console.log('Notification job completed');
  //     }
  // });
  
      notificationJob.on('complete', () => {
          console.log(`Notification job ${notificationJob.id} completed`);
          totalJobs++;
          updatePercentage();
          console.log(`Notification job ${notificationJob.id} ${updatePercentage.percentage}% complete`);
      });
  
      notificationJob.on('failed', (error) => {
          console.error(`Notification job ${notificationJob.id}  failed: ${error}`);
      });

      notificationJob.save();
    }
}

jobCreate(jobs);

