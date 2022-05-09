// file [ticketId].js is equivalent to /tickets/:ticketId
import Router from 'next/router';
import useRequest from '../../hooks/use-request';

const TicketShow = ({ ticket }) => {
  const [doRequest, errors] = useRequest({
    url: '/api/orders',
    method: 'post',
    body: {
      ticketId: ticket.id
    },
    onSuccess: (order) => {
      Router.push('/orders/[orderId]', `/orders/${order.id}`); // Programmatic routing with wildcard. `href` and `as`
    }
  });
  return (
    <div>
      <h1>{ticket.title}</h1>
      <h4>{ticket.price}</h4>
      {errors}
      <button className="btn btn-primary" onClick={(e) => doRequest()}>
        Purchase
      </button>
    </div>
  );
};

TicketShow.getInitialProps = async (context, client) => {
  const { ticketId } = context.query; // query string from the browser

  // Fetch the ticket
  const { data } = await client.get(`/api/tickets/${ticketId}`);

  // Return to the component context
  return { ticket: data };
};

export default TicketShow;
