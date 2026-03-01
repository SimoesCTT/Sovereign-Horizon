import asyncio
import json
import time
from fastapi import FastAPI, WebSocket, Request

app = FastAPI()

# Internal state
manifold_data = {"bits": [0]*1024, "conflicts": 0}

@app.post("/update")
async def update_manifold(request: Request):
    global manifold_data
    data = await request.json()
    manifold_data["bits"] = data.get("bits", [0]*1024)
    manifold_data["conflicts"] = data.get("conflicts", manifold_data["conflicts"])
    return {"status": "ok"}

@app.websocket("/ws/manifold")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            payload = {
                "bits": manifold_data["bits"],
                "conflicts": manifold_data["conflicts"],
                "timestamp": time.time()
            }
            await websocket.send_json(payload)
            await asyncio.sleep(0.05)
    except:
        pass
