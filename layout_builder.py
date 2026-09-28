def build_comic_layout(outline, story, image_paths):
    layout = []
    for i, panel in enumerate(outline):
        layout.append({
            "panel_number": panel["panel_number"],
            "title": panel["title"],
            "scene_description": panel["scene_description"],
            "image_prompt": panel["image_prompt"],
            "image_path": image_paths[i],
            "text": story.get(str(panel["panel_number"]), "")
        })
    return layout
