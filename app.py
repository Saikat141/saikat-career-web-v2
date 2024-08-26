from flask import Flask,request,render_template,jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

# JOBS=[
#     {  
#         'id' : 1,
#         'title': 'Data Analyst',
#         'location': 'Bengaluru, India',
#         'salary': 'Rs. 10,00,000',
        
#     },
#     {
#         'id' : 2,
#         'title': 'Data Scientist',
#         'location': 'Delhi, India',
#         'salary': 'Rs. 15,00,000'
        
#     },
#     {
#         'id' : 3,
#         'title': 'Frontend Engineer',
#         'location': 'Remote',
#         'salary': 'Rs. 12,00,000'

#     },
#     {
#         'id' : 4,
#         'title': 'Backend Engineer',
#         'location': 'San Francisco, USA',
        

#     }
    
# ]

#FOR DATABASE WORK TO FETCH DATA FROM DATABASE
def load_jobs_from_db():
    with engine.connect() as conn:
        # Execute the query
        result = conn.execute(text("SELECT * FROM jobs"))

        job_list=[]
            # Fetch and print all results
        for row in result.fetchall():
            job_list.append(row._asdict())
        
    return job_list 


@app.route("/")

def index():
    JOBS = load_jobs_from_db()
    return render_template('home.html', jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    JOBS = load_jobs_from_db()
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)
