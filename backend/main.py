from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import sqlite3
import time
import random
import re
from fastapi.middleware.cors import CORSMiddleware
from textblob import TextBlob

app = FastAPI(title="NeuroSent Intelligence Core v5.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def init_db():
    conn = sqlite3.connect('fyp_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            reg_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            text TEXT,
            sentiment TEXT,
            polarity_score REAL,
            emotion TEXT,
            sarcasm_score REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

class UserRegister(BaseModel):
    username: str
    password: str
    email: EmailStr
    phone: str

class UserLogin(BaseModel):
    username: str
    password: str

@app.post("/api/register")
async def register(user: UserRegister):
    try:
        conn = sqlite3.connect('fyp_database.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, email, phone, role) VALUES (?, ?, ?, ?, 'user')",
            (user.username, user.password, user.email, user.phone)
        )
        conn.commit()
        conn.close()
        return {"status": "success"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Identity conflict")

@app.post("/api/login")
async def login(user: UserLogin):
    conn = sqlite3.connect('fyp_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, role FROM users WHERE (username=? OR email=?) AND password=?", 
                   (user.username, user.username, user.password))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {"username": result[0], "role": result[1]}
    raise HTTPException(status_code=401, detail="Unauthorized")

# --- ADVANCED NLP ALGORITHMS ---
def extract_aspects(text):
    # Simulated ABSA (Aspect-Based Sentiment Analysis)
    nouns = [word for word, pos in TextBlob(text).tags if pos.startswith('NN')]
    aspects = []
    for noun in nouns:
        if len(noun) > 2:
            score = random.uniform(-1, 1) # In a real ML model, this comes from a dependency parser
            aspects.append({"aspect": noun, "sentiment": "Positive" if score > 0 else "Negative", "score": score})
    return aspects[:4]

def detect_emotion(text):
    text_lower = text.lower()
    if any(w in text_lower for w in ['hate', 'angry', 'worst', 'terrible', 'bakwas']): return "Anger/Frustration"
    if any(w in text_lower for w in ['love', 'amazing', 'best', 'excellent', 'acha']): return "Joy/Satisfaction"
    if any(w in text_lower for w in ['late', 'sad', 'disappointed', 'poor']): return "Sadness/Disappointment"
    if any(w in text_lower for w in ['wow', 'unexpected', 'sudden']): return "Surprise"
    return "Neutral"

def calculate_sarcasm(text, polarity):
    # If text has positive words but overall context implies delay/bad service
    if polarity > 0.2 and any(w in text.lower() for w in ['late', 'slow', 'wait', 'never']):
        return random.uniform(60, 95) # High Sarcasm Probability
    return random.uniform(5, 25)

@app.post("/api/analyze")
async def analyze(request: dict):
    start_time = time.time()
    text = request['text']
    blob = TextBlob(text)
    
    # Core Metrics
    polarity = blob.sentiment.polarity
    sentiment = "Positive" if polarity > 0.1 else "Negative" if polarity < -0.1 else "Neutral"
    
    # Advanced Metrics
    emotion = detect_emotion(text)
    aspects = extract_aspects(text)
    sarcasm_prob = calculate_sarcasm(text, polarity)
    
    latency = (time.time() - start_time) * 1000
    
    conn = sqlite3.connect('fyp_database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (username, text, sentiment, polarity_score, emotion, sarcasm_score) VALUES (?, ?, ?, ?, ?, ?)", 
                   (request.get('username', 'anonymous'), text, sentiment, polarity, emotion, sarcasm_prob))
    conn.commit()
    conn.close()
    
    return {
        "sentiment": sentiment, 
        "score": polarity, 
        "emotion": emotion,
        "aspects": aspects,
        "sarcasm": sarcasm_prob,
        "latency": latency
    }