package com.hvitoi.config;

import org.springframework.web.servlet.support.AbstractAnnotationConfigDispatcherServletInitializer;

// This is equivalent to the web.xml
public class DispatcherServletInitializer extends AbstractAnnotationConfigDispatcherServletInitializer {

  @Override
  protected Class<?>[] getRootConfigClasses() {
    // No root config classes for the project
    return null;
  }

  @Override
  protected Class<?>[] getServletConfigClasses() {
    return new Class[] { AppConfig.class };
  }

  @Override
  protected String[] getServletMappings() {

    return new String[] { "/" };
  }

}
