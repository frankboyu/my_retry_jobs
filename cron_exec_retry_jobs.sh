#!/bin/bash

date
source /work/halld2/home/boyu/retry_jobs/env.sh
export PATH=/site/bin:${PATH} #because .login isn't executed, and need this path for SWIF
python /work/halld2/home/boyu/retry_jobs/swif_retry_jobs.py

