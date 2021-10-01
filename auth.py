from fastapi import APIRouter, status, Depends
from databaseSQ import Session, engine
from schemas import SignUp, LoginModel
from model import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder


auth = APIRouter(
    prefix='/auth',
    tags=['auth']
)

session = Session(bind=engine)

@auth.get('/')
async def try_login(Authorize: AuthJWT = Depends()):
    '''
        ## Try this if you login
    '''
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid token')

    return {'massage': 'Hello User'}


@auth.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup(user: SignUp):
    """
            ## Create a user
            This requires the following
            ```
                    name: str
                    username:str
                    email:str
                    password:str
                    is_staff:bool
                    is_active:bool
            ```
        """

    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail='User with the email already exists')

    db_username = session.query(User).filter(User.username == user.username).first()

    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail='User with the username already exists')

    new_user = User(
        name = user.name,
        username = user.username,
        email = user.email,
        password = generate_password_hash(user.password),
        is_active = user.is_active
    )

    session.add(new_user)

    session.commit()

    return new_user


@auth.post('/login', status_code=status.HTTP_200_OK)
async def login(user: LoginModel, Authorize : AuthJWT = Depends()):

    db_user = session.query(User).filter(User.username == user.username)

    if db_user and check_password_hash(db_user.password, user.password):
        access_token = Authorize.create_access_token(subject=db_user.username)
        refresh_token = Authorize.create_refresh_token(subject=db_user.username)

        response = {
            'access': access_token,
            'refresh': refresh_token
        }

        return jsonable_encoder(response)

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail='Invalid Username Or Password')




