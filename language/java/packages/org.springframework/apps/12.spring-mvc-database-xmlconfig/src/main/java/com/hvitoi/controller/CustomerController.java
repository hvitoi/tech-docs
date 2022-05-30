package com.hvitoi.controller;

import java.util.List;

import com.hvitoi.entity.Customer;
import com.hvitoi.service.CustomerService;
import com.hvitoi.util.SortUtils;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/customer") // Handles any method, GET, POST, PATCH, etc
public class CustomerController {

  @Autowired
  private CustomerService customerService;

  // @RequestMapping(path="/list",method=RequestMethod.GET)
  @GetMapping("/list")
  public String listCustomers(Model model, @RequestParam(required = false) String sort) {
    List<Customer> customers = null;

    if (sort != null) { // check if sorting is required
      int sortField = Integer.parseInt(sort);
      customers = customerService.getCustomers(sortField);
    } else { // no sort field provided ... default to sorting by last name
      customers = customerService.getCustomers(SortUtils.LAST_NAME);
    }

    model.addAttribute("customers", customers); // model for display
    return "list-customers";
  }

  @PostMapping("/saveCustomer")
  public String saveCustomer(@ModelAttribute("customer") Customer customer) {
    customerService.saveCustomer(customer);
    return "redirect:/customer/list";
  }

  @GetMapping("/showFormForAdd")
  public String showFormForAdd(Model model) {
    Customer customer = new Customer();
    model.addAttribute("customer", customer);
    return "customer-form";
  }

  @GetMapping("/showFormForUpdate")
  public String showFormForUpdate(@RequestParam("customerId") int id, Model model) {
    Customer customer = customerService.getCustomer(id);
    model.addAttribute("customer", customer); // to prepopulate the form
    return "customer-form";
  }

  @GetMapping("/deleteCustomer")
  public String deleteCustomer(@RequestParam("customerId") int id) {
    customerService.deleteCustomer(id);
    return "redirect:/customer/list";
  }

  @GetMapping("/search")
  public String searchCustomers(@RequestParam("searchKeyword") String searchKeyword, Model model) {
    List<Customer> customers = customerService.searchCustomers(searchKeyword);
    model.addAttribute("customers", customers);
    return "list-customers";
  }

}
