# Bambinos.live — Marketing Track Submission
## Live Class → Scroll-Stopping Ad Pipeline

**Candidate:** [Your Name]
**Track:** Marketing
**Submitted:** November 2026

---

## 🎯 Solution Overview

This repository contains my end-to-end AI pipeline for mining "magic moments" from Bambinos.live live class recordings and converting them into scroll-stopping ad briefs for Instagram Reels, YouTube Shorts, and WhatsApp Status.

## 📁 Repository Structure

```
├── prompts/
│   ├── 01_pii_tone_filter_prompt.md     ← Filter for PII & negative teacher tone
│   ├── 02_moment_mining_prompt.md       ← AI prompt to extract magic moments
│   └── 03_ad_brief_prompt.md            ← Ad brief generation prompt
├── results/
│   ├── clean_transcripts/               ← Cleaned, PII-safe dialogue files
│   ├── moment_extraction.csv            ← All mined moments across 3 sessions
│   ├── scored_moments.csv               ← Ranked scoring table
│   └── ad_briefs/                       ← One .md file per ad brief
├── workflows_or_scripts/
│   └── pipeline_overview.md             ← Workflow architecture
└── Case_Report.pdf                      ← Compulsory case report
```

## 🚨 Key Decision: Maths Session Excluded

The Maths session (`Maths_2125736982.vtt`) was **fully excluded** from ad content generation due to multiple instances of negative teacher tone (frustration, harsh language directed at the child). Moments were mined from **English, Gita, and Science** sessions only.

## 📊 Sessions Analysed

| Session | Teacher | Student | Topic | Status |
|---|---|---|---|---|
| English | Mridula Bose | Zyan | Story Mountain / Beach Picnic Writing | ✅ Mined |
| Gita (Little Yogi) | Nancy Shukla | Anaya | Markandeya + Lord Shiva Story | ✅ Mined |
| Maths | Naazish Khanam | Manjare | Measurement & Length | ❌ Excluded (negative tone) |
| Science | Mary James Mekkattel | Devnanda | Signs of Life — Living vs Non-Living | ✅ Mined |

## 🎬 Ad Platforms Targeted
- Instagram Reels (9:16, 15–30 sec)
- YouTube Shorts (9:16, up to 60 sec)
- WhatsApp Status (15 sec clips)
