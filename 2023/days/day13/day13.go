package day13

import (
	"aoc2023/days/aocday"
	"aoc2023/utils/tools"
	"fmt"
	"slices"
	"strings"
)

type day13 struct {
	patterns [][][]rune
}

func New(inp string) aocday.AoCDay {
	out := &day13{
		patterns: make([][][]rune, 0),
	}

	for _, lines := range strings.Split(inp, "\n\n") {
		if len(lines) == 0 {
			continue
		}

		runes := make([][]rune, 0)
		for _, line := range strings.Split(lines, "\n") {
			if line == "" {
				continue
			}
			runes = append(runes, []rune(line))
		}

		out.patterns = append(out.patterns, runes)
	}

	return out
}

func findMirror(patterns [][]rune, errors int, vert bool) int64 {
	for i := 1; i < len(patterns[0]); i++ {
		found := true

		lhs := i
		rhs := len(patterns[0]) - i
		curErr := 0

		if lhs < rhs {
			for _, line := range patterns {
				left := line[:i]
				right := slices.Clone(line[i : i+lhs])
				slices.Reverse(right)
				// Search for errors
				for i := range left {
					if left[i] != right[i] {
						curErr++
						if curErr > errors {
							found = false
							break
						}
					}
				}
			}
		} else {
			for _, line := range patterns {
				left := line[i-rhs : i]
				right := slices.Clone(line[i:])
				slices.Reverse(right)
				// Search for errors
				for i := range left {
					if left[i] != right[i] {
						curErr++
						if curErr > errors {
							found = false
							break
						}
					}
				}
			}
		}

		if found && curErr == errors {
			if vert {
				return int64(i)
			}
			return int64(i) * 100
		}
	}

	if vert {
		pat := tools.Transpose(patterns)
		slices.Reverse(pat)
		return findMirror(pat, errors, false)
	}

	return 0
}

func (d *day13) base(errors int) int64 {
	var out int64 = 0
	for i, patterns := range d.patterns {
		res := findMirror(patterns, errors, true)
		if res == 0 {
			fmt.Println("Can't find at", i+1, "/", len(d.patterns))
		}
		out += res
	}
	return out
}

func (d *day13) SolveA(_ bool) interface{} {
	out := d.base(0)
	fmt.Println("Solution A:", out)
	return out
}

func (d *day13) SolveB(_ bool) interface{} {
	out := d.base(1)
	fmt.Println("Solution B:", out)
	return out
}
