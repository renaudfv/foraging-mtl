const { join } = require("path");

const app = require("../app");

app.set("view engine", "pug");
app.set("views", join(__dirname, "../views"));
app.engine(".pug", require("pug").__express);


app.get("*", async (req, res) => {
  res.render("home", {});
});

module.exports = app;
