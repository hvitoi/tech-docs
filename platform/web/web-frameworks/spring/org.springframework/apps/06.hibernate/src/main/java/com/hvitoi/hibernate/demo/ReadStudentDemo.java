package com.hvitoi.hibernate.demo;

import com.hvitoi.hibernate.demo.entity.Student;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class ReadStudentDemo {
    public static void main(String[] args) {

        // create session factory
        SessionFactory factory = new Configuration().configure("hibernate.cfg.xml") // Config file
                .addAnnotatedClass(Student.class) // Class with the field mapping
                .buildSessionFactory(); // build the factory
        Session session;

        try {
            /*
             ** CREATE AND SAVE STUDENT
             */
            System.out.println("Creating a new student object...");

            // create a session
            session = factory.getCurrentSession();

            // create student object
            Student student = new Student("Daffy", "Duck", "daffy@mail.com");

            // start transaction
            session.beginTransaction();

            // save student object
            System.out.println(student);
            session.save(student);

            // commit transaction
            session.getTransaction().commit();
            System.out.println("Student saved! Generated ID: " + student.getId());

            /*
             ** READ STUDENT
             */
            System.out.println("\nSearching for student...");

            // create a session
            session = factory.getCurrentSession();

            // start transaction
            session.beginTransaction(); // The query is also a transaction! In hibernate world everything is a
                                        // transaction

            // get student
            System.out.println("Getting student with ID: " + student.getId());
            Student foundStudent = session.get(Student.class, student.getId()); // Search based on primary key. Returns
                                                                                // null if not found
            System.out.println("Student found: " + foundStudent);

            // commit transaction
            session.getTransaction().commit(); // transactions must be committed even for reading
            System.out.println("Done");

        } finally {
            factory.close();
        }
    }
}
