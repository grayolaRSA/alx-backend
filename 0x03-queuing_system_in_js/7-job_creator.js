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

function updatePercentage(totalJobs, completedJobs) {
    // Track the total number of jobs and the number of completed jobs
    const percentage = totalJobs > 0 ? ((completedJobs / totalJobs) * 100).toFixed(2) : 0;
    return percentage;
}

export function jobCreate(jobs) {

  
    for (const job of jobs) {
      const notificationJob = queue.create('push_notification_code_2', {phoneNumber: job.phoneNumber, message: job.message});
      notificationJob.on('enqueue', () => {
      console.log(`Notification job created: ${notificationJob.id}`);
      totalJobs++;
      console.log(`total jobs: ${totalJobs}`)
      // updatePercentage();
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
          completedJobs++;
          console.log(`jobs completed: ${completedJobs}`);
          const percentage = updatePercentage(totalJobs, completedJobs);
          console.log(`Notification job ${notificationJob.id} ${percentage}% complete`);
      });
  
      notificationJob.on('failed', (error) => {
          console.error(`Notification job ${notificationJob.id}  failed: ${error}`);
      });

      notificationJob.save();
    }

    // Exit gracefully when the job is completed or failed
    queue.process('push_notification_code_2', (job, done) => {
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
}

jobCreate(jobs);

