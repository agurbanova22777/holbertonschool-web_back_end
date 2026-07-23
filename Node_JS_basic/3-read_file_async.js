const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n');
      const students = lines.filter((line) => line !== '');
      const studentData = students.slice(1);

      console.log(`Number of students: ${studentData.length}`);

      const fields = {};

      for (const student of studentData) {
        const info = student.split(',');
        const firstname = info[0];
        const field = info[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      }

      for (const field in fields) {
        if (Object.prototype.hasOwnProperty.call(fields, field)) {
          console.log(
            `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
          );
        }
      }

      resolve();
    });
  });
}

module.exports = countStudents;
