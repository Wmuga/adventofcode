package tools

import "encoding/json"

func Transpose[T any](in [][]T) [][]T {
	out := make([][]T, len(in[0]))
	for i := range out {
		out[i] = make([]T, len(in))
	}
	for i := range out {
		for j := range out[i] {
			out[i][j] = in[j][i]
		}
	}
	return out
}

func Clone[T any](a T) (res T, e error) {
	bytes, err := json.Marshal(a)
	if err != nil {
		return res, err
	}
	b := new(T)
	err = json.Unmarshal(bytes, b)
	return *b, err
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
