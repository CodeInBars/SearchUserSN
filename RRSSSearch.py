from bs4 import BeautifulSoup
import request
import urllib.request
import sys
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

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

def whatsapp(number):
    url = "https://api.whatsapp.com/send?phone=" + number + "/"
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page, "lxml")
    gButton = soup.find('div', attrs={"class": "_whatsapp_www__block_action"})
    r = gButton is None
    if r:
        print(bcolors.OKGREEN + url + ": 404: Available" + bcolors.ENDC)
    else:    
        print(bcolors.FAIL + url + ": 200: Already Exists" + bcolors.ENDC)


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

def geoCach(number):
    chNumber = (phonenumbers.parse(number, 'CH'))
    sNum = phonenumbers.parse(number, 'RO')
    print(geocoder.description_for_number(chNumber, "en"))
    print(carrier.name_for_number(sNum, "en"))


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

# Menu
username = input("Username to check: ")
number = input("Number to check: ")
print("Checking for availability of '" + username + "', please wait...")
facebook(username)
twitter(username)
instagram(username)
github(username) 
tumblr(username)
bitbucket(username)
whatsapp(number)
geoCach(number)