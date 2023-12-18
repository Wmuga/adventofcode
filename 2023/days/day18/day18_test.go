package day18

import (
	"aoc2023/utils/tester"
	"testing"
)

const inp1 = `R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)`

func TestA(t *testing.T) {
	tester.Assert(0, "A", New(inp1).SolveA(true), "62", t)
}

func TestParse(t *testing.T) {
	instrs := []instr{
		{'R', 461937, ""},
		{'D', 56407, ""},
		{'R', 356671, ""},
		{'D', 863240, ""},
		{'R', 367720, ""},
		{'D', 266681, ""},
		{'L', 577262, ""},
		{'U', 829975, ""},
		{'L', 112010, ""},
		{'D', 829975, ""},
		{'L', 491645, ""},
		{'U', 686074, ""},
		{'L', 5411, ""},
		{'U', 500254, ""},
	}
	d := New(inp1).(*day18)
	d.redoInstrs()
	for i := range instrs {
		tester.Assert(i, "PARSE", d.instrs[i], instrs[i], t)
	}
}

func TestB(t *testing.T) {
	tester.Assert(0, "B", New(inp1).SolveB(true), "952408144115", t)
}
