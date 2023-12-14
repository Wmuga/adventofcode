package day5

import (
	aoc "aoc2023/days/aocday"
	"fmt"
	"math"
	"strconv"
	"strings"
	"sync"
)

type interval struct {
	start uint
	end   uint
}

type intervals struct {
	lhs []interval
	rhs []interval
}

type day5 struct {
	rules []intervals
	items []uint
}

func New(inp string) aoc.AoCDay {
	items := strings.Split(inp, "\n\n")
	d := &day5{
		items: parseSeeds(items[0]),
		rules: make([]intervals, 0),
	}
	for i, v := range items {
		if i == 0 {
			continue
		}
		d.rules = append(d.rules, parseIntervals(strings.Split(v, "\n")))
	}
	return d
}

func (d *day5) convert(v uint, deb bool) uint {
	item := v
	if deb {
		fmt.Print(v)
	}
	for _, rule := range d.rules {
		item = rule.convert(item, deb)
	}
	if deb {
		fmt.Println()
	}
	return item
}

func (d *day5) SolveA(deb bool) string {
	convs := make([]uint, len(d.items))
	for i, v := range d.items {
		convs[i] = d.convert(v, deb)
	}
	out := convs[0]
	for _, v := range convs {
		if out > v {
			out = v
		}
	}
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(int64(out), 10)
}

func (d *day5) SolveB(deb bool) string {
	out := uint(math.MaxInt32)
	wg := sync.WaitGroup{}
	mu := sync.Mutex{}
	for i := 0; i < len(d.items); i += 2 {
		for v := d.items[i]; v < d.items[i]+d.items[i+1]; v++ {
			wg.Add(1)
			go func(val uint) {
				defer wg.Done()
				n := d.convert(val, deb)
				mu.Lock()
				defer mu.Unlock()
				if n < out {
					out = n
				}
			}(v)
		}
		wg.Wait()
	}

	fmt.Println("Solution B:", out)
	return strconv.FormatInt(int64(out), 10)
}

func parseIntervals(inp []string) intervals {
	out := intervals{
		lhs: make([]interval, len(inp)-1),
		rhs: make([]interval, len(inp)-1),
	}

	numbs := make([]uint, 3)

	for i, line := range inp {
		if len(line) == 0 {
			continue
		}
		// skip name
		if i == 0 {
			continue
		}
		numbsStr := strings.Split(line, " ")

		if len(numbsStr) != 3 {
			fmt.Println("Can't parse line", i)
			continue
		}

		for i, s := range numbsStr {
			parsed, err := strconv.ParseUint(s, 10, 32)
			if err != nil {
				fmt.Println("Can't parse number", s)
				continue
			}
			numbs[i] = uint(parsed)
		}
		lInt := interval{
			start: numbs[1],
			end:   numbs[1] + numbs[2] - 1,
		}
		rInt := interval{
			start: numbs[0],
			end:   numbs[0] + numbs[2] - 1,
		}
		out.lhs[i-1] = lInt
		out.rhs[i-1] = rInt
	}
	return out
}

func parseSeeds(inp string) []uint {
	str := strings.Split(inp, " ")
	seeds := make([]uint, len(str)-1)
	for i, v := range str {
		if i == 0 {
			continue
		}
		s, err := strconv.ParseUint(v, 10, 32)
		if err != nil {
			fmt.Println("Can't parse number", v)
			continue
		}
		seeds[i-1] = uint(s)
	}
	return seeds
}

func (inter *intervals) convert(val uint, deb bool) uint {
	for i := range inter.lhs {
		lhs := inter.lhs[i]
		rhs := inter.rhs[i]
		if val >= lhs.start && val <= lhs.end {
			out := val - lhs.start + rhs.start
			if deb {
				fmt.Print("->", out)
			}
			return out
		}
	}

	if deb {
		fmt.Print("->", val)
	}
	return val
}
