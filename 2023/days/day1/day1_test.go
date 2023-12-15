package day1

import (
	"aoc2023/utils/tester"
	"testing"
)

const inp1 = `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`

const inp2 = `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`

func TestA(t *testing.T) {
	day := New(inp1)
	tester.Assert(0, "A", day.SolveA(true), "142", t)
}

func TestB(t *testing.T) {
	day := New(inp2)
	tester.Assert(0, "B", day.SolveB(true), "281", t)
}
