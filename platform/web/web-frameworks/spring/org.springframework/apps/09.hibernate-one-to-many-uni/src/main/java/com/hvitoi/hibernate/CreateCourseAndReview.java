package com.hvitoi.hibernate;

import com.hvitoi.hibernate.entity.Course;
import com.hvitoi.hibernate.entity.Instructor;
import com.hvitoi.hibernate.entity.InstructorDetail;
import com.hvitoi.hibernate.entity.Review;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class CreateCourseAndReview {
	public static void main(String[] args) {

		// create session factory
		SessionFactory factory = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Instructor.class)
				.addAnnotatedClass(InstructorDetail.class).addAnnotatedClass(Course.class).addAnnotatedClass(Review.class)
				.buildSessionFactory();

		// create a session
		Session session = factory.getCurrentSession();

		try {
			session.beginTransaction();

			// create course and associate reviews
			Course course = new Course("Pacman - How to score one million points");
			course.addReview(new Review("Great!"));
			course.addReview(new Review("Awesome!"));
			course.addReview(new Review("Bad!"));

			// save
			session.save(course); // save course and reviews
			System.out.println("Course: " + course);
			System.out.println("Reviews: " + course.getReviews());

			// done
			session.getTransaction().commit();
			System.out.println("Done!");
		} finally {
			session.close();
			factory.close();
		}
	}
}
