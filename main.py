from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import zeep

app = FastAPI()

# --- CORS: Esto permite que Ninox y cualquier web pueda hacer POST, GET, OPTIONS, etc ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Puedes especificar ["https://app.ninox.com"] para mayor seguridad
    allow_credentials=True,
    allow_methods=["*"],          # Permitir todos los métodos (POST, OPTIONS, GET, etc)
    allow_headers=["*"],          # Permitir todos los headers
)
# ---------------------------------------------------------------------------------------

wsdl = 'https://demoemision.thefactoryhka.com.pa/ws/obj/v1.0/Service.svc?singleWsdl'

@app.post("/enviar-factura")
async def enviar_factura(request: Request):
    datos = await request.json()
    datos['tokenEmpresa'] = "hqavyygdygrn_tfhka"
    datos['tokenPassword'] = "@&Si-&7m/,dy"
    try:
        cliente = zeep.Client(wsdl=wsdl)
        res = cliente.service.Enviar(**datos)
        return PlainTextResponse("Documento enviado correctamente")
    except Exception as e:
        return PlainTextResponse(f"ERROR: {e}", status_code=500)

