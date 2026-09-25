import os
from pathlib import Path
from dotenv import load_dotenv

RAIZ_PROJETO = Path(__file__).resolve().parent.parent

load_dotenv(RAIZ_PROJETO / ".env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODELO = "gemini-3.5-flash"
TEMPERATURA = 0.3

if not GOOGLE_API_KEY:
    raise RuntimeError(
        f"GOOGLE_API_KEY não encontrada. Verifique se existe: {RAIZ_PROJETO / '.env'}"
    )