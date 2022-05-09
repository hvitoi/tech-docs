// The nats itself is the server!
// publishers publish messages to nats
// Listeners listen to messages coming from nats

// spec:
// containers:
//   - name: nats
//     image: nats-streaming
//     args: [
//         '-p',
//         '4222',
//         '-m',
//         '8222',
//         '-hbi',
//         '5s',
//         '-hbt',
//         '5s',
//         '-hbf',
//         '2',
//         '-SD',
//         '-cid',
//         'ticketing',
//       ]
