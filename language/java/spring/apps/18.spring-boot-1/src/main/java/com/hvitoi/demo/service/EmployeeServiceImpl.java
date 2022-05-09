package com.hvitoi.demo.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.hvitoi.demo.dao.EmployeeRepository;
import com.hvitoi.demo.entity.Employee;

@Service
public class EmployeeServiceImpl implements EmployeeService {

	// @Autowired
	// @Qualifier("employeeDAOHibernateImpl") // Multiple DAO implementations
	// private EmployeeDAO employeeDAO;

	@Autowired
	private EmployeeRepository employeeRepository;

	@Override
	// @Transactional // Spring JPA need no @Transactional annotation
	public List<Employee> findAll() {
		return employeeRepository.findAllByOrderByLastNameAsc();
	}

	@Override
	// @Transactional
	public Employee findById(int id) {
		// "Optional" is a pattern. Handle "null" values
		Optional<Employee> result = employeeRepository.findById(id);

		Employee employee = null;
		if (result.isPresent()) {
			employee = result.get();
		} else {
			throw new RuntimeException("Did not find employee id - " + id);
		}
		return employee;
	}

	@Override
	// @Transactional
	public void save(Employee employee) {
		employeeRepository.save(employee);
	}

	@Override
	// @Transactional
	public void deleteById(int id) {
		employeeRepository.deleteById(id);
	}

}
