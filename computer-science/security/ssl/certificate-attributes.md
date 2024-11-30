# Certificate Fields

## Subject (Entity Information)

- **Common Name (CN)**
  - The fully qualified domain name (FQDN) of the server or entity the certificate is issued for (e.g., example.com).

- **Organization (O)**
  - The legal name of the organization owning the certificate.

- **Organizational Unit (OU)**
  - A department or division within the organization (e.g., "IT Department").

- **Country (C)**
  - The two-letter ISO country code of the entity (e.g., US, BR).

- **State or Province (ST)**
  - The state or region where the entity is located (e.g., California).

- **Locality (L)**
  - The city or town where the entity is located (e.g., San Francisco).

## Issuer Information

- Contains similar fields as the Subject, indicating the entity that issued the certificate (typically a Certificate Authority or CA).

## Validity Period

- **Not Before**
  - The date and time the certificate becomes valid.

- **Not After**
  - The expiration date and time of the certificate.

## Key Information

- **Public Key**
  - The public key associated with the certificate, used for encryption and verification.

- **Signature Algorithm**
  - The cryptographic algorithm used to sign the certificate (e.g., SHA256-RSA).

## Certificate Extensions

- **Subject Alternative Name (SAN)**
  - A list of additional domains or IPs covered by the certificate.

- **Key Usage**
  - Specifies the permitted operations for the certificate (e.g., Digital Signature, Key Encipherment).

- **Extended Key Usage (EKU)**
  - Defines the specific purposes for which the certificate can be used (e.g., TLS Server Authentication, Email Protection).

- **Basic Constraints**
  - Indicates if the certificate is a CA certificate and its path length.

- **Authority Information Access (AIA)**
  - Contains information on how to retrieve the issuing CA’s certificate.

- **CRL Distribution Points (CDP)**
  - Lists where to find the Certificate Revocation List (CRL).

## Serial Number

A unique identifier for the certificate, assigned by the CA.

## Thumbprint (or Fingerprint)

A hash of the certificate, used for quick identification and integrity checks.

These fields together ensure proper identification, validation, and secure communication in TLS.
