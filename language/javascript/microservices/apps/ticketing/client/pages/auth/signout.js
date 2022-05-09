import { useEffect } from 'react';
import Router from 'next/router';
import useRequest from '../../hooks/use-request';

const SignOut = () => {
  const [doRequest, errors] = useRequest({
    url: '/api/users/signout',
    method: 'post',
    body: {},
    onSuccess: () => {
      Router.push('/');
    }
  });

  useEffect(() => {
    doRequest();
  }, []); // [] runs is only once (at startup)

  return <div>Signing you out ...</div>; // This is only appear until (onSuccess is invoked)
};

export default SignOut;
