from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers import album, comment, image, lecture
import config.database as db

app = FastAPI()
app.include_router(album.router)
app.include_router(comment.router)
app.include_router(image.router)
app.include_router(lecture.router)

# database setup
db.Base.metadata.create_all(bind=db.engine)


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
        <html>
            <body>
                <a href="/docs">
                    goto api swagger page
                </a>
                <br><br>
                <a href="/redoc">
                    goto api document page
                </a>
            </body>
        </html>
    """
