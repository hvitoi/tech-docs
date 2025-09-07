package com.hvitoi.aspect;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

@Aspect
@Component
@Order(3)
public class ApiAnalyticsAspect {

  @Before("com.hvitoi.aspect.AopExpressions.forDaoPackageNoGetterSetter()")
  public void performApiAnalytics() {
    System.out.println("ApiAnalyticsAspect @Before");
  }

}
