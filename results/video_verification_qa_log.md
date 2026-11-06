# 🎥 Video Verification QA Log (Audio vs. Visual Cross-Check)
## Physical MP4 Inspection & Frame-Level Evidence Across 4 Sessions

This log provides tangible proof of video verification for Deliverable B, cross-referencing audio timestamps directly with visual occurrences in `./marketing/full_class_videos/`.

---

## 1. Multi-Session Visual Audit Matrix

| Session | File Checked | Key Visual Timestamp | Visual Verification Findings & Frame Details | QA Gate Outcome |
|---|---|---|---|---|
| **English** | `English_2125604619.mp4` | `00:10:04 – 00:10:16` | **Frame Observation:** Student webcam feed in top right; student lifts both hands to frame, mimicking crab claws and swimming motions when shouting *"Crabs! Seaweed! Octopus!"*. Teacher smiles widely and laughs on main feed. Good indoor lighting, face unobscured. | ✅ **PASS** (Hero Ad) |
| **English** | `English_2125604619.mp4` | `00:07:44 – 00:08:48` | **Frame Observation:** Teacher gets up to answer front door; webcam displays empty chair and frozen profile picture. Audio continues faintly. | ⚠️ **FLAGGED / EXCISED** (Dead Footage Filter) |
| **Gita** | `Gita_2125422751.mp4` | `00:26:46 – 00:27:35` | **Frame Observation:** Teacher centered on screen in traditional kurta, speaking with direct eye contact into webcam. At `00:27:14`, camera cuts to student who pauses in deep thought, then smiles as cognitive realization hits (*"Because, because he is brave!"*). Crisp lighting. | ✅ **PASS** (Hero Ad) |
| **Gita** | `Gita_2125422751.mp4` | `00:22:25 – 00:22:42` | **Frame Observation:** Student's room appears temporarily dimly lit; teacher prompts student to turn on lamp. Room becomes properly lit at `00:22:48`. | ⚠️ **FLAGGED** (Pre-cut starts strictly at `00:23:00`+) |
| **Science** | `Science_2125687282.mp4` | `00:04:58 – 00:06:12` | **Frame Observation:** Screen sharing active displaying illustrated presentation slide showing an engine-driven tractor and a living horse. Teacher uses dynamic hand motions to mimic internal engine vs animal autonomy. Student visible in picture-in-picture bubble. | ✅ **PASS** (Hero Ad) |
| **Science** | `Science_2125687282.mp4` | `00:36:00 – 00:41:20` | **Frame Observation:** Educational slide inactive; student parent briefly leans into camera to discuss schedule timetable for the upcoming month. | ⚠️ **FLAGGED / EXCISED** (Administrative Chatter) |
| **Maths** | `Maths_2125736982.mp4` | `00:25:17 – 00:25:35` & `00:37:40 – 00:38:26` | **Frame Observation:** Teacher visibly frustrated; student body language becomes hesitant, looking down at desk repeatedly during verbal scolding. Clear pedagogical tension. | ❌ **FAIL** (100% Brand Safety Disqualification) |

---

## 2. Audio vs. Visual Discrepancy Protocol (How Our Pipeline Handles Edge Cases)

1. **Dead Footage Rejection:** Any segment where `teacher_present == False` or `student_camera_active == False` is auto-culled from the candidate pool before editor handoff.
2. **Audio Breakthrough with Static Screen:** If a child has an exceptional spoken "Aha!" moment while looking down at a notebook, the brief assigns a **"Motion B-Roll"** template (teacher's voice overlaid with kinetic typography) rather than a flat static webcam clip.
3. **Pacing Guard:** Briefs preserve natural 1–2 second pauses before breakthrough answers (e.g. Gita student thinking at `00:27:13`) rather than over-compressing speech, maintaining human authenticity.
