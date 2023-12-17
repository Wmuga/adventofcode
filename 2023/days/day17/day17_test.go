package day17

import (
	"aoc2023/utils/tester"
	"testing"
)

const inp1 = `2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
`

func TestA(t *testing.T) {
	tester.Assert(0, "A", New(inp1).SolveA(true), "102", t)
}

func TestB(t *testing.T) {
	tester.Assert(0, "B", New(inp1).SolveB(true), "94", t)
}
