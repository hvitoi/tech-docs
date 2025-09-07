package com.hvitoi.hibernate;

import com.hvitoi.hibernate.entity.Instructor;
import com.hvitoi.hibernate.entity.InstructorDetail;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class GetInstructorDetail {
	public static void main(String[] args) {

		// create session factory
		SessionFactory factory = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Instructor.class)
				.addAnnotatedClass(InstructorDetail.class).buildSessionFactory(); // add multiple classes to be mapped

		// create a session
		Session session = factory.getCurrentSession();

		try {
			session.beginTransaction();

			// get
			int id = 3;
			InstructorDetail instructorDetail = session.get(InstructorDetail.class, id);
			System.out.println("InstructorDetail: " + instructorDetail);
			System.out.println("Instructor: " + instructorDetail.getInstructor()); // has the Instructor nested

			session.getTransaction().commit();

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			session.close();
			factory.close();
		}
	}
}
