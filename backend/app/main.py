
from fastapi import FastAPI, WebSocket, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from .gemini_client import generate
import os, json, tempfile, shutil

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple in‑memory session store (replace with Redis for prod)
sessions = {}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    sid = id(ws)
    sessions[sid] = {"projector":None}
    await ws.send_json({"role":"assistant",
                        "content":"Will you use a projector today, or only worksheets?"})
    try:
        while True:
            msg = await ws.receive_json()
            user = msg["content"]

            # Handle projector question first
            if sessions[sid]["projector"] is None:
                sessions[sid]["projector"] = "yes" if "yes" in user.lower() else "no"
                await ws.send_json({"role":"assistant",
                                    "content":"Great! Please tell me the lesson topic and level."})
                continue

            # Build minimal prompt (replace with real retrieval logic)
            prompt = f"""[Projector: {sessions[sid]['projector']}]
            USER REQUEST:
            {user}
            Follow the persona rules at all times.
            """
            answer = generate(prompt)
            await ws.send_json({"role":"assistant","content":answer})
    except Exception as e:
        await ws.close()
