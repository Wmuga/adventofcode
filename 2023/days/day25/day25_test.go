package day25

import (
	"aoc2023/utils/tester"
	"testing"
)

const inp0 = `jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr`

func TestA(t *testing.T) {
	day := New(inp0)
	tester.Assert(0, "A", day.SolveA(true), "54", t)
}

func TestB(t *testing.T) {
	day := New(inp0)
	tester.Assert(0, "B", day.SolveB(true), "281", t)
}
