package com.hvitoi.hibernate.demo;

import com.hvitoi.hibernate.demo.entity.Student;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class UpdateStudentDemo {
    public static void main(String[] args) {

        // create session factory
        SessionFactory factory = new Configuration().configure("hibernate.cfg.xml") // Config file
                .addAnnotatedClass(Student.class) // Class with the field mapping
                .buildSessionFactory(); // build the factory

        Session session = factory.getCurrentSession();

        try {
            int studentId = 1;

            // begin transaction
            session.beginTransaction();

            // get student
            System.out.println("\nGetting student with id: " + studentId);
            Student myStudent = session.get(Student.class, studentId);
            System.out.println("Get complete: " + myStudent);

            // update student
            System.out.println("Updating student...");
            myStudent.setFirstName("Scooby");
            System.out.println("updating all student emails...");
            session.createQuery("UPDATE Student SET email='foo@gmail.com'").executeUpdate();

            // commit transaction
            session.getTransaction().commit();
            System.out.println("Done!");
        } finally {
            factory.close();
        }
    }
}
