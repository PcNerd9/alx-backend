import redis from "redis";

let redisClient;
(async () => {
	redisClient = redis.createClient();
	redisClient.on("error", (error) => console.log(" Redis client not connected to the server: " + error));
	redisClient.on("connect", () => console.log("Redis client connected to the server"));
})();

function setNewSchool(schoolName, value) {
	redisClient.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
	redisClient.get(schoolName, (err, value) => {
	if (err) {
		console.log(err)
	} else {
		console.log(value)
	};
	});
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
