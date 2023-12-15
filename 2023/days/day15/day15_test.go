package day15

import (
	"aoc2023/utils/tester"
	"testing"
)

const inp1 = `rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7`

func TestA(t *testing.T) {
	d := New(inp1)
	tester.Assert(0, "A", d.SolveA(true), "1320", t)
}

func TestB(t *testing.T) {
	d := New(inp1)
	tester.Assert(0, "B", d.SolveB(true), "145", t)
}
