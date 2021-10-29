from flask import Flask, render_template, request, redirect, send_file
from wwr import get_wwr_jobs
from so import get_so_jobs
from remoteok import get_re_jobs
from save import save_to_file


app = Flask("gigforgeeks")

db = {}

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
      word = word.lower()
      if db.get(word):
        return render_template("report.html", jobs=db[word], word=word, len_jobs=len(db[word]))
      else:
        wwr_jobs = get_wwr_jobs(word)
        so_jobs = get_so_jobs(word)
        re_jobs = get_re_jobs(word)
        jobs = wwr_jobs + so_jobs + re_jobs
        db[word] = jobs
        return render_template("report.html", jobs=jobs, word=word, len_jobs=len(jobs))
  else:
    return redirect("/")

@app.route("/export")
def export():
  word = request.args.get('word')
  jobs = db.get(word)
  save_to_file(word, jobs)
  return send_file(f"{word}.csv", mimetype="text/csv", as_attachment=True)

app.run(host="0.0.0.0")