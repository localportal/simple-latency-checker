from fastapi import FastAPI, Query, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("index.html", "r") as f:
        return f.read()

@app.get("/http")
async def http_endpoint(number: int = Query(0)):
    return {"status": "ok", "number": number}

@app.websocket("/websocket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
        except:
            break
        if data == "Hi":
            await websocket.send_text("Hi")
    


