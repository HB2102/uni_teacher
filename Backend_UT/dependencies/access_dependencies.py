from authentication.access import get_current_user, get_current_admin, get_current_super_admin
from schemas.user_schemas import UserAuth
from typing import Annotated
from fastapi import Depends


USER_DEPENDENCY = Annotated[UserAuth, Depends(get_current_user)]
ADMIN_DEPENDENCY = Annotated[UserAuth, Depends(get_current_admin)]
SUPER_ADMIN_DEPENDENCY = Annotated[UserAuth, Depends(get_current_super_admin)]


ROUTER_USER_DEPENDENCY = Depends(get_current_user)
ROUTER_ADMIN_DEPENDENCY = Depends(get_current_admin)
ROUTER_SUPER_ADMIN_DEPENDENCY = Depends(get_current_super_admin)