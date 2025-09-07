package com.hvitoi.expection;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice // Set global Exception Handler (it's AOP)
public class CustomerRestExceptionHandler {

	@ExceptionHandler // handle only CustomerNotFoundException
	public ResponseEntity<CustomerErrorResponse> handleException(CustomerNotFoundException e) {

		// create CustomerErrorResponse
		CustomerErrorResponse errorResponse = new CustomerErrorResponse(HttpStatus.NOT_FOUND.value(), e.getMessage(),
				System.currentTimeMillis());

		// return ResponseEntity
		return new ResponseEntity<>(errorResponse, HttpStatus.NOT_FOUND);
	}

	@ExceptionHandler // handle any other Exception
	public ResponseEntity<CustomerErrorResponse> handleException(Exception e) {

		// create CustomerErrorResponse
		CustomerErrorResponse errorResponse = new CustomerErrorResponse(HttpStatus.BAD_REQUEST.value(), e.getMessage(),
				System.currentTimeMillis());

		// return ResponseEntity
		return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
	}

}
