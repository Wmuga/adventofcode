package tester

import "testing"

func Assert(num int, prefix, res, expected string, t *testing.T) {
	if res != expected {
		t.Errorf("%v: Test %v wrong. Expected %v. Got %v", prefix, num, expected, res)
	}
}
