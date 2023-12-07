package day7

import (
	"aoc2023/days/aocday"
	"fmt"
	"slices"
	"strconv"
	"strings"

	"github.com/dlclark/regexp2"
)

type hType int

const (
	high hType = iota
	onep
	twop
	thok
	full
	frok
	fvok
)

type card struct {
	card  string
	value int
	hand  hType
	handB hType
}

type day7 struct {
	cards []card
}

var (
	reFive  = regexp2.MustCompile(`(.)\1{4}`, 0)
	reFour  = regexp2.MustCompile(`(.)\1{3}`, 0)
	reHouse = regexp2.MustCompile(`((.)\2{2}(.)\3)|((.)\5(.)\6{2})`, 0)
	reThree = regexp2.MustCompile(`(.)\1{2}`, 0)
	reTwoP  = regexp2.MustCompile(`(.)\1.?(.)\2`, 0)
	rePair  = regexp2.MustCompile(`(.)\1`, 0)
)

func New(inp string) aocday.AoCDay {
	return &day7{
		cards: parseCards(inp),
	}
}
func (d *day7) SolveA(deb bool) interface{} {
	var out uint64 = 0
	cards := make(map[hType][]card)
	for _, c := range d.cards {
		if _, ex := cards[c.hand]; !ex {
			cards[c.hand] = make([]card, 0)
		}
		cards[c.hand] = append(cards[c.hand], c)
	}
	for _, v := range cards {
		slices.SortFunc(v, func(a, b card) int {
			if less([]rune(a.card), []rune(b.card), toValA) {
				return -1
			}
			return 1
		})
	}
	rank := 1
	for t := high; t <= fvok; t++ {
		for _, c := range cards[t] {
			out += uint64(c.value * rank)
			if deb {
				fmt.Println("Card", c, "with rank", rank)
			}
			rank++
		}
	}
	fmt.Println("Solution A:", out)
	return out
}
func (d *day7) SolveB(deb bool) interface{} {
	var out uint64 = 0
	cards := make(map[hType][]card)
	for _, c := range d.cards {
		if _, ex := cards[c.handB]; !ex {
			cards[c.handB] = make([]card, 0)
		}
		cards[c.handB] = append(cards[c.handB], c)
	}

	for _, v := range cards {
		slices.SortFunc(v, func(a, b card) int {
			if less([]rune(a.card), []rune(b.card), toValB) {
				return -1
			}
			return 1
		})
	}

	rank := 1
	for t := high; t <= fvok; t++ {
		for _, c := range cards[t] {
			out += uint64(c.value * rank)
			if deb {
				fmt.Println("Card", c, "with rank", rank)
			}
			rank++
		}
	}
	fmt.Println("Solution B:", out)
	return out
}

func parseCards(inp string) []card {
	lines := strings.Split(inp, "\n")
	out := make([]card, 0)
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		out = append(out, parseCard(line))
	}
	return out
}

func parseCard(inp string) card {
	c := card{}
	data := strings.Split(inp, " ")
	if len(data) != 2 {
		fmt.Println(inp, "is not a card")
		return c
	}
	c.card = data[0]
	num, err := strconv.Atoi(data[1])
	if err != nil {
		fmt.Println("Can't parse", data[1])
		return c
	}
	c.value = num
	c.hand = assignType(c.card)

	if strings.Count(c.card, "J") == 0 {
		c.handB = c.hand
		return c
	}

	vals := []rune(strings.ReplaceAll(c.card, "J", ""))
	if len(vals) == 0 {
		vals = []rune{'A'}
	}

	for _, val := range vals {
		newCard := strings.ReplaceAll(c.card, "J", string(val))
		newType := assignType(newCard)
		if newType > c.handB {
			c.handB = newType
		}
	}

	return c
}

func assignType(cardStr string) hType {
	nums := []rune(cardStr)
	slices.Sort(nums)
	numsStr := string(nums)
	switch {
	case matchReg(reFive, numsStr):
		return fvok
	case matchReg(reFour, numsStr):
		return frok
	case matchReg(reHouse, numsStr):
		return full
	case matchReg(reThree, numsStr):
		return thok
	case matchReg(reTwoP, numsStr):
		return twop
	case matchReg(rePair, numsStr):
		return onep
	}
	return high
}

func less(l, r []rune, conv func(rune) int) bool {
	for i := range l {
		if l[i] == r[i] {
			continue
		}
		return conv(l[i]) < conv(r[i])
	}
	return false
}

var valsA = []rune("23456789TJQKA")
var valsB = []rune("J23456789TQKA")

func toValA(v rune) int {
	return slices.Index(valsA, v)
}
func toValB(v rune) int {
	return slices.Index(valsB, v)
}

func matchReg(re *regexp2.Regexp, str string) bool {
	s, e := re.MatchString(str)
	if e != nil {
		return false
	}
	return s
}
