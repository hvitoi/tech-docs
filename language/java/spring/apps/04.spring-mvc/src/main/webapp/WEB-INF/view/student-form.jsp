<!-- Spring MVC form tags -->
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>

<!DOCTYPE html>
<html>

<head>
    <title>Student Registration Form</title>
</head>

<body>
    <!-- work with the "student" attribute -->
    <form:form action="processForm" modelAttribute="student">

        First name:
        <form:input path="firstName" /> <!-- student.getFirstName() -->
        <br />

        Last name:
        <form:input path="lastName" /> <!-- student.getLastName() -->
        <br />

        Country:
        <form:select path="country">
            <%-- <form:option value="Brazil" label="Brazil" />--%>
            <%-- <form:option value="France" label="France" />--%>
            <%-- <form:option value="Germany" label="Germany" />--%>
            <%-- <form:option value="India" label="India" />--%>
            <form:options items="${student.countryOptions}" /> <!-- Get countries from the linkedHashMap -->
        </form:select>
        <br />

        Favorite language:
        Java
        <form:radiobutton path="favoriteLanguage" value="Java" /> <!-- Calls student.setFavoriteLanguage("Java") -->
        C#
        <form:radiobutton path="favoriteLanguage" value="C#" />
        PHP
        <form:radiobutton path="favoriteLanguage" value="PHP" />
        Ruby
        <form:radiobutton path="favoriteLanguage" value="Ruby" />
        <br />

        Operating Systems:
        <!-- property must be an array! Multiple options can be selected -->
        Linux:
        <form:checkbox path="operatingSystems" value="Linux" />
        MacOS:
        <form:checkbox path="operatingSystems" value="MacOS" />
        Windows:
        <form:checkbox path="operatingSystems" value="Windows" />

        <br />
        <input type="submit" value="Submit" /> <!-- Calls: student.setFirstName() and student.setLastName() -->

    </form:form>
</body>

</html>