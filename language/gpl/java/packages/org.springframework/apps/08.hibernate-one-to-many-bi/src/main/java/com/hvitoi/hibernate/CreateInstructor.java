package com.hvitoi.hibernate;

import com.hvitoi.hibernate.entity.Course;
import com.hvitoi.hibernate.entity.Instructor;
import com.hvitoi.hibernate.entity.InstructorDetail;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class CreateInstructor {
	public static void main(String[] args) {

		// create session factory
		SessionFactory factory = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Instructor.class)
				.addAnnotatedClass(InstructorDetail.class).addAnnotatedClass(Course.class).buildSessionFactory();

		// create a session
		Session session = factory.getCurrentSession();

		try {
			Instructor instructor = new Instructor("Henrique", "Vitoi", "hey@hey.com");
			InstructorDetail instructorDetail = new InstructorDetail("Henry's channel", "Coding");

			// associate objects
			instructor.setInstructorDetail(instructorDetail); // in-memory association

			// save
			session.beginTransaction();
			session.save(instructor); // this will save Instructor + InstructorDetail because CascadeType.ALL
			session.getTransaction().commit();

			// done
			System.out.println("Instructor saved: " + instructor);
		} finally {
			session.close();
			factory.close();
		}
	}
}
