<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
  <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
    <%@ page import="com.hvitoi.util.SortUtils" %>


      <!DOCTYPE html>

      <html>
      <header>
        <title>List Customers</title>
        <link type="text/css" rel="stylesheet"
          href="${pageContext.request.contextPath}/awesome-content/css/style.css" />
      </header>

      <body>
        <div id="wrapper">
          <div id="header">
            <h2>CRM - Customer Relationship Manager</h2>
          </div>
        </div>
        <div id="container">
          <div id="content">
            <!-- calls spring controller route on add customer -->
            <input type="button" class="add-button" value="Add Customer"
              onclick="window.location.href='showFormForAdd'; return false;" />

            <!--  add a search box -->
            <form:form action="search" method="GET">
              Search customer: <input type="text" name="searchKeyword" />
              <input type="submit" value="Search" class="add-button" />
            </form:form>

            <table>
              <c:url var="sortLinkFirstName" value="/customer/list">
                <!-- construct a sort link for first name -->
                <c:param name="sort" value="<%= Integer.toString(SortUtils.FIRST_NAME) %>" />
              </c:url>

              <c:url var="sortLinkLastName" value="/customer/list">
                <!-- construct a sort link for last name -->
                <c:param name="sort" value="<%= Integer.toString(SortUtils.LAST_NAME) %>" />
              </c:url>

              <c:url var="sortLinkEmail" value="/customer/list">
                <!-- construct a sort link for email -->
                <c:param name="sort" value="<%= Integer.toString(SortUtils.EMAIL) %>" />
              </c:url>

              <tr>
                <th><a href="${sortLinkFirstName}">First Name</a></th>
                <th><a href="${sortLinkLastName}">Last Name</a></th>
                <th><a href="${sortLinkEmail}">Email</a></th>
                <th>Action</th>
              </tr>
              <!-- loop through "customers" attribute -->
              <c:forEach var="customer" items="${customers}">

                <c:url var="updateLink" value="/customer/showFormForUpdate">
                  <!-- create clickable link /customer/showFormForUpdate?customerId={customer.id} -->
                  <c:param name="customerId" value="${customer.id}"></c:param>
                </c:url>

                <c:url var="deleteLink" value="/customer/deleteCustomer">
                  <c:param name="customerId" value="${customer.id}"></c:param>
                </c:url>



                <tr>
                  <td>${customer.firstName}</td>
                  <td>${customer.lastName}</td>
                  <td>${customer.email}</td>
                  <td>
                    <a href="${updateLink}">Update</a>|
                    <a href="${deleteLink}" onclick="return confirm('Are you sure?')">Delete</a>
                  </td>
                </tr>

              </c:forEach>
            </table>
          </div>
        </div>
      </body>

      </html>