package main

import (
    "fmt"
    "net/http"
)

func hello(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello from Go API!")
}

func main() {
    http.HandleFunc("/api/hello", hello)
    http.ListenAndServe(":8080", nil)
}