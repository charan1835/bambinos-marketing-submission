# Bambinos.live — AI Content Mining & Production Pipeline

**Candidate:** Charan  
**Role:** AI Program Manager — Marketing  
**Track:** Marketing (Live Class → Scroll-Stopping Ad Pipeline)  
**Location:** Bengaluru (In-office)  
**Repository:** [https://github.com/charan1835/bambinos-marketing-submission](https://github.com/charan1835/bambinos-marketing-submission)

---

## 📌 Executive Summary

Bambinos.live video editors currently spend **85–90% of their review time** manually scrubbing 50-minute live class recordings to find 10–20 second ad moments. At 500 classes/week, this represents **375 wasted editor-hours per week**. 

This report outlines an AI-powered pipeline reducing review time to **~8 minutes per class** (an **82% time reduction**, saving **~₹2.35L/month**) while enforcing brand safety, 6-bucket taxonomy scoring, and resolving the Audio vs. Visual verification gap.

---

## 📁 Repository Structure

```
bambinos-marketing-submission/
├── README.md                                  # Executive summary & full case documentation
├── CASE_REPORT.md                             # Comprehensive formal report (Deliverables A, B, C & D)
├── Case_Report.html                           # Print-ready HTML document for instant PDF export
├── prompts/
│   ├── 01_pii_tone_filter_prompt.md          # PII masking & negative educator tone filter
│   ├── 02_moment_mining_prompt.md            # 6-bucket AI moment mining prompt
│   └── 03_ad_brief_prompt.md                 # Ad brief generation prompt with 3s hooks & editor notes
├── workflows_or_scripts/
│   ├── pipeline.py                            # Executable Python script for transcript parsing & filtering
│   └── pipeline_overview.md                   # Full n8n + AI workflow architecture & audio/visual SOP
├── results/
│   ├── moment_extraction.csv                  # Complete extraction table across all evaluated sessions
│   ├── scored_moments.csv                     # Quantitative 10-point scoring & ranking table
│   ├── video_verification_qa_log.md           # MP4 video cross-check log (Audio vs. Visual gap analysis)
│   ├── clean_transcripts/                     # PII-masked, cleaned transcripts for all 4 sessions
│   │   ├── English_Cleaned.txt
│   │   ├── Gita_Cleaned.txt
│   │   ├── Science_Cleaned.txt
│   │   └── Maths_Audited_Excluded.txt
│   └── ad_briefs/                             # Editor-ready platform ad briefs (Reels / Shorts / WhatsApp)
│       ├── ad_brief_01_english_imagination.md
│       ├── ad_brief_02_gita_prayer_courage.md
│       └── ad_brief_03_science_horse_energy.md
```

---

## Deliverable A — Research & Creative Taxonomy

### A1. Competitor Benchmark

| Competitor | Content Hook | What Converts | The Gap Bambinos Can Exploit |
|---|---|---|---|
| **PlanetSpark** | Child debate & speech snippets | High child relatability | Inconsistent audio quality; lack of structured moment taxonomy. |
| **Bhanzu** | Speed math solving | Proof of skill outcome | High-stress test-prep feel; lacks warmth, curiosity, and joy. |
| **Vedantu** | WAVE AI highlights | Professional finish | Teacher-monologue heavy; parents cannot see their own child in it. |
| **BrightChamps** | Coding app demos | Tangible output | Scripted, corporate feel; lacks organic classroom emotion. |
| **Outschool (US)** | Parent social proof | Trust and credibility | Western context; misses cultural resonance of India and GCC diaspora. |

---

### A2. The 6 Moment Buckets

1. **Breakthrough (Cognitive Click):** Student connects dots independently without teacher prompting (e.g. Gita student realizing prayer generates bravery).
2. **Wonder & Delight:** Spontaneous outburst of joy and awe (e.g. English student excitedly listing ocean animals: crabs, seaweed, octopus).
3. **Great Teaching:** High-craft pedagogical analogies (e.g. Science teacher explaining internal horse energy vs. external tractor ignition).
4. **Curiosity Spark:** Unexpected, insightful questions from the child demonstrating deep engagement.
5. **Warm Connection:** Authentic educator empathy and emotional validation creating a safe learning space.
6. **Outcome Demonstration:** Child demonstrates structural mastery (e.g. reciting Story Mountain stages unprompted).

---

### A3. 10-Point Scoring Rubric

$$\text{Total Score} = \text{Emotional Pull (3)} + \text{Clarity (2)} + \text{Relatability (2)} + \text{Visual Potential (2)} + \text{Brand Safety (1)}$$

- **Score 10/10: Hero Ad** — Fast-tracked to paid Meta Reels, YouTube Shorts, and WhatsApp Status.
- **Score 8–9/10: Supporting Ad** — Used for organic social, mid-funnel proof, and WhatsApp remarketing.
- **Score < 8/10: Archive** — Stored in pedagogical asset library.

---

### A4. Hard Exclusions & Maths Disqualification Case Study

- **Zero-Tolerance Flags:** Child PII, visible background privacy leaks, and educator hostility.
- **Maths Session (`2125736982`) Disqualification:** Flagged for severe tone violations:
  - `00:25:17`: *"It's stupid. Where is your focus?"*
  - `00:37:40`: *"Silly simple thing you are not understanding"*
  - `00:38:14`: *"This way I will not teach you"*
  - **Verdict:** Disqualified 100% under Brand Safety (0/1 score) and archived for internal academic review.

---

## Deliverable B — Workflow & SOP Design

### B1. End-to-End Pipeline

```
[Zoom Cloud Recording Completes]
       │
       ▼
[n8n Webhook Ingest ➔ S3 Raw Video Storage]
       │
       ▼
[AssemblyAI Speech-to-Text with Speaker Diarization]
       │
       ▼
[GPT-4o Mini: PII Masking & Negative Educator Tone Filter Gate]
       │
       ▼
[Claude 3.5 Sonnet: 6-Bucket Moment Mining]
       │
       ▼
[Quantitative 10-Point Rubric Scoring]
       │
       ▼
[Twelve Labs Pegasus: Audio vs. Visual Verification QA]
       │
       ▼
[FFmpeg Automated Pre-Cut MP4 Clips + Ad Brief Generation]
       │
       ▼
[Airtable Editor Kanban Dashboard Handoff]
```

### B2. Solving the "Audio vs. Visual" Gap

Transcripts describe what is said, not what is seen. Our pipeline integrates **Twelve Labs Pegasus API** to check:
1. `face_visibility_ratio > 0.8` (ensures student is framed, well-lit, and camera is active).
2. Student engagement vs. looking away.
3. Teacher absence/interruptions (e.g. excising doorbell interruptions in English class at `00:07:44`).
4. **Fallback:** If the child's face is obscured during an audio breakthrough, the brief automatically assigns an animated kinetic typography template.

---

## Deliverable C — Extracted Ad Briefs (Real Dataset)

### 🎬 Ad Brief 1: English — "What Did You Imagine?" (Score: 10/10)
- **Clip Window:** `00:09:42 → 00:10:22` (40s) | **Short Cut:** `00:09:57 → 00:10:18` (15s)
- **3s Hook:** 
  - *Audio:* Teacher: *"What did you see when you imagined the beach?"*
  - *Text Overlay:* *"When a 7-year-old imagines the ocean 🌊"*
- **Dialogue:** Student lists sharks, crabs, seaweed, and shouting *"OCTOPUS!"* with wild hand gestures. Teacher laughs warmly in surprise.
- **Editor Directions:** 9:16 split-screen. Highlight student hand gestures. Add subtle 15% ocean wave ambience.

### 🎬 Ad Brief 2: Gita — "Prayer Gives You Bravery" (Score: 10/10)
- **Clip Window:** `00:26:46 → 00:27:35` (49s) | **Short Cut:** `00:26:46 → 00:27:01` (15s)
- **3s Hook:** 
  - *Audio:* Teacher direct to camera: *"Why do you think we pray to God? What do you think it does?"*
  - *Text Overlay:* *"The real reason we teach children to pray 🙏"*
- **Dialogue:** Teacher explains Markandeya wasn't scared because prayer gave him bravery. Student realizes: *"Because, because he is brave!"*
- **Editor Directions:** Sincere, calm close-up on educator. Hold 1s thinking pause before student speaks. Soft tanpura/flute bed.

### 🎬 Ad Brief 3: Science — "Horse vs. Tractor Energy" (Score: 10/10)
- **Primary Ad Cut (Target 15–45s):** `00:05:20 → 00:06:05` (**45 seconds**) | **WhatsApp Cut:** `00:05:40 → 00:05:55` (15s)
- **Full Source Window (Editor Ingest):** `00:04:58 → 00:06:12` (74 seconds)
- **3s Hook:** 
  - *Audio:* Teacher: *"Look at the tractor! From where does the tractor get energy?"* → Student: *"The engine!"*
  - *Text Overlay:* *"Grade 2 Science: Why can't a tractor move on its own? 🐴🚜"*
- **Dialogue:** Teacher contrasts external forced energy (engine) with living self-propelled energy (horse running on its own).
- **Editor Directions:** Split frame with educator webcam and motion graphic illustration. Punchy typography for `SELF-PROPELLED`.

---

## Deliverable D — Business Impact & 30-60-90 Day Rollout

### D1. Unit Economics (500 Classes / Week)

| Operating Metric | Manual Process | AI Pipeline | Net Efficiency Gain |
|---|---|---|---|
| **Review Time per Class** | 45 minutes | 8 minutes | **5.6x faster review** |
| **Weekly Editor Hours** | 375 hours | 67 hours | **308 hrs saved/week (82%)** |
| **FTE Editors Required** | 9–10 editors | 2 editors | **7–8 FTEs freed up** |
| **Monthly Team Labor Cost** | ₹3,15,000 – ₹3,50,000 | ₹70,000 | **₹2.45L–₹2.8L salary saved** |
| **Monthly AI/API Tooling** | ₹0 | ~₹22,500 ($270) | Tooling investment |
| **Net Monthly Savings** | — | — | **₹2,22,500 – ₹2,57,500 / month** |

---

### D2. 30-60-90 Day Phased Rollout Plan

- **Days 1–30 (Pilot & Safety Gate):** Connect n8n + AssemblyAI; calibrate GPT-4o Mini safety filters across 50 historical classes; target False Positive Rate < 20%; zero safety escapes.
- **Days 31–60 (Team Training & Scale):** Onboard 4 editors to Airtable Kanban; implement reject tagging (`Poor Audio`, `Weak Hook`); scale to 150 classes/week; launch 20 test creatives on Meta/YouTube.
- **Days 61–90 (Full Autopilot & Optimization):** Scale to all 500 classes/week; automate FFmpeg timestamp trimming; achieve False Positive Rate < 10%; lock in SOPs.

---

### D3. Quality Assurance & Overcoming Skepticism

- **Editor Empowerment:** AI is positioned as a junior researcher doing the tedious scrubbing; video editors retain 100% creative approval.
- **False Positive Tracking:** Every rejected clip logged with cause in Airtable to continuously fine-tune prompt weights.
