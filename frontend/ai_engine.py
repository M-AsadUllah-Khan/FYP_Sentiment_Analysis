import random

def predict_sentiment(text, threshold):
    if not isinstance(text, str): return "NEUTRAL", 50.0, "😐", "neu-text", "#f59e0b"
    text_lower = text.lower()
    neg_words = ["bad", "worst", "terrible", "poor", "broken", "waste", "hate", "slow", "damaged", "late"]
    pos_words = ["amazing", "great", "good", "love", "excellent", "best", "fast", "perfect", "beautiful"]
    
    neg_count = sum(1 for w in neg_words if w in text_lower)
    pos_count = sum(1 for w in pos_words if w in text_lower)
    
    if neg_count > pos_count:
        conf = min(99.9, 60.0 + (neg_count * 15) + random.uniform(0, 10))
        if conf < threshold: return "UNCERTAIN", conf, "⚠️", "unc-text", "#8b5cf6"
        return "NEGATIVE", round(conf, 2), "😡", "neg-text", "#ef4444"
    elif pos_count > neg_count:
        conf = min(99.9, 60.0 + (pos_count * 15) + random.uniform(0, 10))
        if conf < threshold: return "UNCERTAIN", conf, "⚠️", "unc-text", "#8b5cf6"
        return "POSITIVE", round(conf, 2), "😊", "pos-text", "#10b981"
    else:
        conf = round(random.uniform(50.0, 65.0), 2)
        if conf < threshold: return "UNCERTAIN", conf, "⚠️", "unc-text", "#8b5cf6"
        return "NEUTRAL", conf, "😐", "neu-text", "#f59e0b"

def extract_aspects(text):
    text_lower = text.lower()
    aspects = {}
    if any(w in text_lower for w in ["delivery", "shipping", "arrive", "time", "late", "fast"]):
        aspects['Delivery 🚚'] = "NEGATIVE" if any(w in text_lower for w in ["late", "slow", "delay"]) else "POSITIVE"
    if any(w in text_lower for w in ["quality", "material", "product", "item", "broken", "perfect"]):
        aspects['Quality ⭐'] = "NEGATIVE" if any(w in text_lower for w in ["bad", "poor", "broken", "cheap"]) else "POSITIVE"
    if any(w in text_lower for w in ["price", "money", "cost", "expensive", "cheap", "value", "waste"]):
        aspects['Pricing 💲'] = "NEGATIVE" if any(w in text_lower for w in ["expensive", "waste", "high"]) else "POSITIVE"
    return aspects

def get_quantum_gauge(confidence, color_hex):
    return f"""
    <div style="display: flex; justify-content: center; align-items: center; margin-top: 15px; position: relative;">
        <svg viewBox="0 0 40 40" class="circular-chart" style="width: 130px; height: 130px; filter: drop-shadow(0 0 12px {color_hex}80);">
            <circle cx="20" cy="20" r="18" fill="none" stroke="{color_hex}40" stroke-width="0.5" stroke-dasharray="2 4" style="animation: spin-slow 8s linear infinite; transform-origin: center;" />
            <circle cx="20" cy="20" r="18" fill="none" stroke="{color_hex}80" stroke-width="0.5" stroke-dasharray="10 20" style="animation: spin-fast 4s linear infinite reverse; transform-origin: center;" />
            <path d="M20 4.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" style="fill: none; stroke: rgba(128,128,128,0.2); stroke-width: 2.5; stroke-linecap: round;"/>
            <path stroke-dasharray="{confidence}, 100" d="M20 4.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" style="fill: none; stroke: {color_hex}; stroke-width: 2.5; stroke-linecap: round; animation: ring-fill 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;"/>
            <text x="20" y="23.5" style="fill: var(--text-color); font-family: 'Segoe UI', sans-serif; font-size: 8px; font-weight: 900; text-anchor: middle; animation: pulse-text 2s infinite alternate;">{confidence}%</text>
        </svg>
    </div>
    """