package com.hvitoi.demo.dao;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.Query;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.hvitoi.demo.entity.Employee;

// Standard JPA API using JPQL

@Repository
public class EmployeeDAOJpaImpl implements EmployeeDAO {

	@Autowired
	private EntityManager entityManager;

	@Override
	public List<Employee> findAll() {
		// build query
		Query query = entityManager.createQuery("FROM Employee");

		// execute query
		List<Employee> employees = query.getResultList();

		// return
		return employees;

	}

	@Override
	public Employee findById(int id) {

		// get employee
		Employee employee = entityManager.find(Employee.class, id);

		// return employee
		return employee;
	}

	@Override
	public void save(Employee employee) {

		// save or update employee
		Employee dbEmployee = entityManager.merge(employee); // if id==0 then save new employee

		// update its id (from database) to return the generated ID
		employee.setId(dbEmployee.getId());

	}

	@Override
	public void deleteById(int id) {

		// build query
		Query query = entityManager.createQuery("DELETE FROM Employee WHERE id=:employeeId");
		query.setParameter("employeeId", id);

		// execute query
		query.executeUpdate();
	}

}
