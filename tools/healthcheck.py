import sys
import urllib.request
import urllib.error

HOST = 'http://127.0.0.1:8000'
ROUTES = [
    '/',
    '/hotels/',
    '/malls/',
    '/restaurants/',
    '/reviews/',
    '/bookings/',
    '/accounts/login/',
    '/accounts/signup/',
    '/accounts/profile/',
]

def fetch(path):
    url = HOST.rstrip('/') + path
    req = urllib.request.Request(url, headers={'User-Agent': 'HealthCheck/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode('utf-8', errors='replace')
            return resp.getcode(), body
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode('utf-8', errors='replace')
        except Exception:
            body = ''
        return e.code, body
    except Exception as e:
        return None, str(e)


def main():
    any_error = False
    for route in ROUTES:
        code, body = fetch(route)
        print('---')
        print(f'GET {route} ->', code)
        if code is None:
            print('ERROR:', body)
            any_error = True
            continue
        if code >= 500:
            print('SERVER ERROR:')
            print(body[:1000])
            any_error = True
            continue
        # look for Django debug tracebacks
        if 'Traceback' in body or 'Exception' in body and code >= 400:
            print('POSSIBLE TRACEBACK IN RESPONSE')
            print(body[:1000])
            any_error = True
            continue
        print('OK (length=%d)' % len(body))
    if any_error:
        sys.exit(2)

if __name__ == '__main__':
    main()
