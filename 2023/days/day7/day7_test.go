package day7

import (
	"aoc2023/utils/tester"
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
	tester.Assert(0, "A", day.SolveA(true), "6440", t)
}

func TestB(t *testing.T) {
	day := New(inp1)
	tester.Assert(0, "B", day.SolveB(true), "5905", t)
}
