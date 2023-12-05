package day1

import (
	aoc "aoc2023/days/aocday"
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

type day1 struct {
	inputLines []string
}

var strToNumbers = map[string]string{
	"one":   "o1e",
	"two":   "t2o",
	"three": "t3e",
	"four":  "f4r",
	"five":  "f5e",
	"six":   "s6x",
	"seven": "s7n",
	"eight": "e8t",
	"nine":  "n9e",
}

func New(input string) aoc.AoCDay {
	lines := strings.Split(input, "\n")
	return &day1{
		inputLines: lines,
	}
}

func (d *day1) baseSolver(deb bool, filter func([]string) []string) int {
	out := 0
	filtered := filter(d.inputLines)
	for _, line := range filtered {
		if len(line) == 0 {
			continue
		}
		runes := []rune(line)
		numbStr := string(runes[0]) + string(runes[len(runes)-1])
		numb, err := strconv.ParseInt(numbStr, 10, 32)
		if err != nil {
			fmt.Printf("%v is not a number\n", numbStr)
			continue
		}
		if deb {
			fmt.Print(numb, ", ")
		}
		out += int(numb)
	}
	if deb {
		fmt.Println()
	}
	return out
}

func (d *day1) SolveA(deb bool) {
	out := d.baseSolver(deb, filterNumbersA)
	fmt.Println("Solution A:", out)
}

func (d *day1) SolveB(deb bool) {
	out := d.baseSolver(deb, filterNumbersB)
	fmt.Println("Solution B:", out)
}

func filterNumbersA(inp []string) []string {
	out := make([]string, len(inp))
	for i, v := range inp {
		out[i] = ""
		for _, c := range v {
			if unicode.IsDigit(c) {
				out[i] += string(c)
			}
		}
	}
	return out
}

func filterNumbersB(inp []string) []string {
	inp2 := make([]string, len(inp))
	copy(inp2, inp)
	for k, v := range strToNumbers {
		for i, line := range inp2 {
			inp2[i] = strings.ReplaceAll(line, k, v)
		}
	}
	return filterNumbersA(inp2)
}
