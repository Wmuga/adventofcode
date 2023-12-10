package queue

import (
	"container/list"
	"errors"
)

type queue struct {
	lst *list.List
	Queue
}

type Queue interface {
	Enqueue(any) error
	Dequeue() (any, error)
	IsEmpty() bool
	Count() int
}

var (
	ErrQueueEmpty = errors.New("queue is empty")
)

func New() Queue {
	return &queue{
		lst: list.New(),
	}
}

func (q *queue) Enqueue(val any) error {
	q.lst.PushBack(val)
	return nil
}

func (q *queue) Dequeue() (any, error) {
	if q.IsEmpty() {
		return nil, ErrQueueEmpty
	}

	front := q.lst.Front()
	q.lst.Remove(front)

	return front.Value, nil
}

func (q *queue) IsEmpty() bool {
	return q.Count() == 0
}

func (q *queue) Count() int {
	return q.lst.Len()
}
