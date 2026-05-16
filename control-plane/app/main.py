from fastapi import FastAPI
app = FastAPI(title="TPS Control Plane")
@app.get('/healthz')
def healthz():
    return {'ok': True}
