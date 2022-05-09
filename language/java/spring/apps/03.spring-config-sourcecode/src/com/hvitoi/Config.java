package com.hvitoi;

import com.hvitoi.coach.Coach;
import com.hvitoi.coach.SwimCoach;
import com.hvitoi.coach.TennisCoach;
import com.hvitoi.fortune.FortuneService;
import com.hvitoi.fortune.SadFortuneService;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
// @ComponentScan("com.hvitoi")
// Componentscan should not be annotated if beans are manually created
@PropertySource("classpath:sport.properties")
public class Config {
    @Bean
    public FortuneService sadFortuneService() {
        return new SadFortuneService();
    }

    @Bean
    public Coach swimCoach() {
        return new SwimCoach(sadFortuneService());
    }

    @Bean
    public Coach tennisCoach() {
        return new TennisCoach();
    }
}
