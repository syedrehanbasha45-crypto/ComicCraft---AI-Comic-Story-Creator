import os, json
import google.generativeai as genai

def generate_story(outline, character_name, tone):
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        return {str(p["panel_number"]): f"{character_name}: What an adventure! This is a {tone} moment in the story." for p in outline}

    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
Write narration and dialogue for these 5 comic panels.
Character: {character_name}
Tone: {tone}
Outline: {json.dumps(outline)}
Return ONLY JSON where keys are panel numbers and values are the text.
"""
    response = model.generate_content(prompt)
    text = response.text.strip().replace("```json","").replace("```","")
    return json.loads(text)
