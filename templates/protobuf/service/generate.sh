#!/bin/bash
THIS_DIR=$(dirname $0)

pushd $THIS_DIR

GOPATH=~/.go/ PATH=~/.go/bin:$PATH protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    {{ name }}.proto

popd 