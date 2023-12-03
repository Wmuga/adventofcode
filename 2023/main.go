package main

import (
	"aoc2023/days/day2"
	"aoc2023/utils/inputs"
	"fmt"
	"log"

	"github.com/joho/godotenv"
)

const inpTest = `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`

func main() {
	if godotenv.Load() != nil {
		log.Fatalln("Can't load env")
	}

	inpActual, err := inputs.Day(2)
	if err != nil {
		log.Fatalln(err)
	}

	fmt.Println("Test data:")
	curDay := day2.New(inpTest)
	curDay.SolveA(true)
	curDay.SolveB(true)
	fmt.Println("Actual data:")
	curDay = day2.New(inpActual)
	curDay.SolveA(false)
	curDay.SolveB(false)
}
