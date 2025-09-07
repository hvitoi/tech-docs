package com.hvitoi.dao;

import java.util.List;

import com.hvitoi.entity.Customer;

public interface CustomerDAO {
  public List<Customer> getCustomers(int sortField);

  public Customer getCustomer(int id);

  public void saveCustomer(Customer customer);

  public void deleteCustomer(int id);

  public List<Customer> searchCustomers(String searchKeyword);

}
