from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
import zeep

app = FastAPI()

wsdl = 'https://demoemision.thefactoryhka.com.pa/ws/obj/v1.0/Service.svc?singleWsdl'

@app.post("/enviar-factura")
async def enviar_factura(request: Request):
    datos = await request.json()
    datos['tokenEmpresa'] = "hqavyygdygrn_tfhka"
    datos['tokenPassword'] = "@&Si-&7m/,dy"
    try:
        cliente = zeep.Client(wsdl=wsdl)
        res = cliente.service.Enviar(**datos)
        # Devuelve SOLO un string (texto plano) para Ninox:
        return PlainTextResponse("Documento enviado correctamente")
        # Si quieres un poco más de info:
        # return JSONResponse({"mensaje": "Documento enviado correctamente", "respuesta": str(res)})
    except Exception as e:
        # Devuelve el error en texto plano
        return PlainTextResponse(f"ERROR: {e}", status_code=500)
