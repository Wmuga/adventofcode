package tools

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
