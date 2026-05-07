from flask import Flask, jsonify
from supabase import create_client

app = Flask(__name__)

url = "https://gairuvgaqonaequ....supabase.co"  # SUPABASE NUNCHI FULL URL PASTE CHEY
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."  # SUPABASE NUNCHI ANON KEY PASTE CHEY
supabase = create_client(url, key)

@app.route('/buses')
def get_buses():
    try:
        data = supabase.table("buses").select("*").execute()
        return jsonify({"success": True, "count": len(data.data), "data": data.data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run()
