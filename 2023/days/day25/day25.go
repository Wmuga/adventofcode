package day25

import (
	aoc "aoc2023/days/aocday"
	"aoc2023/entity/pair"
	"aoc2023/entity/queue"
	"aoc2023/entity/set"
	"aoc2023/utils/parsers"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type day25 struct {
	components      map[string]int
	componentsNames map[int]string
	connections     [1500][1500]bool
	consPair        []pair.Pair[int]
	lastNum         int
}

func (d *day25) getOrSetNum(name string) int {
	if val, ex := d.components[name]; ex {
		return val
	}
	d.components[name] = d.lastNum
	d.componentsNames[d.lastNum] = name
	d.lastNum++
	return d.components[name]
}

func New(inp string) aoc.AoCDay {
	d := &day25{
		components:      map[string]int{},
		componentsNames: map[int]string{},
	}
	lines := parsers.GetLinesString(inp)

	// connection matrix
	for _, line := range lines {
		data := strings.Split(line, ":")
		name := data[0]
		cons := strings.Split(data[1], " ")
		curI := d.getOrSetNum(name)
		// d.connections[curI][curI] = true
		for _, c := range cons {
			if c == "" {
				continue
			}
			conI := d.getOrSetNum(c)
			d.connections[curI][conI] = true
			d.connections[conI][curI] = true
			d.consPair = append(d.consPair, pair.Pair[int]{X: curI, Y: conI})
		}
	}

	return d
}

func (d *day25) count() int64 {

	toRemove := []pair.Pair[string]{{X: "lkm", Y: "ffj"}, {X: "ljl", Y: "xhg"}, {X: "vgs", Y: "xjb"}}

	for _, p := range toRemove {
		x := d.components[p.X]
		y := d.components[p.Y]
		d.connections[x][y] = false
		d.connections[y][x] = false
	}

	visited := set.New[int]()
	q := queue.New()
	q.Enqueue(0) //nolint:errcheck

	for !q.IsEmpty() {
		item, _ := q.Dequeue() //nolint:errcheck
		num := item.(int)

		if !visited.Append(num) {
			continue
		}

		for i, val := range d.connections[num] {
			if val {
				q.Enqueue(i) //nolint:errcheck
			}
		}
	}

	return int64(visited.Count()) * int64(len(d.components)-visited.Count())
}

func (d *day25) createdot() {
	file, err := os.Create("temp.dot")
	if err != nil {
		panic(err)
	}

	visited := set.New[pair.Pair[int]]()

	fmt.Fprintln(file, "digraph {")

	for nameL, num := range d.components {
		for i, con := range d.connections[num] {
			if con && i != num {
				p := pair.Pair[int]{X: i, Y: num}
				if i > num {
					p = pair.Pair[int]{X: num, Y: i}
				}

				if !visited.Append(p) {
					continue
				}

				nameR := d.componentsNames[i]
				fmt.Fprintf(file, "%v -> %v\n", nameL, nameR)
			}
		}
	}
	fmt.Fprintln(file, "}")

}

func (d *day25) SolveA(_ bool) string {
	d.createdot()
	out := d.count()
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(out, 10)
}

func (d *day25) SolveB(_ bool) string {
	out := int64(0)
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(out, 10)
}
