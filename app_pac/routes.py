from app_pac import app_var

@app_var.route('/')
def index():
    return "REST API для сайта объявлений"