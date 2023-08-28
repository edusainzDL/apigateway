package store
import "gorm.io/gorm"


func dao_create_store(db *gorm.DB, store_input StoreCreate) Stores {
	store := Stores{
		Name:store_input.Name,
		Location:store_input.Location,
	}

	db.Create(&store)
	return store
}

func dao_get_stores(db *gorm.DB) []Stores {
	stores := []Stores{}  
	db.Find(&stores)
	return stores
}