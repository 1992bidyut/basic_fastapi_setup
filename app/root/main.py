from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.root.api_router import router
from app.root.configs import settings
import uvicorn


def get_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
    origins = [
        'http://localhost:3000',
        settings.FRONTEND_HOST,
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)
    return app


app = get_application()


@app.get("/")
async def read_root():
    """Main function of the web application

    Returns:
        List -- Hello World
    """
    return {"welcome": "Welcome to the ZeroLoop. "
                       "We are working to the create new trading process for bangladesh agro markets"}


if __name__ == "__main__":
    uvicorn.run('app.main:app', host="0.0.0.0", port=9000, reload=True)
