package day15

import (
	"aoc2023/days/aocday"
	"fmt"
	"os"
	"reflect"
	"slices"
	"strconv"
	"strings"
)

type lens struct {
	label []rune
	focal int
}

type day15 struct {
	steps [][]rune
	boxes [256][]*lens
}

func New(inp string) aocday.AoCDay {
	steps := strings.Split(strings.Trim(inp, "\n "), ",")
	d := &day15{
		steps: make([][]rune, len(steps)),
	}

	for i, s := range steps {
		d.steps[i] = []rune(s)
	}

	return d
}

func (d *day15) SolveA(deb bool) string {
	out := int64(0)
	for i, v := range d.steps {
		res := hash(v)
		if deb {
			fmt.Println("Step", i, ":", res)
		}
		out += int64(res)
	}
	fmt.Println("Solution A: ", out)
	return strconv.FormatInt(out, 10)
}

func (d *day15) SolveB(deb bool) string {
	for _, v := range d.steps {
		l, add := parseLens(v)
		num := hash(l.label)
		if add {
			// search for existing
			ind := slices.IndexFunc(d.boxes[num], searcher(l))
			if ind != -1 {
				if deb {
					fmt.Printf("Replace at %v. %v with %v\n", num, string(l.label), l.focal)
				}
				d.boxes[num][ind].focal = l.focal
				continue
			}

			d.boxes[num] = append(d.boxes[num], l)

			if deb {
				fmt.Printf("Added to %v. [%v %v]\n", num, string(l.label), l.focal)
			}

			continue
		}

		// search
		ind := slices.IndexFunc(d.boxes[num], searcher(l))
		if ind == -1 {
			if deb {
				fmt.Printf("Can't remove from %v. [%v %v]\n", num, string(l.label), l.focal)
			}
			continue
		}
		if deb {
			fmt.Printf("Remove from %v. [%v %v]\n", num, string(l.label), l.focal)
		}
		// remove
		d.boxes[num] = append(d.boxes[num][:ind], d.boxes[num][ind+1:]...)
	}

	out := int64(0)

	for i, box := range d.boxes {
		for j, v := range box {
			out += int64(i+1) * int64(j+1) * int64(v.focal)

			if deb {
				fmt.Printf("%v: box %v, slot %v, focal %v\n", string(v.label), i, j+1, v.focal)
			}

		}
	}

	fmt.Println("Solution B: ", out)
	return strconv.FormatInt(out, 10)
}

func parseLens(inp []rune) (l *lens, add bool) {
	out := &lens{}
	if inp[len(inp)-1] == '-' {
		out.label = inp[:len(inp)-1]
		return out, false
	}

	pos := slices.Index(inp, '=')
	out.label = inp[:pos]
	focal, err := strconv.ParseInt(string(inp[pos+1:]), 10, 32)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	out.focal = int(focal)

	return out, true
}

func hash(inp []rune) int {
	out := 0

	for _, v := range inp {
		out += int(v)
		out = ((out % 256) * 17) % 256
	}

	return out
}

func searcher(l *lens) func(e *lens) bool {
	return func(e *lens) bool {
		return reflect.DeepEqual(e.label, l.label)
	}
}
