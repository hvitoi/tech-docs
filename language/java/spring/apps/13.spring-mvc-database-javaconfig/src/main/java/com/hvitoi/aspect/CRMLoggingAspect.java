package com.hvitoi.aspect;

import java.util.logging.Logger;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class CRMLoggingAspect {
  private Logger logger = Logger.getLogger(getClass().getName());

  @Pointcut("execution(* com.hvitoi.controller.*.*(..))")
  private void forControllerPackage() {
  }

  @Pointcut("execution(* com.hvitoi.service.*.*(..))")
  private void forServicePackage() {
  }

  @Pointcut("execution(* com.hvitoi.dao.*.*(..))")
  private void forDaoPackage() {
  }

  @Pointcut("forControllerPackage() || forServicePackage() || forDaoPackage()")
  private void forAppFlow() {
  }

  @Before("forAppFlow()")
  public void before(JoinPoint joinPoint) {
    String method = joinPoint.getSignature().toShortString();
    System.out.println("CRMLoggingAspect @Before (" + method + ")");

    Object[] args = joinPoint.getArgs();
    for (Object arg : args) {
      logger.info("CRMLoggingAspect @Before (" + method + "): Argument " + arg);
    }
  }

  @AfterReturning(pointcut = "forAppFlow()", returning = "result")
  public void AfterReturning(JoinPoint joinPoint, Object result) {
    String method = joinPoint.getSignature().toShortString();
    System.out.println("CRMLoggingAspect @AfterReturning (" + method + ")");

    logger.info("CRMLoggingAspect @AfterReturning (" + method + "): Result " + result);
  }
}
