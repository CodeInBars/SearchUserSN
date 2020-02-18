import urllib.request
import sys
# define ANSI escape sequences for colored output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# a function for each site, which creates the request according to the username
def bitbucket(username):
    url = "https://bitbucket.org/" + username + "/"
    request = urllib.request.Request(url)
    try:
        parse(request,username)
    except urllib.error.URLError :
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")
    except UnicodeError:
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")

def github(username):
    url = "https://github.com/" + username + "/"
    request = urllib.request.Request(url)
    try:
        parse(request,username)
    except urllib.error.URLError :
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")
    except UnicodeError:
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")

def twitter(username):
    url = "https://twitter.com/" + username + "/"
    request = urllib.request.Request(url)
    try:
        parse(request,username)
    except urllib.error.URLError :
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")
    except UnicodeError:
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")

def instagram(username):
    url = "https://instagram.com/" + username + "/"
    request = urllib.request.Request(url)
    try:
        parse(request,username)
    except urllib.error.URLError :
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")
    except UnicodeError:
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")

def facebook(username):
    url = "http://facebook.com/" + username + "/"
    request = urllib.request.Request(url)
    try:
        parse(request,username)
    except urllib.error.URLError :
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")
    except UnicodeError:
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")

def tumblr(username):
    url = "https://" + username + ".tumblr.com"
    request = urllib.request.Request(url)
    try:
        parse(request,username)
    except urllib.error.URLError :
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")
    except UnicodeError:
        print(bcolors.FAIL + url)
        print(bcolors.FAIL + "Fail in the url, Probably this page can't have a usernames whit this characters (/ , _ . -)")

# process the request and capture the response code
def middleware(request, username):
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return (404, "Available")
        else:
            return (e.code, e.reason)
    else:
        if response.getcode() == 200:
            return (200, "Already exists")

# used for generating colored responses
def parse(request, username):
    response = middleware(request, username)
    if response[0] == 200:
        # printout(response, RED)
        print(bcolors.FAIL + request.get_full_url() + ": 200: Already Exists" + bcolors.ENDC)
    elif response[0] == 404:
        # printout(response, GREEN)
        print(bcolors.OKGREEN + request.get_full_url() + ": 404: Available" + bcolors.ENDC)

# ask for a username, instead of an argument
# username = raw_input("Username to check: ")
# take username as a system argument
username = input("Username to check: ")
print("Checking for availability of '" + username + "', please wait...")
facebook(username)
twitter(username)
instagram(username)
github(username) 
tumblr(username)
bitbucket(username)