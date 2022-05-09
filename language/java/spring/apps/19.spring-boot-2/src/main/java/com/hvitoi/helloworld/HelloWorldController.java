package com.hvitoi.helloworld;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWorldController {

	@Autowired // Map the "messages.properties_xx" file (spring.messages.basename)
	private MessageSource messageSource;

	@GetMapping(path = "/hello-world")
	public String helloWorld() {
		return "Hello World";
	}

	@GetMapping(path = "/hello-world-bean")
	public HelloWorldBean helloWorldBean() {
		return new HelloWorldBean("Hello World");
	}

	@GetMapping(path = "/hello-world/path-variable/{name}")
	public HelloWorldBean helloWorldPathVariable(@PathVariable String name) {
		return new HelloWorldBean(String.format("Hello World, %s", name));
	}

	// Customize the response for different people around the world (i18n)
	// "Accept-Language" in request header defines the lang
	@GetMapping(path = "/hello-world-internationalized")
	public String helloWorldInternationalized(/** @RequestHeader(name="Accept-Language", required=false) Locale locale */
	) {
		// the appropriate messages.properties file is read according to the locale
		return messageSource.getMessage("good.morning.message", null,
				"default message with message.properties is not found", LocaleContextHolder.getLocale());
	}

}
