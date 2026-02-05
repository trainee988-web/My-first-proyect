Analyze the audio transcript: {resultado['text']} and generate ONLY clearly separated slides following these STRICT rules.

!!! CRITICAL: LANGUAGE ENFORCEMENT !!!
1. FIRST, analyze the input text to identify the source language exactly.
2. YOUR OUTPUT MUST BE 100% IN THAT IDENTIFIED SOURCE LANGUAGE.
3. IF the audio is in English -> Generate slides/notes in ENGLISH.
4. DO NOT translate.

=== BEGIN DESIGN & CONTENT INSTRUCTIONS ===

1. MANDATORY MULTI-SLIDE RULE (CRITICAL)
- You MUST generate EXACTLY 5 SLIDES.
- Each slide MUST represent only ONE sub-topic of the transcript.
- If the transcript is brief, you MUST expand the content with your knowledge to reach the 5-slide requirement.
- NEVER put all information in one single slide or block.

2. SEPARATION FORMAT
- You MUST use the following separator between slides:
--- SLIDE N ---
(Where N is the slide number from 1 to 5).

3. SLIDE STRUCTURE (MANDATORY & CLEAN)
Each slide MUST follow this exact internal structure. DO NOT add "Visual Concepts" or extra text inside the slide body.

# [INSERT RELEVANT EMOJI] TITLE OF THE SLIDE

🔹 **[Keyword]:** [Brief explanation]
🔸 **[Keyword]:** [Brief explanation]
🔹 **[Keyword]:** [Brief explanation]

notes_slide:
Full, natural speaker notes written as if a real presenter were explaining the slide aloud.
THE NOTES MUST BE IN THE SAME LANGUAGE AS THE TRANSCRIPT.

4. FORMATTING RULES
- Use Emojis (🔹, 🔸) as bullet points.
- ALWAYS bold the key concept at the start.
- Max 2 lines per bullet point.
- Keep the slide body clean; only the Title and the 3 bullet points.

5. OUTPUT RESTRICTIONS
- DO NOT generate a single summary slide.
- DO NOT mix content from different topics in one slide.
- DO NOT include "Visual Concept" descriptions in the body.
