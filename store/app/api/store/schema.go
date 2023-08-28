package store

import "time"

type Store struct {
	ID uint `json:"id"`
	Name string `json:name`
	Location string `json:location`
	CreatedAt time.Time `json:created_at`
	UpdatedAt time.Time `json:updated_at`

}

type StoreCreate struct {
	Name 		string `json:"name"`
	Location 	string `json:"location"`
}

type StoreResponse struct {
	Message string `json:"Message"`
	Data 	Store  `json:"data"`
}
type StoreResponseAll struct {
	Message string `json:"Message"`
	Data 	[]Store  `json:"data"`
}