package com.hvitoi.hibernate;

import com.hvitoi.hibernate.entity.Course;
import com.hvitoi.hibernate.entity.Instructor;
import com.hvitoi.hibernate.entity.InstructorDetail;
import com.hvitoi.hibernate.entity.Review;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class DeleteCourseAndReview {
	public static void main(String[] args) {

		// create session factory
		SessionFactory factory = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Instructor.class)
				.addAnnotatedClass(InstructorDetail.class).addAnnotatedClass(Course.class).addAnnotatedClass(Review.class)
				.buildSessionFactory();

		// create a session
		Session session = factory.getCurrentSession();

		try {
			session.beginTransaction();

			// get course
			int id = 10;
			Course course = session.get(Course.class, id);

			// delete course
			session.delete(course); // cascade delete (on reviews)
			System.out.println("Deleted course: " + course);

			// done
			session.getTransaction().commit();
			System.out.println("Done!");
		} finally {
			session.close();
			factory.close();
		}
	}
}
