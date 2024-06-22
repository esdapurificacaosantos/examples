const Logger = require("./Logger");
const logger = new Logger();

logger.on("log", (arg) => {
  console.log("Listener called!", arg);
});

logger.log("Hello World!");
