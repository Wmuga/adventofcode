package day13

import "testing"

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
	res := d.SolveB(true)
	if res != "400" {
		t.Error("Wrong B answer. Got", res)
	}
}
