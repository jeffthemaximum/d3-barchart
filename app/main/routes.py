import urllib2
import json
from flask import Flask, render_template
from flask.ext.script import Manager
from .forms import NameForm
import string
import pudb
from . import main


def fetch_json(query):
    response = urllib2.urlopen('https://api.github.com/search/users?q=' + query)
    return json.loads(response.read())


def get_first_five_usernames(usernames):
    max_five_usernames = []
    search_range = 5
    if len(usernames) < 5:
        search_range = len(usernames)
    for i in range(search_range):
        max_five_usernames.append(usernames[i])
    return max_five_usernames


def get_usernames(response):
    usernames = [x['login'] for x in response]
    return usernames


def empty_alph_dict():
    letters = {}
    all_chars = string.ascii_lowercase
    for x in all_chars:
        letters[x] = 0
    return letters

def get_alph_count(name_array):
    name_chars = "".join(name_array).strip().lower()
    total_letters = len(name_chars)
    letter_count = empty_alph_dict()
    for x in name_chars:
        if x.isalpha():
            letter_count[x] += 1

    return letter_count


@main.route('/github/<jsdata>')
def github(jsdata):
    # need to add some server side validation of form!!!
    # get form data
    query = jsdata
    # get json data
    response_json = fetch_json(query)
    # sort by login name
    sorted_response = sorted(response_json['items'], key=lambda k: k['login'])
    # get just logins and ignore other data
    usernames = get_usernames(sorted_response)
    # get first five usernames
    first_five_usernames = get_first_five_usernames(usernames)
    print first_five_usernames
    alph_count = get_alph_count(first_five_usernames)

    return json.dumps(alph_count)

@main.route('/')
def index():
    form = NameForm()

    return render_template('index.html', form=form)
