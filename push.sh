#!/usr/bin/env bash

./build.sh

TAG=${1:-latest}

echo "Using tag: $TAG."

docker tag iris_mlp tommos0/iris_mlp:$TAG
docker push tommos0/iris_mlp