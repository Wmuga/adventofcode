package tester

import "testing"

func Assert[T comparable](num int, prefix string, res, expected T, t *testing.T) {
	if res != expected {
		t.Errorf("%v: Test %v wrong. Expected %v. Got %v", prefix, num, expected, res)
	}
}
