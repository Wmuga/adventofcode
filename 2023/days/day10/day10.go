package day10

import (
	"aoc2023/days/aocday"
	"aoc2023/entity/pair"
	"aoc2023/entity/queue"
	"fmt"
	"log"
	"strconv"
	"strings"
)

type coord pair.Pair[int]

type day10 struct {
	pipes   [][]rune
	lengths [][]int
}

type qData struct {
	xy    coord
	steps int
}

func New(inp string) aocday.AoCDay {
	pipes := make([][]rune, 0)
	for _, line := range strings.Split(inp, "\n") {
		if len(line) == 0 {
			continue
		}
		pipes = append(pipes, []rune(line))
	}

	lengths := make([][]int, len(pipes))
	for i, v := range pipes {
		lengths[i] = make([]int, len(v))
		for j := range lengths[i] {
			lengths[i][j] = -1
		}
	}

	return &day10{
		pipes:   pipes,
		lengths: lengths,
	}
}

func (d *day10) setLengths() {
	// set all to -1
	d.lengths = make([][]int, len(d.pipes))
	for i, v := range d.pipes {
		d.lengths[i] = make([]int, len(v))
		for j := range d.lengths[i] {
			d.lengths[i][j] = -1
		}
	}

	start := coord{}

searchloop:
	for y, line := range d.pipes {
		for x, val := range line {
			if val == 'S' {
				start.X = x
				start.Y = y
				break searchloop
			}
		}
	}

	q := queue.New()

	err := q.Enqueue(qData{
		xy: start,
	})
	if err != nil {
		log.Fatalln(err)
	}

	// Simple BFS
	for !q.IsEmpty() {
		cur, err := q.Dequeue()
		if err != nil {
			log.Fatalln(err)
		}

		curPos := cur.(qData)

		if d.lengths[curPos.xy.Y][curPos.xy.X] <= curPos.steps && d.lengths[curPos.xy.Y][curPos.xy.X] >= 0 {
			continue
		}

		d.lengths[curPos.xy.Y][curPos.xy.X] = curPos.steps
		neigbours := d.getNeighbours(curPos.xy)

		for _, v := range neigbours {
			err = q.Enqueue(qData{
				xy:    v,
				steps: curPos.steps + 1,
			})

			if err != nil {
				log.Fatalln(err)
			}
		}
	}
}

func (d *day10) SolveA(_ bool) string {
	out := 0

	d.setLengths()

	// max length
	for _, line := range d.lengths {
		for _, v := range line {
			if v > out {
				out = v
			}
		}
	}
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(int64(out), 10)
}

func (d *day10) SolveB(deb bool) string {
	d.expandPipes()
	d.setLengths()

	// drop everything that is not main loop
	for y, line := range d.lengths {
		for x, v := range line {
			if v < 0 {
				d.pipes[y][x] = '.'
			}
		}
	}

	if deb {
		for _, line := range d.pipes {
			fmt.Println(string(line))
		}
	}

	for y := range d.pipes {
		for x := range d.pipes[y] {
			if d.pipes[y][x] == '.' {
				d.checkConnection(x, y)
			}
		}
	}

	// remove added
	d.compressPipes()

	if deb {
		for _, line := range d.pipes {
			fmt.Println(string(line))
		}
	}

	out := 0
	for _, line := range d.pipes {
		out += strings.Count(string(line), "I")
	}
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(int64(out), 10)
}

func canGoUp(pipe rune) bool {
	return pipe == '|' || pipe == 'L' || pipe == 'J' || pipe == 'S'
}

func canGoDown(pipe rune) bool {
	return pipe == '|' || pipe == 'F' || pipe == '7' || pipe == 'S'
}

func canGoLeft(pipe rune) bool {
	return pipe == '-' || pipe == '7' || pipe == 'J' || pipe == 'S'
}

func canGoRight(pipe rune) bool {
	return pipe == '-' || pipe == 'L' || pipe == 'F' || pipe == 'S'
}

func (d *day10) getNeighbours(xy coord) []coord {
	out := make([]coord, 0)
	if xy.Y != 0 && canGoUp(d.pipes[xy.Y][xy.X]) && canGoDown(d.pipes[xy.Y-1][xy.X]) {
		out = append(out, coord{X: xy.X, Y: xy.Y - 1})
	}
	if xy.X != 0 && canGoLeft(d.pipes[xy.Y][xy.X]) && canGoRight(d.pipes[xy.Y][xy.X-1]) {
		out = append(out, coord{X: xy.X - 1, Y: xy.Y})
	}
	if xy.Y != len(d.pipes)-1 && canGoDown(d.pipes[xy.Y][xy.X]) && canGoUp(d.pipes[xy.Y+1][xy.X]) {
		out = append(out, coord{X: xy.X, Y: xy.Y + 1})
	}
	if xy.X != len(d.pipes[xy.Y])-1 && canGoRight(d.pipes[xy.Y][xy.X]) && canGoLeft(d.pipes[xy.Y][xy.X+1]) {
		out = append(out, coord{X: xy.X + 1, Y: xy.Y})
	}
	return out
}

func (d *day10) tryGet(x, y int) rune {
	if y < 0 || y >= len(d.pipes) {
		return '0'
	}

	if x < 0 || x >= len(d.pipes[y]) {
		return '0'
	}

	return d.pipes[y][x]
}

func (d *day10) expandPipes() {
	pipes := make([][]rune, len(d.pipes)*2)
	for i, line := range d.pipes {
		newLine := make([]rune, len(line)*2)
		for i := range newLine {
			newLine[i] = '.'
		}
		// copy old
		for j, v := range line {
			if v == 0 {
				continue
			}
			newLine[j*2] = v
		}
		// setup new
		for j := range line {
			if j == len(line)-1 {
				continue
			}

			// if were connected - restore
			if canGoRight(d.pipes[i][j]) && canGoLeft(d.pipes[i][j+1]) {
				newLine[j*2+1] = '-'
			}
		}

		pipes[i*2] = newLine
		// will connect later
		addedLine := make([]rune, len(line)*2)
		for j := range addedLine {
			addedLine[j] = '.'
		}
		pipes[i*2+1] = addedLine
	}

	for j := range d.pipes[0] {
		for i := range d.pipes {
			if i == len(d.pipes)-1 {
				continue
			}
			// restore vert connection
			if canGoDown(d.pipes[i][j]) && canGoUp(d.pipes[i+1][j]) {
				pipes[i*2+1][j*2] = '|'
			}
		}
	}

	d.pipes = pipes
}

func (d *day10) compressPipes() {
	pipes := make([][]rune, len(d.pipes)/2)
	for i := range pipes {
		newLine := make([]rune, len(d.pipes[i*2])/2)
		for j := range newLine {
			newLine[j] = d.pipes[i*2][j*2]
		}
		pipes[i] = newLine
	}
	d.pipes = pipes
}

func (d *day10) checkConnection(x, y int) {
	visited := map[coord]struct{}{}

	nonEdge := true

	q := queue.New()
	err := q.Enqueue(qData{xy: coord{X: x, Y: y}})
	if err != nil {
		log.Fatalln(err)
	}
	// seatching all connected dots
	for !q.IsEmpty() {
		val, err := q.Dequeue()
		if err != nil {
			log.Fatalln(err)
		}

		cur := val.(qData)
		if _, ex := visited[cur.xy]; ex {
			continue
		}

		visited[cur.xy] = struct{}{}

		coords := []coord{{X: cur.xy.X + 1, Y: cur.xy.Y}, {X: cur.xy.X - 1, Y: cur.xy.Y}, {X: cur.xy.X, Y: cur.xy.Y + 1}, {X: cur.xy.X, Y: cur.xy.Y - 1}}
		for _, c := range coords {
			s := d.tryGet(c.X, c.Y)
			if s == '.' {
				err = q.Enqueue(qData{xy: c})
				if err != nil {
					log.Fatalln(err)
				}
				continue
			}
			// edge connected
			if s == '0' {
				nonEdge = false
			}
		}
	}

	if nonEdge {
		// set as visited hidden
		for k := range visited {
			d.pipes[k.Y][k.X] = 'I'
		}
		return
	}

	for k := range visited {
		d.pipes[k.Y][k.X] = '0'
	}
}
