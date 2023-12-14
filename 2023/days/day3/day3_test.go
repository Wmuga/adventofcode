package day3

import "testing"

const inp1 = `467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..`

func TestA(t *testing.T) {
	d := New(inp1)
	res := d.SolveA(true)
	if res != "4361" {
		t.Error("Wrong A solution. Got ", res)
	}
}

func TestB(t *testing.T) {
	d := New(inp1)
	d.SolveA(false)
	res := d.SolveB(true)
	if res != "467835" {
		t.Error("Wrong B solution. Got ", res)
	}
}
