package com.hvitoi.hibernate;

import com.hvitoi.hibernate.entity.Course;
import com.hvitoi.hibernate.entity.Instructor;
import com.hvitoi.hibernate.entity.InstructorDetail;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.hibernate.query.Query;

public class FetchJoin {
	public static void main(String[] args) {

		// create session factory
		SessionFactory factory = new Configuration().configure("hibernate.cfg.xml").addAnnotatedClass(Instructor.class)
				.addAnnotatedClass(InstructorDetail.class).addAnnotatedClass(Course.class).buildSessionFactory();

		// create a session
		Session session = factory.getCurrentSession();

		try {
			session.beginTransaction();

			// build query
			Query<Instructor> query = session.createQuery(
					"SELECT i FROM Instructor i " + "JOIN FETCH i.courses " + "WHERE i.id=:instructorId", Instructor.class);

			// set query parameter
			query.setParameter("instructorId", 1);

			// execute query
			Instructor instructor = query.getSingleResult();

			// get courses
			System.out.println("Instructor: " + instructor);

			// done
			session.getTransaction().commit();
			System.out.println("Done!");
		} finally {
			session.close();
			factory.close();
		}
	}
}
