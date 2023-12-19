package day19

import (
	"aoc2023/utils/tester"
	"testing"
)

const inp1 = `px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}`

const inp0 = `in{a<2001:w1,m>2000:A,w2}
w1{a>1000:R,A}
w2{s>3000:A,R}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}`

func TestA(t *testing.T) {
	tester.Assert(0, "A", New(inp1).SolveA(true), "19114", t)
}

func TestB(t *testing.T) {
	tester.Assert(0, "B", New(inp0).SolveB(true), "144000000000000", t)
	tester.Assert(1, "B", New(inp1).SolveB(true), "167409079868000", t)
}
