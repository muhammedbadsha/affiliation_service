from fastapi import APIRouter






routers = APIRouter()


@routers.get('/')
def get_another_value():
    return 'valuesadfmksdf'