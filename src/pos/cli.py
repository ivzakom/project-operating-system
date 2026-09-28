import typer

app = typer.Typer(help="Project Operating System")


@app.command()
def init():
    """Initialize POS."""
    typer.echo("POS initialized")


@app.command()
def state():
    """Show current project state."""
    typer.echo("No project selected")


@app.command("continue")
def continue_():
    """Run the next allowed POS action."""
    typer.echo("Control loop is not implemented yet")


if __name__ == "__main__":
    app()