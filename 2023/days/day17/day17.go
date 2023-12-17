package day17

import (
	"aoc2023/days/aocday"
	"aoc2023/entity/priorityQueue"
	"aoc2023/utils/parsers"
	"fmt"
	"math"
	"strconv"

	"golang.org/x/exp/maps"
)

type day17 struct {
	field [][]int
}

type qItem struct {
	x     int
	y     int
	dir   int
	steps int
	heat  int
	len   int
}

type mapKey struct {
	x     int
	y     int
	steps int
	dir   int
}

func (lhs *qItem) HigherPriorityThan(rhs priorityQueue.Interface) bool {
	return (lhs.heat + lhs.len) < (rhs.(*qItem).heat + rhs.(*qItem).len)
}

func New(inp string) aocday.AoCDay {
	runes := parsers.GetLinesRune(inp)
	ints := make([][]int, len(runes))
	for i, line := range runes {
		ints[i] = make([]int, len(line))
		for j, v := range line {
			ints[i][j] = int(v - '0')
		}
	}

	return &day17{
		field: ints,
	}
}

func (d *day17) SolveA(_ bool) string {
	out := d.dijkstra(0, 3, &qItem{}, &qItem{x: len(d.field[0]) - 1, y: len(d.field) - 1})
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(int64(out), 10)
}

func (d *day17) SolveB(_ bool) string {
	out := d.dijkstra(4, 10, &qItem{}, &qItem{x: len(d.field[0]) - 1, y: len(d.field) - 1})
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(int64(out), 10)
}

func (d *day17) dijkstra(minSteps, maxSteps int, start, end *qItem) int {
	visited := map[mapKey]int{}
	q := priorityQueue.New()

	for _, n := range d.getNeighbours(start, 0, maxSteps) {
		n.len = abs(end.x-n.x) + abs(end.y-n.y)
		q.Push(n)
	}

	out := -1
	for {
		v := q.Pop()
		if v == nil {
			break
		}
		item := v.(*qItem)
		item.heat += d.field[item.y][item.x]

		if item.heat >= out && out > 0 {
			continue
		}

		c := mapKey{x: item.x, y: item.y, steps: item.steps, dir: item.dir}
		if v, ex := visited[c]; ex && v < item.heat {
			continue
		}

		if item.x == end.x && item.y == end.y {
			if item.heat < out || out < 0 {
				out = item.heat
			}
		}

		visited[c] = item.heat
		for _, n := range d.getNeighbours(item, minSteps, maxSteps) {
			n.len = abs(end.x-n.x) + abs(end.y-n.y)
			q.Push(n)
		}
	}

	return out
}

func (d *day17) getNeighbours(pos *qItem, minSteps, maxSteps int) []*qItem {
	m := map[int]*qItem{}
	m[0] = &qItem{x: pos.x, y: pos.y - 1, dir: 0, steps: 1, heat: pos.heat}
	m[1] = &qItem{x: pos.x + 1, y: pos.y, dir: 1, steps: 1, heat: pos.heat}
	m[2] = &qItem{x: pos.x, y: pos.y + 1, dir: 2, steps: 1, heat: pos.heat}
	m[3] = &qItem{x: pos.x - 1, y: pos.y, dir: 3, steps: 1, heat: pos.heat}

	m[pos.dir].steps = pos.steps + 1
	// delete backwards move
	delete(m, (pos.dir+2)%4)
	// remove invalid
	for k, item := range m {
		if item.x < 0 || item.x >= len(d.field[0]) || item.y < 0 || item.y >= len(d.field) || item.steps > maxSteps {
			delete(m, k)
			continue
		}

		if item.dir != pos.dir && pos.steps < minSteps {
			delete(m, k)
		}
	}

	return maps.Values(m)
}

func abs(v int) int {
	return int(math.Abs(float64(v)))
}
