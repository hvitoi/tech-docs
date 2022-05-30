package com.hvitoi.service;

import java.util.concurrent.TimeUnit;

import org.springframework.stereotype.Component;

@Component
public class TrafficFortuneService {
  public String getFortune() {
    try {
      TimeUnit.SECONDS.sleep(5); // sleep(5)
    } catch (InterruptedException e) {
      e.printStackTrace();
    }

    return "Be happy!zz";
  }
}
