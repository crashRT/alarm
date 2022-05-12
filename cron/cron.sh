!/bin/bash
cron_job=$1
cron_file="/var/spool/cron/crontabs/pi"
echo "${cron_job}" > "${cron_file}"
/etc/init.d/cron restart
