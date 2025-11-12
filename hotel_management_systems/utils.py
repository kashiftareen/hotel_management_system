from pydantic_settings import BaseSettings
# Define a Settings class to manage environment variables
class Settings(BaseSettings):
    dburi:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    # Inner Config class tells Pydantic to load variables from the .env file
    class Config:
        env_file=".env"

settings=Settings()



