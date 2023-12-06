package main

import (
	"flag"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func strToInt(str string) (r []int) {
	for _, s := range strings.Split(str, " ") {
		i, _ := strconv.Atoi(strings.TrimSpace(s))
		r = append(r, i)
	}

	return
}

func parseRaces(str []string, part *int) [][]int {
	space := regexp.MustCompile(`\s+`)
	rows := [][]int{}

	for _, row := range str {
		row = strings.TrimSpace(space.ReplaceAllString(strings.Split(row, ":")[1], " "))
		if *part == 2 {
			row = strings.ReplaceAll(row, " ", "")
		}
		
		rows = append(rows, strToInt(row))
	}
	return rows
}

func find(t, d, start, stop, ridx int, result chan [2]int) {
	step := 1
	if start > stop {
		step = -1
	}

	s := start
	for {
		if step == 1 && s > stop {
			break
		} else if step == -1 && s < stop {
			break
		}
		if s * (t - s) > d {
			result <- [2]int{ridx, s}
			break
		}
		s += step
	}
}

func main() {
	file := flag.String("file", "example", "run example or input")
	part := flag.Int("part", 1, "part to run")
	flag.Parse()

	input, _ := os.ReadFile(fmt.Sprintf("2023/06/%s", *file))
	races := parseRaces(
		strings.Split(strings.TrimSpace(string(input)), "\n"), 
		part,
	)

	solutions := 1
	for idx := range races[0] {
		t := races[0][idx]
		d := races[1][idx]
		tt := make(chan [2]int, 2)

		find(t, d, 1, t, 0, tt)
		find(t, d, t, 0, 1, tt)

		rr := [2]int{}
		for _ = range []int{0, 1} {
			r := <- tt
			rr[r[0]] = r[1]
		}

		solutions *= rr[1] - rr[0] + 1
	}

	fmt.Printf("[%d] %s = %d\n", *part, *file, solutions)
}
