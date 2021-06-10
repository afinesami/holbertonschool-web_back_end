const express = require('express');
const app = express();
const port = 7865;

app.get('/', (req, res) => {
  res.end('Welcome to the payment system');
});

app.listen(port, () => {
  console.log('API available on localhost port 7865');
});