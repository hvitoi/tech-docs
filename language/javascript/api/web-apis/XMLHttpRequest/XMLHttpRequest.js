var http = new XMLHttpRequest();

http.onreadystatechange = () => {
  if (this.readyState == 4 && this.status == 200) {
    // JSON response
    const res = http.responseText;
    console.log(res);

    // Parsed response
    res = JSON.parse(http.responseText);
    console.log(res);

    // Render HTML
    const renderedHtml = res.people
      .map((person) => {
        return `
				<li>
					<b>Nome</b>: ${person.name}
					<b>Idade</b>: ${person.age}
				</li>
			`;
      })
      .join("");
    document.getElementById("people").innerHTML = renderedHtml;
  }
};

http.open("GET", "people.json", true);
http.send();
