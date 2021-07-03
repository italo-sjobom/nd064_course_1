FROM golang:alpine
LABEL mainteiner="Italo Sjobom"

COPY . /go/src/app
WORKDIR /go/src/app
RUN go build -o helloworld

# command to run on container start
CMD [ "go", "run", "main.go" ]
