package com.hvitoi.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

  public static void main(String[] args) {
    SpringApplication.run(DemoApplication.class, args);
  }

  // beans can be manually created here
  // @Bean
  // public DataSource dataSource(){
  // DriverManagerDataSource dataSource = new DriverManagerDataSource();
  // dataSource.setDriverClassName("com.mysql.jdbc.Driver");
  // dataSource.setUrl("jdbc:mysql://localhost:3306/listavip");
  // dataSource.setUsername("root");
  // dataSource.setPassword("root");
  // return dataSource;
  // }

}
