package day9

import (
	"aoc2023/days/aocday"
	"aoc2023/utils/parsers"
	"fmt"
	"strings"
)

type day9 struct {
	nums [][]int
}

func New(inp string) aocday.AoCDay {
	d := &day9{
		nums: make([][]int, 0),
	}

	for _, line := range strings.Split(inp, "\n") {
		if len(line) == 0 {
			continue
		}

		d.nums = append(d.nums, parsers.ExtractNums(line))
	}

	return d
}

func analyzeLine(line []int, forw bool, deb bool) int {
	lines := make([][]int, 0)
	curLine := &line
	nz := true
	// form pyramid
	for nz {
		nz = false
		newLine := make([]int, len(*curLine)-1)
		for i := range newLine {
			newLine[i] = (*curLine)[i+1] - (*curLine)[i]
			if newLine[i] != 0 {
				nz = true
			}
		}
		lines = append(lines, newLine)
		curLine = &newLine
	}

	if deb {
		fmt.Println(lines)
	}

	last := 0
	res := 0
	if forw {
		for i := len(lines) - 2; i >= 0; i-- {
			last = lines[i][len(lines[i])-1] + last
		}
		res = line[len(line)-1] + last
	} else {
		for i := len(lines) - 2; i >= 0; i-- {
			last = lines[i][0] - last
		}
		res = line[0] - last
	}

	if deb {
		fmt.Println(res)
	}

	return res
}

func (d *day9) SolveA(deb bool) interface{} {
	out := 0
	for _, line := range d.nums {
		out += analyzeLine(line, true, deb)
	}
	fmt.Println("Solution A:", out)
	return out
}
func (d *day9) SolveB(deb bool) interface{} {
	out := 0
	for _, line := range d.nums {
		out += analyzeLine(line, false, deb)
	}
	fmt.Println("Solution B:", out)
	return out
}
