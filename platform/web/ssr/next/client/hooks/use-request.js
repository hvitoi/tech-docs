import axios from 'axios';
import { useState } from 'react';

const useRequest = ({ url, method, body, onSuccess }) => {
  const [errors, setErrors] = useState(null); // null by default

  const doRequest = async () => {
    try {
      const response = await axios[method](url, body);
      setErrors(null);

      // onSuccess here will be a function to redirect to a page
      if (onSuccess) {
        onSuccess(response.data);
      }
    } catch (err) {
      // err.response.data.errors = [{message, field}]
      setErrors(
        <div className="alert alert-danger">
          <h4>Oooops...</h4>
          <ul className="my-0">
            {err.response.data.errors.map((err) => (
              <li key={err.message}>{err.message}</li>
            ))}
          </ul>
        </div>
      );
    }
  };

  return [doRequest, errors];
};

export default useRequest;
