package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.New() // no middleware
	// r := gin.Default() // middlewares: gin.New() + Logger + Recovery

	// Add middlewares to the router
	r.Use(gin.Recovery(), Timer())

	r.StaticFile("/", "./public/index.html")
	r.Static("/assets", "./public/assets")

	r.GET("/health", func(c *gin.Context) {
		c.String(http.StatusOK, "ok")
	})

	api := r.Group("/api", APIKey("secret"))
	{
		api.GET("/greet/:name", greet)
		api.GET("/divide", divide)
	}

	r.Run(":8080")
}
