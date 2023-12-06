package day3

import (
	aoc "aoc2023/days/aocday"
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

type xy complex128 // x - real, y - imaginary

type day3 struct {
	numbers map[xy]gameObject
	symbols map[xy]gameObject
	stars   map[xy][]gameObject
}

type gameObject struct {
	number   int
	symbol   rune
	isSymbol bool
	coord    xy
	width    int
}

func New(inp string) aoc.AoCDay {
	day := &day3{
		numbers: make(map[xy]gameObject),
		symbols: make(map[xy]gameObject),
		stars:   make(map[xy][]gameObject),
	}

	lines := strings.Split(inp, "\n")
	for i, line := range lines {
		day.extractFromLine(i, line)
	}

	return day
}

func (d *day3) SolveA(deb bool) interface{} {
	out := 0
	for _, num := range d.numbers {
		if d.hasAdjacent(num) {
			out += num.number
			continue
		}
		if deb {
			fmt.Println("Number", num.number, "at", num.coord, "skipped")
		}
	}
	fmt.Println("Solution A:", out)
	return out
}
func (d *day3) SolveB(deb bool) interface{} {
	out := 0
	for coord, adj := range d.stars {
		if len(adj) != 2 {
			continue
		}
		rat := adj[0].number * adj[1].number
		if deb {
			fmt.Println("Gear at", coord, "with ratio", rat)
		}
		out += rat
	}
	fmt.Println("Solution B:", out)
	return out
}

func (d *day3) extractFromLine(y int, line string) {
	buffer := ""
	x := 0
	for i, c := range line {
		// dot is “not a symbol”. Buffer reset
		if c == '.' {
			d.addSymbol(buffer, x, y)
			buffer = ""
			continue
		}
		// Adding a digit to the buffer
		if unicode.IsDigit(c) {
			// If just started filling, update x
			if buffer == "" {
				x = i
			}
			buffer += string(c)
			continue
		}
		// Reset buffer, add character to pool
		d.addSymbol(buffer, x, y)
		d.addSymbol(string(c), i, y)
		buffer = ""
	}
	// Additional buffer reset
	d.addSymbol(buffer, x, y)
}

func (d *day3) addSymbol(buffer string, x, y int) {
	coord := xy(complex(float64(x), float64(y)))
	switch len(buffer) {
	case 0:
		return
	case 1:
		r := []rune(buffer)[0]
		if unicode.IsDigit(r) {
			d.parseNumber(buffer, coord)
			return
		}
		d.symbols[coord] = gameObject{
			isSymbol: true,
			coord:    coord,
			symbol:   r,
		}
	default:
		d.parseNumber(buffer, coord)
	}
}

func (d *day3) parseNumber(buffer string, coord xy) {
	num, err := strconv.Atoi(buffer)
	if err != nil {
		fmt.Println(buffer, "is not a number")
	}
	d.numbers[coord] = gameObject{
		coord:  coord,
		number: num,
		width:  len(buffer),
	}
}

func (d *day3) hasAdjacent(numb gameObject) bool {
	xBase := int(real(numb.coord))
	yBase := int(imag(numb.coord))
	xL := xBase - 1
	yL := yBase - 1
	xR := xBase + numb.width
	yR := yBase + 1
	found := false
	for y := yL; y <= yR; y++ {
		for x := xL; x <= xR; x++ {
			// skip number
			if y == yBase && !(x == xR || x == xL) {
				continue
			}
			coord := xy(complex(float64(x), float64(y)))
			if s, ex := d.symbols[coord]; ex {
				found = true
				// for part B
				if s.symbol == '*' {
					if _, ex = d.stars[coord]; !ex {
						d.stars[coord] = make([]gameObject, 0)
					}
					d.stars[coord] = append(d.stars[coord], numb)
				}
			}
		}
	}
	return found
}
