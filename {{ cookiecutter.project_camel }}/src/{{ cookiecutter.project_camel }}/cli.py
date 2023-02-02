import click


@click.command()
def main():
    click.echo("Hello, {{ cookiecutter.project_camel }}!")
