package store

import "github.com/gin-gonic/gin"
import "net/http"
// import "fmt"

type store struct {
	ID string `json:"id"`
	Name string `json:name`
	Location string `json:location`
}

var stores = []store {
	{ID: "1", Name: "Sucursa Cielo", Location: "Av Cielo #567. Deelgación Benito Juárez. Ciudad de México."},
    {ID: "2", Name: "Sucursal Alfa", Location: "Calle Alfa #22. Guadalajara, Jalisco."},
    {ID: "3", Name: "Sucursal Guerrero", Location: "Boulevard de la paz #3456. Acapulco. Guerrero."},
}

func getStores() gin.HandlerFunc {
	return func (c *gin.Context) {
		c.IndentedJSON(http.StatusOK, stores)
	}
} 