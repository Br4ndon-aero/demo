import random

statuses = [
    "All systems nominal",
    "Low fuel warning",
    "Solar panels deployed",
    "Communication link stable",
    "Minor temperature fluctuation detected",
    "Thrusters firing",
    "Entering low Earth orbit",
    "Docking sequence initiated"
]

spacecraft_name = "AURORA-1"

print("SPACECRAFT STATUS SIMULATOR")
print("---------------------------")
print(f"Spacecraft: {spacecraft_name}")
print("Status:", random.choice(statuses))
