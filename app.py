from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ROOT CHECK
@app.route('/')
def home():
    return jsonify({
        "message": "RideMyABC Private Bus API is running 🚌",
        "status": "live",
        "version": "1.0"
    })

# BUS SEARCH - MAIN ROUTE
@app.route('/search')
def search():
    start = request.args.get('start')
    end = request.args.get('end')
    
    if not start or not end:
        return jsonify({
            "success": False,
            "error": "start and end parameters required"
        }), 400
    
    # MANA PRIVATE SERVICE BUSES
    buses = [
        {
            "id": 1,
            "bus_name": "RideMyABC Sleeper",
            "bus_number": "RM001",
            "start_time": "21:00",
            "end_time": "05:00",
            "duration": "8h",
            "price": 650,
            "seats_available": 20,
            "total_seats": 30,
            "from": start,
            "to": end,
            "type": "AC Sleeper",
            "amenities": ["Water Bottle", "Blanket", "Charging Point"]
        },
        {
            "id": 2,
            "bus_name": "RideMyABC Express",
            "bus_number": "RM002",
            "start_time": "06:00",
            "end_time": "10:30",
            "duration": "4h 30m",
            "price": 450,
            "seats_available": 30,
            "total_seats": 40,
            "from": start,
            "to": end,
            "type": "AC Semi-Sleeper",
            "amenities": ["Water Bottle", "Charging Point"]
        },
        {
            "id": 3,
            "bus_name": "RideMyABC Deluxe",
            "bus_number": "RM003",
            "start_time": "14:00",
            "end_time": "18:30",
            "duration": "4h 30m",
            "price": 400,
            "seats_available": 35,
            "total_seats": 45,
            "from": start,
            "to": end,
            "type": "Non-AC Seater",
            "amenities": ["Water Bottle"]
        }
    ]
    
    return jsonify({
        "success": True,
        "count": len(buses),
        "route": f"{start} to {end}",
        "buses": buses
    })

# HEALTH CHECK
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True)
