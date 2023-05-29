#!/bin/bash

docker build -t bd2-front:1.0 .
docker stack deploy -c docker-stack.yml bd2-front