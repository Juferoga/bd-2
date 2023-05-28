#!/bin/bash

docker build -t juferoga/bd2-back:1.0 .
docker stack deploy -c docker-stack.yml bd2-back