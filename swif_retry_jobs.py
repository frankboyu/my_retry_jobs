import sys
import os
import glob
import time
from optparse import OptionParser
from subprocess import Popen, PIPE
from collections import defaultdict, deque

with open('/work/halld2/home/boyu/retry_jobs/retry_workflow.txt', 'r') as file:
    for line in file:
        workflow = line.strip()
        command = "/usr/bin/swif2 retry-jobs -workflow " + workflow + " -problems SLURM_FAILED SLURM_CANCELLED SLURM_TIMEOUT SLURM_NODE_FAIL SLURM_OUT_OF_MEMORY SITE_LAUNCH_FAIL SITE_PREP_FAIL SWIF_INPUT_FAIL SWIF_SYSTEM_ERROR"
        process = Popen(command.split(), stdout=PIPE)
        output = process.communicate()[0].decode('ASCII')
        print(workflow)
        print(output)
        return_code = process.returncode
