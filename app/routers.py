from fastapi import APIRouter
from app.api import agents, auth


router = APIRouter()
api_prefix = "/api/v1"

router.include_router(agents.router, tags=["Agent"], prefix=api_prefix)
router.include_router(auth.router, tags=["Auth"], prefix=api_prefix)