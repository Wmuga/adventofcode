package day8

import (
	"testing"
)

const inp1 = `RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)`

const inp2 = `LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)`

const inp3 = `LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)`

func TestParse(t *testing.T) {
	day := New(inp2).(*day8)
	nodes := map[string]*tree{
		"AAA": {name: "AAA"},
		"BBB": {name: "BBB"},
		"ZZZ": {name: "ZZZ"},
	}
	nodes["AAA"].lhs = nodes["BBB"]
	nodes["AAA"].rhs = nodes["BBB"]
	nodes["BBB"].lhs = nodes["AAA"]
	nodes["BBB"].rhs = nodes["ZZZ"]
	nodes["ZZZ"].lhs = nodes["ZZZ"]
	nodes["ZZZ"].rhs = nodes["ZZZ"]

	for k, v := range nodes {
		v2 := day.nodes[k]
		if v.lhs.name != v2.lhs.name || v.rhs.name != v2.rhs.name {
			t.Error("Wrong", k)
		}
	}
}

func TestA(t *testing.T) {
	day := New(inp1)
	res := day.SolveA(true)
	if res.(int) != 2 {
		t.Error("First input wrong. Expected 2. Got", res)
	}
	day = New(inp2)
	res = day.SolveA(true)
	if res.(int) != 6 {
		t.Error("First input wrong. Expected 6. Got", res)
	}
}

func TestB(t *testing.T) {
	day := New(inp3)
	res := day.SolveB(true)
	if res.(int) != 6 {
		t.Error("First input wrong. Expected 6. Got", res)
	}
}
