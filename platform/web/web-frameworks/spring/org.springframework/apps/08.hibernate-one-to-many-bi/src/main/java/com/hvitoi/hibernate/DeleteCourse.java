package com.hvitoi.hibernate;

import com.hvitoi.hibernate.entity.Course;
import com.hvitoi.hibernate.entity.Instructor;
import com.hvitoi.hibernate.entity.InstructorDetail;
import com.mysql.cj.Session.SessionEventListener;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class DeleteCourse {
	public static void main(String[] args) {

		// create session factory
		SessionFactory factory = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Instructor.class)
				.addAnnotatedClass(InstructorDetail.class).addAnnotatedClass(Course.class).buildSessionFactory();

		// create a session
		Session session = factory.getCurrentSession();

		try {
			session.beginTransaction();

			// get course
			int id = 10;
			Course course = session.get(Course.class, id);

			// delete course
			session.delete(course);
			System.out.println("Course deleted: " + course);

			// done
			session.getTransaction().commit();
			System.out.println("Done!");
		} finally {
			session.close();
			factory.close();
		}
	}
}
