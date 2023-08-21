package store

import "github.com/gin-gonic/gin"



func StoresRouter(inComingRoutes *gin.Engine) {
	inComingRoutes.GET("/store", getStores())
}