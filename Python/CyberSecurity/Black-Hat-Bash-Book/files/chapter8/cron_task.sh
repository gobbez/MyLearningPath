#!/bin/bash
job_name="scheduled_job"

echo "The time now is ${date}" >> "/tmp/${job_name}"
exit 0
