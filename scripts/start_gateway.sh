#!/usr/bin/env bash

IP="127.0.0.1"
PORT="8000"

uvicorn gateway.app.main:app --reload --host $IP --port $PORT 