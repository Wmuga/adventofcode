package day14

import (
	"aoc2023/utils/parsers"
	"reflect"
	"testing"
)

const inp1 = `O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....`

const c1 = `.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....`

const c2 = `.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O`

const c3 = `.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O`

func TestA(t *testing.T) {
	d := New(inp1)
	res := d.SolveA(true)
	if res != "136" {
		t.Error("Wrong A answer. Got", res)
	}
}

func TestCycle(t *testing.T) {
	d := New(inp1).(*day14)
	d.field = d.fieldBase
	cycles := []string{c1, c2, c3}
	for i, c := range cycles {
		for i := 0; i < 4; i++ {
			d.move(i, d.field)
		}
		if !reflect.DeepEqual(d.field, parsers.GetLinesRune(c)) {
			t.Error("Wrong cycle", i)
			d.printField()
			return
		}
	}
}

func TestB(t *testing.T) {
	d := New(inp1)
	res := d.SolveB(true)
	if res != "64" {
		t.Error("Wrong A answer. Got", res)
	}
}
