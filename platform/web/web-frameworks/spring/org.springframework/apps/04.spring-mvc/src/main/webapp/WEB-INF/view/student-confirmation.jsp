<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>

<head>
    <title>Student Confirmation</title>
</head>

<body>
    <!-- Call getFirstName and getLastName  -->
    The student is confirmed: ${student.firstName} ${student.lastName}
    <br />

    Country: ${student.country}
    <br />

    Favorite language: ${student.favoriteLanguage}
    <br />

    Operating Systems language:
    <ul>
        <c:forEach var="temp" items="${student.operatingSystems}">
            <li>${temp}</li>
        </c:forEach>
    </ul>
    <br />
</body>

</html>