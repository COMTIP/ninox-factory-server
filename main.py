from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
import zeep

app = FastAPI()

# WSDL de The Factory HKA (usa el de producción si tienes acceso)
wsdl = 'https://demoemision.thefactoryhka.com.pa/ws/obj/v1.0/Service.svc?singleWsdl'

@app.post("/enviar-factura")
async def enviar_factura(request: Request):
    datos = await request.json()
    # Agregar tokens obligatorios
    datos['tokenEmpresa'] = "hqavyygdygrn_tfhka"
    datos['tokenPassword'] = "@&Si-&7m/,dy"
    try:
        cliente = zeep.Client(wsdl=wsdl)
        res = cliente.service.Enviar(**datos)
        print("RESPUESTA REAL DEL WEBSERVICE:", res)
        # Devuelve la respuesta SOAP real a Ninox o a tu frontend
        return JSONResponse({"respuesta": str(res)})
    except Exception as e:
        print("ERROR:", e)
        return JSONResponse({"error": str(e)}, status_code=500)
