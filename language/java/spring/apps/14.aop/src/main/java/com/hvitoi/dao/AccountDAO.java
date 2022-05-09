package com.hvitoi.dao;

import java.util.ArrayList;
import java.util.List;

import com.hvitoi.entity.Account;

import org.springframework.stereotype.Component;

@Component
public class AccountDAO {
  private String name;
  private String serviceCode;

  public List<Account> findAccounts() {
    List<Account> accounts = new ArrayList<>();
    Account acc1 = new Account("John", "Silver");
    Account acc2 = new Account("Senna", "Gold");
    Account acc3 = new Account("Lucca", "Platinum");
    accounts.add(acc1);
    accounts.add(acc2);
    accounts.add(acc3);
    return accounts;
  }

  public void addAccount(Account account, boolean vipFlag) {
    System.out.println(getClass() + "db work add account");
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getServiceCode() {
    return serviceCode;
  }

  public void setServiceCode(String serviceCode) {
    this.serviceCode = serviceCode;
  }

}
