package com.hvitoi;

import com.hvitoi.coach.Coach;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class AppScope {
    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");

        Coach alphaCoach = context.getBean("tennisCoach", Coach.class);
        Coach betaCoach = context.getBean("tennisCoach", Coach.class);

        // check if beans are the same
        boolean result = (alphaCoach == betaCoach);

        // print results
        System.out.println("\nPointing to the same object: " + result);
        System.out.println("Memory location of alphaCoach: " + alphaCoach);
        System.out.println("Memory location of betaCoach: " + betaCoach);

        // close context
        context.close();

    }
}
