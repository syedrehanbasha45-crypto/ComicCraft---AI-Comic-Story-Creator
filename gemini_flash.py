import os, json
import google.generativeai as genai

def generate_outline(story_prompt, character_name, setting, tone, art_style):
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        return demo_outline(story_prompt, character_name, setting, tone, art_style)

    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
Create exactly 5 comic panels in JSON.
Story prompt: {story_prompt}
Main character: {character_name}
Setting: {setting}
Tone: {tone}
Art style: {art_style}

Return ONLY a JSON array. Each item must contain:
panel_number, title, scene_description, image_prompt.
"""
    response = model.generate_content(prompt)
    text = response.text.strip().replace("```json","").replace("```","")
    return json.loads(text)

def demo_outline(story_prompt, character_name, setting, tone, art_style):
    return [
        {"panel_number":1,"title":"The Beginning","scene_description":f"{character_name} begins the adventure in {setting}.","image_prompt":f"{character_name} in {setting}, {art_style} comic style"},
        {"panel_number":2,"title":"A Strange Discovery","scene_description":f"{character_name} discovers something unexpected.","image_prompt":f"{character_name} making a mysterious discovery in {setting}, {art_style} comic style"},
        {"panel_number":3,"title":"The Challenge","scene_description":"A difficult challenge appears.","image_prompt":f"{character_name} facing a dramatic challenge in {setting}, {art_style} comic style"},
        {"panel_number":4,"title":"The Turning Point","scene_description":f"{character_name} finds the courage to continue.","image_prompt":f"{character_name} showing courage, dramatic scene, {art_style} comic style"},
        {"panel_number":5,"title":"A New Beginning","scene_description":"The adventure reaches a hopeful ending.","image_prompt":f"{character_name} celebrating a hopeful ending in {setting}, {art_style} comic style"}
    ]
