package day6

import (
	"aoc2023/days/aocday"
	"aoc2023/utils/parsers"
	"fmt"
	"math"
	"strconv"
	"strings"
)

type day6 struct {
	times []int
	dists []int
}

func New(inp string) aocday.AoCDay {
	lines := strings.Split(inp, "\n")
	d := &day6{
		times: parsers.ExtractNums(lines[0]),
		dists: parsers.ExtractNums(lines[1]),
	}
	return d
}

func calcCount(time, dist int, deb bool) int {
	d := math.Sqrt(float64(time*time - 4*dist))
	x1 := math.Max((float64(time)-d)/2, 0)
	x2 := (float64(time) + d) / 2
	count := int(math.Ceil(x2) - math.Floor(x1) - 1)
	if deb {
		fmt.Println("Count:", count, x1, x2, time, dist)
	}
	return count
}

func (d *day6) SolveA(deb bool) interface{} {
	out := 1
	for i := range d.times {
		count := calcCount(d.times[i], d.dists[i], deb)
		out *= count
	}
	fmt.Println("Solution A:", out)
	return out
}

func (d *day6) SolveB(deb bool) interface{} {
	times := ""
	dists := ""
	for _, time := range d.times {
		times += strconv.Itoa(time)
	}
	for _, dist := range d.dists {
		dists += strconv.Itoa(dist)
	}
	time, err := strconv.Atoi(times)
	dist, err2 := strconv.Atoi(dists)
	if err != nil || err2 != nil {
		fmt.Println("Can't convert back", times, "and", dists)
		return nil
	}
	out := calcCount(time, dist, deb)
	fmt.Println("Solution B:", out)
	return out
}
