import time
from flask import Flask, render_template

app = Flask(__name__)

# --- Configuration ---
PORT = 8002
DURATION = 10  # Seconds the device stays on

# Initialize timestamp to 0 so it starts "OFF"
last_scan_time = 0.0

@app.route('/')
def index():
    return "NFC Server Ready on Port 8002. Waiting for scan..."

# --- The Phone hits this URL ---
@app.route('/activate')
def activate():
    global last_scan_time
    last_scan_time = time.time() # Save current server time
    
    # Calculate when the timer should end
    end_time = last_scan_time + DURATION
    
    # Format a readable string for the display (e.g., 14:30:05)
    readable_start = time.strftime('%H:%M:%S', time.localtime(last_scan_time))
    
    # Render the HTML page
    return render_template('activate.html', 
                           start_time_str=readable_start, 
                           end_timestamp=end_time)

# --- The ESP Microcontroller hits this URL ---
@app.route('/status')
def status():
    global last_scan_time
    # Check if we are still within the 10-second window
    if (time.time() - last_scan_time) <= DURATION:
        return "ON"
    else:
        return "OFF"

if __name__ == '__main__':
    # Run on Port 8002
    print(f"Starting server on port {PORT}...")
    app.run(host='0.0.0.0', port=PORT)
