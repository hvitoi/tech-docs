package com.hvitoi;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import io.github.resilience4j.bulkhead.annotation.Bulkhead;

@RestController
public class CircuitBreakerController {

	private Logger logger = LoggerFactory.getLogger(CircuitBreakerController.class);

	@GetMapping("/sample-api")
	// Retry: default retry config (try 3 times)
	// @Retry(name = "default")

	// Retry: custom retry config (defined in application.properties)
	// @Retry(name = "sample-api", fallbackMethod = "hardcodedResponse")

	// CircuitBreaker: open circuit after % of failures
	// @CircuitBreaker(name = "default", fallbackMethod = "hardcodedResponse")

	// RateLimiter: // in 10s allow max of 10000 calls
	// @RateLimiter(name="default")

	// Bulkhead: set concurrent calls limit
	@Bulkhead(name = "sample-api")
	public String sampleApi() {
		logger.info("Sample api call received");

		// This will fail
		// ResponseEntity<String> forEntity = new
		// RestTemplate().getForEntity("http://localhost:8080/some-dummy-url",
		// String.class);
		// return forEntity.getBody();

		return "This is a sample API";
	}

	public String hardcodedResponse(Exception ex) {
		return "This is a default fallback response";
	}
}
