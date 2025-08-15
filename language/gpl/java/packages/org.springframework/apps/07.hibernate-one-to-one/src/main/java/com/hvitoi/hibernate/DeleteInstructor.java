package com.hvitoi.hibernate;

import com.hvitoi.hibernate.entity.Instructor;
import com.hvitoi.hibernate.entity.InstructorDetail;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class DeleteInstructor {
	public static void main(String[] args) {

		// create session factory
		SessionFactory factory = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Instructor.class)
				.addAnnotatedClass(InstructorDetail.class).buildSessionFactory(); // add multiple classes to be mapped

		// create a session
		Session session = factory.getCurrentSession();

		try {
			session.beginTransaction();

			// get
			int instructorId = 1;
			Instructor instructor = session.get(Instructor.class, instructorId); // returns null if not found
			System.out.println("Found instructor: " + instructor);

			// delete
			if (instructor != null) {
				session.delete(instructor);
				System.out.println("Deleted instructor: " + instructor); // also delete instructorDetail
			}

			session.getTransaction().commit();

		} finally {
			factory.close();
		}
	}
}
