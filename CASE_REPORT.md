# Bambinos.live — AI Content Mining & Production Pipeline
## Case Report | Marketing AI PM Take-Home Assessment

**Candidate:** Charan
**Role:** AI Program Manager — Marketing | **Location:** Bengaluru (In-office)
**Track:** Marketing Problem Statement

---

## Executive Summary

Bambinos.live's creative marketing and video editing teams currently spend **85–90% of their time** manually scrubbing through 50-minute live class recordings to extract 10–20 second scroll-stopping moments for paid social ads. At a scale of 500 live classes per week, this represents **375 editor-hours wasted weekly** on dead footage review.

This case report presents an end-to-end **AI-Powered Content Mining & Production Pipeline** that reduces review time per class from ~45 minutes to ~8 minutes — an **82% reduction in manual effort** (saving ~₹2.35L per month) — while establishing rigorous brand safety gates, a 6-bucket creative taxonomy, quantitative rubric scoring, and an automated solution to bridge the "Audio vs. Visual" verification gap.

---

## Deliverable A — Research & Taxonomy ("What Makes a Scroll-Stopping Clip?")

### A1. Market & Competitor Research

We inspected ad campaigns from leading EdTech players (PlanetSpark, Bhanzu, Vedantu, BrightChamps, Outschool) on Meta Ad Library and YouTube Shorts:

| Competitor | Hook & Content Strategy | What Actually Converts Parents | Critical Flaw / Gap Bambinos Exploits |
|---|---|---|---|
| **PlanetSpark** | Student speeches, debate snippets, Hinglish dialogue | High relatability, spontaneous child personality | Inconsistent audio quality; lack of structured moment taxonomy; high ad fatigue |
| **Bhanzu** | Speed math tricks, child solving equations under pressure | Immediate proof of cognitive outcome | Feels high-stress and test-prep focused; lacks warmth and joy |
| **Vedantu** | WAVE AI clips, educator lecturing highlights | Professional visual production | Teacher-monologue heavy; scrolling parents cannot picture their child in it |
| **BrightChamps** | Tech/Coding output showcases, student app demos | Tangible project results | Scripted and artificial; lacks authentic classroom emotion |
| **Outschool (US)** | Parent reactions + unscripted classroom joy | High emotional trust and social proof | Culturally Western-centric; lacks diaspora & Indian value alignment |

**The Strategic Opportunity:** Authentic, unscripted classroom "Aha!" moments where a child's natural wonder and cognitive breakthroughs shine through live 1-on-1 and small-group engagement.

---

### A2. The 6 Moment Buckets (Creative Taxonomy)

| # | Bucket | Definition & Emotional Trigger | Why Parents Stop Scrolling | Real Dataset Evidence |
|---|---|---|---|---|
| **1** | 🌟 **Breakthrough** | Sudden cognitive clarity — student connects dots independently without teacher feeding the answer. | Proof of learning: *"My child could master difficult concepts like that."* | **Gita:** Student pauses, connects Markandeya's prayer to bravery: *"Because, because he is brave!"* (`00:27:15`) |
| **2** | 🤩 **Wonder & Delight** | Spontaneous outburst of joy, curiosity, or awe about the subject matter. | High emotional hook: Learning is fun, not a chore. | **English:** Student excitedly lists ocean animals: *"Crabs! Seaweed! OCTOPUS!"* (`00:10:06`) |
| **3** | 💡 **Great Teaching** | Teacher delivers a masterclass analogy or reframes an abstract idea into everyday language. | Institutional trust: *"I want an educator this skilled for my child."* | **Science:** Teacher contrasts internal horse energy vs. external tractor ignition (`00:03:49`) |
| **4** | 🔍 **Curiosity Spark** | Child asks a surprisingly sharp, quirky, or deep question. | Relatability: Parents recognize their own curious child. | **Science:** Student investigates touch-me-not plant sensitivity vs. snapping dead twig (`00:17:30`) |
| **5** | ❤️ **Warm Connection** | Genuine emotional warmth, encouraging validation, and educator empathy. | Safety & emotional care in online environments. | **English:** Teacher forgives student's distraction warmly: *"I'm taking away my anger. Good boy."* (`00:32:09`) |
| **6** | 🏆 **Outcome Demonstration**| Child demonstrates structural mastery (e.g. story arc, recitation). | Concrete return on investment for the parent. | **English:** Student recites Story Mountain structure unprompted (`00:14:41`) |

---

### A3. Quantitative Scoring Rubric (Out of 10)

Every extracted candidate moment is scored across 5 dimensions:

$$\text{Total Score} = \text{Emotional Pull (3)} + \text{Clarity (2)} + \text{Relatability (2)} + \text{Visual Potential (2)} + \text{Brand Safety (1)}$$

* **Emotional Pull (0–3 pts):** Does it spark an immediate emotional response (laugh, awe, inspiration)?
* **Clarity Out-of-Context (0–2 pts):** Can a parent scrolling on mute understand the premise within 3 seconds?
* **Relatability (0–2 pts):** Does the interaction resonate universally with parents across India, GCC, and International markets?
* **Visual Potential (0–2 pts):** Is the child's facial reaction dynamic and expressive (not static or camera-off)?
* **Brand Safety Gate (0 or 1 pt):** Binary multiplier. **If 0, the moment is immediately disqualified.**

#### Action Thresholds:
- **Score 10/10:** **Hero Ad Candidate** — Immediate fast-track to video editing for paid Meta/YouTube campaigns.
- **Score 8–9/10:** **Supporting Creative** — Organic social clips, WhatsApp remarketing sequences, and mid-funnel proof.
- **Score < 8/10:** **Archive** — Insufficient hook strength; stored in content repository for training.

---

### A4. Hard Exclusions & Compliance Red Flags

#### 🔴 Hard Exclusions (Immediate Session Disqualification)
1. **Child PII (Privacy):** Any spoken or visible child surname, school name, residential city/address, or contact information. (All first names masked in public materials).
2. **Negative Educator Tone / Shaming:** Any verbal frustration, sarcastic reprimands, defeatist language, or punitive remarks.
3. **Child Distress / Discomfort:** Visible embarrassment, crying, reluctance, or parental coercion.
4. **Third-Party Copyright / Background Distractions:** Visible copyrighted media playing in the background or family members entering frame without consent.

#### ⚠️ Case Study: Disqualification of the Maths Session (`Maths_2125736982`)
During automated filtering, the Maths class was flagged for multiple severe pedagogical and tone violations:
- `00:25:17`: *"It's stupid. I explained it taking 5-10 minutes. Then also you, where is your focus?"*
- `00:37:40`: *"Silly simple thing you are not understanding... Not at all studying at home."*
- `00:38:14`: *"This way I will not teach you... This is enough."*
- `00:45:38`: *"From the next time you will score full zero."*

**Action Taken:** Under Bambinos.live Brand Safety Policy, this entire session was **100% excluded** from ad production. A safety alert was routed to Academic Ops for educator coaching.

---

## Deliverable B — End-to-End Workflow & SOP Design

### B1. Pipeline Architecture: Class Recording Ends → Final Creative Handoff

```
[Zoom Cloud Class Recording Ends]
               │
               ▼
   [Step 1: Ingest & Storage]
   • Webhook triggers n8n workflow upon Zoom MP4 completion
   • Raw MP4 & WAV stored in secure S3/GCS bucket
               │
               ▼
   [Step 2: Diarization & Transcription]
   • AssemblyAI / Deepgram Nova-2 transcribes audio with Speaker Diarization
   • Generates timestamped speaker segments: [Teacher] vs [Student]
               │
               ▼
   [Step 3: PII Masking & Safety Gate Filter]
   • Prompt 01 (GPT-4o Mini) scans dialogue for PII and negative educator tone
   • Session Gate: Hostile tone flags (e.g. Maths) disqualify the entire session
               │
               ▼
   [Step 4: AI Moment Mining & 6-Bucket Categorization]
   • Prompt 02 (Claude 3.5 Sonnet) parses safe transcripts
   • Identifies 15–45s candidate moments aligned with the 6 taxonomy buckets
               │
               ▼
   [Step 5: Quantitative Scoring Rubric]
   • Automated scoring engine evaluates moments on the 10-point rubric
   • Moments scoring >= 8/10 proceed to visual verification
               │
               ▼
   [Step 6: Multimodal Video Verification (Twelve Labs / Pegasus API)]
   • Solves the "Audio vs Visual Gap" (checks student face, lighting, screen activity)
   • Video verification QA log generated
               │
               ▼
   [Step 7: Automated Ad Brief Generation & Pre-Cut Clips]
   • Prompt 03 formats 3-second hook, platform cuts (Reels/Shorts/WhatsApp), and editor notes
   • FFmpeg automated worker cuts lossless MP4 preview clips based on timestamps
               │
               ▼
   [Step 8: Video Editor Dashboard Handoff]
   • Delivered to Airtable Kanban board:
     1. Pre-cut preview video
     2. Structured ad brief & hook options
     3. Editor instruction checklist
```

---

### B2. Tooling Stack Specification

| Stage | Tool | Function in Pipeline | Key Advantage |
|---|---|---|---|
| Orchestration | **n8n** | Event-driven workflow orchestrator | Self-hostable, low cost, seamless API integrations |
| Speech-to-Text | **AssemblyAI** | Speaker diarization & timestamp generation | Superior accuracy with Indian accents & children's voices |
| Filtering & Masking | **GPT-4o Mini** | PII masking & negative tone detection | High speed, cost-effective ($0.15/1M tokens) |
| Moment Mining | **Claude 3.5 Sonnet** | Deep pedagogical & narrative mining | Industry-leading reasoning for conversational context |
| Visual QA Engine | **Twelve Labs Pegasus API** | Multimodal video inspection | Validates facial presence, lighting, and expressions |
| Automated Pre-trim | **FFmpeg Script** | Headless video extraction | Zero-latency lossless cutting at exact timestamps |
| Editor Handoff | **Airtable** | Central creative ops repository | Non-technical interface for video editors & marketers |

---

### B3. Solving the "Audio vs. Visual" Gap

Transcripts only record spoken words. In reality:
- A child might say something brilliant while their camera is turned off or covered.
- A visual demonstration (e.g. educator holding up a prop or slide game) has no transcript equivalent.
- A student might be distracted, yawn, or look away during an otherwise good quote.

#### The 3-Step Verification Protocol:
1. **Automated Facial & Pose Verification:** For every flagged timestamp, Twelve Labs Pegasus checks if `face_visibility_ratio > 0.8` and `lighting_quality == PASS`.
2. **Visual Anomaly Flagging:** Any segment where the teacher steps away from the camera (e.g. English teacher answering the doorbell at `00:07:44` and `00:23:13`) is automatically tagged as `VISUAL_ANOMALY` and excised.
3. **Editor Fallback Templates:**
   - **Scenario A (Face visible & expressive):** 9:16 vertical split-screen showing student reaction on top and teacher below.
   - **Scenario B (Visual is slide-based):** Picture-in-picture with teacher in an animated bubble overlaying dynamic slide graphics.

---

## Deliverable C — Prototype Outputs & Extracted Ad Briefs

### Overview of Evaluated Sessions

| Session | Subject | Educator | Student | Assessment Status | Video QA |
|---|---|---|---|---|---|
| `2125604619` | English | Mridula Bose | Student (Masked) | ✅ Analyzed & Mined | PASS |
| `2125422751` | Gita (Little Yogi) | Nancy Shukla | Student (Masked) | ✅ Analyzed & Mined | PASS |
| `2125687282` | Science | Mary James Mekkattel | Student (Masked) | ✅ Analyzed & Mined | PASS |
| `2125736982` | Maths | Naazish Khanam | Student (Masked) | ❌ Disqualified (Negative Tone) | FAIL |

---

### Extracted Hero Ad Briefs (Rank 1 — 10/10 Score)

#### 🎬 Ad Brief 1: English — "What Did You Imagine?" (Bucket: Wonder & Delight)
- **Session:** `English_2125604619` | **Timestamps:** `00:09:42 → 00:10:30` (Short Cut: `00:10:04 → 00:10:19`)
- **Score:** **10/10** (Emotional: 3, Clarity: 2, Relatability: 2, Visual: 2, Safety: 1)
- **3-Sec Hook:**
  - *Audio:* Teacher asks: *"What did you see when you went to the beach?"*
  - *Visual:* Student leans into camera with wide eyes.
  - *Text Overlay:* *"When a 7-year-old imagines the ocean 🌊"*
- **Verbatim Dialogue:**
  > **Teacher (00:09:42):** "What did you see when you imagined the beach? What did you see?"
  > **Student (00:09:57):** "Water and sun... and that animal's... fish! Sharks... don't fail? Fish..."
  > **Student (00:10:06):** "Crabs! A seaweed! OCTOPUS!" *(gestures wildly with hands)*
  > **Teacher (00:10:14):** *(laughing warmly)* "Octopus also you saw?! All in the beach playing around?!"
  > **Student (00:10:32):** "In the beach! Some of them are sent to sand, some of them are sent to water!"
- **Editor Instructions:** 9:16 vertical split. Highlight student's wild hand gestures at `00:10:06`. Cut to teacher's warm laugh. Add soft ocean wave sound at 15% volume. End card: *"Unscripted curiosity. Creative Writing at Bambinos.live | Book a Free Trial"*.
- **Platforms:** Instagram Reels (35s), YouTube Shorts (45s), WhatsApp Status (15s cut `00:10:04 → 00:10:19`).

---

#### 🎬 Ad Brief 2: Gita — "Prayer Gives You Confidence & Bravery" (Bucket: Great Teaching & Breakthrough)
- **Session:** `Gita_2125422751` | **Timestamps:** `00:26:46 → 00:27:35` (Short Cut: `00:26:46 → 00:27:01`)
- **Score:** **10/10** (Emotional: 3, Clarity: 2, Relatability: 2, Visual: 2, Safety: 1)
- **3-Sec Hook:**
  - *Audio:* Teacher direct to camera: *"Why do you think we pray to God? What do you think it does?"*
  - *Visual:* Sincere, calm close-up of teacher; cut to student thinking.
  - *Text Overlay:* *"The real reason we teach children to pray 🙏"*
- **Verbatim Dialogue:**
  > **Teacher (00:26:46):** "The most important reason that we pray to God, because when we pray now, God gives us confidence. Look at Markandeya. His time was up, right? He could have feared the time God Yamdev, but he did not. Why do you think he was not scared of anyone?"
  > **Student (00:27:15):** *(eyes widen with realization)* "Because, because he is brave!"
  > **Teacher (00:27:19):** "Because he is brave! And how do you think he became so brave? Because he prayed! He prayed to Lord Shiva himself."
  > **Teacher (00:27:35):** "So when you pray, you get to be brave, courageous, and full of confidence."
- **Editor Instructions:** 9:16 vertical crop. Full-frame focus on teacher's calm delivery. Hold the 1-second pause at `00:27:13` before student answers (*"Because he is brave!"*). Add gentle ambient flute/tanpura at 10% volume.
- **Platforms:** Instagram Reels (45s), YouTube Shorts (49s), WhatsApp Status (15s cut `00:26:46 → 00:27:01`).

---

#### 🎬 Ad Brief 3: Science — "The Horse vs. The Tractor" (Bucket: Great Teaching)
- **Session:** `Science_2125687282`
- **Primary Ad Cut (Target 15–45s):** `00:05:20 → 00:06:05` (**45 seconds**)
- **Full Source Window (Editor Ingest):** `00:04:58 → 00:06:12` (74 seconds)
- **WhatsApp Status Cut:** `00:05:40 → 00:05:55` (15 seconds)
- **Score:** **10/10** (Emotional: 3, Clarity: 2, Relatability: 2, Visual: 2, Safety: 1)
- **3-Sec Hook:**
  - *Audio:* Teacher: *"Look at the tractor! From where does the tractor get energy?"* → Student: *"The engine!"*
  - *Visual:* Split animation of galloping horse vs. key turning in a tractor ignition.
  - *Text Overlay:* *"Grade 2 Science: Why can't a tractor move on its own? 🐴🚜"*
- **Verbatim Dialogue (45s Primary Cut):**
  > **Teacher (00:05:20):** "From where does this tractor get the energy?"
  > **Student (00:05:24):** "The engine!"
  > **Teacher (00:05:25):** "From the engine! It's external! It's forced energy pushed from outside. But all living things have something known as self-propelled energy."
  > **Teacher (00:05:40):** "For example, the horse can decide when to run and where to go on its own! The tractor does not have that. The energy is forced from outside."
- **Editor Instructions:** 9:16 layout. Top 40% educator webcam; bottom 60% dynamic graphic. Emphasize words `SELF-PROPELLED` vs `FORCED ENERGY` in bold typography.
- **Platforms:** Instagram Reels (40s), YouTube Shorts (45s), WhatsApp Status (15s cut `00:05:40 → 00:05:55`).

---

## Deliverable D — Business Impact, Metrics & 30-60-90 Day Rollout

### D1. Unit Economics & Time Saved (At 500 Live Classes / Week)

#### Manual Baseline vs. AI Pipeline Comparison

| Operating Metric | Manual Process (Current) | AI-Powered Pipeline (Proposed) | Net Efficiency Gain |
|---|---|---|---|
| Scrubbing & Review Time per Class | 45 minutes | 8 minutes (Verification only) | **5.6x faster review** |
| Total Weekly Review Hours (500 classes) | **375 hours / week** | **67 hours / week** | **308 hours saved / week (82%)** |
| Video Editors Required (Full-Time) | 9 to 10 editors | 2 editors | **7 to 8 FTEs freed up** |
| Monthly Team Labor Cost (@ ₹35,000/editor) | ₹3,15,000 – ₹3,50,000 | ₹70,000 (2 editors) | ₹2,45,000 – ₹2,80,000 saved |
| Monthly AI & API Infrastructure Cost | ₹0 | ~₹22,500 ($270 USD)* | Tooling investment |
| **Net Financial Savings** | — | — | **₹2,22,500 – ₹2,57,500 / month** |
| Ad-Worthy Creative Velocity | 50–70 clips / month | 180–220 clips / month | **~3x ad creative output** |

*\*API Cost breakdown: AssemblyAI audio transcription ($0.0065/min = $162.50) + GPT-4o Mini filtering ($25) + Claude 3.5 Sonnet mining ($50) + Pegasus visual spot checks ($32.50).*

---

### D2. 30-60-90 Day Rollout Plan

```
[Day 1–30: Pilot & Safety Baseline] ──▶ [Day 31–60: Team Integration & Scale] ──▶ [Day 61–90: Full Autopilot & Growth]
  • n8n + AssemblyAI pipeline setup      • Train 4 editors on Airtable queue      • Scale to all 500 classes/week
  • Calibrate Prompt 01 & 02 on 50 classes • Track False Positives & editor tags    • Automated FFmpeg pre-cutting
  • Target: False Positive Rate < 20%      • Target: False Positive Rate < 15%      • Target: False Positive Rate < 10%
  • Zero Brand Safety Escapes              • Paid Meta/YouTube A/B testing          • Full SOP handoff to Marketing Ops
```

#### 📅 Phase 1 (Days 1–30) — System Build & Safety Calibration
- **Goal:** Deploy core infrastructure and validate safety guardrails.
- **Actions:**
  - Build n8n webhook listener connected to Zoom Cloud recordings and S3 storage.
  - Implement AssemblyAI diarization and GPT-4o Mini PII/Tone filter.
  - Backtest prompts across 50 historical classes from English, Maths, Science, and Gita.
  - Establish baseline: ensure 100% of negative tone moments are flagged.
- **KPI:** Zero Brand Safety escapes; pipeline latency < 10 minutes per class.

#### 📅 Phase 2 (Days 31–60) — Team Onboarding & Feedback Loops
- **Goal:** Drive editor adoption, eliminate skepticism, and refine scoring thresholds.
- **Actions:**
  - Conduct hands-on workshop with video editing team: *"AI curates the candidate pool; editors make the creative call."*
  - Integrate Airtable Kanban dashboard where editors click `Approve`, `Reject`, or `Edit Timestamps`.
  - Introduce mandatory reject tagging (`Poor Video`, `Weak Hook`, `Pedagogical Lag`) to feed prompt calibration.
  - Scale from 50 to 150 classes/week. Launch first 20 AI-mined creatives on Meta Reels and YouTube Shorts.
- **KPI:** Editor adoption rate > 80%; False positive rate reduced from 20% to < 15%.

#### 📅 Phase 3 (Days 61–90) — Full Scale & Automated Production
- **Goal:** Process all 500 classes/week and automate clip trimming.
- **Actions:**
  - Connect headless FFmpeg service to automatically extract pre-cut MP4 clips at flagged timestamps.
  - Expand coverage to Chess and Coding tracks.
  - Run continuous A/B tests: AI-mined clips vs. legacy manually scrubbed clips (track 3s Hook Rate, Average Watch Time, and Cost Per Demo Booking).
  - Codify SOP documentation for continuous training of new educators and editors.
- **KPI:** 500 classes/week processed; False positive rate < 10%; Cost per finished ad brief < ₹150.

---

### D3. Quality Assurance & Managing Team Skepticism

#### Overcoming Editor Skepticism
1. **Positioning as a Superpower, Not a Replacement:** Frame the pipeline as an intelligent assistant that eliminates the mind-numbing 45-minute scrub, letting editors spend their energy on storytelling, sound design, and color grading.
2. **The "Blind Test" Alignment Session:** In Week 4, present editors with 10 unlabeled clips (5 chosen manually by senior marketers, 5 chosen by AI). Reviewing conversion potential together proves AI selection matches human editorial instinct.
3. **Editor Override Authority:** Editors hold 100% sign-off authority. No clip enters the paid ad account without human QA.

#### Ongoing QA & False Positive Tracking Framework
- **False Positive Rate (FPR):** 
  $$\text{FPR} = \frac{\text{Clips Rejected by Editors}}{\text{Total Clips Delivered by AI}} \times 100$$
- **Root Cause Categorization:** Every rejection is tagged in Airtable (`Mismatched Lip-Sync`, `Low Lighting`, `Pacing Too Slow`, `Boring Screen`).
- **Prompt Iteration Cadence:** Bi-weekly prompt weight adjustments based on rejection tag distributions.
