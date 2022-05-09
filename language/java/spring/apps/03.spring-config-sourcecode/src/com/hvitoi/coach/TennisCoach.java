package com.hvitoi.coach;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

import com.hvitoi.fortune.FortuneService;

// Annotation to make from a class a spring bean, so that spring will register it. In quote is the bean ID
@Component
@Scope("singleton")
public class TennisCoach implements Coach {

    // field injection
    @Autowired
    @Qualifier("randomFortuneService")
    private FortuneService fortuneService;

    // Default constructor
    public TennisCoach() {
        System.out.println(">> inside default constructor");
    }

    // define init method
    @PostConstruct
    public void doMyStartup() {
        System.out.println(">> TennisCoach: inside of doMyStartup()");
    }

    @PreDestroy
    public void doMyCleanup() {
        System.out.println(">> TennisCoach: inside of doMyCleanup()");
    }

    // define destroy method

    // // method injection
    // @Autowired
    // public void doSomeCrazyStuff(FortuneService fortuneService) {
    // System.out.println(">> TennisCoach: inside doSomeCrazyStuff()");
    // this.fortuneService = fortuneService;
    // }

    // // setter injection
    // @Autowired // Substitute the constructor for dependency injection
    // public void setFortuneService(FortuneService fortuneService) {
    // System.out.println(">> TennisCoach: inside setFortuneService");
    // this.fortuneService = fortuneService;
    // }

    // // constructor injection
    // @Autowired
    // public TennisCoach(FortuneService fortuneService) {
    // this.fortuneService = fortuneService;
    // }

    @Override
    public String getDailyFortune() {
        return fortuneService.getFortune();
    }

    @Override
    public String getDailyWorkout() {
        return "Practice your backhand volley";
    }

}
