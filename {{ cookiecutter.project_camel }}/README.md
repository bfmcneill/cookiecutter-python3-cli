# {{ cookiecutter.project_camel }}


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
~/.local/share/virtualenvs/code-qa-Xg4J_/bin/python
```

### environment variables

- `settings.toml`
- `secrets.toml`

### entrypoint scripts

- `pcmd`