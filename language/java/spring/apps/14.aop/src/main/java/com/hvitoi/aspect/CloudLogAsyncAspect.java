package com.hvitoi.aspect;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

@Aspect
@Component
@Order(1) // Order to run this aspect
public class CloudLogAsyncAspect {

  @Before("com.hvitoi.aspect.AopExpressions.forDaoPackageNoGetterSetter()")
  public void logToCloudAsync() {
    System.out.println("CloudLogAsyncAspect @Before");
  }

}
