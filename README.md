# LiveKit SIP Outbound Caller Agent

A Python voice-agent example that starts an outbound SIP call from a LiveKit room and runs a voice pipeline to confirm an appointment.

## What it demonstrates

- Creates a SIP participant using a configured LiveKit outbound trunk
- Receives the destination number through job metadata
- Runs a voice pipeline using Deepgram `nova-2-phonecall` speech recognition, OpenAI language and speech services, and Silero VAD
- Exposes function-call examples for ending a call, checking sample availability, confirming an appointment, and detecting voicemail

The appointment details and availability response are hard-coded examples in `agent.py`; they are not connected to a calendar or booking service. This repository’s existing README points to `kylecampbell/livekit-outbound-caller-agent` for its setup source. Keep that upstream attribution and clarify any local changes so the repository does not imply sole authorship of the example.

## Setup

Create a virtual environment and install the project requirements:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Set `SIP_OUTBOUND_TRUNK_ID` and the LiveKit, Deepgram, and OpenAI credentials in a local `.env.local` file. Do not commit credentials or trunk secrets. The agent entry point is `agent.py`; configure a valid LiveKit SIP trunk before placing calls.

## Stack

Python · LiveKit Agents · LiveKit SIP · Deepgram · OpenAI · Silero VAD

