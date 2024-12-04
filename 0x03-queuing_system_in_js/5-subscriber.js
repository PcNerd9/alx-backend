import redis from "redis";

let redisClient;

(async () => {
	redisClient = redis.createClient();

	redisClient.on("error", (err) => {
		console.log("Redis client not connected to the server: " + err);
	});

	redisClient.on("connect", () => {
		console.log("Redis client connected to the server");
	});
})();

redisClient.subscribe("holberton school channel", (err, count) => {
	if (err) {
		console.log(err);
	}
});

redisClient.on("message", (channel, message) => {
	if (message === "KILL_SERVER") {
		console.log("What is going on");
		redisClient.unsubscribe("holberton school channel");
		redisClient.quit();
	} else {
		console.log(message);
	}
});
