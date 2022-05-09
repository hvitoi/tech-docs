package com.hvitoi.aspect;

import java.util.List;
import java.util.logging.Logger;

import com.hvitoi.entity.Account;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.AfterThrowing;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.reflect.MethodSignature;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

@Aspect
@Component
@Order(2)
public class LoggingAspect {
  private Logger logger = Logger.getLogger(getClass().getName());

  @Before("com.hvitoi.aspect.AopExpressions.forDaoPackageNoGetterSetter()")
  public void beforeAddAccountAdvice(JoinPoint joinPoint) {

    // Method signature: com.hvitoi.Account(Account, boolean)
    MethodSignature methodSignature = (MethodSignature) joinPoint.getSignature();
    logger.info("LoggingAspect @Before (" + methodSignature.toShortString());

    // Method arguments
    Object[] args = joinPoint.getArgs();
    for (Object arg : args) {
      logger.info(arg.toString());
      if (arg instanceof Account) {
        Account account = (Account) arg;
        logger.info("Account name: " + account);
      }
    }
  }

  @AfterReturning(pointcut = "execution(* com.hvitoi.dao.AccountDAO.findAccounts(..))", returning = "result")
  public void AfterReturningFindAccountsAdvice(JoinPoint joinPoint, List<Account> result) {
    String method = joinPoint.getSignature().toShortString();
    logger.info("LoggingAspect @AfterReturning (" + method + "): Original names " + result);
    convertAccountNamesToUpperCase(result);
    logger.info("LoggingAspect @AfterReturning (" + method + "): Converted names " + result);
  }

  private void convertAccountNamesToUpperCase(List<Account> result) {
    for (Account account : result) {
      String accountNameUpperCase = account.getName().toUpperCase();
      account.setName(accountNameUpperCase);
    }
  }

  @AfterThrowing(pointcut = "execution(* com.hvitoi.dao.AccountDAO.findAccounts(..))", throwing = "theExc")
  public void afterThrowingFindAccountsAdvice(JoinPoint joinPoint, Throwable theExc) {
    String method = joinPoint.getSignature().toShortString();
    logger.info("LoggingAspect @AfterThrowing (" + method + "): Exception " + theExc);
    // The exception is also handled by the catch block of the method
  }

  @After("execution(* com.hvitoi.dao.AccountDAO.findAccounts(..))")
  public void afterFinallyFindAccountsAdvice(JoinPoint joinPoint) {
    // @After does not have access to the exception
    String method = joinPoint.getSignature().toShortString();
    logger.info("LoggingAspect @After (" + method + ")");
  }

  @Around("execution(* com.hvitoi.service.*.getFortune(..))")
  public Object afterGetFortune(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
    String method = proceedingJoinPoint.getSignature().toShortString();
    logger.info("LoggingAspect @Around (" + method + ")");

    long begin = System.currentTimeMillis();
    Object result = proceedingJoinPoint.proceed(); // proceedingJoinPoint is a handle to the target method
    long end = System.currentTimeMillis();

    long duration = end - begin;
    logger.info("LoggingAspect @Around (" + method + "): Duration: " + duration + " ms");

    return result; // return result to the calling program
  }

  @Around("execution(* com.hvitoi.service.*.getFortune(..))")
  public Object afterGetFortuneHandleException(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
    String method = proceedingJoinPoint.getSignature().toShortString();
    logger.info("LoggingAspect @Around (" + method + ")");

    Object result = null;
    try {
      result = proceedingJoinPoint.proceed();
    } catch (Exception e) {
      logger.warning("LoggingAspect @Around (" + method + "): We have a problem " + e);
      result = "Nothing to do here"; // Exception is handled (it's never thrown to main app)
      // throw e; // optionally rethrow the exception
    }
    return result;
  }

}
