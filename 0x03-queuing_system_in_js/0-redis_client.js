import redis from "redis";

(async () => {
	let redisClient = redis.createClient();
	redisClient.on("error", (error) => console.log(" Redis client not connected to the server: " + error));
	redisClient.on("connect", () => console.log("Redis client connected to the server"));
})();
