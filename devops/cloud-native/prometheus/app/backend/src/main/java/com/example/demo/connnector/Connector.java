package com.example.demo.connnector;

public interface Connector {

	 String failure();

	 String success();

	 String ignoreException();

	 String failureWithFallback();
}
