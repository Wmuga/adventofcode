package main

import (
	"aoc2023/days/day1"
	"aoc2023/utils/inputs"
	"fmt"
	"log"

	"github.com/joho/godotenv"
)

type AoCDay interface {
	SolveA(bool)
	SolveB(bool)
}

const inpTest = `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`

func main() {
	var curDay AoCDay

	if godotenv.Load() != nil {
		log.Fatalln("Can't load env")
	}

	inpActual, err := inputs.Day(1)
	if err != nil {
		log.Fatalln(err)
	}

	fmt.Println("Test data:")
	curDay = day1.New(inpTest)
	curDay.SolveA(true)
	curDay.SolveB(true)
	fmt.Println("Actual data:")
	curDay = day1.New(inpActual)
	curDay.SolveA(false)
	curDay.SolveB(false)
}
