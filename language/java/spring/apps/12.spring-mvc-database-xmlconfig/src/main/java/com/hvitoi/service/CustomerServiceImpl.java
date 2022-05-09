package com.hvitoi.service;

import java.util.List;

import com.hvitoi.dao.CustomerDAO;
import com.hvitoi.entity.Customer;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class CustomerServiceImpl implements CustomerService {

  @Autowired
  private CustomerDAO customerDAO; // scans all components that implements this interface and picks the first

  @Override
  @Transactional // Automatically starts and commits transactions)
  public List<Customer> getCustomers(int sortField) {
    return customerDAO.getCustomers(sortField);
  }

  @Override
  @Transactional
  public Customer getCustomer(int id) {
    return customerDAO.getCustomer(id);
  }

  @Override
  @Transactional
  public void saveCustomer(Customer customer) {
    customerDAO.saveCustomer(customer);
  }

  @Override
  @Transactional
  public void deleteCustomer(int id) {
    customerDAO.deleteCustomer(id);
  }

  @Override
  @Transactional
  public List<Customer> searchCustomers(String searchKeyword) {
    return customerDAO.searchCustomers(searchKeyword);
  }

}
