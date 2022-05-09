<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %> <%@
taglib prefix="security" uri="http://www.springframework.org/security/tags" %>
<html>
  <head>
    <title>Company Homepage</title>
  </head>

  <body>
    <h2>My Homepage</h2>
    <hr />
    Welcome!

    <!-- display user name and role -->

    <p>
      User: <security:authentication property="principal.username" />
      <br /><br />
      Role(s): <security:authentication property="principal.authorities" />
    </p>

    <hr />

    <!-- /leaders route  -->
    <security:authorize access="hasRole('MANAGER')">
      <p>
        <a href="${pageContext.request.contextPath}/leaders"
          >Leadership Meeting</a
        >
        (Only for Manager peeps)
      </p>
    </security:authorize>

    <!-- /systems route  -->
    <security:authorize access="hasRole('ADMIN')">
      <p>
        <a href="${pageContext.request.contextPath}/systems"
          >IT Systems Meeting</a
        >
        (Only for Admin peeps)
      </p>
    </security:authorize>

    <!-- logout button -->
    <form:form action="${pageContext.request.contextPath}/logout" method="POST">
      <input type="submit" value="Logout" />
    </form:form>
  </body>
</html>
