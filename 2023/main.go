package main

import (
	"aoc2023/days/day7"
	"aoc2023/utils/inputs"
	"fmt"
	"log"

	"github.com/joho/godotenv"
)

func main() {
	if godotenv.Load() != nil {
		log.Fatalln("Can't load env")
	}

	inpActual, err := inputs.Day(7)
	if err != nil {
		log.Fatalln(err)
	}
	// Tests moved to _test.go files
	fmt.Println("Actual data:")
	curDay := day7.New(inpActual)
	curDay.SolveA(false)
	curDay.SolveB(false)
}
