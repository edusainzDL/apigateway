package store

import "github.com/gin-gonic/gin"
import "gorm.io/gorm"

func StoresRouter(inComingRoutes *gin.Engine, db *gorm.DB) {
	inComingRoutes.GET("/store", getStores(db))
	inComingRoutes.POST("/store", CreateStore(db))
}