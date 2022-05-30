package com.hvitoi.service;

import java.util.List;

import com.hvitoi.entity.Customer;

public interface CustomerService {
  public List<Customer> getCustomers(int sortField);

  public Customer getCustomer(int id);

  public void saveCustomer(Customer customer);

  public void deleteCustomer(int id);

  public List<Customer> searchCustomers(String searchKeyword);

}
