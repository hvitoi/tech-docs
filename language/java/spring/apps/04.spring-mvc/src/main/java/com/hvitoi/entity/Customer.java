package com.hvitoi.entity;

import javax.validation.constraints.*;

import com.hvitoi.validation.CourseCode;

public class Customer {
    private String firstName;

    @NotNull(message = "must not be null")
    @Size(min = 3, message = "not long enough")
    private String lastName;

    @NotNull(message = "is required")
    @Min(value = 0, message = "must be equal or greater than zero")
    @Max(value = 10, message = "must be equal or less than ten")
    private Integer freePasses; // if the type is 'int', initBinder will trim it to string 'null'

    @Pattern(regexp = "^[a-zA-Z0-9]{5}", message = "only 5 chars/digits")
    private String postalCode;

    @CourseCode
    // @CourseCode(value={"TOPS", "LUV"}, message="must start with LUV") is the
    // default
    private String courseCode;

    // ---

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public Integer getFreePasses() {
        return freePasses;
    }

    public void setFreePasses(Integer freePasses) {
        this.freePasses = freePasses;
    }

    public String getPostalCode() {
        return postalCode;
    }

    public void setPostalCode(String postalCode) {
        this.postalCode = postalCode;
    }

    public String getCourseCode() {
        return courseCode;
    }

    public void setCourseCode(String courseCode) {
        this.courseCode = courseCode;
    }
}
