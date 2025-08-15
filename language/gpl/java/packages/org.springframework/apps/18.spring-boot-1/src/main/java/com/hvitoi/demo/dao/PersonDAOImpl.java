package com.hvitoi.demo.dao;

import java.util.ArrayList;
import java.util.List;

import com.hvitoi.demo.entity.Person;

import org.springframework.stereotype.Repository;

@Repository
public class PersonDAOImpl implements PersonDAO {

  // in-memory database
  private static List<Person> people = new ArrayList<>();
  private static int peopleCount = 3;

  static {
    people.add(new Person("Henry", "Doe", 14));
    people.add(new Person("Albert", "Doe", 14));
    people.add(new Person("John", "Doe", 14));
  }

  @Override
  public List<Person> findAll() {
    return people;
  }

  @Override
  public Person findById(int id) {
    for (Person person : people) {
      if (person.getId() == id) {
        return person;
      }
    }
    return null;
  }

  @Override
  public void save(Person person) {
    peopleCount++;
    person.setId(peopleCount);
    people.add(person);

  }

  @Override
  public void deleteById(int id) {
    // TODO Auto-generated method stub

  }

}