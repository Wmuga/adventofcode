package day24

import (
	"aoc2023/days/aocday"
	"aoc2023/utils/parsers"
	"fmt"
	"os"
	"strconv"
)

type v3 struct {
	x int64
	y int64
	z int64
}

type lineT struct {
	pos       v3
	direction v3
}

type day24 struct {
	rays   []lineT
	boundL v3
	boundR v3
}

func New(inp string) aocday.AoCDay {
	lines := parsers.GetLinesString(inp)
	d := &day24{
		rays: make([]lineT, len(lines)),
	}
	for i, line := range lines {
		nums := parsers.ExtractNums64(line)
		d.rays[i] = lineT{v3{nums[0], nums[1], nums[2]},
			v3{nums[3], nums[4], nums[5]}}
	}
	return d
}

func (d *day24) intersectXY(l, r lineT) bool {
	// (x-x0)/dx = (y-y0)/dy => y = ax + b
	a1 := float64(l.direction.y) / float64(l.direction.x)
	a2 := float64(r.direction.y) / float64(r.direction.x)

	if a1 == a2 {
		return false
	}

	b1 := float64(l.pos.y) - a1*float64(l.pos.x)
	b2 := float64(r.pos.y) - a2*float64(r.pos.x)

	x := (b2 - b1) / (a1 - a2)
	if x < float64(d.boundL.x) || x > float64(d.boundR.x) {
		return false
	}

	y := a1*x + b1
	if y < float64(d.boundL.y) || y > float64(d.boundR.y) {
		return false
	}

	stepsL := (y - float64(l.pos.y)) / float64(l.direction.y)
	stepsR := (y - float64(r.pos.y)) / float64(r.direction.y)

	return stepsL >= 0 && stepsR >= 0
}

func (d *day24) SolveA(test bool) string {
	d.boundL = v3{200000000000000, 200000000000000, 0}
	d.boundR = v3{400000000000000, 400000000000000, 0}
	if test {
		d.boundL = v3{7, 7, 0}
		d.boundR = v3{27, 27, 0}
	}

	out := int64(0)

	for i := 0; i < len(d.rays)-1; i++ {
		for j := i + 1; j < len(d.rays); j++ {
			if d.intersectXY(d.rays[i], d.rays[j]) {
				out++
			}
		}
	}

	fmt.Println("Solution A:", out)
	return strconv.FormatInt(out, 10)
}

func (d *day24) SolveB(_ bool) string {
	out := int64(0)
	file, err := os.Create("solve.py")
	if err != nil {
		panic(err)
	}

	fmt.Fprintln(file, "from z3 import *")
	fmt.Fprintln(file, "\nA=Real('A')\nB=Real('B')\nC=Real('C')\nX=Real('X')\nY=Real('Y')\nZ=Real('Z')")
	for i := 0; i < 6; i++ {
		fmt.Fprintf(file, "s%v=Real('s%v')\n", i, i)
	}
	fmt.Fprintln(file, "solver = Solver()")
	for i, ray := range d.rays {
		fmt.Fprintf(file, "solver.add(A * s%v + X == %v * s%v + %v)\n", i, ray.direction.x, i, ray.pos.x)
		fmt.Fprintf(file, "solver.add(B * s%v + Y == %v * s%v + %v)\n", i, ray.direction.y, i, ray.pos.y)
		fmt.Fprintf(file, "solver.add(C * s%v + Z == %v * s%v + %v)\n", i, ray.direction.z, i, ray.pos.z)
		fmt.Fprintf(file, "solver.add(s%v > 0)\n", i)
		if i > 4 {
			break
		}
	}
	fmt.Fprintln(file, "print(solver.check())\nm=solver.model()")
	fmt.Fprintln(file, "x_res=m[X]\ny_res=m[Y]\nz_res=m[Z]")
	fmt.Fprintln(file, "print(x_res,y_res,z_res,sep='+')")

	fmt.Println("Solution B:", out)
	return strconv.FormatInt(out, 10)
}
