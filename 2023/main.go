package main

import (
	"aoc2023/utils/inputs"
	"fmt"
	"log"

	"github.com/joho/godotenv"
)

type AoCDay interface {
	SolveA(bool)
	SolveB(bool)
}

func main() {
	if godotenv.Load() != nil {
		log.Fatalln("Can't load env")
	}

	inp, err := inputs.Day(1)
	if err != nil {
		log.Fatalln(err)
	}

	fmt.Println(inp)
}
