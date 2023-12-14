package main

import (
	"aoc2023/days/day14"
	"aoc2023/utils/inputs"
	"fmt"
	"log"
	"time"

	"github.com/joho/godotenv"
)

func main() {
	if godotenv.Load() != nil {
		log.Fatalln("Can't load env")
	}

	inpActual, err := inputs.Day(14)
	if err != nil {
		log.Fatalln(err)
	}
	// Tests moved to _test.go files
	curDay := day14.New(inpActual)
	ts1 := time.Now()
	curDay.SolveA(false)
	ts2 := time.Now()
	curDay.SolveB(false)
	ts3 := time.Now()
	dur1 := ts2.Sub(ts1)
	dur2 := ts3.Sub(ts2)
	fmt.Printf("\nTime A: %v\nTime B: %v\n", dur1, dur2)
}
