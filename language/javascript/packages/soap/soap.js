import * as soap from "soap";

soap.createClient(
  url,
  { wsdl_headers: { Authorization: auth } },
  (err, client) => {
    // Create client error
    if (err) {
      this.logger.error("Failed to create SOAP client", "soap-error", {
        error: err,
      });
      throw new InternalServerErrorException();
    }

    // Security header
    client.setSecurity(
      new soap.BasicAuthSecurity(this.getWsseUserName(), this.getWssePassword())
    );

    // Call WS
    client[operation](leadParams, (err, result) => {
      // Call WS error
      if (err) {
        this.logger.error("Failed to call SOAP WS", "soap-error", {
          data: leadParams,
          error: err,
        });
        throw new InternalServerErrorException();
      }

      // Success response
      return result;
    });
  }
);
