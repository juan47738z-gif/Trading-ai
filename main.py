from fastapi import FastAPI, UploadFile
import base64
import requests

app = FastAPI()

OPENAI_API_KEY = "AQUI_TU_API_KEY"

@app.post("/scan-chart")
async def scan_chart(image: UploadFile):
    img_bytes = await image.read()
    img_b64 = base64.b64encode(img_bytes).decode()

    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "user",
             "content": [
                 {"type": "text", "text": "Analiza este gráfico de trading y dame la tendencia, soportes, resistencias y patrón."},
                 {"type": "image_url", "image_url": f"data:image/png;base64,{img_b64}"}
             ]}
        ]
    }

    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}

    r = requests.post("https://api.openai.com/v1/chat/completions",
                      json=payload, headers=headers)

    return r.json()
