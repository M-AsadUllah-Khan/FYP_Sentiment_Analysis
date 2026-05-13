import psycopg2
import datetime
import urllib.parse

DB_URL = "postgresql://neondb_owner:npg_Gh9ASTp0QUzB@ep-plain-water-aohw9oyz.c-2.ap-southeast-1.aws.neon.tech:5432/neondb?sslmode=require"
url = urllib.parse.urlparse(DB_URL)

def get_connection():
    return psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port if url.port else 5432,
        sslmode='require'
    )

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS system_logs 
                 (id SERIAL PRIMARY KEY, 
                  timestamp TEXT, 
                  review_text TEXT, 
                  polarity REAL, 
                  sentiment TEXT)''')
    conn.commit()
    conn.close()

def save_analysis(text, polarity, sentiment):
    conn = get_connection()
    c = conn.cursor()
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO system_logs (timestamp, review_text, polarity, sentiment) VALUES (%s, %s, %s, %s)", 
              (time_now, text, polarity, sentiment))
    conn.commit()
    conn.close()

def get_all_logs():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM system_logs ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return [{"id": r[0], "timestamp": r[1], "review": r[2], "polarity": r[3], "sentiment": r[4]} for r in rows]