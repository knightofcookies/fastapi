# fastapi

API for a social media app built with FastAPI.

This project follows the FastAPI tutorial by Sanjeev Thiyagarajan available on the freeCodeCamp YouTube channel [here](https://www.youtube.com/watch?v=0sOvCWFmrtA).

Sanjeev's repository: <https://github.com/Sanjeev-Thiyagarajan/fastapi-course>

## Details

- This API uses a `PostgreSQL` database with `Alembic` and `SQLAlchemy`.
- There are four routes: `posts`, `users`, `auth` and `vote` 


## Requirements
- `Python 3.11`
- Packages in `requirements.txt`

## Usage
To reload every time you save changes, use
```commandline
uvicorn app.main:app --reload
```
I've noticed this breaks more often, especially if you use Auto Save on your IDE.

To reload manually, use
```commandline
uvicorm app.main:app
```

To use this API with a PostgreSQL database, include the following information in a `.env` file in the root directory of the project.

```env
DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_PASSWORD = passward_that_you_set
DATABASE_NAME = name_of_database
DATABASE_USERNAME = User_name
SECRET_KEY = 09d25e094faa2556c818166b7a99f6f0f4c3b88e8d3e7 
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 60(base)
```