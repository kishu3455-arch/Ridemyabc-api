from flask import Flask, jsonify
from supabase import create_client

app = Flask(__name__)

# EE 2 LINES LO MATRAM SUPABASE NUNCHI PASTE CHEY
url = "https://gairuvgaqonaequXXXXXX.supabase.co"  # Full URLp
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdhaXJ1dmdhcW9uYWVxdSIsInJvbGUiOiJhbm9uIiwiaWF0IjoxNzE0NTAwODk4LCJleHAiOjIwMzAwNzY4OTh9.XXXXXXXXXXXXXXXX"  # Full key

supabase = create_client(url, key)

@app.route('/buses')
def get_buses():
    try:
        data = supabase.table("buses").select("*").execute()
        return jsonify({
            "success": True, 
            "count": len(data.data), 
            "data": data.data
        })
    except Exception as e:
        return jsonify({
            "success": False, 
            "error": str(e)
        })

@app.route('/')
def home():
    return jsonify({"message": "Ridemyabc API is running 🚌"})

if __name__ == '__main__':
    app.run()
