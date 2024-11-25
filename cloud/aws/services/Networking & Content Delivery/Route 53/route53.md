# Route 53

- Route53 offers various resources for the AWS Cloud, but it can also offer standalone DNS features
- Route53 is both an `authoritative DNS server` and a `domain registrar`

## Domain Registrar

- Route 53 can be used to `register and manage domains` with anual payment
- Once the domain is registered in Route 53, it is automatically added to a hosted zone (AWS::Route53::HostedZone), but you have delete the hosted zone

## Authoritative DNS Server

- A DNS Server where the customer (you) can modify the DNS records
