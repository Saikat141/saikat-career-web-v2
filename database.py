from sqlalchemy import create_engine, text
import pymysql
import os 
pymysql.install_as_MySQLdb()

# Update the connection string by removing the ssl-mode=REQUIRED from it
db_connection_string = os.environ['DB_CONNECTION_STRING']

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

# Connect to the database and execute the query
# with engine.connect() as conn:
#     # Execute the query
#     result = conn.execute(text("SELECT * FROM jobs"))

#     # Fetch and print all results
#     for row in result.fetchall():
#         print(row)

