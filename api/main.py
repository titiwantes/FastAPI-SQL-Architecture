import fastapi
import fastapi.middleware
import fastapi.middleware.cors

import api.routers.users_router as users

app = fastapi.FastAPI()

app.include_router(users.router)

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
