package com.hvitoi.hibernate.entity;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity
@Table(name = "instructor")
public class Instructor {
  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  @Column(name = "id")
  private int id;

  @Column(name = "first_name")
  private String firstName;

  @Column(name = "last_name")
  private String lastName;

  @Column(name = "email")
  private String email;

  @OneToOne(cascade = CascadeType.ALL)
  @JoinColumn(name = "instructor_detail_id") // PK of the related table. Indicates the column to join on
  private InstructorDetail instructorDetail; // inject the related table

  @OneToMany(mappedBy = "instructor", fetch = FetchType.LAZY, cascade = { CascadeType.PERSIST, CascadeType.MERGE,
      CascadeType.DETACH, CascadeType.REFRESH }) // refers to "instructor" property in "Course" class
  private List<Course> courses; // new field (do not exist in the table)

  public Instructor() {
  }

  public Instructor(String firstName, String lastName, String email) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.email = email;
  }

  public int getId() {
    return id;
  }

  public void setId(int id) {
    this.id = id;
  }

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

  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }

  public InstructorDetail getInstructorDetail() {
    return instructorDetail;
  }

  public void setInstructorDetail(InstructorDetail instructorDetail) {
    this.instructorDetail = instructorDetail;
  }

  public List<Course> getCourses() {
    return courses;
  }

  public void setCourses(List<Course> courses) {
    this.courses = courses;
  }

  @Override
  public String toString() {
    return "Instructor [email=" + email + ", firstName=" + firstName + ", id=" + id + ", instructorDetail="
        + instructorDetail + ", lastName=" + lastName + "]";
  }

  // convenience method for the bidirectional relationship (optional)
  public void add(Course course) {
    if (courses == null) {
      courses = new ArrayList<>();
    }
    courses.add(course);
    course.setInstructor(this);
  }

}
