import os
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from app.gemini_flash import generate_outline
from app.gemini_pro import generate_story
from app.image_generator import generate_image
from app.layout_builder import build_comic_layout
from app.exporters import save_pdf

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates_response(request, "index.html", {})

@router.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):
    try:
        outline = generate_outline(story_prompt, character_name, setting, tone, art_style)
        story = generate_story(outline, character_name, tone)
        layout = []

        for panel in outline:
            image_path = generate_image(panel["image_prompt"], art_style)
            layout.append({
                "panel_number": panel["panel_number"],
                "title": panel["title"],
                "scene_description": panel["scene_description"],
                "image_prompt": panel["image_prompt"],
                "image_path": image_path,
                "text": story.get(str(panel["panel_number"]), "")
            })

        pdf_path = save_pdf(layout)
        return templates_response(request, "comic_preview.html", {
            "layout": layout,
            "pdf_path": pdf_path
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def templates_response(request, template, context):
    from app.main import templates
    context["request"] = request
    return templates.TemplateResponse(
        request=request,
        name=template,
        context=context
    )
