package main

import (
	"net/http"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

func greet(c *gin.Context) {
	msg := "Hello, " + c.Param("name") + "!"
	if c.Query("shout") == "true" {
		msg = strings.ToUpper(msg)
	}
	c.JSON(http.StatusOK, gin.H{"message": msg})
}

func divide(c *gin.Context) {
	a, err := strconv.Atoi(c.Query("a"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "a must be an integer"})
		return
	}
	b, err := strconv.Atoi(c.Query("b"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "b must be an integer"})
		return
	}
	if b == 0 {
		c.JSON(http.StatusBadRequest, gin.H{"error": "cannot divide by zero"})
		return
	}
	c.JSON(http.StatusOK, gin.H{"result": a / b})
}
