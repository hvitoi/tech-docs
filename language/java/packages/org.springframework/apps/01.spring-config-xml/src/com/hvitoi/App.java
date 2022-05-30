package com.hvitoi;

import com.hvitoi.coach.Coach;
import com.hvitoi.coach.TrackCoach;

public class App {
    public static void main(String[] args) {
        Coach coach = new TrackCoach(); // create object
        System.out.println(coach.getDailyWorkout()); // use object
    }

}
