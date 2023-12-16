package set

import "golang.org/x/exp/maps"

type Set[T comparable] interface {
	Append(T) bool
	Exists(T) bool
	Remove(T) bool
	Count() int
	Values() []T
	Clear()
}

type set[T comparable] struct {
	m map[T]struct{}
}

func New[T comparable]() Set[T] {
	return &set[T]{
		m: make(map[T]struct{}),
	}
}

func (s *set[T]) Append(value T) bool {
	if s.Exists(value) {
		return false
	}

	s.m[value] = struct{}{}

	return true
}

func (s *set[T]) Exists(value T) bool {
	var _, exists = s.m[value]
	return exists
}

func (s *set[T]) Remove(value T) bool {
	if s.Exists(value) {
		return false
	}

	delete(s.m, value)

	return true
}

func (s *set[T]) Count() int {
	return len(s.m)
}

func (s *set[T]) Clear() {
	s.m = make(map[T]struct{})
}

func (s *set[T]) Values() []T {
	return maps.Keys(s.m)
}
