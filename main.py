from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import zeep

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
