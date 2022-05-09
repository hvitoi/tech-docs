package com.hvitoi.validation;

import javax.validation.Constraint;
import javax.validation.Payload;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Constraint(validatedBy = CourseCodeConstraintValidator.class) // Class with the business logic for the validator
@Target({ ElementType.METHOD, ElementType.FIELD }) // Where to apply this annotation: Methods and Fields
@Retention(RetentionPolicy.RUNTIME) // How long the annotation will be stored/used. Retain at source code and use at
                                    // runtime by the JVM
public @interface CourseCode {
    // default value
    public String[] value() default { "LUV" }; // Validate against an array of strings

    // default message (for errors)
    public String message() default "must start with LUV";

    // default groups
    public Class<?>[] groups() default {};

    // default payloads
    public Class<? extends Payload>[] payload() default {};
}
