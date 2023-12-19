package day19

import (
	"aoc2023/days/aocday"
	"aoc2023/entity/queue"
	"aoc2023/utils/parsers"
	"aoc2023/utils/tools"
	"fmt"
	"slices"
	"strconv"
	"strings"
)

type branch struct {
	parent string
	part   int
	less   bool
	border int
	next   string
}

type constraint struct {
	min int
	max int
}

type day19 struct {
	workflows map[string][]branch
	parts     [][]int
}

func New(inp string) aocday.AoCDay {
	data := strings.Split(inp, "\n\n")
	parts := strings.Split(data[1], "\n")

	d := &day19{
		workflows: make(map[string][]branch),
		parts:     make([][]int, 0, len(parts)),
	}

	d.parseWorkflows(data[0])
	for _, part := range parts {
		if part == "" {
			continue
		}
		d.parts = append(d.parts, parsers.ExtractNums(part))
	}

	return d
}

func (d *day19) SolveA(_ bool) string {
	out := int64(0)
	for _, part := range d.parts {
		out += d.testPart(part)
	}
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(out, 10)
}

func (d *day19) SolveB(_ bool) string {
	// Getting contraints
	constrs := d.forward()
	out := int64(0)
	for _, c := range constrs {
		tmp := int64(1)
		for _, p := range c {
			tmp *= int64(p.max - p.min - 1)
		}
		if tmp < 0 {
			continue
		}
		out += tmp
	}
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(out, 10)
}

func (d *day19) forward() [][4]constraint {
	type qType struct {
		flow string
		c    [4]constraint
	}

	out := make([][4]constraint, 0)

	q := queue.New()
	q.Enqueue(&qType{"in", [4]constraint{{0, 4001}, {0, 4001}, {0, 4001}, {0, 4001}}}) //nolint:errcheck
	for !q.IsEmpty() {
		v, _ := q.Dequeue() //nolint:errcheck
		item := v.(*qType)

		cool := true
		for _, c := range item.c {
			if c.min >= c.max {
				cool = false
				break
			}
		}
		if !cool {
			continue
		}

		if item.flow == "R" {
			continue
		}

		if item.flow == "A" {
			out = append(out, item.c)
			continue
		}

		for _, b := range d.workflows[item.flow] {
			item2 := &qType{b.next, item.c}
			if b.less {
				item2.c[b.part].max = tools.Min(item2.c[b.part].max, b.border)
				item.c[b.part].min = tools.Max(item.c[b.part].min, b.border-1)
			} else {
				item2.c[b.part].min = tools.Max(item2.c[b.part].min, b.border)
				item.c[b.part].max = tools.Min(item.c[b.part].max, b.border+1)
			}

			q.Enqueue(item2) //nolint:errcheck
		}
	}

	return out
}

func (d *day19) testPart(part []int) int64 {
	cur := "in"

	for cur != "A" && cur != "R" {
		for _, b := range d.workflows[cur] {
			if b.less == (part[b.part] < b.border) {
				cur = b.next
				break
			}
		}
	}

	if cur == "R" {
		return 0
	}

	return int64(part[0] + part[1] + part[2] + part[3])
}

func (d *day19) parseWorkflows(inp string) {
	for _, line := range strings.Split(inp, "\n") {
		line = strings.Trim(line, "}")
		data := strings.Split(line, "{")
		branches := strings.Split(data[1], ",")
		d.workflows[data[0]] = make([]branch, len(branches))
		for i, v := range branches {
			d.workflows[data[0]][i] = parseBranch(data[0], []rune(v))
		}
	}
}

var m = map[rune]int{'x': 0, 'm': 1, 'a': 2, 's': 3}

func parseBranch(parent string, inp []rune) branch {
	dd := slices.Index(inp, ':')
	if dd == -1 {
		return branch{
			parent: parent,
			next:   string(inp),
		}
	}
	border, err := strconv.ParseInt(string(inp[2:dd]), 10, 32)
	if err != nil {
		panic(err)
	}
	return branch{
		part:   m[inp[0]],
		less:   inp[1] == '<',
		border: int(border),
		next:   string(inp[dd+1:]),
		parent: parent,
	}
}
