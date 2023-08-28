package store

import "github.com/gin-gonic/gin"
import "net/http"
import "fmt"
import "gorm.io/gorm"


func getStores(db *gorm.DB) gin.HandlerFunc {
	return func (c *gin.Context) {
		stores := dao_get_stores(db)
		var __stores []Store
		for store := range stores {

			sto := GetStoreSchema(stores[store])
			__stores = append(__stores,sto)
		}
		ResponseStoreAll(c, __stores)
	}
}

func CreateStore(db *gorm.DB) gin.HandlerFunc {
	return func (c *gin.Context) {
		var __store StoreCreate
		if err := c.ShouldBindJSON(&__store); err != nil {
			c.IndentedJSON(http.StatusBadRequest, gin.H{"error":err.Error()})
			return
		}
		store := dao_create_store(db,__store)
		store_dto := GetStoreSchema(store)
		fmt.Println(__store.Name)
		ResponseCreate(c, store_dto)
		return
	}
}