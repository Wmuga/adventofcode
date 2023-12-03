package inputs

import (
	"fmt"
	"io"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"os"
)

const (
	urlInputDay = "https://adventofcode.com/2023/day/%v/input"
	urlAoC      = "https://adventofcode.com"
)

func Day(day int) (string, error) {
	url, err := url.Parse(urlAoC)
	if err != nil {
		return "", err
	}
	// Setting up cookie jar
	sess := os.Getenv("COOKIE")
	jar, err := cookiejar.New(nil)
	if err != nil {
		return "", err
	}
	jar.SetCookies(url, []*http.Cookie{{
		Name:  "session",
		Value: sess,
	}})
	// getting input
	client := http.Client{
		Jar: jar,
	}
	resp, err := client.Get(fmt.Sprintf(urlInputDay, day))
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()
	bytes, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	return string(bytes), nil
}
