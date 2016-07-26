import sys
import requests
import json

def make_request(args):
    root = "http://jsonplaceholder.typicode.com"
    endpoint = args[1]
    method   = args[2]
    request_url = root + endpoint

    if method == "GET":
        request = requests.get(request_url)
        response = request.json()
        print(response)

    elif method == "POST":
        payload = args[3:]
        data    = {}

        if payload:
            for item in payload:
                key, value = item.split("=")
                data[key] = value

            request = requests.post(request_url, data=data)
            response = request.json()
            pretty_response = json.dumps(response, indent=4, sort_keys=True)
            print("Server responded with : \n" + str(pretty_response))

        else:
            print("Please provide data to send")

    elif method == "PUT":
        payload = args[3:]
        data = {}

        for item in payload:
            key, value = item.split("=")
            data[key] = value

        request = requests.put(root + endpoint, data=data)
        response = request.json()
        pretty_response = json.dumps(response, indent=4, sort_keys=True)
        print("Server responded with : \n" + str(pretty_response))

    elif method == "DELETE":
        request = requests.delete(request_url)
        response = request.json()
        pretty_response = json.dumps(response, indent=4, sort_keys=True)
        print("Server responded with: \n" + str(pretty_response))

    else: 
        print("Please provide a valid request method")

# Check if the user passed at least one argument
if __name__ == "__main__":
    if len(sys.argv) > 1:
        make_request(sys.argv)
