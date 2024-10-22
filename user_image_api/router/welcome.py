from fastapi import APIRouter

router = APIRouter()


@router.get('/', summary="User Image System API", status_code=200)
def welcome():
    return 'User Image System API - OK.'
