from flask import Flask, render_template, request
from bs4 import BeautifulSoup
# from wework import get_wework_jobs

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
# wework_jobs  = get_wework_jobs()

app = Flask("gigforgeeks")

db = {}


@app.route("/")
def home():
    return render_template("index.html")


# app.run(host="0.0.0.0")
