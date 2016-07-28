## Usage

- User gives the URL for a site and we output the scan to multiple files in a folder
- We create one master folder called analysis and the scans will be saved under that
  directory (ex: we scan ebay, the scan will be saved under analysis/ebay )


# Steps

### Create a general.py file that will hold two functions
### The first one will be called create_directory (and will check if that directory exists
### before creating it)
### The second function will be called create file and it will take a name and a path

1. get top level domain from the url (tld module ?)
2. get the ip of that top level domain (by issuing the command "host + tld" using the os
   module)
3. Do a port scan of that ip using python-nmap (by passing the ip)
4. Check the robots.txt file if there is one (check if the url endswith "/" first, then
   make a request to the domain + /robots.txt and return the response using the requests
   module)
5. Do a whois lookup (process open "whois" + tld)

# Requirements
At the start of each function, print a message detailing what is happening to let the user
know the program is working

create a file for each of the jobs in the master function

each step should be done in a separate file
