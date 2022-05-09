import { useEffect, useState } from 'react';
import StripeCheckout from 'react-stripe-checkout';
import Router from 'next/router';
import useRequest from '../../hooks/use-request';

const OrderShow = ({ order, currentUser }) => {
  const [timeLeft, setTimeLeft] = useState(0);
  const [doRequest, errors] = useRequest({
    url: '/api/payments',
    method: 'post',
    body: {
      orderId: order.id
      // token will be provided on the token callback
    },
    onSuccess: (payment) => Router.push('/orders')
  });

  useEffect(() => {
    const findTimeLeft = () => {
      const msLeft = new Date(order.expiresAt) - new Date() - 840000; // 840s to correct the timezone
      setTimeLeft(Math.round(msLeft / 1000));
    };
    findTimeLeft();

    const timerId = setInterval(findTimeLeft, 1000); // Check the time left every 1s
    return () => clearInterval(timerId); // Clear the timer when left the page
  }, []);

  if (timeLeft < 0) return <div>Order Expired</div>;
  return (
    <div>
      Time left to pay: {timeLeft} seconds
      <StripeCheckout
        token={(token) => doRequest({ token: token.id })}
        stripeKey="pk_test_51HKRtrEQEC6n74trq2YRLKBW0OAVEjNTL092T1poyiE2Hc7C9rMaZbhond1wnCexidU4p6l5Zu8yxYAZPYVF45bR00uPaQHdPf"
        amount={order.ticket.price * 100}
        email={currentUser.email}
      />
      {/* 
        - token: Callback to execute after the token is received by the stripe API
        - stripeKey: Publishable key of stripe
        - amount: Amount to pay (in cents)
        - email: User email
      
      */}
      {errors}
    </div>
  );
};

OrderShow.getInitialProps = async (context, client) => {
  const { orderId } = context.query;

  // Fetch the order
  const { data } = await client.get(`/api/orders/${orderId}`);

  return { order: data };
};

export default OrderShow;
