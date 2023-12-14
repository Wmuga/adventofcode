package day4

import (
	aoc "aoc2023/days/aocday"
	"fmt"
	"math"
	"strconv"
	"strings"
)

type card struct {
	winning map[int]struct{}
	have    map[int]struct{}
}

type day4 struct {
	cards []card
}

func New(inp string) aoc.AoCDay {
	d := &day4{
		cards: make([]card, 0),
	}
	for _, line := range strings.Split(inp, "\n") {
		if len(line) == 0 {
			continue
		}
		d.cards = append(d.cards, parseCard(line))
	}
	return d
}

func (d *day4) SolveA(_ bool) string {
	out := 0
	for _, card := range d.cards {
		count := intersect(card.winning, card.have)
		if count == 0 {
			continue
		}
		out += int(math.Pow(2.0, float64(count-1)))
	}
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(int64(out), 10)
}
func (d *day4) SolveB(deb bool) string {
	cards := make([]int, len(d.cards))
	for i := range cards {
		cards[i] = 1
	}

	for i := range cards {
		card := d.cards[i]
		k := cards[i]
		count := intersect(card.winning, card.have)
		for j := 1; j <= count; j++ {
			cards[i+j] += k
		}
	}
	out := 0
	for _, v := range cards {
		out += v
	}
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(int64(out), 10)
}

func parseCard(line string) card {
	out := card{
		winning: make(map[int]struct{}),
		have:    make(map[int]struct{}),
	}
	// remove card nn:
	data := strings.Split(line, ": ")
	if len(data) == 1 {
		fmt.Println("Wrong line of data")
		return out
	}
	// split by " | "
	data = strings.Split(data[1], " | ")
	out.winning = parseNumbs(data[0])
	out.have = parseNumbs(data[1])
	return out
}

func parseNumbs(line string) map[int]struct{} {
	out := make(map[int]struct{})
	numbs := strings.Split(line, " ")
	for _, num := range numbs {
		num = strings.Trim(num, " ")
		if len(num) == 0 {
			continue
		}
		val, err := strconv.Atoi(num)
		if err != nil {
			fmt.Println(num, "is not a number")
			continue
		}
		out[val] = struct{}{}
	}
	return out
}

func intersect(lhs, rhs map[int]struct{}) int {
	count := 0
	for k := range lhs {
		if _, ex := rhs[k]; ex {
			count++
		}
	}
	return count
}
