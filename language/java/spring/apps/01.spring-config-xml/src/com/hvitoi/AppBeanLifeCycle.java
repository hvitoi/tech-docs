package com.hvitoi;

import com.hvitoi.coach.Coach;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class AppBeanLifeCycle {
    public static void main(String[] args) {
        // load spring config
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext(
                "applicationContext-beanLifeCycle.xml");

        // retrieve bean
        Coach myTrackCoach = context.getBean("myTrackCoach", Coach.class);

        // call methods
        System.out.println(myTrackCoach.getDailyWorkout());

        // close context
        context.close();
    }
}
