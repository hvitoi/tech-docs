package com.hvitoi.hibernate.demo;

import com.hvitoi.hibernate.demo.entity.Student;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import java.util.List;

public class QueryStudentDemo {
    public static void main(String[] args) {

        // create session factory
        SessionFactory factory = new Configuration().configure("hibernate.cfg.xml") // Config file
                .addAnnotatedClass(Student.class) // Class with the field mapping
                .buildSessionFactory(); // build the factory

        // create a session
        Session session = factory.getCurrentSession();

        try {
            // begintransaction
            session.beginTransaction();

            // query students
            // use the "lastname" from entity, not "last_name" from column name
            List<Student> theStudents = session.createQuery("from Student").getResultList();
            List<Student> theStudents2 = session.createQuery("from Student s WHERE s.lastName='Vitoi'").getResultList();
            List<Student> theStudents3 = session
                    .createQuery("from Student s WHERE s.lastName='Vitoi' OR s.firstName='Daffy'").getResultList();
            List<Student> theStudents4 = session.createQuery("from Student s WHERE s.email LIKE '%mail.com'")
                    .getResultList();

            displayStudents(theStudents);
            displayStudents(theStudents2);
            displayStudents(theStudents3);
            displayStudents(theStudents4);

            // commit transaction
            session.getTransaction().commit();
            System.out.println("Done!");
        } finally {
            factory.close();
        }
    }

    private static void displayStudents(List<Student> theStudents) {
        for (Student student : theStudents) {
            System.out.println(student);

        }
    }
}
