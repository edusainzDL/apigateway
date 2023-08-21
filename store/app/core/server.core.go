package core;

import "github.com/gin-gonic/gin"

func engine() *gin.Engine{
	r := gin.Default()
	return r
}
