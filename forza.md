# Forza Motorsport "Data Out" Documentation

Forza Motorsport (2023) carries forward the technology from Forza Motorsport 7 that powers motion sleds, companion apps, and more. We call it “Data Out,” and players can configure it in-game to fit their needs. This page covers details of how to use and configure the feature.

# Overview

After being configured in-game, telemetry output sends data packets for use by external apps. This one-way UDP traffic is sent to a remote IP address at a rate of 60 packets per second. New to Forza Motorsport (2023), this functionality is now also available to the localhost address (127.0.01).

There are currently two packet formats that can be sent to the remote address, and they are identical to Forza Motorsport 7. The original data structure, “Sled,” was designed specifically for motion sleds. The second structure, “Dash,” contains all the Sled data as well as some extra data points.

# Configuration

The following settings can be configured in-game and are found under SETTINGS > GAMEPLAY & HUD > “UDP RACE TELEMETRY” header:

- Data Out: Toggles the data output function on and off. When set to On, data will begin to send as soon as the player gets onto a track.
- Data Out IP Address: The target IP address of the remote machine receiving data. The localhost address (127.0.0.1) is supported.
- Data Out IP Port: The target IP port of the remote machine receiving data. Be sure your app is listening on the same port and that firewall rules allow data on these ports to be received by your app.
- Data Out Packet Format: The format of the data to send, either “Sled” or “Dash.” See below for an outline of each format.

# Output Structures

`[Letter][Number]`

The letter defines the type from one of the following:

- S: Signed Integer
- U: Unsigned Integer
- F: Floating Point

The number defines the amount of bits used.

## Examples:

S8 is a signed byte (8-bits) with potential values between -128 and 127.

F32 is a 32-bit floating point number, equivalent to float/single

## Options

### Sled

`// = 1 when race is on. = 0 when in menus/race stopped`

- S32 IsRaceOn; 0

`// Can overflow to 0 eventually`

- U32 TimestampMS; 4
- F32 EngineMaxRpm; 8
- F32 EngineIdleRpm; 12
- F32 CurrentEngineRpm; 16

`// In the car's local space; X = right, Y = up, Z = forward`

- F32 AccelerationX; 20
- F32 AccelerationY; 24
- F32 AccelerationZ; 28

`// In the car's local space; X = right, Y = up, Z = forward`

- F32 VelocityX; 32
- F32 VelocityY; 36
- F32 VelocityZ; 40
- F32 AngularVelocityX; 44
- F32 AngularVelocityY; 48
- F32 AngularVelocityZ; 52

`// In the car's local space; X = pitch, Y = yaw, Z = roll` 

- F32 Yaw; 56
- F32 Pitch; 60
- F32 Roll; 64

`// Suspension travel normalized: 0.0f = max stretch; 1.0 = max compression`

- F32 NormalizedSuspensionTravelFrontLeft; 68
- F32 NormalizedSuspensionTravelFrontRight; 72
- F32 NormalizedSuspensionTravelRearLeft; 76
- F32 NormalizedSuspensionTravelRearRight; 80

`// Tire normalized slip ratio, = 0 means 100% grip and |ratio| > 1.0 means loss of grip.`

- F32 TireSlipRatioFrontLeft; 84
- F32 TireSlipRatioFrontRight; 88
- F32 TireSlipRatioRearLeft; 92
- F32 TireSlipRatioRearRight; 96

`// Wheels rotation speed radians/sec.`

- F32 WheelRotationSpeedFrontLeft; 100
- F32 WheelRotationSpeedFrontRight; 104
- F32 WheelRotationSpeedRearLeft; 108
- F32 WheelRotationSpeedRearRight; 112

`// = 1 when wheel is on rumble strip, = 0 when off.`

- S32 WheelOnRumbleStripFrontLeft; 116
- S32 WheelOnRumbleStripFrontRight; 120
- S32 WheelOnRumbleStripRearLeft; 124
- S32 WheelOnRumbleStripRearRight; 128

`// = from 0 to 1, where 1 is the deepest puddle`

- F32 WheelInPuddleDepthFrontLeft; 132
- F32 WheelInPuddleDepthFrontRight; 136
- F32 WheelInPuddleDepthRearLeft; 140
- F32 WheelInPuddleDepthRearRight; 144

`// Non-dimensional surface rumble values passed to controller force feedback`

- F32 SurfaceRumbleFrontLeft; 148
- F32 SurfaceRumbleFrontRight; 152
- F32 SurfaceRumbleRearLeft; 156
- F32 SurfaceRumbleRearRight; 160

`// Tire normalized slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.`

- F32 TireSlipAngleFrontLeft; 164
- F32 TireSlipAngleFrontRight; 168
- F32 TireSlipAngleRearLeft; 172
- F32 TireSlipAngleRearRight; 176

`// Tire normalized combined slip, = 0 means 100% grip and |slip| > 1.0 means loss of grip.`

- F32 TireCombinedSlipFrontLeft; 180
- F32 TireCombinedSlipFrontRight; 184
- F32 TireCombinedSlipRearLeft; 188
- F32 TireCombinedSlipRearRight; 192

`// Actual suspension travel in meters`

- F32 SuspensionTravelMetersFrontLeft; 196
- F32 SuspensionTravelMetersFrontRight; 200
- F32 SuspensionTravelMetersRearLeft; 204
- F32 SuspensionTravelMetersRearRight; 208

`// Unique ID of the car make/model`

- S32 CarOrdinal; 212

`// Between 0 (D -- worst cars) and 7 (X class -- best cars) inclusive`

- S32 CarClass; 216

`// Between 100 (worst car) and 999 (best car) inclusive`

- S32 CarPerformanceIndex; 220

`// 0 = FWD, 1 = RWD, 2 = AWD`

- S32 DrivetrainType; 224

`// Number of cylinders in the engine`

- S32 NumCylinders; 228

### Dash

`// = 1 when race is on. = 0 when in menus/race stopped`

- S32 IsRaceOn; 0

`// Can overflow to 0 eventually`

- U32 TimestampMS; 4
- F32 EngineMaxRpm; 8
- F32 EngineIdleRpm; 12
- F32 CurrentEngineRpm; 16

`// In the car's local space; X = right, Y = up, Z = forward`

- F32 AccelerationX; 20
- F32 AccelerationY; 24
- F32 AccelerationZ; 28

`// In the car's local space; X = right, Y = up, Z = forward`

- F32 VelocityX; 32
- F32 VelocityY; 36
- F32 VelocityZ; 40
- F32 AngularVelocityX; 44
- F32 AngularVelocityY; 48
- F32 AngularVelocityZ; 52

`// In the car's local space; X = pitch, Y = yaw, Z = roll`

- F32 Yaw; 56
- F32 Pitch; 60
- F32 Roll; 64

`// Suspension travel normalized: 0.0f = max stretch; 1.0 = max compression`

- F32 NormalizedSuspensionTravelFrontLeft; 68
- F32 NormalizedSuspensionTravelFrontRight; 72
- F32 NormalizedSuspensionTravelRearLeft; 76
- F32 NormalizedSuspensionTravelRearRight; 80

`// Tire normalized slip ratio, = 0 means 100% grip and |ratio| > 1.0 means loss of grip.`

- F32 TireSlipRatioFrontLeft; 84
- F32 TireSlipRatioFrontRight; 88
- F32 TireSlipRatioRearLeft; 92
- F32 TireSlipRatioRearRight; 96

`// Wheels rotation speed radians/sec.`

- F32 WheelRotationSpeedFrontLeft; 100
- F32 WheelRotationSpeedFrontRight; 104
- F32 WheelRotationSpeedRearLeft; 108
- F32 WheelRotationSpeedRearRight; 112

`// = 1 when wheel is on rumble strip, = 0 when off.`

- S32 WheelOnRumbleStripFrontLeft; 116
- S32 WheelOnRumbleStripFrontRight; 120
- S32 WheelOnRumbleStripRearLeft; 124
- S32 WheelOnRumbleStripRearRight; 128

`// = from 0 to 1, where 1 is the deepest puddle`

- F32 WheelInPuddleDepthFrontLeft; 132
- F32 WheelInPuddleDepthFrontRight; 136
- F32 WheelInPuddleDepthRearLeft; 140
- F32 WheelInPuddleDepthRearRight; 144

`// Non-dimensional surface rumble values passed to controller force feedback`

- F32 SurfaceRumbleFrontLeft; 148
- F32 SurfaceRumbleFrontRight; 152
- F32 SurfaceRumbleRearLeft; 156
- F32 SurfaceRumbleRearRight; 160

`// Tire normalized slip angle, = 0 means 100% grip and |angle| > 1.0 means loss of grip.`

- F32 TireSlipAngleFrontLeft; 164
- F32 TireSlipAngleFrontRight; 168
- F32 TireSlipAngleRearLeft; 172
- F32 TireSlipAngleRearRight; 176

`// Tire normalized combined slip, = 0 means 100% grip and |slip| > 1.0 means loss of grip.`

- F32 TireCombinedSlipFrontLeft; 180
- F32 TireCombinedSlipFrontRight; 184
- F32 TireCombinedSlipRearLeft; 188
- F32 TireCombinedSlipRearRight; 192

`// Actual suspension travel in meters`

- F32 SuspensionTravelMetersFrontLeft; 196
- F32 SuspensionTravelMetersFrontRight; 200
- F32 SuspensionTravelMetersRearLeft; 204
- F32 SuspensionTravelMetersRearRight; 208

`// Unique ID of the car make/model`

- S32 CarOrdinal; 212

`// Between 0 (D -- worst cars) and 7 (X class -- best cars) inclusive`

- S32 CarClass; 216

`// Between 100 (worst car) and 999 (best car) inclusive`

- S32 CarPerformanceIndex; 220

`// 0 = FWD, 1 = RWD, 2 = AWD`

- S32 DrivetrainType; 224

`// Number of cylinders in the engine`

- S32 NumCylinders; 228
- F32 PositionX; 232
- F32 PositionY; 236
- F32 PositionZ; 240
- F32 Speed; 244
- F32 Power; 248
- F32 Torque; 252
- F32 TireTempFrontLeft; 256
- F32 TireTempFrontRight; 260
- F32 TireTempRearLeft; 264
- F32 TireTempRearRight; 268
- F32 Boost; 272
- F32 Fuel; 276
- F32 DistanceTraveled; 280
- F32 BestLap; 284
- F32 LastLap; 288
- F32 CurrentLap; 292
- F32 CurrentRaceTime; 296
- U16 LapNumber; 300
- U8 RacePosition; 302
- U8 Accel; 303
- U8 Brake; 304
- U8 Clutch; 305
- U8 HandBrake; 306
- U8 Gear; 307
- S8 Steer; 308
- S8 NormalizedDrivingLine; 309
- S8 NormalizedAIBrakeDifference; 310
- F32 TireWearFrontLeft; 314
- F32 TireWearFrontRight; 318
- F32 TireWearRearLeft; 322
- F32 TireWearRearRight; 326

`// ID for track`

- S32 TrackOrdinal; 330