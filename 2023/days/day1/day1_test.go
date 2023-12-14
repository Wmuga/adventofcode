package day1

import "testing"

const inp1 = `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`

const inp2 = `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`

func TestA(t *testing.T) {
	d := New(inp1)
	res := d.SolveA(true)
	if res != "142" {
		t.Error("Wrong A solution. Got ", res)
	}
}

func TestB(t *testing.T) {
	d := New(inp2)
	res := d.SolveB(true)
	if res != "281" {
		t.Error("Wrong B solution. Got ", res)
	}
}
