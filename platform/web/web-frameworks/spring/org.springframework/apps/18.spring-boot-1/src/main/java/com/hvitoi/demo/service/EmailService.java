package com.hvitoi.demo.service;

import org.apache.commons.mail.DefaultAuthenticator;
import org.apache.commons.mail.Email;
import org.apache.commons.mail.EmailException;
import org.apache.commons.mail.SimpleEmail;
import org.springframework.stereotype.Service;

@Service
public class EmailService {

	public void send(String name, String destEmail) {

		try {
			Email email = new SimpleEmail();
			email.setHostName("smtp.googlemail.com");
			email.setSmtpPort(465);
			email.setAuthenticator(new DefaultAuthenticator("bot@gmail.com", "springboot"));
			email.setSSLOnConnect(true);

			email.setFrom("myself@gmail.com");
			email.setSubject("You are in the VIP list");
			email.setMsg("Hi " + name + ", congratulations!");
			email.addTo(destEmail);
			email.send();

		} catch (EmailException e) {
			e.printStackTrace();
		}

	}

}
