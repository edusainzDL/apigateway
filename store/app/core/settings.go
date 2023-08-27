package core

import (
	// "fmt"
	// "os"
	"log"
	// "reflect"
	"github.com/spf13/viper"
)

type Setting struct {
	host 		string
	user 		string
	password 	string
	dbname 		string
	port 		string
	sslmode 	string
	TimeZone 	string
}

func InitSettings() {
	// dir,_ := os.UserHomeDir()

	viper.SetConfigFile(".env")
	
	err := viper.ReadInConfig()
	
	if err != nil{
		log.Fatalf("Error while reading config file %s", err)
	}

}

func get_env(key string) string {
	value, ok := viper.Get(key).(string)
	if !ok {
		log.Fatalf("Invalid type assertion")
	}
	return value
}


func Settings() Setting{
	settings := Setting{
		host:get_env("HOST"),
		user:get_env("USER"),
		password:get_env("PASSWORD"),
		dbname:get_env("DBNAME"),
		port:get_env("PORT"),
		sslmode:get_env("SSLMODE"),
		TimeZone:get_env("TIMEZONE"),
	}
	return settings
}
