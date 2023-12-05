package main

import (
	"aoc2023/days/day3"
	"aoc2023/utils/inputs"
	"fmt"
	"log"

	"github.com/joho/godotenv"
)

const inpTest = `467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..`

func main() {
	if godotenv.Load() != nil {
		log.Fatalln("Can't load env")
	}

	inpActual, err := inputs.Day(3)
	if err != nil {
		log.Fatalln(err)
	}

	fmt.Println("Test data:")
	curDay := day3.New(inpTest)
	curDay.SolveA(true)
	curDay.SolveB(true)
	fmt.Println("Actual data:")
	curDay = day3.New(inpActual)
	curDay.SolveA(false)
	curDay.SolveB(false)
}
