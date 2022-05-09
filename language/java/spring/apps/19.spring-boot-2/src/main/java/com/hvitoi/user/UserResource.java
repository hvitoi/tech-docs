package com.hvitoi.user;

import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.linkTo;
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.methodOn;

import java.net.URI;
import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.server.mvc.WebMvcLinkBuilder;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

@RestController
public class UserResource {

	@Autowired
	private UserDao userDao;

	@GetMapping("/users")
	public List<User> retrieveAllUsers() {
		return userDao.findAll();
	}

	@GetMapping("/users/{id}")
	// EntityModel implements HATEOS (user data + links)
	public EntityModel<User> retrieveUser(@PathVariable int id) {
		User user = userDao.findOne(id);

		if (user == null) {
			throw new UserNotFoundException("id-" + id);
		}

		// HATEOAS
		EntityModel<User> resource = EntityModel.of(user);
		WebMvcLinkBuilder linkTo = linkTo(methodOn(this.getClass()).retrieveAllUsers()); // link to allUsers
		resource.add(linkTo.withRel("all-users")); // name of the method in the json

		return resource;
	}

	@DeleteMapping("/users/{id}")
	public void deleteUser(@PathVariable int id) {
		User user = userDao.deleteById(id);

		if (user == null) {
			throw new UserNotFoundException("id-" + id);
		}
	}

	@PostMapping("/users")
	public ResponseEntity<Object> createUser(@Valid @RequestBody User user) {
		User savedUser = userDao.save(user);

		URI location = ServletUriComponentsBuilder//
				.fromCurrentRequest() // get current URI
				.path("/{id}") // append the id
				.buildAndExpand(savedUser.getId()) // tell who is the id
				.toUri(); // build URI

		// Modify the response (created status code)
		// "Location" header points to the newly created resource
		return ResponseEntity.created(location).build();

	}
}
