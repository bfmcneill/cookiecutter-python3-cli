import pathlib
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
)

settings.ROOT_DIR = pathlib.Path(__file__).parents[2]
settings.DATA_DIR = settings.ROOT_DIR / "data"
settings.SQL_DIR = settings.ROOT_DIR / "sql"
settings.NOTEBOOK_DIR = settings.ROOT_DIR / "notebooks"
settings.CONFIG_DIR = settings.ROOT_DIR / "config"
settings.LOG_DIR = settings.ROOT_DIR / "logs"
settings.TEMP_DIR = settings.ROOT_DIR / "temp"

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
