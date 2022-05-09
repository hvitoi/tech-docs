package com.hvitoi.versioning;

import org.springframework.web.bind.annotation.GetMapping;

//@RestController
public class PersonVersioningController {

	// "URI" versioning
	@GetMapping("v1/person")
	public PersonV1 personV1() {
		return new PersonV1("Bob Charlie");
	}

	@GetMapping("v2/person")
	public PersonV2 personV2() {
		return new PersonV2(new Name("Bob", "Charlie"));
	}

	// "Request parameter" versioning
	@GetMapping(value = "/person/param", params = "version=1") // person/param?version=1
	public PersonV1 paramV1() {
		return new PersonV1("Bob Charlie");
	}

	@GetMapping(value = "/person/param", params = "version=2") // person/param?version=2
	public PersonV2 paramV2() {
		return new PersonV2(new Name("Bob", "Charlie"));
	}

	// "Header" versioning
	@GetMapping(value = "/person/header", headers = "X-API-VERSION=1")
	public PersonV1 headerV1() {
		return new PersonV1("Bob Charlie");
	}

	@GetMapping(value = "/person/header", headers = "X-API-VERSION=2")
	public PersonV2 headerV2() {
		return new PersonV2(new Name("Bob", "Charlie"));
	}

	// "Accept Header" versioning (media type versioning - content negotiation)
	@GetMapping(value = "/person/produces", produces = "application/vnd.company.app-v1+json")
	public PersonV1 producesV1() {
		return new PersonV1("Bob Charlie");
	}

	@GetMapping(value = "/person/produces", produces = "application/vnd.company.app-v2+json")
	public PersonV2 producesV2() {
		return new PersonV2(new Name("Bob", "Charlie"));
	}

}
