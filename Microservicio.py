from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

# Cambia esto por el endpoint real de The Factory HKA
FACTORY_URL = "https://the-factory-hka-endpoint.com/api/tu-endpoint"

@app.post("/webhook-ninox")
async def webhook_ninox(request: Request):
    try:
        payload = await request.json()
        print("Recibido de Ninox:", payload)  # Para debug en logs

        # Aquí puedes validar, ajustar, limpiar, etc. el payload si es necesario

        # Reenvía al endpoint real (opcionalmente puedes modificar el payload aquí)
        factory_response = requests.post(FACTORY_URL, json=payload)

        # Log de la respuesta de The Factory
        print("Respuesta de The Factory:", factory_response.text)

        # Devuelve la respuesta al cliente de Ninox (puedes customizar esto)
        return JSONResponse(
            status_code=factory_response.status_code,
            content={"ok": True, "respuesta_factory": factory_response.json()}
        )
    except Exception as e:
        print("ERROR:", e)
        return JSONResponse(status_code=400, content={"ok": False, "error": str(e)})
