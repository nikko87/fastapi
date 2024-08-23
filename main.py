import logging
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.iris_controller import router as iris_router
from controllers.jitsi_controller import router as jitsi_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

app.include_router(jitsi_router)
app.include_router(iris_router)
