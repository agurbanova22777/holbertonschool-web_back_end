const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(database)
      .then((result) => {
        res.end(`This is the list of our students\n${result}`);
      })
      .catch((err) => {
        res.end(`This is the list of our students\n${err.message}`);
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
