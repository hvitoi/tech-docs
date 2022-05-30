package com.hvitoi.dao;

import java.util.List;

import com.hvitoi.entity.Customer;
import com.hvitoi.util.SortUtils;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.query.Query;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class CustomerDAOImpl implements CustomerDAO {

  @Autowired // inject dependency
  private SessionFactory sessionFactory;

  @Override
  public List<Customer> getCustomers(int sortField) {
    Session session = sessionFactory.getCurrentSession();

    String fieldName = null;
    switch (sortField) {
      case SortUtils.FIRST_NAME:
        fieldName = "firstName";
        break;
      case SortUtils.LAST_NAME:
        fieldName = "lastName";
        break;
      case SortUtils.EMAIL:
        fieldName = "email";
        break;
      default:
        fieldName = "lastName";
    }

    String queryString = "from Customer order by " + fieldName;
    Query<Customer> query = session.createQuery(queryString, Customer.class);

    List<Customer> customers = query.getResultList();
    return customers;

  }

  @Override
  public Customer getCustomer(int id) {
    Session session = sessionFactory.getCurrentSession();
    Customer customer = session.get(Customer.class, id);
    return customer;
  }

  @Override
  public void saveCustomer(Customer customer) {
    Session session = sessionFactory.getCurrentSession();
    session.saveOrUpdate(customer);
  }

  @Override
  public void deleteCustomer(int id) {
    Session session = sessionFactory.getCurrentSession();
    Query query = session.createQuery("DELETE FROM Customer WHERE id=:customerId");
    query.setParameter("customerId", id);
    query.executeUpdate();
  }

  @Override
  public List<Customer> searchCustomers(String searchKeyword) {
    Session session = sessionFactory.getCurrentSession();
    Query query = null;
    if (searchKeyword != null && searchKeyword.trim().length() > 0) {
      // search for firstName or lastName ... case insensitive
      query = session.createQuery("FROM Customer WHERE lower(firstName) LIKE :keyword OR lower(lastName) LIKE :keyword",
          Customer.class);
      query.setParameter("keyword", "%" + searchKeyword.toLowerCase() + "%");
    } else {
      // theSearchName is empty ... so just get all customers
      query = session.createQuery("FROM Customer", Customer.class);
    }
    List<Customer> customers = query.getResultList();
    return customers;
  }

}
