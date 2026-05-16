from fastapi import FastAPI
app = FastAPI(title="TPS Node Agent")
@app.get('/healthz')
def healthz():
    return {'ok': True}
