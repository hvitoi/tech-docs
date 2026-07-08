package com.example.demo.service;

public interface BusinessService {

	String failure();

    String success();

    String ignore();

    String failureWithFallback();
}
