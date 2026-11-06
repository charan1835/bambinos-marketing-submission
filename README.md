# Bambinos.live — AI Program Manager (Marketing) Take-Home Assessment
## Live Class → Scroll-Stopping Ad Pipeline

**Candidate:** Charan  
**Track:** Marketing (Live Class → Scroll-Stopping Ad Pipeline)  
**Submission Date:** November 2026  
**Repository:** [https://github.com/charan1835/bambinos-marketing-submission](https://github.com/charan1835/bambinos-marketing-submission)

---

## 📌 Executive Overview

Bambinos.live runs thousands of live, small-group online classes every week across India, GCC, and International markets. While unscripted 10–20 second classroom captures generate our highest-converting paid social ads, video editors currently waste **85–90% of their time manually scrubbing through 50-minute recordings**.

This repository contains the end-to-end design, production-grade prompts, automation workflow scripts, visual verification logs, and extracted ad briefs for an **AI-powered Content Mining & Production Pipeline** that accelerates this process by **10x** while enforcing strict brand safety and child privacy guardrails.

---

## 📁 Repository Structure

```
bambinos-marketing-submission/
├── README.md                                  # Executive summary & navigation guide
├── CASE_REPORT.md                             # Comprehensive report covering Deliverables A, B, C & D
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

## 🎯 Deliverables Summary

### Deliverable A: Creative Taxonomy & Scoring Rubric
- **Competitor Benchmark:** Detailed audit of PlanetSpark, Bhanzu, Vedantu, BrightChamps, and Outschool.
- **The 6 Moment Buckets:**
  1. 🌟 **Breakthrough** (Cognitive click moment)
  2. 🤩 **Wonder & Delight** (Spontaneous excitement & awe)
  3. 💡 **Great Teaching** (High-craft pedagogical analogies)
  4. 🔍 **Curiosity Spark** (Unexpected student questions)
  5. ❤️ **Warm Connection** (Educator empathy & encouragement)
  6. 🏆 **Outcome Demonstration** (Concrete skill mastery)
- **10-Point Scoring Rubric:** `Emotional Pull (3) + Clarity (2) + Relatability (2) + Visual (2) + Brand Safety (1)`.
- **Zero-Tolerance Hard Exclusions:** Child PII, visible background privacy leaks, and educator hostility.

---

### Deliverable B: Workflow Architecture & Audio vs. Visual Gap
- **8-Stage Pipeline:** Zoom Ingest ➔ AssemblyAI Diarization ➔ PII/Tone Gate ➔ Claude 3.5 Mining ➔ Rubric Scoring ➔ Twelve Labs Visual QA ➔ FFmpeg Pre-cut ➔ Airtable Editor Kanban.
- **Solving the Audio vs. Visual Gap:** Automated verification protocol using Twelve Labs Pegasus API to check `face_visibility_ratio > 0.8` and identify visual anomalies (such as educators answering doors or dark lighting).

---

### Deliverable C: Real Dataset Evaluation & Top Ad Briefs

All 4 official repository sessions were thoroughly processed:

| Session ID | Subject | Educator | Student Status | Assessment Outcome | Video QA |
|---|---|---|---|---|---|
| `2125604619` | English | Mridula Bose | Student [Masked] | ✅ **Mined** — Hero Ad (10/10) | PASS |
| `2125422751` | Gita (Little Yogi) | Nancy Shukla | Student [Masked] | ✅ **Mined** — Hero Ad (10/10) | PASS |
| `2125687282` | Science | Mary James Mekkattel | Student [Masked] | ✅ **Mined** — Hero Ad (10/10) | PASS |
| `2125736982` | Maths | Naazish Khanam | Student [Masked] | ❌ **100% Disqualified** (Negative Tone) | FAIL |

> **⚠️ Critical Brand Safety Case Study — Maths Disqualification:**  
> The Maths session exhibited multiple instances of severe pedagogical frustration (`"It's stupid. Where is your focus?"` at `00:25:17`; `"Silly simple thing you are not understanding"` at `00:37:40`; `"This way I will not teach you"` at `00:38:14`). Under our safety rubric, the session scored **0/1 on Brand Safety** and was immediately blocked from creative pipelines.

#### Hero Ad Highlights:
1. **English (`00:09:42 – 00:10:30`):** Unscripted beach imagination — child listing crabs, seaweed, and octopus with wide gestures.
2. **Gita (`00:26:46 – 00:27:35`):** Calm educator delivery explaining how prayer creates bravery, followed by student's cognitive realization.
3. **Science (`00:03:49 – 00:04:35`):** Clear living vs. non-living analogy comparing internal horse energy with an external tractor engine.

---

### Deliverable D: Business Impact & 30-60-90 Day Rollout
- **Unit Economics (at 500 classes/week):**
  - Editor review hours reduced from **375 hrs/week to 67 hrs/week** (**82% reduction**).
  - Required editing capacity drops from **9–10 FTEs to 2 FTEs**.
  - **Net Monthly Savings: ₹2,22,500 – ₹2,57,500/month** (factoring in all transcription and LLM API costs).
  - Creative output scales from **50–70 clips/month to 180–220 clips/month** (~3x acceleration).
- **Rollout Strategy:**
  - **Days 1–30:** Infrastructure build, negative-tone threshold calibration, pilot on 50 classes.
  - **Days 31–60:** Editor onboarding, Airtable rejection tagging, Meta/YouTube A/B testing.
  - **Days 61–90:** Full scale to 500 classes/week, automated FFmpeg pre-cutting, `< 10%` false positive rate.

---

## 🛠️ How to Inspect & Run the Prototype

1. **Review Prompts:** See [`prompts/`](./prompts/) for production system prompts with XML constraints.
2. **Inspect Cleaned Data:** See [`results/clean_transcripts/`](./results/clean_transcripts/) for PII-masked dialogue and safety audit logs.
3. **Inspect Output Tables:** See [`results/moment_extraction.csv`](./results/moment_extraction.csv) and [`results/scored_moments.csv`](./results/scored_moments.csv).
4. **Inspect Editor Briefs:** See [`results/ad_briefs/`](./results/ad_briefs/) for detailed 3s hooks, captions, and editor instructions.
5. **Run Script:**
   ```bash
   python workflows_or_scripts/pipeline.py
   ```
