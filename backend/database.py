import sqlite3
import datetime

DB_NAME = "ecommerce_ai.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS system_logs 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  timestamp TEXT, 
                  review_text TEXT, 
                  polarity REAL, 
                  sentiment TEXT)''')
    conn.commit()
    conn.close()

def save_analysis(text, polarity, sentiment):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO system_logs (timestamp, review_text, polarity, sentiment) VALUES (?, ?, ?, ?)", 
              (time_now, text, polarity, sentiment))
    conn.commit()
    conn.close()

def get_all_logs():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM system_logs ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return [{"id": r[0], "timestamp": r[1], "review": r[2], "polarity": r[3], "sentiment": r[4]} for r in rows]