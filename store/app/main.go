package main
// import "store.com/store/core"
// import "net/http"


import "github.com/gin-gonic/gin"
import "store.com/store/api/store"
import "store.com/store/core"
import "store.com/store/database"
import "fmt"

func main() {
	r := gin.Default()
	core.InitSettings()
	db := database.InitConnection()
	fmt.Println(db)
	db.AutoMigrate(&store.Stores{})
	settings := core.Settings()
	fmt.Println(settings)
	store.StoresRouter(r)
	// r.GET("/stores", store.StoresRouter)
	r.Run()
}