"""
Bambinos.live — AI Content Mining & Production Pipeline
Automated pipeline script to parse WebVTT transcripts, mask PII,
detect negative teacher tone, extract candidate moments, and output structured ad briefs.
"""

import re
import csv
import json
import os
from typing import List, Dict, Any

# 1. Negative tone indicator dictionary
NEGATIVE_TONE_PATTERNS = [
    r"\b(it's|is)\s+stupid\b",
    r"\bsilly\b",
    r"\bnot\s+teach\s+you\b",
    r"\bwhere\s+is\s+your\s+focus\b",
    r"\bcomplete\s+wastage\b",
    r"\bscore\s+(full\s+)?zero\b",
    r"\bdon't\s+study\s+at\s+home\b"
]

# 2. PII Replacement Map
PII_NAMES = [
    r"\bZyan\b", r"\bZian\b", r"\bZiyang\b",
    r"\bAnaya\b", r"\bMahato\b",
    r"\bManjare\b", r"\bShree\s*Shah\b", r"\bShirisha\b",
    r"\bDevnanda\b", r"\bArun\b"
]

def clean_and_mask_transcript(raw_vtt_text: str) -> Dict[str, Any]:
    """Strips timestamps/cue numbers, masks child names, and evaluates negative tone."""
    lines = raw_vtt_text.splitlines()
    cleaned_dialogue = []
    tone_flags = []
    
    # Simple regex for VTT cues
    cue_pattern = re.compile(r'^\d+$|^\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}|^WEBVTT', re.IGNORECASE)
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean or cue_pattern.match(line_clean):
            continue
        
        # Check negative tone
        for pattern in NEGATIVE_TONE_PATTERNS:
            if re.search(pattern, line_clean, re.IGNORECASE):
                tone_flags.append(line_clean)
        
        # Mask PII
        masked_line = line_clean
        for name_pattern in PII_NAMES:
            masked_line = re.sub(name_pattern, "Student", masked_line, flags=re.IGNORECASE)
            
        cleaned_dialogue.append(masked_line)
        
    is_safe = len(tone_flags) == 0
    return {
        "cleaned_text": "\n".join(cleaned_dialogue),
        "tone_flags_detected": len(tone_flags),
        "tone_flags": tone_flags,
        "is_safe_for_ads": is_safe
    }

def score_moment(emotional_pull: int, clarity: int, relatability: int, visual_potential: int, brand_safe: int) -> int:
    """Returns score out of 10 based on rubric."""
    if brand_safe == 0:
        return 0
    return emotional_pull + clarity + relatability + visual_potential + brand_safe

if __name__ == "__main__":
    print("Bambinos.live AI Content Mining Pipeline Initialized.")
