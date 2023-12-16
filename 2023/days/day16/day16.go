package day16

import (
	"aoc2023/days/aocday"
	"aoc2023/entity/pair"
	"aoc2023/entity/queue"
	"aoc2023/entity/set"
	"aoc2023/utils/parsers"
	"aoc2023/utils/tools"
	"fmt"
	"strconv"
)

type day16 struct {
	field [][]rune
	tiles set.Set[coord]
}

type coord pair.Pair[int]

type beam struct {
	xy  coord
	dir int
}

func New(inp string) aocday.AoCDay {
	return &day16{
		field: parsers.GetLinesRune(inp),
	}
}

func (d *day16) SolveA(deb bool) string {
	out := d.bounce(&beam{xy: coord{X: 0, Y: 0}, dir: 0})
	if deb {
		printField(d.field, d.tiles.Values())
	}
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(int64(out), 10)
}

func (d *day16) SolveB(_ bool) string {
	starts := make([]*beam, 0)
	for i := range d.field[0] {
		starts = append(starts, &beam{xy: coord{X: i, Y: 0}, dir: 1}, &beam{xy: coord{X: i, Y: len(d.field) - 1}, dir: 3})
	}
	for i := range d.field {
		starts = append(starts, &beam{xy: coord{X: 0, Y: i}, dir: 0}, &beam{xy: coord{X: len(d.field[0]) - 1, Y: i}, dir: 2})
	}
	out := 0
	for _, s := range starts {
		temp := d.bounce(s)
		if temp > out {
			out = temp
		}
	}
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(int64(out), 10)
}

// м.б кеш
func (d *day16) bounce(start *beam) int {
	tiles := set.New[coord]()
	visited := set.New[beam]()
	q := queue.New()

	err := q.Enqueue(start)
	if err != nil {
		fmt.Print(err)
		return -1
	}

	for !q.IsEmpty() {
		v, err := q.Dequeue()
		if err != nil {
			fmt.Print(err)
			return -1
		}

		val := v.(*beam)
		// check for out of bound
		if val.xy.X < 0 || val.xy.X >= len(d.field[0]) || val.xy.Y < 0 || val.xy.Y >= len(d.field) {
			continue
		}

		tiles.Append(val.xy)
		// Skip if beam crossed tile with same direction
		if !visited.Append(*val) {
			continue
		}

		switch val.dir {
		case 0:
			err = d.right(q, val)
		case 1:
			err = d.down(q, val)
		case 2:
			err = d.left(q, val)
		case 3:
			err = d.up(q, val)
		}

		if err != nil {
			return -1
		}
	}
	d.tiles = tiles
	return tiles.Count()
}

func (d *day16) right(q queue.Queue, val *beam) error {
	// current tile
	switch d.field[val.xy.Y][val.xy.X] {
	case '.':
		fallthrough
	case '-':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X + 1, Y: val.xy.Y}, dir: 0})
		if err != nil {
			fmt.Println(err)
			return err
		}
	case '|':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X, Y: val.xy.Y + 1}, dir: 1})
		err2 := q.Enqueue(&beam{xy: coord{X: val.xy.X, Y: val.xy.Y - 1}, dir: 3})
		if err != nil || err2 != nil {
			fmt.Println(err, err2)
			return err
		}
	case '/':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X, Y: val.xy.Y - 1}, dir: 3})
		if err != nil {
			fmt.Println(err)
			return err
		}
	case '\\':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X, Y: val.xy.Y + 1}, dir: 1})
		if err != nil {
			fmt.Println(err)
			return err
		}
	}
	return nil
}

func (d *day16) left(q queue.Queue, val *beam) error {
	// current tile
	switch d.field[val.xy.Y][val.xy.X] {
	case '.':
		fallthrough
	case '-':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X - 1, Y: val.xy.Y}, dir: 2})
		if err != nil {
			fmt.Println(err)
			return err
		}
	case '|':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X, Y: val.xy.Y + 1}, dir: 1})
		err2 := q.Enqueue(&beam{xy: coord{X: val.xy.X, Y: val.xy.Y - 1}, dir: 3})
		if err != nil || err2 != nil {
			fmt.Println(err, err2)
			return err
		}
	case '/':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X, Y: val.xy.Y + 1}, dir: 1})
		if err != nil {
			fmt.Println(err)
			return err
		}
	case '\\':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X, Y: val.xy.Y - 1}, dir: 3})
		if err != nil {
			fmt.Println(err)
			return err
		}
	}
	return nil
}

func (d *day16) down(q queue.Queue, val *beam) error {
	// current tile
	switch d.field[val.xy.Y][val.xy.X] {
	case '-':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X + 1, Y: val.xy.Y}, dir: 0})
		err2 := q.Enqueue(&beam{xy: coord{X: val.xy.X - 1, Y: val.xy.Y}, dir: 2})
		if err != nil || err2 != nil {
			fmt.Println(err, err2)
			return err
		}

	case '.':
		fallthrough
	case '|':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X, Y: val.xy.Y + 1}, dir: 1})
		if err != nil {
			fmt.Println(err)
			return err
		}
	case '/':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X - 1, Y: val.xy.Y}, dir: 2})
		if err != nil {
			fmt.Println(err)
			return err
		}
	case '\\':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X + 1, Y: val.xy.Y}, dir: 0})
		if err != nil {
			fmt.Println(err)
			return err
		}
	}
	return nil
}

func (d *day16) up(q queue.Queue, val *beam) error {
	// current tile
	switch d.field[val.xy.Y][val.xy.X] {
	case '-':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X + 1, Y: val.xy.Y}, dir: 0})
		err2 := q.Enqueue(&beam{xy: coord{X: val.xy.X - 1, Y: val.xy.Y}, dir: 2})
		if err != nil || err2 != nil {
			fmt.Println(err, err2)
			return err
		}

	case '.':
		fallthrough
	case '|':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X, Y: val.xy.Y - 1}, dir: 3})
		if err != nil {
			fmt.Println(err)
			return err
		}
	case '/':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X + 1, Y: val.xy.Y}, dir: 0})
		if err != nil {
			fmt.Println(err)
			return err
		}
	case '\\':
		err := q.Enqueue(&beam{xy: coord{X: val.xy.X - 1, Y: val.xy.Y}, dir: 2})
		if err != nil {
			fmt.Println(err)
			return err
		}
	}
	return nil
}

func printField(field [][]rune, tiles []coord) {
	f, err := tools.Clone(field)
	if err != nil {
		fmt.Println(err)
		return
	}
	for _, xy := range tiles {
		f[xy.Y][xy.X] = '#'
	}

	for _, line := range f {
		fmt.Println(string(line))
	}
}
