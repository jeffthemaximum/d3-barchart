EquityZen Github API Challenge
======

## What you need to run or use this challenge locally:
* Pull the repository to your local machine.
* Install virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/install.html
* setup a new virtual environment where you want to run crispy hippopotamus on your local machine.:
```
mkvirtualenv equityzen
```
* on command line, run:
```
pip install -r requirements.txt
```
* Make sure you have postgres setup on your local machine: http://www.postgresql.org/
* on command line, to setup your database, run:
```
python manage.py db upgrade
```
* Startup the localhost server by running on command line:
```
python manage.py db runserver
```
* Point your browser to localhost:5000
* enjoy playing some beautiful chess.

Question 1
Here at EquityZen we leverage APIs in order to connect our app to third party services that
provide pre-built functionality. While we do not currently connect to GitHub, they provide a
good API for searching repositories and users (they rate-limit so don’t abuse the API).
Please be sure to use JavaScript and D3 (http://d3js.org/) library for this project. Please
include a link to your solution.
Create a webpage with a search bar where I can enter some text. When I “submit” the search, take
this text and perform a “Users Search” using the GitHib’s API’s search function
(https://developer.github.com/v3/users/).
For example, if I had typed “barack” in the search bar, you would perform the following call:
https://api.github.com/search/users?q=barack
and, GitHub would return many results that look like:

{login: "PresidentObama", id: 10196880, avatar_url:
"https://avatars.githubusercontent.com/u/10196880?v=3",
url: "https://api.github.com/users/PresidentObama",
:
type: "User",
score: 43.27139}

Sort over the results by login attribute. Using up to five Users’ login attributes (or fewer if API
results contain fewer Users), please display a bar chart where (ignoring upper or lower case):
X-axis has 27 values (26 letters of the alphabet and “Other”)
Y-axis has count each letter appears in the set of name attributes
(in Ariel Barack, “a” appeared 3 times, “r” 2 times, “q” 0 times)
Bonus: add tool-tips so when you mouse over a given bar, it displays the count value for that letter.
The result would look something like below (except Y-axis would have count instead of frequency,
and data would represent “ArielBarack”).

