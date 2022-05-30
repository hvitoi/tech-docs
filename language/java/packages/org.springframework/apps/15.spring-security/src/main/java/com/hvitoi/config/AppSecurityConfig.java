package com.hvitoi.config;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableWebSecurity
public class AppSecurityConfig extends WebSecurityConfigurerAdapter {

  @Autowired
  private DataSource dataSource; // data source with user information

  @Override
  protected void configure(AuthenticationManagerBuilder auth) throws Exception {
    // SQL Database
    auth.jdbcAuthentication().dataSource(dataSource);

    // In Memory Database
    // UserBuilder users = User.withDefaultPasswordEncoder();
    // auth.inMemoryAuthentication()//
    // .withUser(users.username("john").password("123").roles("EMPLOYEE"))
    // .withUser(users.username("maria").password("123").roles("MANAGER"))
    // .withUser(users.username("henry").password("123").roles("ADMIN"))
    // .withUser(users.username("lucca").password("123").roles("ADMIN", "MANAGER"));

  }

  @Override
  protected void configure(HttpSecurity http) throws Exception {
    // Provide custom login page and processing route
    http //
        .authorizeRequests() // restrict access based on HttpServletRequest
        // .anyRequest().authenticated() // any request must be authenticated
        .antMatchers("/").hasRole("EMPLOYEE")//
        .antMatchers("/leaders/**").hasRole("MANAGER")//
        .antMatchers("/systems/**").hasRole("ADMIN")

        .and() //
        .formLogin() //
        .loginPage("/showMyLoginPage") // custom login with <form:form> tag
        .loginProcessingUrl("/authenticateTheUser") // route that handles the auth data
        .permitAll() // allow everyone to see login page

        .and()//
        .logout() // /logout by default
        .permitAll()

        .and()//
        .exceptionHandling()//
        .accessDeniedPage("/access-denied");
  }

}
