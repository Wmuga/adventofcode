package day14

import (
	"aoc2023/days/aocday"
	"aoc2023/utils/parsers"
	"aoc2023/utils/tools"
	"fmt"
	"strconv"
	"strings"
)

type day14 struct {
	fieldBase [][]rune
	field     [][]rune
}

func New(inp string) aocday.AoCDay {
	d := &day14{
		fieldBase: parsers.GetLinesRune(inp),
	}
	return d
}

func (d *day14) SolveA(_ bool) string {
	d.move(0, d.fieldBase)
	out := d.count()
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(out, 10)
}

func (d *day14) SolveB(_ bool) string {
	f, err := tools.Clone(d.fieldBase)
	if err != nil {
		fmt.Println(err)
		return "0"
	}

	times := int64(1000000000)

	cache := make(map[string]int64)
	d.field = f

	counter := int64(0)
	for counter <= times {
		for i := 0; i < 4; i++ {
			d.move(i, d.field)
		}
		counter++
		key := parsers.RunesToString(d.field)
		if start, ex := cache[key]; ex {
			cLen := counter - start
			// Number of needed field
			num := ((times - start) % cLen) + start
			// Search
			for k, v := range cache {
				if v == num {
					d.field = parsers.GetLinesRune(k)
					break
				}
			}
			// Out
			break
		}
		cache[key] = counter
	}
	out := d.count()
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(out, 10)
}

func (d *day14) count() int64 {
	out := int64(0)
	for y, line := range d.field {
		rocks := strings.Count(string(line), "O")
		out += int64(rocks) * int64(len(d.field)-y)
	}
	return out
}

func (d *day14) move(dir int, field [][]rune) {
	f, err := tools.Clone(field)
	if err != nil {
		fmt.Println(err)
		return
	}

	switch dir {
	case 0:
		moveUp(f)
	case 1:
		moveLeft(f)
	case 2:
		moveDown(f)
	case 3:
		moveRight(f)
	default:
		fmt.Println("Wrong direction")
	}

	d.field = f
}

func moveUp(field [][]rune) {
	changed := true

	for changed {
		changed = false
		for i := 1; i < len(field); i++ {
			for j := range field[i] {
				if field[i-1][j] == '.' && field[i][j] == 'O' {
					changed = true
					field[i-1][j] = 'O'
					field[i][j] = '.'
				}
			}
		}
	}

}

func moveRight(field [][]rune) {
	changed := true
	for changed {
		changed = false
		for _, line := range field {
			for j := len(line) - 2; j >= 0; j-- {
				if line[j] == 'O' && line[j+1] == '.' {
					line[j+1] = 'O'
					line[j] = '.'
					changed = true
				}
			}
		}
	}
}

func moveLeft(field [][]rune) {
	changed := true
	for changed {
		changed = false
		for _, line := range field {
			for j := 1; j < len(line); j++ {
				if line[j] == 'O' && line[j-1] == '.' {
					line[j-1] = 'O'
					line[j] = '.'
					changed = true
				}
			}
		}
	}
}

func moveDown(field [][]rune) {
	changed := true

	for changed {
		changed = false
		for i := len(field) - 2; i >= 0; i-- {
			for j := range field[i] {
				if field[i+1][j] == '.' && field[i][j] == 'O' {
					changed = true
					field[i+1][j] = 'O'
					field[i][j] = '.'
				}
			}
		}
	}
}

func (d *day14) printField() {
	fmt.Println(parsers.RunesToString(d.field))
}
