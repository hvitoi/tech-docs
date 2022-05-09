# Microservices

## Monolith vs Microservices

### Monolith

- A monolith contains:
  - Routing
  - Middleware
  - Business Logic
  - Database access
- Implement all features of the app

### Microservice

- Each microservice contains all the elements from monolith systems
- Implement ONE feature of the app
- Each service gets its own database (Database-per-service)
  - Easier to scale only the necessary database, instead of scaling everything
  - DB schema might change unexpectedly
  - Some services might function more efficiently with different types of DB's

## Communication between services

- Sync: direct requests
  - Plain http requests with json exchange format
  - Can create a big web of dependencies between services
- Async: communication using events
  - Services emit and receive events to/from a Event Bus
  - Has data duplication!
  - The Query Service is responsible for the Event Bus (Event Broker)

## Event Bus

- Implementations: RabbitMQ, Kafka, NATS, etc
- A simple plain event bus can be created with Express

## Error handling middleware

- A function to handle all `throw new Error('')` along the code
- A class is created for each error type and extends the 'Error' class
- Error structure:

```json
{
  "errors": [
    {
      "message": "Database error",
      "field": "field"
    },
    {
      "message": "Validation error"
    }
  ]
}
```

```typescript
export abstract class CustomError extends Error {
  abstract statusCode: number;

  constructor() {
    super(); // Invoke the constructor of the Error class
    Object.setPrototypeOf(this, CustomError.prototype); // setPrototypeOf must be called when extending a built in class
  }

  abstract serializeErrors(): { message: string; field?: string }[];
}
```

## Authentication strategies

- Tokens: JWT, Cookie, etc

- Option 1:

  - "order" service always ask "auth" service
  - "auth" service checks if the token is valid and the user is authenticated
  - "auth" sends the response back to "order" directly (not through event bus

- Option 2:

  - "order" has all the logic to validate a token
  - "order" doesn't need to reach auth service
  - user could be banned and the auth service could not tell the order
  - A "ban event" could also be emitted b the auth service

- JWT

  - **Request**: Authorization (header), token (body), Cookie (header)
  - A payload is transformed in a jwt string by means of a secret key
  - the jwt is decoded by the server

- Cookie
  - **Request**: Cookie: 'blabla'
  - **Response**: Set-Cookie: 'blabla'
  - Server emitts a Set-Cookie and the Client stores it in the browser
  - The Cookie is sent back by the Client when it makes a new request

## Server-side render

- Browser make request to an back-end server (NextJS)
- NextJS build the html for the entire app by requesting other services
- NextJS sends back to browser fully rendered pure HTML
- Boost the page load speed
- With server-side rendering, NextJS must know auth info with the first request
- Auth info MUST be passed as a Cookie (with jwt inside) with server-side rendering

## Cross Service data replication

### Embedding strategy

- Strategy to associate a internal model to another external model from another service
- A property of the internal model receives a whole document of the external model

### Ref/Population Feature

- Populates an external model to inside of a property
- Two separate collections

## Optimistic Concurrency Control

- Add a version to any document in the database
- Each update will be made considering the previous version
- If the version is not the desired, the update will hang
- 'mongoose-update-if-current' module
- The version number should only be incremented in the service that primarily stores it

## Scheduled event

- The event will only be redistributed by the event bus after some time window
- Not supported by nats
- BullJS library handles timing notifications

## Worker server

- A independent standalone service that process demanding actions
- Example: a video file conversion is process demanding and takes time
- That way, the original service is free to perform other activities
- A `Job` is the unit for the action to be processed by the worker
- `BullJS` handles the jobs in the worker

## Payment handling

- Stripe handle credit card payment
- A token is created and with that the payment is sent to stripe API
- default test token `tok_visa`

## Hosting providers

- Digital Ocean
- AWS
- Google Cloud
- Azure

## Further development

- HTTPS support
  - cert-manager.io
- Email support
  - Mailchimp/Sendgrid
- Production dockerfile and K8S config files
  - Production files adding the build step
- Staging cluster
  - Cluster for testing on Digital Ocean
