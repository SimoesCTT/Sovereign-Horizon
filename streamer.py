import asyncio
import json
import time
from fastapi import FastAPI, WebSocket
import sovereign_logic as sl

app = FastAPI()
# Initializing the 1024-bit logic gate
bridge = sl.Bridge() 

@app.websocket("/ws/manifold")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("[HORIZON] Node Connected. Streaming Manifold Data...")
    try:
        while True:
            # Capturing the current state of the 1024-bit lattice
            state = bridge.get_state() 
            data = {
                "fidelity": 1.0000000000000000, # Reihman-Lock Baseline
                "bits": state, # The raw 1024-bit vector
                "entropy": 0.963, # The Singapore Zenith Resonance
                "timestamp": time.time()
            }
            await websocket.send_json(data)
            await asyncio.sleep(0.05) # 20Hz refresh for high-fidelity tracking
    except Exception as e:
        print(f"[HORIZON] Stream interrupted: {e}")
