package com.example.demo.exception;

public class BusinessException extends RuntimeException {

    /**
	 * 
	 */
	private static final long serialVersionUID = -2076448930823098016L;

	public BusinessException(String message) {
        super(message);
    }

}
