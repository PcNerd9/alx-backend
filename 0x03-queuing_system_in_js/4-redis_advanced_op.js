import redis from "redis";

let redisClient;

(async () => {
	redisClient = redis.createClient();

	redisClient.on("error", () => {
		console.log("Redis client not connected to the server: " + error)
	});

	redisClient.on("connect", () => {
		console.log("Redis client connected to the server ");
	});
})();

redisClient.hset("HolbertonSchools",
	"Portland", 50,
	"Seattle", 80,
	"New York", 20,
	"Bogota", 20,
	"Cali", 40,
	"Paris", 2,
	redis.print
);

redisClient.hgetall("HolbertonSchools", (err, value) => {
	if (err) {
		console.log(err);
	} else {
		console.log(value);
	}
}
);
