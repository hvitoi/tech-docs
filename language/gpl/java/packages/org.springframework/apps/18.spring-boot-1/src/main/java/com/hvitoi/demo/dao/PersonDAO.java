package com.hvitoi.demo.dao;

import java.util.List;

import com.hvitoi.demo.entity.Person;

public interface PersonDAO {

	public List<Person> findAll();

	public Person findById(int id);

	public void save(Person person);

	public void deleteById(int id);

}
