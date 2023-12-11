#!/bin/bash

sleep 15

celery -A atomic_habits.celery worker -l INFO -S django