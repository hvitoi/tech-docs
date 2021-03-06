package com.example.demo.connnector;

import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.client.HttpServerErrorException;

import com.example.demo.exception.BusinessException;

import io.github.resilience4j.circuitbreaker.annotation.CircuitBreaker;
import io.github.resilience4j.retry.annotation.Retry;
import io.vavr.control.Try;

@CircuitBreaker(name = "backendB")
@Retry(name = "backendB")
@Component(value = "backendBConnector")
public class BackendBConnector implements Connector {

	@Override
	public String failure() {
		throw new HttpServerErrorException(HttpStatus.INTERNAL_SERVER_ERROR, "This is a remote exception");
	}

	@Override
	public String success() {
		return "Hello World from backend B";
	}

	@Override
	public String ignoreException() {
		throw new BusinessException("This exception is ignored by the CircuitBreaker of backend B");
	}

	@Override
	public String failureWithFallback() {
		return Try.ofSupplier(this::failure).recover(ex -> "Recovered").get();
	}

}
