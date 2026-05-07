from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
CORS(app)

url = "https://gairuvgaqonaequakocx.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdhaXJ1dmdhcW9uYWVxdWFrb2N4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc5ODU3NjEsImV4cCI6MjA5MzU2MTc2MX0.F7DHVLPDXciFytNfa34lCTspfEjwL_xiXDObCW00r-w"

supabase: Client = create_client(url, key)

@app.route('/')
def home():
    return jsonify({"message": "RideMyABC Platform API 🚌", "status": "live", "version": "2.0"})

@app.route('/owner/register', methods=['POST'])
def owner_register():
    data = request.json
    try:
        result = supabase.table("owners").insert({
            "name": data['name'],
            "phone": data['phone'],
            "email": data.get('email'),
            "password": data['password'],
            "company_name": data.get('company_name')
        }).execute()
        return jsonify({"success": True, "message": "Owner registered", "owner": result.data[0]})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/owner/add-bus', methods=['POST'])
def add_bus():
    data = request.json
    try:
        result = supabase.table("buses").insert({
            "owner_id": data['owner_id'],
            "bus_name": data['bus_name'],
            "bus_number": data['bus_number'],
            "from_city": data['from_city'],
            "to_city": data['to_city'],
            "start_time": data['start_time'],
            "end_time": data['end_time'],
            "price": data['price'],
            "total_seats": data['total_seats'],
            "seats_available": data['total_seats'],
            "bus_type": data['bus_type'],
            "amenities": data.get('amenities', [])
        }).execute()
        return jsonify({"success": True, "message": "Bus added", "bus": result.data[0]})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/search')
def search():
    start = request.args.get('start')
    end = request.args.get('end')
    if not start or not end:
        return jsonify({"success": False, "error": "start and end cities required"}), 400
    try:
        result = supabase.table("buses").select("*").eq("from_city", start).eq("to_city", end).eq("status", "active").execute()
        return jsonify({
            "success": True,
            "count": len(result.data),
            "route": f"{start} to {end}",
            "buses": result.data
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
