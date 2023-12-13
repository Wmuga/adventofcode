package tools

func Transpose[T any](in [][]T) [][]T {
	out := make([][]T, len(in[0]))
	for i := range in[0] {
		out[i] = make([]T, len(in))
		for j := range in {
			out[i][j] = in[j][i]
		}
	}
	return out
}
