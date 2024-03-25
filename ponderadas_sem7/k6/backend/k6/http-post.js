// import http from 'k6/http';
// import { file } from 'k6';

// export default function () {
// const url = 'http://localhost:3001/link-lists/upload';
// const fileData = file.open('backend/src/ink-lists/mocked-file/file_model.csv');
// const params = {
// headers: {
// 'Content-Type': 'text/csv',
// },
// };

// http.post(url, fileData, params);
// }


import http from 'k6/http';
import { sleep } from 'k6';

const fileData = open('../src/link-lists/mocked-file/file_model.csv', 'b');

export default function () {
  const data = {
    field: 'this is a standard form field',
    file: http.file(fileData, 'file_model.csv'),
  };
  const res = http.post('http://localhost:3001/link-lists/upload', data);
  sleep(3);
}
