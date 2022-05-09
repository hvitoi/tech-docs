package com.hvitoi.controller;

import java.util.ArrayList;
import java.util.List;

import javax.annotation.PostConstruct;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.hvitoi.entity.Student;
import com.hvitoi.exception.StudentNotFoundException;

@RestController
@RequestMapping("/api")
public class StudentController {
	private List<Student> students;

	@PostConstruct // called only once when the bean is constructed
	public void loadData() {
		students = new ArrayList<>();
		students.add(new Student("Poornima", "Patel"));
		students.add(new Student("Mario", "Rossi"));
		students.add(new Student("Mary", "Smith"));
	}

	@GetMapping("/students")
	public List<Student> getStudents() {
		return students; // students object will be serialized into json
	}

	@GetMapping("/students/{studentId}")
	public Student getStudent(@PathVariable int studentId) {

		if ((studentId >= students.size()) || (studentId < 0)) {
			throw new StudentNotFoundException("Student id not found - " + studentId);
		}

		return students.get(studentId);
	}

}
