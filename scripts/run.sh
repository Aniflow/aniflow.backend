#!/usr/bin/env bash

IP="127.0.0.1"
GATEWAY_PORT="8000"
ANIME_MS_PORT="8001"

start_anime_ms() {
    if uvicorn services.animes.app.main:app --reload --host $IP --port $ANIME_MS_PORT; then
        echo "Anime microservice started successfully on port $ANIME_MS_PORT"
    else
        echo "Failed to start anime microservice" >&2
        exit 1
    fi
}

start_gateway() {
    if uvicorn gateway.app.main:app --reload --host $IP --port $GATEWAY_PORT; then
        echo "Gateway started successfully on port $GATEWAY_PORT"
    else
        echo "Failed to start API Gateway" >&2
        exit 1
    fi
}

(
    trap "exit" INT TERM
    start_anime_ms
) &

(
    trap "exit" INT TERM
    start_gateway
) &

wait
