package day5

import (
	"aoc2023/utils/tester"
	"reflect"
	"testing"
)

const inp1 = `seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4`

func TestParse(t *testing.T) {
	day := New(inp1).(*day5)
	seeds := []uint{79, 14, 55, 13}
	if !reflect.DeepEqual(seeds, day.items) {
		t.Error("Seeds", day.items, "is not expected", seeds, "\n")
	}
	if len(day.rules) != 7 {
		t.Error("Not enough rules", len(day.rules), "expected 7")
		return
	}
	rule1 := intervals{
		lhs: []interval{
			{start: 98, end: 99},
			{start: 50, end: 97},
		},
		rhs: []interval{
			{start: 50, end: 51},
			{start: 52, end: 99},
		},
	}
	if !reflect.DeepEqual(rule1, day.rules[0]) {
		t.Error("Wrong rules")
	}
}

func TestA(t *testing.T) {
	day := New(inp1)
	tester.Assert(0, "A", day.SolveA(true), "35", t)
}

func TestB(t *testing.T) {
	day := New(inp1)
	tester.Assert(0, "B", day.SolveB(true), "46", t)
}
