package com.hvitoi.demo.dao;

import java.util.List;

import javax.persistence.EntityManager;

import org.hibernate.Session;
import org.hibernate.query.Query;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.hvitoi.demo.entity.Employee;

// Hibernate API using HQL

@Repository
public class EmployeeDAOHibernateImpl implements EmployeeDAO {

	private EntityManager entityManager;

	@Autowired // constructor injection (field injection could be used too)
	public EmployeeDAOHibernateImpl(EntityManager entityManager) {
		this.entityManager = entityManager;
	}

	@Override
	public List<Employee> findAll() {
		// hibernate session
		Session session = entityManager.unwrap(Session.class);

		// build query
		Query<Employee> query = session.createQuery("FROM Employee", Employee.class);

		// execute query
		List<Employee> employees = query.getResultList();

		// return
		return employees;
	}

	@Override
	public Employee findById(int id) {
		// hibernate session
		Session session = entityManager.unwrap(Session.class);

		// get employee
		Employee employee = session.get(Employee.class, id);

		// return
		return employee;
	}

	@Override
	public void save(Employee employee) {
		// hibernate session
		Session session = entityManager.unwrap(Session.class);

		// save or update employee
		session.saveOrUpdate(employee);
	}

	@Override
	public void deleteById(int id) {
		// hibernate session
		Session session = entityManager.unwrap(Session.class);

		// build query
		Query query = session.createQuery("DELETE FROM Employee WHERE id=:employeeId");
		query.setParameter("employeeId", id);

		// execute query
		query.executeUpdate();
	}

}
