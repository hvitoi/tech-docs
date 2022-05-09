package com.hvitoi;

import com.hvitoi.coach.Coach;
import com.hvitoi.coach.CricketCoach;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class AppBean {
    public static void main(String[] args) {
        // load spring config
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");

        // retrieve beans from spring container (beans come assembled with all
        // dependencies)
        Coach trackCoach = context.getBean("myTrackCoach", Coach.class); // coach interface is specified here because
                                                                         // the interface is passed to the method
        CricketCoach cricketCoach = context.getBean("myCricketCoach", CricketCoach.class);

        // call methods on trackCoach bean
        System.out.println(trackCoach.getDailyWorkout()); // method from the own class
        System.out.println(trackCoach.getDailyFortune()); // method from the dependency

        // call methods on cricketCoach bean
        System.out.println(cricketCoach.getDailyWorkout());
        System.out.println(cricketCoach.getDailyFortune());
        System.out.println(cricketCoach.getEmailAddress());
        System.out.println(cricketCoach.getTeam());

        // close context
        context.close();

    }
}
