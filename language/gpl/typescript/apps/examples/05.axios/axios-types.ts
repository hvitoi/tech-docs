import axios, { AxiosResponse } from 'axios';
const id = 1;
axios
  .get('http://localhost:3000/users/' + id)
  .then((res: AxiosResponse): void => {
    console.log(res);
  });
