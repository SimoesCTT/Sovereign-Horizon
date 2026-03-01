import requests
import time
import math

def send_state(bits):
    try:
        requests.post("http://localhost:8000/update", json={"bits": bits})
    except:
        pass

print("Starting Manifold Collapse Simulation...")
for t in range(100):
    # Create a wave pattern through the 1024 bits
    bits = [1 if math.sin(i/10 + t/5) > 0 else 0 for i in range(1024)]
    send_state(bits)
    time.sleep(0.05)
print("Collapse Complete.")
