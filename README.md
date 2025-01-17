## my_retry_jobs

Scripts to retry the jobs that failed due to transient farm errors.

JLab: /work/halld2/home/boyu/my_retry_jobs

GitHub: https://github.com/frankboyu/scripts/tree/master/my_retry_jobs

### Usage

1.  On one ifarm node, load the crontab config file:

    `crontab cron_config_retry-jobs`

2.  Edit the list of workflows in swif_retry_jobs.py

3.  Check the status log at retry_status.log

4.  To check the crontab job, run:

    `crontab -l`

    To stop the crontab job, run:

    `crontab -r`

### Notes

1. These scripts are modified based on Hall D's scripts to merge the output trees in the analysis launch: https://github.com/JeffersonLab/hd_utilities/tree/master/launch_scripts/merge_trees