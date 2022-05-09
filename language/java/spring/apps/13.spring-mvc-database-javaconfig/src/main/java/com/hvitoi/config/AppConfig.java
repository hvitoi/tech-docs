package com.hvitoi.config;

import java.beans.PropertyVetoException;
import java.util.Properties;
import java.util.logging.Logger;

import javax.sql.DataSource;

import com.mchange.v2.c3p0.ComboPooledDataSource;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.core.env.Environment;
import org.springframework.orm.hibernate5.HibernateTransactionManager;
import org.springframework.orm.hibernate5.LocalSessionFactoryBean;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.web.servlet.ViewResolver;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.web.servlet.view.InternalResourceViewResolver;

@Configuration
@EnableWebMvc
@EnableTransactionManagement // hibernate transactions
@ComponentScan(basePackages = "com.hvitoi")
@PropertySource("classpath:persistence-mysql.properties") // src/main/resources is copied to classpath during build
public class AppConfig implements WebMvcConfigurer {

  private Logger logger = Logger.getLogger(getClass().getName());

  @Autowired
  Environment env; // load envs from .properties files

  @Override
  public void addResourceHandlers(ResourceHandlerRegistry registry) {
    registry.addResourceHandler("/awesome-content/**").addResourceLocations("/resources/");
  }

  // View resolver
  @Bean
  public ViewResolver viewResolver() {
    InternalResourceViewResolver viewResolver = new InternalResourceViewResolver();
    viewResolver.setPrefix("/WEB-INF/view/");
    viewResolver.setSuffix(".jsp");
    return viewResolver;
  }

  // Data source object
  @Bean
  public DataSource dataSource() {
    // create connection pool
    ComboPooledDataSource dataSource = new ComboPooledDataSource();

    // set jdbc driver class
    try {
      dataSource.setDriverClass(env.getProperty("jdbc.driver"));
    } catch (PropertyVetoException e) {
      throw new RuntimeException(e);
    }

    // log connection props
    logger.info("jdbc.url=" + env.getProperty("jdbc.url"));
    logger.info("jdbc.user=" + env.getProperty("jdbc.user"));

    // set database connection props
    dataSource.setJdbcUrl(env.getProperty("jdbc.url"));
    dataSource.setUser(env.getProperty("jdbc.user"));
    dataSource.setPassword(env.getProperty("jdbc.password"));

    // set connection pool props
    dataSource.setInitialPoolSize(Integer.parseInt(env.getProperty("connection.pool.initialPoolSize")));
    dataSource.setMinPoolSize(Integer.parseInt(env.getProperty("connection.pool.minPoolSize")));
    dataSource.setMaxPoolSize(Integer.parseInt(env.getProperty("connection.pool.maxPoolSize")));
    dataSource.setMaxIdleTime(Integer.parseInt(env.getProperty("connection.pool.maxIdleTime")));

    return dataSource;
  }

  @Bean
  public LocalSessionFactoryBean sessionFactory() {
    // create session factory
    LocalSessionFactoryBean sessionFactory = new LocalSessionFactoryBean();

    // create properties
    Properties props = new Properties();
    props.setProperty("hibernate.dialect", env.getProperty("hibernate.dialect"));
    props.setProperty("hibernate.show_sql", env.getProperty("hibernate.show_sql"));

    // set the properties
    sessionFactory.setDataSource(dataSource());
    sessionFactory.setPackagesToScan(env.getProperty("hibernate.packagesToScan"));
    sessionFactory.setHibernateProperties(props);

    return sessionFactory;
  }

  @Bean
  @Autowired
  public HibernateTransactionManager transactionManager(SessionFactory sessionFactory) {
    // setup transaction manager based on session factory
    HibernateTransactionManager txManager = new HibernateTransactionManager();
    txManager.setSessionFactory(sessionFactory);
    return txManager;
  }

}
