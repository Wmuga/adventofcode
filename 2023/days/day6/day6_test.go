package day6

import (
	"reflect"
	"testing"
)

const inp1 = `Time:      7  15   30
Distance:  9  40  200`

func TestParse(t *testing.T) {
	day := New(inp1).(*day6)
	times := []int{7, 15, 30}
	dists := []int{9, 40, 200}
	if !reflect.DeepEqual(times, day.times) {
		t.Error("Times", day.times, "is not expected", times, "\n")
	}
	if !reflect.DeepEqual(dists, day.dists) {
		t.Error("Distances", day.dists, "is not expected", dists, "\n")
	}
}

func TestA(t *testing.T) {
	day := New(inp1)
	res := day.SolveA(true)
	if res != "288" {
		t.Error("Result", res, "is not equal to", 288, "\n")
	}
}

func TestB(t *testing.T) {
	day := New(inp1)
	res := day.SolveB(true)
	if res != "71503" {
		t.Error("Result", res, "is not equal to", 71503, "\n")
	}
}
