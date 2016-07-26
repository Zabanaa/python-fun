import argparse
import requests
import webbrowser


# Step 1: user passes what he wants to retrieve categories search or trending / explore along with client id and client
# secret

# An example would look like this. python fsq.py categories client_id client_secret
# or even : python fsq.py search client_id client_secret

# based on the endpoint they are trying to access we ask certain questions (except for categories where we just return
# the categories as json)

# we check if the endpoint is categories if it is, we run the get_categories function where we make a request to that
# endpoint and return the categories

# if they are trying to search
# we then run the function search_venues that will ask the correct questions then return the answer


# we do the same for explore and trending (create separate functions for now and see if you can refactor afterwards)

ROOT_URL = "https://api.foursquare.com/v2/venues/"
CLIENT_ID = "Y5IGDTNYOSPCOOXGSHBC0XGALFKBNO0MSZFA1QSXP3LKILG5"
CLIENt_SECRET = "3RCSCB0GEVZX3CERI2DC4I1LU5G41ZPXFB2BUFPHWHVWBJRB"

parser = argparse.ArgumentParser(description="Wrapper around the foursquare API. Use it to retrieve information about\
                                 specific venues or groups of venues.")
parser.add_argument("endpoint", help="Name of the resource you want to access", choices=["categories", "trending",\
                                                                                         "explore", "search"])
parser.add_argument("client_id", help="Your Foursquare Client ID")
parser.add_argument("client_secret", help="Your Foursquare Client Secret")
args = parser.parse_args()

payload = {
    "v": 20160612,
    "m": "foursquare",
    "client_id": args.client_id,
    "client_secret": args.client_secret
}

def get_categories():
    print("Fetching all categories ...")
    req  = requests.get(ROOT_URL + "categories", params=payload)
    response = req.json()
    print(response)

def search_venues():

    while True:

        query = input("Please provide a search query: \n")
        while not all(c.isalpha() or c.isspace() for c in query) or not query:
            print("This is a required field that should only contain letters and spaces. Try Again.\n")
            query = input("Please provide a search query: \n")

        location    = input("Please provide a location for the venues\n")
        while not all(c.isalpha() or c.isspace() or c == "," for c in location) or not location:
            print("This is a required field that should only contain letters and spaces. Try again\n")
            location = input("Please provide a location for the venues\n")

        radius = input("Please provide a search radius in meters (up to 2000, default is 100 - Leave blank to continue): \n")
        while radius and int(radius) not in range(1, 2001):
            print("The maximum radius should be 2000")
            radius = input("Please provide a search radius (max 2000), return to ignore): \n")

        limit  = input("How many results do you wish to get back ? (up to 50, default it 10 - Leave blank to continue): \n")
        while limit and int(limit) not in range(1, 51):
            print("The maximum amount of result return cannot exceed 50\n")
            limit = input("Number of results: \n")

        category_id = input("Please provide a category id if you have one (Leave blank to continue) \n")

        break

    payload['query'] = query
    payload['near'] = location
    payload['radius'] = int(radius) if radius else  100
    payload['limit'] = int(limit) if limit else 10
    if category_id: payload['category_id'] = category_id

    venues_request = requests.get(ROOT_URL + "search", params=payload)
    print("Fetching results for %s in %s" % (query, location))
    response = venues_request.json()
    webbrowser.open(venues_request.url)

def get_trending_venues():
    pass
    # Required : Location
    # Optional : Radius, Limit

def explore_venues():
    pass
    # Required: Location
    # Optional : Section (pre defined list of choices), query, limit, price (again has to be an int and has to be
    # within range)

if __name__ == "__main__":

    if args.endpoint == "categories":
        get_categories()
    elif args.endpoint == "search":
        search_venues()
