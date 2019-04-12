from datetime import datetime
from config import api_key

URL = 'https://wakatime.com/api/v1/users/current/durations'

def main():
    params = {'api_key': api_key}
    while True:
        params['date'] = datetime.today().strftime('%Y-%m-%d')
        print(requies.get(URL, params))

if __name__ == '__main__':
    main()
