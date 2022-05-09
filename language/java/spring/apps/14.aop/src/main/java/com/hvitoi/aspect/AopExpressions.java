package com.hvitoi.aspect;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;

// Pointcut declarations (using pointcut expressions)
@Aspect
public class AopExpressions {
  @Pointcut("execution(* add*(com.hvitoi.entity.Account, ..))")
  public void forDaoPackage() {
  }

  @Pointcut("execution(* com.hvitoi.dao.*.get(..))")
  public void getter() {
  }

  @Pointcut("execution(* com.hvitoi.dao.*.setter(..))")
  public void setter() {
  }

  @Pointcut("forDaoPackage() && !(getter() || setter())")
  public void forDaoPackageNoGetterSetter() {
  }
}
