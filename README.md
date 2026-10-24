# LiveKit SIP Outbound Caller Agent

A Python example that starts an outbound SIP call from a LiveKit room and runs a voice pipeline to confirm an appointment.

## What it demonstrates

- Creates a SIP participant using a configured LiveKit outbound trunk.
- Reads the destination from LiveKit job metadata and validates it as E.164 before connecting or dialing.
- Runs a voice pipeline with Deepgram `nova-2-phonecall` speech recognition, OpenAI language and speech services, and Silero VAD.
- Includes function-call examples for ending a call, checking sample availability, confirming an appointment, and detecting voicemail.

Appointment details and availability are hard-coded examples; confirmation does not connect to a calendar or booking service. This repository is based on the example at [kylecampbell/livekit-outbound-caller-agent](https://github.com/kylecampbell/livekit-outbound-caller-agent); retain that upstream attribution and verify differences before presenting the implementation as original work.

## Setup

Use Python 3.10 or newer:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env.local
```

Set `LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET`, `OPENAI_API_KEY`, `DEEPGRAM_API_KEY`, and `SIP_OUTBOUND_TRUNK_ID` in `.env.local`. The trunk ID must be configured before the worker starts. Dispatch jobs with an E.164 destination in their metadata. The agent can place billable calls; use only authorized test numbers and an appropriately configured trunk.

## Tests

```bash
python -m pip install -r requirements-test.txt
python -m pytest -q tests
```

Tests do not place calls or exercise external provider services.
