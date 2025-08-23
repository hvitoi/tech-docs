from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


# Attributes defined in the Settings class will be automatically populated with the correspondent environment variables
# It will throw in case the env is not defined and not assigned a default value
# Variables <-> Envs are case insensitive


class Settings(BaseSettings):
    app_name: str = "Henry's App"
    database_url: str = "sqlite:////tmp/myfastapi.db"  # absolute path; sqlite:///myfastapi.db for relative
    home: str  # automatically populated with $HOME

    # pick it from ".env" file (uncomment the model_config line)
    # SecretStr masks it for logging
    my_secret: SecretStr | None = None

    # Adds a new "source" for settings. To pick it from the ".env" file
    # model_config = SettingsConfigDict(env_file="app/.env", env_file_encoding="utf-8")


settings = Settings()
