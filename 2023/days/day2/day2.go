package day2

import (
	aoc "aoc2023/days/aocday"
	"fmt"
	"strconv"
	"strings"
)

type bundle struct {
	red   int
	green int
	blue  int
}

type day2 struct {
	games [][]*bundle
}

var (
	maxBundle = bundle{
		red:   12,
		green: 13,
		blue:  14,
	}
)

func New(inp string) aoc.AoCDay {
	data := strings.Split(inp, "\n")
	parsed := make([]string, 0)
	// cut "GAME NN:"
	for _, v := range data {
		if len(v) == 0 {
			continue
		}
		gameInfo := strings.Split(v, ": ")
		parsed = append(parsed, gameInfo[1])
	}
	return &day2{
		games: parseGames(parsed),
	}
}

func getGameMax(game []*bundle) bundle {
	gameMax := bundle{}
	//retirieving max balls count in game
	for _, bund := range game {
		gameMax.red = max(gameMax.red, bund.red)
		gameMax.green = max(gameMax.green, bund.green)
		gameMax.blue = max(gameMax.blue, bund.blue)
	}
	return gameMax
}

func (d *day2) SolveA(deb bool) string {
	out := 0
	for i, game := range d.games {
		gameMax := getGameMax(game)

		if gameMax.red <= maxBundle.red && gameMax.green <= maxBundle.green && gameMax.blue <= maxBundle.blue {
			out += i + 1
			continue
		}

		if deb {
			fmt.Println("Game", i+1, "overflowed with", gameMax)
		}

	}
	fmt.Println("Solution A:", out)
	return strconv.FormatInt(int64(out), 10)
}

func (d *day2) SolveB(deb bool) string {
	var out int64 = 0
	for i, game := range d.games {
		gameMax := getGameMax(game)
		power := int64(gameMax.red) * int64(gameMax.blue) * int64(gameMax.green)
		if deb {
			fmt.Println("Game", i+1, "maxes are", gameMax, "power is", power)
		}
		out += power
	}
	fmt.Println("Solution B:", out)
	return strconv.FormatInt(int64(out), 10)
}

func parseGames(inp []string) [][]*bundle {
	out := make([][]*bundle, len(inp))
	for i, line := range inp {
		// Samples in one game
		samples := strings.Split(line, "; ")
		out[i] = make([]*bundle, len(samples))
		for j, sample := range samples {
			// Gathering bundle in one game
			curBundle := bundle{}
			balls := strings.Split(sample, ", ")
			for _, ball := range balls {
				// Getting balls count and color
				ballData := strings.Split(ball, " ")
				count, err := strconv.ParseInt(ballData[0], 10, 32)
				if err != nil {
					fmt.Println(ballData[0], " is not a number")
					continue
				}

				switch ballData[1] {
				case "red":
					curBundle.red = int(count)
				case "green":
					curBundle.green = int(count)
				case "blue":
					curBundle.blue = int(count)
				default:
					fmt.Println("Unknown color ", ballData[1])
				}
			}
			out[i][j] = &curBundle
		}
	}
	return out
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}
