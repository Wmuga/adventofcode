package day12

import (
	"aoc2023/utils/tester"
	"reflect"
	"testing"
)

const inp1 = `???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1`

func TestParse(t *testing.T) {
	d := New(inp1).(*day12)
	lines := [][]rune{
		[]rune("???.###"),
		[]rune(".??..??...?##."),
		[]rune("?#?#?#?#?#?#?#?"),
		[]rune("????.#...#..."),
		[]rune("????.######..#####."),
		[]rune("?###????????"),
	}
	conds := [][]int{
		{1, 1, 3},
		{1, 1, 3},
		{1, 3, 1, 6},
		{4, 1, 1},
		{1, 6, 5},
		{3, 2, 1},
	}

	if !reflect.DeepEqual(lines, d.lines) {
		t.Error("Wrong lines")
	}
	if !reflect.DeepEqual(conds, d.conds) {
		t.Error("Wrong conditions")
	}
}

func TestA(t *testing.T) {
	d := New(inp1)
	tester.Assert(0, "A", d.SolveA(true), "21", t)
}

func TestB(t *testing.T) {
	d := New(inp1)
	tester.Assert(0, "B", d.SolveB(true), "525152", t)
}
