package com.hvitoi.controller;

import org.springframework.beans.propertyeditors.StringTrimmerEditor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.InitBinder;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.validation.Valid;

import com.hvitoi.entity.Customer;

@Controller
@RequestMapping("/customer")
public class CustomerController {

    // Pre-processing method. This method is called for every
    // web request coming to the controller
    @InitBinder
    public void initBinder(WebDataBinder dataBinder) {
        // Apply string processing: remove whitespaces (leading and trailing)
        dataBinder.registerCustomEditor(String.class, new StringTrimmerEditor(true));
    }

    @RequestMapping("/showForm")
    public String showForm(Model model) {
        // Create the customer instance so that the form can change it
        model.addAttribute("customer", new Customer());
        return "customer-form";
    }

    @RequestMapping("/processForm")
    public String processForm(@Valid @ModelAttribute("customer") Customer customer,
            BindingResult bindingResult /* Result of the validation. It must come after the @valid */) {

        System.out.printf("Last name: |" + customer.getLastName() + "|");
        System.out.println("Binding result: " + bindingResult);
        System.out.println("\n\n\n\n");

        if (bindingResult.hasErrors()) {
            return "customer-form";
        } else {
            return "customer-confirmation";
        }
    }

}
