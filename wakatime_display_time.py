from datetime import datetime
import time
import requests
import sys
from config import api_key

URL = 'https://wakatime.com/api/v1/users/current/durations'


def main():
    params = {'api_key': api_key}
    while True:
        params['date'] = datetime.today().strftime('%Y-%m-%d')
        req = requests.get(URL, params=params)
        seconds = int(sum(i['duration'] for i in req.json()['data']))
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        print('Coding progress: {:d}:{:02d}:{:02d}'.format(hours, minutes, seconds), end="\r", flush=True)
        # sys.stdout.write('Coding progress: {:d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
        # sys.stdout.flush()
        time.sleep(60)


if __name__ == '__main__':
    main()
