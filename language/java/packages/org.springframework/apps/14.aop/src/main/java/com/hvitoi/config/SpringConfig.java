package com.hvitoi.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;

@Configuration // pure java spring config
@EnableAspectJAutoProxy // enable spring AOP Proxy support
@ComponentScan("com.hvitoi") // scans @Component annotations and create beans
public class SpringConfig {
}
