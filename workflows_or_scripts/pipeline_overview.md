# ⚙️ Workflow Architecture & SOP Design
## Bambinos.live AI Content Mining & Production Pipeline

---

## 1. End-to-End Technical Flow

```
[Zoom/Live Class Session Ends]
            │
            ▼
[Automated Webhook / Cloud Storage Ingest]
  • Trigger: Webhook triggers n8n workflow upon Zoom MP4 cloud recording completion
  • Storage: Raw MP4 & Audio stream pushed to Google Cloud Storage / AWS S3
            │
            ▼
[Audio Diarization & Transcription]
  • Engine: AssemblyAI (or Deepgram Nova-2) with Speaker Diarization enabled
  • Output: Timestamped WebVTT & JSON with speaker turns (Teacher vs Student)
            │
            ▼
[Step 1: Automated PII Masking & Toxicity / Negative Tone Filter]
  • LLM: GPT-4o Mini with strict schema
  • Checks: Child full names, geographical PII, contact info, and Teacher Tone Red Flags
  • Logic Gate: If session exhibits hostile tone (e.g., Maths session audit), status = EXCLUDED
            │
            ▼
[Step 2: Moment Mining & 6-Bucket Categorization]
  • LLM: Claude 3.5 Sonnet / GPT-4o
  • Input: Verified Safe Transcripts only
  • Output: Candidate 15–45s clips classified into the 6 Moment Buckets
            │
            ▼
[Step 3: Quantitative 10-Point Rubric Scoring]
  • Evaluates: Emotional Pull (0–3), Clarity (0–2), Relatability (0–2), Visual Potential (0–2), Safety (0–1)
  • Threshold: Score >= 8 -> Hero Ad candidate; Score 6–7 -> Supporting Content; < 6 -> Archive
            │
            ▼
[Step 4: Multimodal Audio vs Visual Verification (Pegasus / Twelve Labs)]
  • Edge Case Resolver: Checks student face visibility, camera angle, and screen activity
  • Flags: Camera off, bad lighting, teacher screen freeze
            │
            ▼
[Step 5: Automated Ad Brief & Pre-cut Clip Generation]
  • Clip Extractor: Automated FFmpeg worker trims exact MP4 segments based on start/end timestamps
  • Brief Generator: Produces 3-second hook, platform-specific cuts (Reels, Shorts, WhatsApp), captions & hashtags
            │
            ▼
[Step 6: Editor Handoff Dashboard (Airtable / Notion)]
  • Editor receives: 
      1. Pre-trimmed 9:16 / 16:9 MP4 candidate
      2. Ad brief with 3s hook, captions, and visual instructions
      3. Quality assurance checklist
```

---

## 2. Tooling Stack

| Stage | Primary Tool | Fallback / Alternative | Purpose |
|---|---|---|---|
| **Orchestration** | **n8n** (self-hosted / cloud) | Zapier / Make | Connects Zoom Webhooks, S3, LLM APIs, and Airtable |
| **Speech-to-Text** | **AssemblyAI** | Whisper Large v3 / Deepgram | Multilingual & Indian English diarization |
| **PII & Safety** | **GPT-4o Mini** | Custom Python Regex | High-speed, zero-retention PII & negative tone filter |
| **Moment Mining** | **Claude 3.5 Sonnet** | GPT-4o | Nuanced narrative comprehension and emotional arc detection |
| **Visual QA** | **Twelve Labs Pegasus API** | Google Video Intelligence | Verifies face visibility & visual-audio coherence |
| **Video Pre-trim** | **FFmpeg Script** | Cloudinary Video API | Lossless automated timestamp cutting |
| **Editor Dashboard**| **Airtable** | Notion Database | Kanban queue for Human-in-the-loop review and approval |

---

## 3. Resolving the "Audio vs. Visual" Gap (Edge Case SOP)

Transcripts describe what is said, never what is seen. To prevent video editors from wasting time cutting dead footage:

1. **Automated Visual Verification API (Twelve Labs Pegasus):**
   - For every timestamp flagged as an audio moment, the API inspects the ±5 second video window.
   - Outputs:
     - `face_detected`: boolean (checks if student face is visible)
     - `screen_sharing_status`: boolean (checks if slide/whiteboard or speaker view)
     - `occlusion_score`: 0.0 to 1.0 (flags hands covering face, dark room)
2. **Quality Gate Rule:**
   - If `face_detected == False` during an audio breakthrough, the brief automatically switches format:
     - **Format A (Standard):** Split-screen (Teacher + Student video).
     - **Format B (Visual Fallback):** Teacher video + Animated text overlay / motion graphic representing student voiceover.
3. **Teacher Off-Screen / Distraction Gate:**
   - Any segment where teacher steps away (e.g. English session door opening) is tagged with `visual_anomaly_detected = True` and auto-excised.
