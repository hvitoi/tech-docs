package com.hvitoi.coach;

import com.hvitoi.fortune.FortuneService;

public class TrackCoach implements Coach {
    private FortuneService fortuneService;

    public TrackCoach() {
    }

    public TrackCoach(FortuneService fortuneService) {
        this.fortuneService = fortuneService;
    }

    @Override
    public String getDailyWorkout() {
        return "Run 5 kilometers";
    }

    @Override
    public String getDailyFortune() {
        return "Just Do It: " + fortuneService.getFortune();
    }

    // Init method
    public void doMyStartup() {
        System.out.println("TrackCoach: inside doMyStartup");
    }

    // Destroy method
    public void doMyCleanup() {
        System.out.println("TrackCoach: inside doMyCleanup");
    }
}
