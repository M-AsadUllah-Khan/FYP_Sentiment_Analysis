import psycopg2
import datetime

# YAHAN APNA NEON DB KA URL PASTE KAREIN
DB_URL = "postgresql://user:password@ep-host.neon.tech/neondb"

def init_db():
    conn = psycopg2.connect(DB_URL)
    c = conn.cursor()
    # AUTOINCREMENT ki jagah SERIAL
    c.execute('''CREATE TABLE IF NOT EXISTS system_logs 
                 (id SERIAL PRIMARY KEY, 
                  timestamp TEXT, 
                  review_text TEXT, 
                  polarity REAL, 
                  sentiment TEXT)''')
    conn.commit()
    conn.close()

def save_analysis(text, polarity, sentiment):
    conn = psycopg2.connect(DB_URL)
    c = conn.cursor()
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # ? ki jagah %s 
    c.execute("INSERT INTO system_logs (timestamp, review_text, polarity, sentiment) VALUES (%s, %s, %s, %s)", 
              (time_now, text, polarity, sentiment))
    conn.commit()
    conn.close()

def get_all_logs():
    conn = psycopg2.connect(DB_URL)
    c = conn.cursor()
    c.execute("SELECT * FROM system_logs ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return [{"id": r[0], "timestamp": r[1], "review": r[2], "polarity": r[3], "sentiment": r[4]} for r in rows]