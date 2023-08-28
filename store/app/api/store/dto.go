package store

import "github.com/gin-gonic/gin"
import "net/http"


func ResponseCreate(c *gin.Context, store Store) {

	response := StoreResponse{
		Message : "Created satisfactoriamente",
		Data    : store,
	}
	c.IndentedJSON(http.StatusOK, response)
}

func ResponseStoreAll(c *gin.Context, store []Store) {

	response := StoreResponseAll{
		Message : "Created satisfactoriamente",
		Data    : store,
	}
	c.IndentedJSON(http.StatusOK, response)
}

func GetStoreSchema(store Stores) Store {
	return Store{
		ID: store.ID,
		Name: store.Name,
		Location: store.Location,
		CreatedAt: store.CreatedAt,
		UpdatedAt: store.UpdatedAt,
	}
}