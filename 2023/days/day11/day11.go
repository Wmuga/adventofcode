package day11

import (
	"aoc2023/days/aocday"
	"aoc2023/entity/pair"
	"aoc2023/utils/parsers"
	"aoc2023/utils/tools"
	"fmt"
	"math"
	"slices"
	"strconv"

	"golang.org/x/exp/maps"
)

type coord pair.Pair[int64]

type day11 struct {
	inp  string
	gals map[coord]struct{}
}

func New(inp string) aocday.AoCDay {
	out := &day11{
		inp: inp,
	}
	return out
}

func (d *day11) base(add int64) int64 {
	d.parse(d.inp, add)
	coords := maps.Keys(d.gals)
	var out int64
	for i := 0; i < len(coords)-1; i++ {
		for j := i + 1; j < len(coords); j++ {
			out += dist(coords[i], coords[j])
		}
	}
	return out
}

func (d *day11) SolveA(_ bool) string {
	out := d.base(1)
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(out, 10)
}

func (d *day11) SolveB(_ bool) string {
	out := d.base(1000000)
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(out, 10)
}

func dist(a, b coord) int64 {
	x := math.Abs(float64(a.X) - float64(b.X))
	y := math.Abs(float64(a.Y) - float64(b.Y))
	return int64(x + y)
}

func (d *day11) parse(inp string, add int64) {
	d.gals = make(map[coord]struct{})
	add--

	lines := parsers.GetLinesRune(inp)

	linesT := tools.Transpose(lines)

	//lines[y][x] = linesT[x][y]
	var addY int64
	for y, line := range lines {
		if slices.Index(line, '#') == -1 {
			addY += add
			continue
		}

		var addX int64
		for x, v := range lines[y] {
			if slices.Index(linesT[x], '#') == -1 {
				addX += add
				continue
			}
			if v == '#' {
				d.gals[coord{X: int64(x) + addX, Y: int64(y) + addY}] = struct{}{}
			}
		}
	}
}
