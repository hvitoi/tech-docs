package com.hvitoi.exception;

import java.util.Date;

import com.hvitoi.user.UserNotFoundException;

import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

// @RestControllerAdvice // @ControllerAdvice + @RestController
@ControllerAdvice // Applicable across all the other controllers
@RestController // It will be the default path in case of exceptions
public class MyResponseEntityExceptionHandler extends ResponseEntityExceptionHandler {

	// @ResponseStatus(code = HttpStatus.BAD_REQUEST)
	@ExceptionHandler(Exception.class) // Exception (generic)
	public final ResponseEntity<Object> handleAllExceptions(Exception ex, WebRequest request) {
		MyExceptionResponse exceptionResponse = new MyExceptionResponse(new Date(), ex.getMessage(),
				request.getDescription(false));
		return new ResponseEntity<Object>(exceptionResponse, HttpStatus.INTERNAL_SERVER_ERROR);
	}

	@ExceptionHandler(UserNotFoundException.class) // UserNotFoundException
	public final ResponseEntity<Object> handleUserNotFoundException(UserNotFoundException ex, WebRequest request) {
		MyExceptionResponse exceptionResponse = new MyExceptionResponse(new Date(), ex.getMessage(),
				request.getDescription(false));
		return new ResponseEntity<Object>(exceptionResponse, HttpStatus.NOT_FOUND);
	}

	@Override // MethodArgumentNotValidException (when validation fails)
	protected ResponseEntity<Object> handleMethodArgumentNotValid(MethodArgumentNotValidException ex, HttpHeaders headers,
			HttpStatus status, WebRequest request) {
		MyExceptionResponse exceptionResponse = new MyExceptionResponse(new Date(), "Validation Failed",
				ex.getBindingResult().toString());
		return new ResponseEntity<Object>(exceptionResponse, HttpStatus.BAD_REQUEST);
	}
}
