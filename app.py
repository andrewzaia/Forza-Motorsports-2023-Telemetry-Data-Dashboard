from flask import Flask, render_template
from flask_socketio import SocketIO
import socket
import struct
import threading

app = Flask(__name__)
socketio = SocketIO(app)

telemetry_data = {
    "IsRaceOn": 0,
    "CurrentEngineRpm": 0,
    "AccelerationX": 0,
    "AccelerationY": 0,
    "AccelerationZ": 0,
    "WheelRotationSpeedFrontLeft": 0,
    "WheelRotationSpeedFrontRight": 0,
    "WheelRotationSpeedRearLeft": 0,
    "WheelRotationSpeedRearRight": 0,
    "CarOrdinal": 0,
    "CarClass": 0,
    "CarPerformanceIndex": 0,
    "DrivetrainType": 0,
    "NumCylinders": 0,
    "PositionX": 0,
    "PositionY": 0,
    "PositionZ": 0,
    "Speed": 0,
    "Speed_KMH": 0,
    "Speed_MPH": 0,
    "Power": 0,
    "Torque": 0,
    "Gear": 0
    # Add more telemetry data here
}

@app.route('/')
def index():
    return render_template('index.html', telemetry_data=telemetry_data)

def udp_listener():
    # Define the UDP server address and port
    host = "127.0.0.1"  # localhost
    port = 5300

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified host and port
    sock.bind((host, port))

    while True:
        try:
            # Receive data from the socket
            data, addr = sock.recvfrom(1024)  # Adjust buffer size as needed

            # Unpack the data according to the Forza Motorsport 2023 structure
            IsRaceOn = struct.unpack('i', data[:4])[0]
            EngineMaxRpm = int(struct.unpack('f', data[8:12])[0])
            EngineIdleRpm = int(struct.unpack('f', data[12:16])[0])
            CurrentEngineRpm = int(struct.unpack('f', data[16:20])[0])
            AccelerationX = int(struct.unpack('f', data[20:24])[0])
            AccelerationY = int(struct.unpack('f', data[24:28])[0])
            AccelerationZ = int(struct.unpack('f', data[28:32])[0])
            WheelRotationSpeedFrontLeft = int(struct.unpack('f', data[100:104])[0])
            WheelRotationSpeedFrontRight = int(struct.unpack('f', data[104:108])[0])
            WheelRotationSpeedRearLeft = int(struct.unpack('f', data[108:112])[0])
            WheelRotationSpeedRearRight = int(struct.unpack('f', data[112:116])[0])
            CarOrdinal = int(struct.unpack('i', data[212:216])[0])
            CarClass = int(struct.unpack('i', data[216:220])[0])
            CarPerformanceIndex = int(struct.unpack('i', data[220:224])[0])
            DrivetrainType = int(struct.unpack('i', data[224:228])[0])
            NumCylinders = int(struct.unpack('i', data[228:232])[0])
            PositionX = int(struct.unpack('f', data[232:236])[0])
            PositionZ = int(struct.unpack('f', data[236:240])[0])
            PositionY = int(struct.unpack('f', data[240:244])[0])
            Speed = int(struct.unpack('f', data[244:248])[0])
            Speed_KMH = int(struct.unpack('f', data[244:248])[0] * 3.6)
            Speed_MPH = int(struct.unpack('f', data[244:248])[0] * 2.23694)
            Power = int(struct.unpack('f', data[248:252])[0])
            Torque = int(struct.unpack('f', data[252:256])[0])
            TireTempFrontLeft = int(struct.unpack('f', data[256:260])[0])
            TireTempFrontRight = int(struct.unpack('f', data[260:264])[0])
            TireTempRearLeft = int(struct.unpack('f', data[264:268])[0])
            TireTempRearRight = int(struct.unpack('f', data[268:272])[0])
            Boost = int(struct.unpack('f', data[272:276])[0])
            Fuel = int(struct.unpack('f', data[276:280])[0])
            
            # Dash telemetry data (with BufferOffset)
            Gear = struct.unpack('B', data[307:308])[0]

            # Make all the telemtries!
            telemetry_data["IsRaceOn"] = IsRaceOn
            telemetry_data["EngineMaxRpm"] = EngineMaxRpm
            telemetry_data["EngineIdleRpm"] = EngineIdleRpm
            telemetry_data["CurrentEngineRpm"] = CurrentEngineRpm
            telemetry_data["AccelerationX"] = AccelerationX
            telemetry_data["AccelerationY"] = AccelerationY
            telemetry_data["AccelerationZ"] = AccelerationZ
            telemetry_data["WheelRotationSpeedFrontLeft"] = WheelRotationSpeedFrontLeft
            telemetry_data["WheelRotationSpeedFrontRight"] = WheelRotationSpeedFrontRight
            telemetry_data["WheelRotationSpeedRearLeft"] = WheelRotationSpeedRearLeft
            telemetry_data["WheelRotationSpeedRearRight"] = WheelRotationSpeedRearRight
            telemetry_data["CarOrdinal"] = CarOrdinal
            telemetry_data["CarClass"] = CarClass
            telemetry_data["CarPerformanceIndex"] = CarPerformanceIndex
            telemetry_data["DrivetrainType"] = DrivetrainType
            telemetry_data["NumCylinders"] = NumCylinders
            telemetry_data["PositionX"] = PositionX
            telemetry_data["PositionY"] = PositionY
            telemetry_data["PositionZ"] = PositionZ
            telemetry_data["Speed"] = Speed
            telemetry_data["Speed_KMH"] = Speed_KMH
            telemetry_data["Speed_MPH"] = Speed_MPH
            telemetry_data["Power"] = Power
            telemetry_data["Torque"] = Torque
            telemetry_data["TireTempFrontLeft"] = TireTempFrontLeft
            telemetry_data["TireTempFrontRight"] = TireTempFrontRight
            telemetry_data["TireTempRearLeft"] = TireTempRearLeft
            telemetry_data["TireTempRearRight"] = TireTempRearRight
            telemetry_data["Boost"] = Boost
            telemetry_data["Fuel"] = Fuel

            telemetry_data["Gear"] = Gear

            # Emit telemetry data to connected clients via WebSocket
            socketio.emit('telemetry', telemetry_data)

        except KeyboardInterrupt:
            print("Exiting...")
            break

    # Close the socket when done
    sock.close()

if __name__ == '__main__':
    @socketio.on('connect')
    def handle_connect():
        socketio.emit('telemetry', telemetry_data)

    udp_listener_thread = threading.Thread(target=udp_listener)
    udp_listener_thread.start()

    socketio.run(app, debug=False, port=8080)
