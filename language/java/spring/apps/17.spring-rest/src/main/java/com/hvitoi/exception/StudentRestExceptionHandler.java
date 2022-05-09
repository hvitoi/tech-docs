package com.hvitoi.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice // Set global Exception Handler (it's AOP)
public class StudentRestExceptionHandler {

	@ExceptionHandler // handle only StudentNotFoundException
	public ResponseEntity<StudentErrorResponse> handleException(StudentNotFoundException e) {

		// create a StudentErrorResponse
		StudentErrorResponse errorResponse = new StudentErrorResponse();
		errorResponse.setStatus(HttpStatus.NOT_FOUND.value());
		errorResponse.setMessage(e.getMessage());
		errorResponse.setTimeStamp(System.currentTimeMillis());

		// return ResponseEntity
		return new ResponseEntity<>(errorResponse, HttpStatus.NOT_FOUND);
	}

	@ExceptionHandler // handle any other Exception
	public ResponseEntity<StudentErrorResponse> handleException(Exception e) {

		// create a StudentErrorResponse
		StudentErrorResponse errorResponse = new StudentErrorResponse();
		errorResponse.setStatus(HttpStatus.BAD_REQUEST.value());
		errorResponse.setMessage(e.getMessage());
		errorResponse.setTimeStamp(System.currentTimeMillis());

		// return ResponseEntity
		return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
	}

}
