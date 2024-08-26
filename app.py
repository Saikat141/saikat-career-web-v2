from flask import Flask,request,render_template,jsonify
from database import load_jobs_from_db,load_job_from_db


app = Flask(__name__)





@app.route("/")

def index():
    JOBS = load_jobs_from_db()
    return render_template('home.html', jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)

def list_jobs():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)


@app.route("/jobs/<id>")

def show_job(id):
    
    job = load_job_from_db(id)
    
    if not job:
        return "NOT FO"
    return render_template('jobpage.html', jobs = job)

if __name__ == "__main__":
    app.run("0.0.0.0",debug=True)
