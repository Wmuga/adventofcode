package day12

import (
	"aoc2023/days/aocday"
	"aoc2023/utils/parsers"
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
)

type day12 struct {
	lines   [][]rune
	conds   [][]int
	workers chan struct{}
}

type cacheKey struct {
	line  string
	conds string
}

var (
	reIsles     = regexp.MustCompile(`#*[\.\?]?`)
	reEmpty     = regexp.MustCompile(`^[\.\?]+$`)
	reStartDots = regexp.MustCompile(`^\.+`)
	workers     = 10
)

func New(inp string) aocday.AoCDay {
	out := &day12{
		lines:   make([][]rune, 0),
		conds:   make([][]int, 0),
		workers: make(chan struct{}, workers),
	}
	lines := strings.Split(inp, "\n")
	for _, line := range lines {
		if line == "" {
			continue
		}

		data := strings.Split(line, " ")
		out.lines = append(out.lines, []rune(data[0]))
		out.conds = append(out.conds, parsers.ExtractNums(data[1]))
	}
	return out
}

func (d *day12) base(dup bool) int64 {
	if dup {
		for i, line := range d.lines {
			b := strings.Builder{}
			// duplicate
			b.WriteString(string(line))
			for k := 0; k < 4; k++ {
				_, err := b.WriteString("?" + string(line))
				if err != nil {
					fmt.Println(err)
					return -1
				}
			}
			d.lines[i] = []rune(b.String())
		}
		for i, cond := range d.conds {
			newCond := make([]int, 0)
			for k := 0; k < 5; k++ {
				newCond = append(newCond, cond...)
			}
			d.conds[i] = newCond
		}
	}

	var out atomic.Int64
	var count atomic.Int64

	wg := &sync.WaitGroup{}
	for i, line := range d.lines {
		wg.Add(1)
		go func(l []rune, cond []int, w *sync.WaitGroup) {
			d.workers <- struct{}{}
			defer func() {
				<-d.workers
				wg.Done()
			}()
			out.Add(countVariants(l, cond, make(map[cacheKey]int64)))
			count.Add(1)
			if (count.Load()*100)%int64(len(d.lines)) == 0 {
				fmt.Print("Progress:", (count.Load()*100)/int64(len(d.lines)), "%\r")
			}
		}(line, d.conds[i], wg)
	}
	wg.Wait()

	return out.Load()
}

func (d *day12) SolveA(_ bool) string {
	out := d.base(false)
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(out, 10)
}

func (d *day12) SolveB(_ bool) string {
	out := d.base(true)
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(out, 10)
}

func countVariants(line []rune, cond []int, cache map[cacheKey]int64) int64 {
	if len(line) == 0 {
		if len(cond) == 0 {
			return 1
		}
		return 0
	}

	if len(cond) == 0 {
		if reEmpty.MatchString(string(line)) {
			return 1
		}
		return 0
	}

	dotsInd := reStartDots.FindStringIndex(string(line))
	if dotsInd != nil {
		return countVariants(line[dotsInd[1]:], cond, cache)
	}

	key := getKey(line, cond)

	if r, ex := cache[key]; ex {
		return r
	}

	isleInd := reIsles.FindStringIndex(string(line))
	match := line[isleInd[0]:isleInd[1]]
	if match[len(match)-1] == '?' {
		line[isleInd[1]-1] = '.'
		out := countVariants(line, cond, cache)
		line[isleInd[1]-1] = '#'
		out += countVariants(line, cond, cache)
		line[isleInd[1]-1] = '?'

		cache[key] = out

		return out
	}

	count := strings.Count(string(match), "#")
	if count == 0 {
		return countVariants(line[isleInd[1]:], cond, cache)
	}

	if count != cond[0] {
		return 0
	}

	return countVariants(line[isleInd[1]:], cond[1:], cache)
}

func getKey(line []rune, cond []int) cacheKey {
	return cacheKey{
		line:  string(line),
		conds: fmt.Sprint(cond),
	}
}
