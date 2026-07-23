import fs from 'fs';

const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line !== '');
    const students = lines.slice(1);

    const fields = {};

    students.forEach((student) => {
      const info = student.split(',');
      const firstname = info[0];
      const field = info[3];

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstname);
    });

    resolve(fields);
  });
});

export default readDatabase;
