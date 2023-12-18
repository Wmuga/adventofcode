package day18

import (
	"aoc2023/days/aocday"
	"aoc2023/entity/pair"
	"aoc2023/utils/parsers"
	"fmt"
	"math"
	"slices"
	"strconv"
	"strings"
)

type instr struct {
	dir   rune
	steps int
	color string
}

type coord pair.Pair[int]

type day18 struct {
	instrs []instr
}

func New(inp string) aocday.AoCDay {
	return &day18{
		instrs: parseInstrs(inp),
	}
}

func (d *day18) SolveA(_ bool) string {
	out := d.dig()
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(out, 10)
}

func (d *day18) SolveB(_ bool) string {
	d.redoInstrs()
	out := d.dig()
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(int64(out), 10)
}

func (d *day18) dig() int64 {
	prevDir := 'N'
	verts := make([]coord, 0, len(d.instrs))
	// get boundaries
	start, _ := getBoundaries(d)
	if start.X < 0 {
		start.X = -start.X
	}
	if start.Y < 0 {
		start.Y = -start.Y
	}
	start.X++
	start.Y++

	cur := coord{start.X, start.Y}
	outer := int64(0)
	// Adding verticies
	for _, inst := range d.instrs {
		if inst.dir != prevDir {
			verts = append(verts, cur)
			prevDir = inst.dir
		}
		switch inst.dir {
		case 'R':
			cur.X += inst.steps
		case 'L':
			cur.X -= inst.steps
		case 'U':
			cur.Y -= inst.steps
		case 'D':
			cur.Y += inst.steps
		}
		outer += int64(inst.steps)
	}

	inner := int64(0)
	// Shoulace (interioir) + boundaries (perim)
	for i := 0; i < len(verts)-1; i++ {
		inner += int64(verts[i].X * verts[i+1].Y)
		inner -= int64(verts[i+1].X * verts[i].Y)
	}
	inner += int64(verts[len(verts)-1].X * verts[0].Y)
	inner -= int64(verts[0].X * verts[len(verts)-1].Y)
	return inner/2 + outer/2 + 1
}

func dist(a, b coord) int64 {
	x := float64(a.X - b.X)
	y := float64(a.Y - b.Y)
	return int64(math.Sqrt(x*x + y*y))
}

func angle(cur, center coord) float64 {
	out := math.Atan(float64(cur.Y-center.Y)/float64(-cur.X+center.X)) + math.Pi*2
	if out > math.Pi*2 {
		out -= math.Pi * 2
	}
	return out
}

func (d *day18) digOld() int64 {
	// get boundaries
	start, end := getBoundaries(d)
	// dig site
	field := map[int][]int{}
	cur := coord{0, 0}
	field[0] = make([]int, 1)
	field[0][0] = 0
	// dig by instructions
	for _, ins := range d.instrs {
		for i := 0; i < ins.steps; i++ {
			switch ins.dir {
			case 'R':
				cur.X++
			case 'L':
				cur.X--
			case 'U':
				cur.Y--
			case 'D':
				cur.Y++
			}
			if _, ex := field[cur.Y]; !ex {
				field[cur.Y] = make([]int, 0, 1)
			}
			field[cur.Y] = append(field[cur.Y], cur.X)
		}
	}

	return count(field, start, end)
}

func count(field map[int][]int, start, end coord) int64 {
	out := int64(0)
	hole := false

	for _, v := range field {
		slices.Sort(v)

		i := 0
		for i < len(v) {
			if i == len(v)-1 {
				out++
				break
			}

			diff := v[i+1] - v[i]
			if diff == 1 {
				out++
				i++
				continue
			}

			if hole {
				hole = false
				i++
			}

			out += int64(diff)
			hole = true
			i++
		}

	}

	return out
}

func getBoundaries(d *day18) (coord, coord) {
	countX := 0
	countY := 0

	startX := 0
	startY := 0
	endX := 0
	endY := 0

	for _, ins := range d.instrs {
		switch ins.dir {
		case 'R':
			countX += ins.steps
		case 'L':
			countX -= ins.steps
		case 'U':
			countY -= ins.steps
		case 'D':
			countY += ins.steps
		}
		if countX > endX {
			endX = countX
		}
		if countY > endY {
			endY = countY
		}

		if countX < startX {
			startX = countX
		}
		if countY < startY {
			startY = countY
		}
	}
	return coord{startX, startY}, coord{X: endX, Y: endY}
}

var dirs = []rune("RDLU")

func (d *day18) redoInstrs() {
	for i, ins := range d.instrs {
		l := []rune(ins.color)[2:7]
		newIns := instr{}
		newIns.dir = dirs[int([]rune(ins.color)[7]-'0')]
		out, err := strconv.ParseInt(string(l), 16, 32)
		if err != nil {
			panic(err)
		}
		newIns.steps = int(out)
		d.instrs[i] = newIns
	}
}

func parseInstrs(inp string) []instr {
	out := make([]instr, 0)

	for _, line := range parsers.GetLinesString(inp) {
		ins := instr{}

		data := strings.Split(line, " ")
		ins.dir = []rune(data[0])[0]
		count, err := strconv.ParseInt(data[1], 10, 32)
		if err != nil {
			panic(err)
		}
		ins.steps = int(count)
		ins.color = data[2]

		out = append(out, ins)
	}

	return out
}
