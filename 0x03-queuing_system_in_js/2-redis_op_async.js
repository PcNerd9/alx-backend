import redis from "redis";
import { promisify } from "util";


let redisClient;
(async () => {
	redisClient = redis.createClient();
	redisClient.on("error", (error) => console.log(" Redis client not connected to the server: " + error));
	redisClient.on("connect", () => console.log("Redis client connected to the server"));
})();

const getAsync = promisify(redisClient.get).bind(redisClient);

function setNewSchool(schoolName, value) {
	redisClient.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
	const value = await getAsync(schoolName);
	console.log(value);
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
