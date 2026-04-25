from fastapi import FastAPI
from database import engine, Base
from router import router 
from fastapi.openapi.docs import get_swagger_ui_html
app = FastAPI(title="I-Phone Sales API", version="1.0.0",docs_url=None)

# Create tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(router)

# Custom Swagger UI
@app.get("/", include_in_schema=False)
def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="iPhone Sales API Dashboard",
        swagger_favicon_url="https://cdn-icons-png.flaticon.com/128/831/831278.png",
    )