package com.hvitoi;

import com.hvitoi.coach.SwimCoach;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class AppSwim {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(Config.class);

        // get beans
        SwimCoach swimCoach = context.getBean("swimCoach", SwimCoach.class);

        // call methods
        System.out.println(swimCoach.getDailyWorkout());
        System.out.println(swimCoach.getDailyFortune());
        System.out.println("email: " + swimCoach.getEmail());
        System.out.println("team: " + swimCoach.getTeam());

        // close context
        context.close();
    }
}
