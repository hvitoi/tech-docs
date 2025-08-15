package com.hvitoi.hibernate;

import com.hvitoi.hibernate.entity.Course;
import com.hvitoi.hibernate.entity.Instructor;
import com.hvitoi.hibernate.entity.InstructorDetail;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class CreateCourse {
	public static void main(String[] args) {

		// create session factory
		SessionFactory factory = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Instructor.class)
				.addAnnotatedClass(InstructorDetail.class).addAnnotatedClass(Course.class).buildSessionFactory();

		// create a session
		Session session = factory.getCurrentSession();

		try {
			session.beginTransaction();

			// get instructor
			int id = 1;
			Instructor instructor = session.get(Instructor.class, id);

			// create courses
			Course course1 = new Course("Java for beginners");
			Course course2 = new Course("Python for beginners");

			// add course to instructor
			instructor.add(course1);
			instructor.add(course2);

			// save
			session.save(course1);
			session.save(course2);

			// done
			session.getTransaction().commit();
			System.out.println("Courses saved: " + course1 + ", " + course2);
		} finally {
			session.close();
			factory.close();
		}
	}
}
