package com.hvitoi.coach;

import com.hvitoi.fortune.FortuneService;

public class CricketCoach implements Coach {
    private FortuneService fortuneService;

    // Constructor with no arguments
    public CricketCoach() {
        System.out.println("CricketCoach inside no-arg constructor");
    }

    // Setter dependency injection
    public void setFortuneService(FortuneService fortuneService) {
        System.out.println("CricketCoach inside setter method - setFortuneService");
        this.fortuneService = fortuneService;
    }

    // -----------------------

    private String emailAddress;
    private String team;

    public String getEmailAddress() {
        return emailAddress;
    }

    public void setEmailAddress(String emailAddress) {
        System.out.println("CricketCoach inside setter method - setEmailAddress");
        this.emailAddress = emailAddress;
    }

    public String getTeam() {
        return team;
    }

    public void setTeam(String team) {
        System.out.println("CricketCoach inside setter method - setTeam");
        this.team = team;
    }

    // -----------------

    @Override
    public String getDailyWorkout() {
        return "Practice whatever cricket does";
    }

    @Override
    public String getDailyFortune() {
        return fortuneService.getFortune();
    }
}
