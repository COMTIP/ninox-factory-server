from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import zeep

app = FastAPI()
wsdl = 'https://demoemision.thefactoryhka.com.pa/ws/obj/v1.0/Service.svc?singleWsdl'

@app.post("/enviar-factura")
async def enviar_factura(request: Request):
    try:
        datos = await request.json()
        print("DATOS RECIBIDOS:", datos) 
        datos['tokenEmpresa'] = "hqavyygdygrn_tfhka"
        datos['tokenPassword'] = "@&Si-&7m/,dy"
        cliente = zeep.Client(wsdl=wsdl)
        res = cliente.service.Enviar(**datos)
        print("RESPUESTA FACTORY:", res)
        return JSONResponse(content={"respuesta": str(res)})
    except Exception as e:
        print("ERROR:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)


