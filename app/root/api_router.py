"""
This File Imports all Route Files and Prepare The Endpoints with Prefix.
Each API Router takes a Router Object as First Argument and an optional Prefix as KWARGS.
"""
from fastapi import APIRouter
from app.routers.parties import parties_router
from app.routers.users import users_router
from app.routers.users import auth

router = APIRouter()

router.include_router(
        auth.api_router,
        prefix="/api/auth"
)
router.include_router(
        users_router.api_router,
        prefix="/api/users"
)
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




