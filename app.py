from flask import Flask, jsonify
from supabase import create_client

app = Flask(__name__)

url = "https://himwwdufpswsblssnvrw.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhpbXd3ZHVmcHN3c2Jsc3NudnJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDg5MzU3MzYsImV4cCI6MjA2NDUxMTczNn0.rKm40TepoHwU7i3k62OHIJI5mMZL2p4SXTnXY14aNgc"
supabase = create_client(url, key)

@app.route('/buses')
def get_buses():
    try:
        data = supabase.table("buses").select("*").execute()
        return jsonify({"success": True, "count": len(data.data), "buses": data.data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run()
    
