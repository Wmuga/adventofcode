package parsers

import (
	"fmt"
	"regexp"
	"strconv"
)

var reg = regexp.MustCompile("\\d+")

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
