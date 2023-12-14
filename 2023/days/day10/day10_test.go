package day10

import (
	"strconv"
	"testing"
)

const inp1 = `.....
.S-7.
.|.|.
.L-J.
.....` // 4

const inp2 = `..F7.
.FJ|.
SJ.L7
|F--J
LJ...` // 8

const inp3 = `...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........`

const inp31 = `..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........`

const inp4 = `.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...`

const inp5 = `FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L`

func TestA(t *testing.T) {
	day := New(inp1)
	res := day.SolveA(true)
	if res != "4" {
		t.Error("Input 1: Expected 4. Got", res)
	}

	day = New(inp2)
	res = day.SolveA(true)
	if res != "8" {
		t.Error("Input 2: Expected 8. Got", res)
	}
}

func TestB(t *testing.T) {
	inps := []string{inp3, inp31, inp4, inp5}
	ress := []int{4, 4, 8, 10}
	for i := range inps {
		inp := inps[i]
		exp := ress[i]

		day := New(inp)
		res := day.SolveB(true)
		if res != strconv.FormatInt(int64(exp), 10) {
			t.Error(i, "input wrong. Expected", exp, "Got", res)
		}
	}
}

const inpHorror = `.S---7.
.|F-7|.
.||.||.
.|L7||.
.L-J||.
.F--J|.
.L---J.
.......`

func TestHorror(t *testing.T) {
	day := New(inpHorror)
	res := day.SolveB(true)
	if res != "0" {
		t.Error("Expected", 0, "Got", res)
	}
}
