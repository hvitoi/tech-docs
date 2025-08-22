from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
    WebSocketException,
    status,
)
from fastapi.responses import HTMLResponse


router = APIRouter(
    prefix="/websockets",
    tags=["WebSockets"],
)


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off" />
            <button>Send</button>
        </form>
        <ul id='messages'></ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/websockets/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@router.get("/demo")
async def get():
    # this is front a frontend for exploring the websocket api
    return HTMLResponse(html)


# ------ WS


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # accept connection
    while True:
        try:
            data = await websocket.receive_text()  # receive message from client
            if False:
                # WebSocket protocol has its own exceptions. HTTP exceptions are not used here
                # This closes the websocket connection
                raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
            await websocket.send_text(f"Message text was: {data}")  # send response back
        except WebSocketDisconnect:
            # If the client has closed the connection...
            manager.disconnect(websocket)
            await manager.broadcast("A client left the chat")


# let ws = new WebSocket("ws://localhost:8000/websockets/ws");
# ws.onopen = () => ws.send("Hello from browser!");
# ws.onmessage = (event) => console.log("Received:", event.data);
