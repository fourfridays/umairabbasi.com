#!/bin/bash

# Script to monitor the pull-movies-tv CronJob
# Usage: ./monitor-cronjob.sh

CRONJOB_NAME="pull-movies-tv-cronjob-robust"
NAMESPACE="umairabbasi"

echo "=== CronJob Status ==="
kubectl get cronjob $CRONJOB_NAME -n $NAMESPACE

echo ""
echo "=== Recent Jobs ==="
kubectl get jobs -l job-name -n $NAMESPACE | head -5

echo ""
echo "=== Latest Job Logs ==="
LATEST_JOB=$(kubectl get jobs -n $NAMESPACE -l app=pull-movies-tv-job --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[-1].metadata.name}' 2>/dev/null)

if [ ! -z "$LATEST_JOB" ]; then
    echo "Showing logs for job: $LATEST_JOB"
    kubectl logs job/$LATEST_JOB -n $NAMESPACE
else
    echo "No jobs found"
fi

echo ""
echo "=== Next Scheduled Run ==="
kubectl get cronjob $CRONJOB_NAME -n $NAMESPACE -o jsonpath='{.status.lastScheduleTime}' | xargs -I {} echo "Last run: {}"
kubectl get cronjob $CRONJOB_NAME -n $NAMESPACE -o jsonpath='{.spec.schedule}' | xargs -I {} echo "Schedule: {}"
