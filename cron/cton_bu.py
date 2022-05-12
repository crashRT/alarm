import subprocess

def set_job(time: str):
    command = '/usr/bin/python3 /home/pi/works/alarm/alarm.py'
    time_list = time.split(':')
    hour = time_list[0]
    minute = time_list[1]
    job = f'{int(minute)} {int(hour)} * * * {command}'

    #スクリプトファイルの呼び出し
    subprocess.call(['sudo', '/home/pi/works/alarm/cron/cron.sh', job])
