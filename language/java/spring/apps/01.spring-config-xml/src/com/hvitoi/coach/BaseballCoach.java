package com.hvitoi.coach;

import com.hvitoi.fortune.FortuneService;

public class BaseballCoach implements Coach {
    private FortuneService fortuneService;

    // Constructor dependency injection
    public BaseballCoach(FortuneService theFortuneService) {
        fortuneService = theFortuneService;
    }

    @Override // Override placeholder method from coach interface
    public String getDailyWorkout() {
        return "Hit 10 balls with the bat.";
    }

    @Override
    public String getDailyFortune() {
        return fortuneService.getFortune(); // use fortuneService injected dependency
    }
}
