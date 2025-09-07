package com.hvitoi.demo.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import java.util.List;

import com.hvitoi.demo.entity.Employee;

// Spring Data JPA

@RepositoryRestResource(path = "employees") // if not specified "employee + s" will be used
public interface EmployeeRepository extends JpaRepository<Employee, Integer> { // CrudRepository

	// Give "Entity Type" and "Primary Key" and receive a funcional DAO
	// There is no implementation, just the interface

	// add a method to sort by last name
	public List<Employee> findAllByOrderByLastNameAsc(); // Spring Data JPA will parse the method name and create the
																												// query for this query automatically

}
