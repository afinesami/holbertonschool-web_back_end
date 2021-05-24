const express = require('express');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');

const DATABASE = args[0];

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const msg = 'This is the list of our students\n';
  try {
    const students = await countStudents(DATABASE);
    res.send(`${msg}${students.join('\n')}`);
  } catch (error) {
    res.send(`${msg}${error.message}`);
  }
});

app.listen(port, () => {
  //   console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
