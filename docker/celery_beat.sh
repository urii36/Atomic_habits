#!/bin/bash

sleep 15

celery -A atomic_habits beat -l INFO -S django