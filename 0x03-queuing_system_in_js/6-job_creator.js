const kue = require("kue");



const queue = kue.createQueue();

const data = {
    phoneNumber: "09036977142",
    message: "You are the best software engineer in the world"
}
const job = queue.create("push_notification_code", data).save(() => {
    console.log(`Notification job created: ${job.id}`)
});

job.on("complete", () => console.log("Notification job completed"));

job.on("failed", () => console.log("Notification job failed"));


