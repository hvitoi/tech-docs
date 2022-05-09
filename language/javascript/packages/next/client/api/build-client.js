import axios from 'axios';

const buildClient = ({ req }) => {
  // window object only exists inside of the browser
  if (typeof window === 'undefined') {
    // If on the server ...
    // Pre-configured version of axios!
    return axios.create({
      baseURL: 'http://ingress-nginx-controller.kube-system.svc.cluster.local',
      headers: req.headers
    });
  } else {
    // If on the browser ...
    return axios.create({
      baseURL: '/'
    });
  }
};

export default buildClient;
