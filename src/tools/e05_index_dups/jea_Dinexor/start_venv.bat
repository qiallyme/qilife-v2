@echo off
python -m venv .venv
call .\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install flask lxml pillow pytesseract pdf2image