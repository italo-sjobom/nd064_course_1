FROM golang:alpine
LABEL mainteiner="Italo Sjobom"

WORKDIR /go/src/app
# Copy all the content of current directory of localhost to the directory inside the container
ADD . .
RUN go build -o helloworld

# Expose port 6111
EXPOSE 6111

# command to run on container start
CMD [ "./helloworld" ]
