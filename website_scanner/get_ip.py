import os

def get_ip_from_tld(domain_name):
    print("Retrieveing ip address for %s " % (domain_name))
    get_host = os.popen("host " + domain_name)
    result = get_host.readline()
    ip     = result.split("has address")[1].strip()
    return ip
