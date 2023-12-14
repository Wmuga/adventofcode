package parsers

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

var reg = regexp.MustCompile(`[+-]?\d+`)

func ExtractNums(inp string) []int {
	digs := reg.FindAllString(inp, -1)
	out := make([]int, len(digs))
	for i, v := range digs {
		num, err := strconv.ParseInt(v, 10, 32)
		if err != nil {
			fmt.Println("Can't convert", v, "to number")
		}
		out[i] = int(num)
	}
	return out
}

func GetLinesString(inp string) []string {
	out := make([]string, 0)
	for _, line := range strings.Split(inp, "\n") {
		if line == "" {
			continue
		}
		out = append(out, line)
	}
	return out
}

func GetLinesRune(inp string) [][]rune {
	strs := GetLinesString(inp)
	out := make([][]rune, len(strs))
	for i, str := range strs {
		out[i] = []rune(str)
	}
	return out
}
