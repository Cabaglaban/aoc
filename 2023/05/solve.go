package main

import (
	"flag"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"time"
)

func strToInt(str string) (r []int) {
	for _, s := range strings.Split(str, " ") {
		i, _ := strconv.Atoi(s)
		r = append(r, i)
	}

	return
}

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type Map struct {
	ranges [][3]int
}

func NewMap(str string) *Map {
	mapRanges := strings.Split(str, "\n")[1:]
	ranges := [][3]int{}

	for _, item := range mapRanges {
		arr := [3]int{}
		copy(arr[:], strToInt(item))
		ranges = append(ranges, arr)
	}

	return &Map{ranges}
}

func (m *Map) Next(k int) int {
	for _, r := range m.ranges {
		if k >= r[1] && k < r[1]+r[2] {
			return r[0] + k - r[1]
		}
	}
	return k
}

type Result struct {
	min     float64
	comp    int
	elapsed time.Duration
}

func solveSeedRange(sr [2]int, maps []*Map, ret chan Result) {
	t0 := time.Now()

	min := math.Inf(1)
	for i := sr[0]; i < sr[1]; i++ {
		s := i
		for _, m := range maps {
			s = m.Next(s)
		}

		min = math.Min(min, float64(s))
	}
	ret <- Result{
		min:     min,
		comp:    sr[1] - sr[0],
		elapsed: time.Since(t0),
	}
}

func main() {
	file := flag.String("file", "example", "run example or input")
	part := flag.Int("part", 1, "part to run")
	flag.Parse()

	input, _ := os.ReadFile(fmt.Sprintf("2023/05/%s", *file))
	rawMaps := strings.Split(string(input), "\n\n")

	parsedSeeds := strToInt(strings.ReplaceAll(rawMaps[0], "seeds: ", ""))
	seeds := [][2]int{}

	if *part == 2 {
		limit := 50_000_000
		for i := 0; i < len(parsedSeeds); i += 2 {
			s0, s1 := parsedSeeds[i], parsedSeeds[i+1]
			for j := s0; j < s0+s1; j += limit {
				seeds = append(seeds, [2]int{j, j + minInt(s1, limit)})
			}
		}
	} else {
		for i := 0; i < len(parsedSeeds); i++ {
			seeds = append(seeds, [2]int{parsedSeeds[i], parsedSeeds[i] + 1})
		}
	}

	maps := []*Map{}
	for _, m := range rawMaps[1:] {
		maps = append(maps, NewMap(m))
	}

	solveCh := make(chan Result)
	for _, sr := range seeds {
		go solveSeedRange(sr, maps, solveCh)
	}

	min := math.Inf(1)
	for i := 0; i < len(seeds); i++ {
		res := <-solveCh
		
		fmt.Printf("%d/%d (%d) done in %s\n", i + 1, len(seeds), res.comp, res.elapsed)
		min = math.Min(min, res.min)
	}

	fmt.Printf("[%d] %s = %d\n", *part, *file, int(min))
}
