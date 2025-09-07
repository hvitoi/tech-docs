package com.hvitoi.demo.controller;

import java.time.LocalDateTime;
import java.util.Map;

import com.hvitoi.demo.entity.Person;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController // tells how to format the message (@ResponseBody + json serialize)
// @RequestMapping(value = "subpath", method = RequestMethod.GET )
public class HomeController {

  @GetMapping("/home")
  // @ResponseBody // if not used spring uses normal thymeleaf/jsp navigation
  public String helloWorld() {
    return "Hello World! Time on server is " + LocalDateTime.now();
  }

  @GetMapping("/myself")
  public Person mySelf(@RequestParam(required = false) String name) { // Optional<String> works the same
    return new Person(name, "Vitoi", 27); // serializes to json (uses the getters)
  }

  @GetMapping("/myparams")
  public String myParams(@RequestParam Map<String, String> allParams) {
    System.out.println(allParams);
    return "lol";
  }

}
