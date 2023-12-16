package day16

import (
	"aoc2023/utils/tester"
	"testing"
)

const inp1 = `.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....`

func TestA(t *testing.T) {
	tester.Assert(0, "A", New(inp1).SolveA(true), "46", t)
}

func TestB(t *testing.T) {
	tester.Assert(0, "A", New(inp1).SolveB(true), "51", t)
}
