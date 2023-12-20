package day8

import (
	"aoc2023/days/aocday"
	"aoc2023/utils/tools"
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

type tree struct {
	name    string
	insides string
	lhs     *tree
	rhs     *tree
}

type cycleTree struct {
	start *tree
	pre   int
	cycle int
}

type day8 struct {
	steps []rune
	nodes map[string]*tree
}

var reInsides = regexp.MustCompile(`\((.+), (.+)\)`)

func New(inp string) aocday.AoCDay {
	data := strings.Split(inp, "\n\n")
	day := &day8{
		steps: []rune(data[0]),
		nodes: map[string]*tree{},
	}
	lines := strings.Split(data[1], "\n")
	// create all nodes with their names
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}

		data := strings.Split(line, " = ")
		if len(data) != 2 {
			fmt.Println("Wrong line")
			continue
		}

		day.nodes[data[0]] = &tree{
			name:    data[0],
			insides: data[1],
		}
	}
	// link
	for _, v := range day.nodes {
		names := reInsides.FindAllStringSubmatch(v.insides, -1)
		if len(names) != 1 || len(names[0]) != 3 {
			fmt.Println("Parsing error", v.insides, names)
			continue
		}
		v.insides = ""
		v.lhs = day.nodes[names[0][1]]
		v.rhs = day.nodes[names[0][2]]
	}
	return day
}

func move(cur **tree, step rune, b bool) bool {
	switch step {
	case 'L':
		(*cur) = (*cur).lhs
	case 'R':
		(*cur) = (*cur).rhs
	default:
		fmt.Println("Unknown", step)
	}
	if !b {
		return (*cur).name == "ZZZ"
	}

	return (*cur).name[2] == 'Z'
}

func (d *day8) SolveA(_ bool) string {
	out := 0
	cur := d.nodes["AAA"]
	i := 0
	end := false
	for !end {
		end = move(&cur, d.steps[i], false)
		out++
		i++
		i %= len(d.steps)
	}
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(int64(out), 10)
}
func (d *day8) SolveB(_ bool) string {
	cur := make([]cycleTree, 0)
	for k, v := range d.nodes {
		if k[2] == 'A' {
			cur = append(cur, cycleTree{
				start: v,
			})
		}
	}

	for i, v := range cur {
		step := 0
		count := 0
		start := v.start
		stage := 0
		for stage != 2 {
			count++
			if move(&start, d.steps[step], true) {
				switch stage {
				case 0:
					v.pre = count
					count = 0
					stage = 1
				case 1:
					v.cycle = count
					cur[i] = v
					stage = 2
				}
			}
			step = (step + 1) % len(d.steps)
		}
	}

	for _, v := range cur {
		if v.pre != v.cycle {
			fmt.Println("Works only with pre == cycle")
			return "-1"
		}
	}

	out := cur[0].cycle
	for i, v := range cur {
		if i == 0 {
			continue
		}
		out = int(tools.LCM(int64(out), int64(v.cycle)))
	}

	fmt.Println("Solution B:", out)
	return strconv.FormatInt(int64(out), 10)
}
