package com.hvitoi.hibernate.demo;

import com.hvitoi.hibernate.demo.entity.Student;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class CreateStudentDemo {
    public static void main(String[] args) {

        // create session factory
        SessionFactory factory = new Configuration().configure("hibernate.cfg.xml") // Config file
                .addAnnotatedClass(Student.class) // Class with the field mapping
                .buildSessionFactory(); // build the factory

        // create a session
        Session session = factory.getCurrentSession();

        try {
            System.out.println("Creating 3 student objects...");

            // create student objects
            Student tempStudent1 = new Student("Henry", "Vitoi", "henry@heyhey.com");
            Student tempStudent2 = new Student("Martin", "Applebaum", "martin@heyhey.com");
            Student tempStudent3 = new Student("Luther", "Santos", "luther@heyhey.com");

            // start transaction
            session.beginTransaction();

            // save student object
            System.out.println("Saving student...");
            session.save(tempStudent1);
            session.save(tempStudent2);
            session.save(tempStudent3);

            // commit transaction
            session.getTransaction().commit();
            System.out.println("Done!");
        } finally {
            factory.close();
        }
    }
}
