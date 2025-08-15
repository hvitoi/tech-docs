package com.hvitoi.hibernate;

import com.hvitoi.hibernate.entity.Instructor;
import com.hvitoi.hibernate.entity.InstructorDetail;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class DeleteInstructorDetail {
	public static void main(String[] args) {

		// create session factory
		SessionFactory factory = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Instructor.class)
				.addAnnotatedClass(InstructorDetail.class).buildSessionFactory(); // add multiple classes to be mapped

		// create a session
		Session session = factory.getCurrentSession();

		try {
			session.beginTransaction();

			// get
			int instructorId = 2;
			InstructorDetail instructorDetail = session.get(InstructorDetail.class, instructorId); // returns null if not
																																															// found
			System.out.println("Found instructorDetail: " + instructorDetail);
			System.out.println("Associated instructor: " + instructorDetail.getInstructor());

			// delete
			if (instructorDetail != null) {
				// instructorDetail.getInstructor().setInstructorDetail(null); // update the
				// instructorDetail reference in Instructor (because the instructorDetail will
				// be deleted). Use it only if the relationship is not bidirectional
				session.delete(instructorDetail);
				System.out.println("Deleted instructorDetail: " + instructorDetail); // also delete instructor
			}

			session.getTransaction().commit();

		} finally {
			factory.close();
		}
	}
}
