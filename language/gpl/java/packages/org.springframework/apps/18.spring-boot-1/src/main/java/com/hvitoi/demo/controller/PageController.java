
package com.hvitoi.demo.controller;

import java.util.ArrayList;
import java.util.List;

import javax.annotation.PostConstruct;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.hvitoi.demo.entity.Employee;
import com.hvitoi.demo.service.EmployeeService;

@Controller
@RequestMapping("/pages")
public class PageController {

	@Autowired
	private EmployeeService employeeService;

	private List<Employee> employees;

	@PostConstruct
	private void loadData() {
		// // create employees
		// Employee emp1 = new Employee(1, "Leslie", "Andrews", "leslie@luv2code.com");
		// Employee emp2 = new Employee(2, "Emma", "Baumgarten", "emma@luv2code.com");
		// Employee emp3 = new Employee(3, "Avani", "Gupta", "avani@luv2code.com");

		// // create the list
		// employees = new ArrayList<>();

		// // add to the list
		// employees.add(emp1);
		// employees.add(emp2);
		// employees.add(emp3);
	}

	@GetMapping("/hello")
	public String sayHello(Model model) {
		model.addAttribute("theDate", new java.util.Date());
		return "hello-world"; // look at src/main/resources/templates
	}

	@GetMapping("/list")
	public String listEmployees(Model model) {

		// get employees
		List<Employee> employees = employeeService.findAll();

		// add to the spring model
		model.addAttribute("employees", employees);

		return "employees/list-employees";
	}

	@PostMapping("/save")
	public String saveEmployee(@ModelAttribute("employee") Employee employee) {
		// save employee
		employeeService.save(employee);

		// redirect (prevent duplicates)
		return "redirect:/pages/list"; // post-redirect-get Pattern
	}

	@GetMapping("/delete")
	public String delete(@RequestParam("employeeId") int id) {

		// delete employee
		employeeService.deleteById(id);

		// redirect
		return "redirect:/pages/list";

	}

	@GetMapping("/showFormForAdd")
	public String showFormForAdd(Model model) {

		// create empty employee
		Employee employee = new Employee();

		// set model attribute (thymelead will use it for binding form data)
		model.addAttribute("employee", employee);

		// send to form
		return "employees/employee-form";
	}

	@GetMapping("/showFormForUpdate")
	public String showFormForUpdate(@RequestParam("employeeId") int id, Model model) {

		// get employee
		Employee employee = employeeService.findById(id);

		// set model attribute to pre-populate the form
		model.addAttribute("employee", employee);

		// send to form
		return "employees/employee-form";
	}
}
