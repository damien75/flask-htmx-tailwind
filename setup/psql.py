from psycopg2 import connect

# Connect to your postgres DB
conn = connect(dbname='flask_htmx', user='postgres', password='postgres', host='localhost')

# Open a cursor to perform database operations
cur = conn.cursor()

# Create table
# id is the primary key
# user_id  is the user's ID who has completed the task
# title is the title of the task
# completed is a boolean value that indicates whether the task is completed or not
cur.execute("""
    CREATE TABLE IF NOT EXISTS completion_tracker (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        title VARCHAR(255) NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT FALSE
    )
""")

# Commit the transaction
conn.commit()

# Close the connection
cur.close()
conn.close()