package day13

import (
	"aoc2023/utils/tester"
	"testing"
)

const inp1 = `#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#`

func TestVert(t *testing.T) {
	d := New(inp1).(*day13)
	res := findMirror(d.patterns[0], 0, true)
	if res != 5 {
		t.Error("Wrong vertical mirroring. Got", res)
	}
}

func TestHor(t *testing.T) {
	d := New(inp1).(*day13)
	res := findMirror(d.patterns[1], 0, true)
	if res != 400 {
		t.Error("Wrong horizontal mirroring. Got", res)
	}
}

func TestB(t *testing.T) {
	d := New(inp1)
	tester.Assert(0, "B", d.SolveB(true), "400", t)
}
