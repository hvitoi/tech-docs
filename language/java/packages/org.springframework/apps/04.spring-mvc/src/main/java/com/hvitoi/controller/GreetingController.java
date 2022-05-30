package com.hvitoi.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import javax.servlet.http.HttpServletRequest;

@Controller
@RequestMapping("/hello") // parent mapping
public class GreetingController {

    @RequestMapping("/showForm") // /hello/showForm
    public String showForm() {
        return "greeting-form";
    }

    @RequestMapping("/greeting")
    public String processForm() {
        return "greeting-display";
    }

    // method to read form data
    @RequestMapping("/yoGreeting")
    public String shoutName(HttpServletRequest request, Model model) {

        String studentName = request.getParameter("studentName"); // GET param
        String greetingMessage = "Yo! " + studentName.toUpperCase();

        // add "message" attribute to the model
        model.addAttribute("message", greetingMessage);

        return "greeting-display";
    }

    @RequestMapping("/heyGreeting")
    public String shoutNameDifferently(@RequestParam("studentName") String studentName /* take name from GET params */,
            Model model) {

        String greetingMessage = "Hey! " + studentName.toUpperCase();

        // add "message" attribute to the model
        model.addAttribute("message", greetingMessage);

        return "greeting-display";
    }
}
