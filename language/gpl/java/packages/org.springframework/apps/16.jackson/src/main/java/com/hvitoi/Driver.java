package com.hvitoi;

import java.io.File;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.hvitoi.entity.Address;
import com.hvitoi.entity.Student;

public class Driver {

	public static void main(String[] args) {

		try {
			// create object mapper
			ObjectMapper mapper = new ObjectMapper();

			// read JSON file and map/convert to Java POJO:
			Student student = mapper.readValue(new File("src/main/resources/sample-full.json"), Student.class);

			// print first name and last name
			System.out.println("First name = " + student.getFirstName());
			System.out.println("Last name = " + student.getLastName());

			// print out address: street and city
			Address address = student.getAddress();
			System.out.println("Street = " + address.getStreet());
			System.out.println("City = " + address.getCity());

			// print out languages
			for (String language : student.getLanguages()) {
				System.out.println(language);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
