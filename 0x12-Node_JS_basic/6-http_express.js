const express = require('express');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(port, () => {
  //   console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
