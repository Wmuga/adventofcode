package day3

import (
	"aoc2023/utils/tester"
	"testing"
)

const inp1 = `467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..`

func TestA(t *testing.T) {
	day := New(inp1)
	tester.Assert(0, "A", day.SolveA(true), "4361", t)
}

func TestB(t *testing.T) {
	day := New(inp1)
	day.SolveA(false)
	tester.Assert(0, "B", day.SolveB(true), "467835", t)
}
