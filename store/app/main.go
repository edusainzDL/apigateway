package main
// import "store.com/store/core"
// import "net/http"


import "github.com/gin-gonic/gin"
import "store.com/store/api/store"

func main() {
	r := gin.Default()
	store.StoresRouter(r)
	// r.GET("/stores", store.StoresRouter)
	r.Run()
}