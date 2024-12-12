package com.example.demo.service;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.example.demo.connnector.Connector;

@Service(value = "businessAService")
public class BusinessAService implements BusinessService {

	private final Connector backendAConnector;

	public BusinessAService(@Qualifier("backendAConnector") Connector backendAConnector) {
		this.backendAConnector = backendAConnector;
	}

	@Override
	public String failure() {
		return backendAConnector.failure();
	}

	@Override
	public String success() {
		return backendAConnector.success();
	}

	@Override
	public String ignore() {
		return backendAConnector.ignoreException();
	}

	@Override
	public String failureWithFallback() {
		return backendAConnector.failureWithFallback();
	}

}
