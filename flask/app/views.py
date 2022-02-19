from app import app

@app.route("/")
def index():
    return "<h1>Aqui uma página legal pra você!! =) https://github.com/MayconPCampos</h1>"
