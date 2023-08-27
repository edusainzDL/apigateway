package database

import (
    "fmt"
    "reflect"
    "gorm.io/gorm"
    "gorm.io/driver/postgres"
    "store.com/store/core"
)


func get_connect_str() string {
    settings := core.Settings()
    values := reflect.ValueOf(settings)
    fmt.Println(settings)
    return fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%s sslmode=%s TimeZone=%s",
            values.Field(0),
            values.Field(1),
            values.Field(2),
            values.Field(3),
            values.Field(4),
            values.Field(5),
            values.Field(6),
        )
}

func InitConnection() *gorm.DB{
    db, err := gorm.Open(
        postgres.New(postgres.Config{
                DSN:get_connect_str(),
                PreferSimpleProtocol:true,
            }),
        &gorm.Config{})   
    

    type_ := reflect.TypeOf(db)
    fmt.Println("type database")
    fmt.Println(type_)
    if err != nil {
        fmt.Println(err)
        panic("Failed to connect database")
    }
    return db
   
}

