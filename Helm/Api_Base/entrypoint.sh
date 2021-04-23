#!/bin/bash

# uvicorn -b 0.0.0.0:6008 main:app
uvicorn app.main:app --host 0.0.0.0 --port 6008