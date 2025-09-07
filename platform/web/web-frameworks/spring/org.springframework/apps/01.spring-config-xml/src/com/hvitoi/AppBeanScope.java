package com.hvitoi;

import com.hvitoi.coach.Coach;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class AppBeanScope {
    public static void main(String[] args) {
        // load spring config
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext-beanScope.xml");

        // retrieve bean
        Coach alphaCoach = context.getBean("myCoach", Coach.class);
        Coach betaCoach = context.getBean("myCoach", Coach.class);

        // check if they are the same beans
        boolean areBeansEqual = (alphaCoach == betaCoach);

        // print out the results
        System.out.println("\nPointing to the same object: " + areBeansEqual);
        System.out.println("\nMemory location for alphaCoach: " + alphaCoach);
        System.out.println("\nMemory location for betaCoach: " + betaCoach);

        // close context
        context.close();
    }
}
