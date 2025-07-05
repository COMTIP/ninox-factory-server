from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import zeep

app = FastAPI()

# CORS para aceptar requests desde Ninox/web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O reemplaza * por ["https://app.ninox.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

wsdl = 'https://demoemision.thefactoryhka.com.pa/ws/obj/v1.0/Service.svc?singleWsdl'

@app.post("/enviar-factura")
async def enviar_factura(request: Request):
    datos = await request.json()
    print("DATOS RECIBIDOS:", datos)  # Debug en logs Render
    datos['tokenEmpresa'] = "hqavyygdygrn_tfhka"
    datos['tokenPassword'] = "@&Si-&7m/,dy"
    try:
        cliente = zeep.Client(wsdl=wsdl)
        res = cliente.service.Enviar(**datos)
        return JSONResponse(content={"respuesta": str(res)})
    except Exception as e:
        print("ERROR:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/")
async def root():
    return {"mensaje": "API Ninox-Factory funcionando"}

