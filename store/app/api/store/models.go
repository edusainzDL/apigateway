package store
import ("time")

type Stores struct {
	ID 		  uint   `gorm:"autoIncrement;primaryKey"`
	Name 	  string  `gorm:"size:250;not null"`     
	Location  string  `gorm:"size:250;not null"`
	CreatedAt time.Time `gorm:"autoCreateTime;not null"`
	UpdatedAt time.Time `gorm:autoUpdateTime`

}