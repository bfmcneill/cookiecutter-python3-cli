from dynaconf import Dynaconf

ROOT_DIR = pathlib.Path(__file__).parents[2]
DATA_DIR = ROOT_DIR / "data"
SQL_DIR = ROOT_DIR / "sql"
NOTEBOOK_DIR = ROOT_DIR / "notebooks"
CONFIG_DIR = ROOT_DIR / "config"

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
