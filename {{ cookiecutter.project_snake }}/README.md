# {{ cookiecutter.project_snake }}

## getting started

```
pipenv install --dev
pipenv run pcmd
pipenv run pytest -v --tb=no
```

## docker

```
make init
```

### virtual environments

- python when not using pipenv

```bash
$ which python
$ /usr/local/bin/python
```

-- python when using pipenv

```bash
pipenv shell
which python
~/.local/share/virtualenvs/{{ cookiecutter.project_snake }}-venv/bin/python
```

### environment variables

- `settings.toml`
- `secrets.toml`

### entrypoint scripts

- `pcmd`