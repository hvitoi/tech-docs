package com.example.demo.service;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.example.demo.connnector.Connector;
import com.example.demo.service.BusinessService;

import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry;

@Service(value = "businessBService")
public class BusinessBService implements BusinessService {

	private final Connector backendBConnector;
    private final CircuitBreaker circuitBreaker;

    public BusinessBService(@Qualifier("backendBConnector") Connector backendBConnector,
                            CircuitBreakerRegistry circuitBreakerRegistry){
        this.backendBConnector = backendBConnector;
        circuitBreaker = circuitBreakerRegistry.circuitBreaker("backendB");
    }
	
	@Override
	public String failure() {
		 return CircuitBreaker.decorateSupplier(circuitBreaker, backendBConnector::failure).get();
	}

	@Override
	public String success() {
		return CircuitBreaker.decorateSupplier(circuitBreaker, backendBConnector::success).get();
	}

	@Override
	public String ignore() {
		return CircuitBreaker.decorateSupplier(circuitBreaker, backendBConnector::ignoreException).get();
	}

	@Override
	public String failureWithFallback() {
		return backendBConnector.failureWithFallback();
	}

}
