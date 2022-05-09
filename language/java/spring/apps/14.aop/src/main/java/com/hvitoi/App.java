package com.hvitoi;

import java.util.List;

import com.hvitoi.config.SpringConfig;
import com.hvitoi.dao.AccountDAO;
import com.hvitoi.entity.Account;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class App {
  public static void main(String[] args) {
    AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(SpringConfig.class);
    AccountDAO accountDAO = context.getBean("accountDAO", AccountDAO.class); // get bean from spring container

    List<Account> accounts = accountDAO.findAccounts();
    System.out.println(accounts);

    context.close();
  }
}
