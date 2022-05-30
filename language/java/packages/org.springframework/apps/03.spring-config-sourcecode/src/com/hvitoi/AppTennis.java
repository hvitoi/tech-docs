package com.hvitoi;

import com.hvitoi.coach.Coach;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class AppTennis {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(Config.class);

        // get beans
        Coach theCoach = context.getBean("tennisCoach", Coach.class);

        // call methods
        System.out.println(theCoach.getDailyWorkout());
        System.out.println(theCoach.getDailyFortune());

        // close context
        context.close();
    }
}
