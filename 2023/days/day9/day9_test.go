package day9

import (
	"reflect"
	"testing"
)

const inp1 = `0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45`

const inp2 = `0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 -45`

func TestParse(t *testing.T) {
	day := New(inp2).(*day9)
	nums := [][]int{
		{0, 3, 6, 9, 12, 15},
		{1, 3, 6, 10, 15, 21},
		{10, 13, 16, 21, 30, -45},
	}

	if !reflect.DeepEqual(day.nums, nums) {
		t.Errorf("Wrong nums. got %v expected %v\n", day.nums, nums)
	}
}

func TestA(t *testing.T) {
	day := New(inp1)
	res := day.SolveA(true)
	if res != "114" {
		t.Error("Expected 114. Got", res)
	}
}

func TestB(t *testing.T) {
	day := New(inp1)
	res := day.SolveB(true)
	if res != "2" {
		t.Error("First input wrong. Expected 2. Got", res)
	}
}
