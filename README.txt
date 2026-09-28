COMICCRAFT - BEGINNER SETUP

1. Install Python 3.11+ and VS Code.
2. Open this folder in VS Code.
3. Open Terminal.
4. Create environment:
   python -m venv env
5. Activate on Windows:
   env\Scripts\activate
6. Install packages:
   pip install -r requirements.txt
7. OPTIONAL: create .env and add your GEMINI_API_KEY.
8. Start:
   uvicorn app.main:app --reload
9. Open:
   http://127.0.0.1:8000

IMPORTANT:
The starter version includes a safe image placeholder so the website can run first.
After the basic app works, we can replace image_generator.py with Hugging Face Stable Diffusion.
