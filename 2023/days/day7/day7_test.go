package day7

import (
	"reflect"
	"testing"
)

const inp1 = `32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483`

func TestParse(t *testing.T) {
	day := New(inp1).(*day7)
	cards := []card{
		{card: "32T3K", value: 765, hand: onep, handB: onep},
		{card: "T55J5", value: 684, hand: thok, handB: frok},
		{card: "KK677", value: 28, hand: twop, handB: twop},
		{card: "KTJJT", value: 220, hand: twop, handB: frok},
		{card: "QQQJA", value: 483, hand: thok, handB: frok},
	}

	if !reflect.DeepEqual(day.cards, cards) {
		t.Error("Wrong cards parsed,want:", cards, "got", day.cards, "\n")
	}
}

func TestA(t *testing.T) {
	day := New(inp1)
	res := day.SolveA(true)
	if res.(uint64) != 6440 {
		t.Error("Result", res, "is not equal to", 6440, "\n")
	}
}

func TestB(t *testing.T) {
	day := New(inp1)
	res := day.SolveB(true)
	if res.(uint64) != 5905 {
		t.Error("Result", res, "is not equal to", 5905, "\n")
	}
}
