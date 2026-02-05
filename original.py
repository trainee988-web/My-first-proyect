           Analyze the audio transcript: {resultado['text']} and generate ONLY clearly separated slides following these STRICT rules.

            !!! CRITICAL: LANGUAGE ENFORCEMENT !!!
            1. FIRST, analyze the input text to identify the source language exactly.
            2. YOUR OUTPUT MUST BE 100% IN THAT IDENTIFIED SOURCE LANGUAGE.
            3. IF the audio is in English -> Generate slides/notes in ENGLISH.
            4. IF the audio is in French -> Generate slides/notes in FRENCH.
            5. DO NOT translate to Spanish unless the audio is actually in Spanish.
            6. IGNORE the language of these instructions; follow ONLY the language of the transcript.

            === BEGIN INSTRUCTIONS ===

            1. TRANSCRIPTION
            Include the complete transcription of the audio.
            Write it ONLY in the original source language.
            Place it at the beginning under the heading:
            === TRANSCRIPTION ===

            2. INSTRUCTION DETECTION
            Determine whether the audio contains a clear instruction to create content.

            3. IF A CLEAR INSTRUCTION EXISTS
            Generate a presentation with a MINIMUM of 5 SLIDES.
            Each slide must be clearly separated and numbered.
            Each slide must represent a distinct idea or part of the requested content.

            Inside each slide:
            First line: Short Title
            Following lines: Bullet-point content only

            Use EXACTLY this separator:
            --- SLIDE N ---

            4. SLIDE STRUCTURE (MANDATORY)
            Each slide MUST follow this exact internal structure:

            Title
            • Bullet point
            • Bullet point

            notes_slide:
            Full, natural speaker notes written as if a real presenter were explaining the slide aloud.
            Notes must expand the slide content and provide context, explanations, or examples.
            *** THE NOTES MUST BE IN THE SAME LANGUAGE AS THE TRANSCRIPT ***

            5. IF NO CLEAR INSTRUCTION EXISTS
            Generate ONLY ONE slide.
            Clearly state (in the source language) that an explicit instruction is required in the audio.
            That slide MUST also include notes_slide.

            6. FORMAT RESTRICTIONS
            Speaker notes must appear ONLY inside notes_slide.
            Do NOT place notes in the slide body.
            Do NOT add explanations, comments, or text outside the defined structure.
            Output must be strictly structured for PowerPoint slide + notes usage.
            """
