# Ports

- `Tracing Server` (Zipkin): 9411
- `Event Broker` (RabbitMQ): 5672 and 15672 (management)
- `Spring Cloud Config Server`: 8888
- `Spring Cloud Eureka Naming Server`: 8761
- `Spring Cloud Gateway`: 8765

- `Currency Exchange Service`: 8000
- `Currency Conversion Service`: 8100
- `Limits Service`: 8080

## URLs

- `Tracing Server`

  - <http://localhost:9411/zipkin/traces/df13de3cfdcd23bd>

- `Naming Server`

  - <http://localhost:8761/>

- `Currency Exchange` (direct)

  - <http://localhost:8000/currency-exchange/from/USD/to/INR/>
  - <http://localhost:8765/currency-exchange/from/USD/to/INR/>

- `Currency Conversion` (direct)

  - <http://localhost:8100/currency-conversion/from/USD/to/INR/quantity/1>
  - <http://localhost:8765/currency-conversion/from/USD/to/INR/quantity/1>

  - <http://localhost:8100/currency-conversion-feign/from/USD/to/INR/quantity/1>
  - <http://localhost:8765/currency-conversion-feign/from/USD/to/INR/quantity/1>
