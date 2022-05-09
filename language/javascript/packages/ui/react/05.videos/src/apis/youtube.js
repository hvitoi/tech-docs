import axios from 'axios';

const KEY = 'AIzaSyDRpuU79qlZcoxN-CHuiOPhCk-I6ua9aGI';

export default axios.create({
  baseURL: 'https://www.googleapis.com/youtube/v3',
  params: {
    part: 'snippet',
    maxResults: 5,
    key: KEY
  }
});
