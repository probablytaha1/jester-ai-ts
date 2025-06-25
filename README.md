
# Jester AI – TS

Full‑stack AI teaching assistant powered by Gemini and Google Drive.

## Quick Start (Local)

```bash
# backend
cd backend
cp .env.example .env   # add your GEMINI_API_KEY
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
bash start.sh
```

```bash
# frontend
cd frontend
cp .env.local.example .env.local  # add your GOOGLE keys + backend url
npm install
npm run dev
```

Visit http://localhost:3000 to chat.

## Docker

```bash
docker-compose up --build
```

## Where to Add API Keys

| Key                     | File                              |
|-------------------------|-----------------------------------|
| `GEMINI_API_KEY`        | `backend/.env`                    |
| `NEXT_PUBLIC_GOOGLE_API_KEY` | `frontend/.env.local`      |
| `NEXT_PUBLIC_GOOGLE_CLIENT_ID` | `frontend/.env.local`  |

## Features Implemented (Skeleton)

- Projector question logic
- Folder picker placeholder (frontend TODO)
- File upload placeholder
- Quiz Builder / PPT / Weekly Planner modules (stubs)

Enhance each module inside **backend/app** to unlock full power.
