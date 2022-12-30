"""
This File Imports all Route Files and Prepare The Endpoints with Prefix.
Each API Router takes a Router Object as First Argument and an optional Prefix as KWARGS.
"""
from fastapi import APIRouter
from app.routers.Parties import parties_router

router = APIRouter()


router.include_router(
        parties_router.api_router,
        prefix="/api/parties"
)


# api_router.include_router(
#         auth.router,
#         prefix="/o"
# )
# api_router.include_router(
#         users.router,
#         prefix="/api/users"
# )




