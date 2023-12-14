package day11

import (
	"reflect"
	"testing"

	"golang.org/x/exp/maps"
)

const inp1 = `...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....`

func TestParse(t *testing.T) {
	day := New(inp1).(*day11)
	day.parse(day.inp, 2)
	gals := map[coord]struct{}{
		{X: 4, Y: 0}:  {},
		{X: 9, Y: 1}:  {},
		{X: 0, Y: 2}:  {},
		{X: 8, Y: 5}:  {},
		{X: 1, Y: 6}:  {},
		{X: 12, Y: 7}: {},
		{X: 9, Y: 10}: {},
		{X: 0, Y: 11}: {},
		{X: 5, Y: 11}: {},
	}

	if !reflect.DeepEqual(gals, day.gals) {
		t.Error("Wrong coords", maps.Keys(day.gals))
	}
}

func TestAll(t *testing.T) {
	day := New(inp1).(*day11)
	adds := []int64{2, 10, 100}
	ress := []int64{374, 1030, 8410}
	for i := range adds {
		res := day.base(adds[i])
		if res != ress[i] {
			t.Error(i, "Input wrong. Expected", ress[i], "Got", res)
		}
	}

}
