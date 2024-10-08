from sqlalchemy import create_engine, text
import pymysql
import os

from sqlalchemy.engine import result 
pymysql.install_as_MySQLdb()

# Update the connection string by removing the ssl-mode=REQUIRED from it
# db_connection_string = os.environ['DB_CONNECTION_STRING']
db_connection_string = "mysql://avnadmin:AVNS_umE4KpdtvLRwxJ9oeZ3@jobinscareer-jobinscareer.h.aivencloud.com:12523/defaultdb"

# Create the SQLAlchemy engine with SSL arguments
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_mode": "REQUIRED",
            # Optionally, you can add paths to SSL certificates
            # "ca": "/path/to/ca-cert.pem",
            # "cert": "/path/to/client-cert.pem",
            # "key": "/path/to/client-key.pem"
        }
    }
)

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


# TO SELECT A JOB ROW FROM DATABASE


def load_job_from_db(id):
     with engine.connect() as conn:
         # Execute the query with correct SQL syntax
            result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
                    {"val": id}
                )
            rows = result.fetchall()  # fetchall() returns all rows
            if len(rows) == 0:
                return None
            else:
                return rows[0]._asdict()  # Convert the first row to a dictionary



def add_application_to_db(job_ids, data):
    with engine.connect() as conn:
        query = text("""
            INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
            VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
        """)

        # Prepare data for batch insertion
        insert_data = [
            {
                'job_id': job_id,
                'full_name': data['full_name'],
                'email': data['email'],
                'linkedin_url': data['linkedin_url'],
                'education': data['education'],
                'work_experience': data['work_experience'],
                'resume_url': data['resume_url']
            }
            for job_id in job_ids
        ]

        conn.execute(query, insert_data)
        conn.close()


# Connect to the database and execute the query
# with engine.connect() as conn:
#     # Execute the query
#     result = conn.execute(text("SELECT * FROM jobs"))

#     # Fetch and print all results
#     for row in result.fetchall():
#         print(row)

