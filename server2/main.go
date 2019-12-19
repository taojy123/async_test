package main

import "github.com/kataras/iris/v12"
import "net/http"
import "io/ioutil"

func main() {
    app := iris.Default()
    app.Get("/", func(ctx iris.Context) {

	url := "http://lovegaudi.art:3000"
	req, _ := http.NewRequest("GET", url, nil)
	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)
	content := string(body)


        ctx.JSON(iris.Map{
            "message": content,
        })
    })

    app.Run(iris.Addr(":8080"))
}


// add-apt-repository ppa:longsleep/golang-backports apt-get update
// apt-get install golang-go
// export GO111MODULE=on
// export GOPROXY=https://goproxy.io
// go run main.go

