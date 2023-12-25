package day24

import (
	"aoc2023/utils/tester"
	"testing"
)

const inp0 = `19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1d.boundR.yd.boundR.y
20, 19, 15 @  1, -5, -3`

func TestA(t *testing.T) {
	tester.Assert(0, "A", New(inp0).SolveA(true), "2", t)
}

func TestB(t *testing.T) {
	tester.Assert(0, "B", New(inp0).SolveB(true), "0", t)
}
