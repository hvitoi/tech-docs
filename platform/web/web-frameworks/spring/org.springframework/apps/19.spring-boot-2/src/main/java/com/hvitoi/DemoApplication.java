package com.hvitoi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	// @Bean
	// public LocaleResolver localeResolver() {
	// AcceptHeaderLocaleResolver localeResolver = new AcceptHeaderLocaleResolver();
	// localeResolver.setDefaultLocale(Locale.US);
	// return localeResolver;
	// }
}
