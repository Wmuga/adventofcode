package main

import (
	"aoc2023/days/day8"
	"aoc2023/utils/inputs"
	"fmt"
	"log"

	"github.com/joho/godotenv"
)

func main() {
	if godotenv.Load() != nil {
		log.Fatalln("Can't load env")
	}

	inpActual, err := inputs.Day(8)
	if err != nil {
		log.Fatalln(err)
	}
	// Tests moved to _test.go files
	fmt.Println("Actual data:")
	curDay := day8.New(inpActual)
	curDay.SolveA(false)
	curDay.SolveB(false)
}
