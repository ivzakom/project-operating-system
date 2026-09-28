from pathlib import Path

import typer
import yaml

app = typer.Typer(help="Project Operating System")

PROJECTS_DIR = Path("projects")


@app.command()
def init():
    """Initialize POS."""
    PROJECTS_DIR.mkdir(exist_ok=True)
    typer.echo("POS initialized")


@app.command()
def project_create(name: str):
    """Create a new project."""
    project_dir = PROJECTS_DIR / name

    if project_dir.exists():
        typer.echo(f"Project already exists: {name}")
        raise typer.Exit(code=1)

    for directory in [
        "hypotheses",
        "evidence",
        "requirements",
        "user_stories",
        "ux",
        "decisions",
        "tasks",
        "artifacts",
        "tests",
        "risks",
        "questions",
        "experiments",
        "releases",
    ]:
        (project_dir / directory).mkdir(parents=True)

    project = {
        "id": f"PRJ-{name.upper()}",
        "name": name,
        "status": "ACTIVE",
        "phase": "DISCOVERY",
        "current_goal": "",
    }

    state = {
        "project": name,
        "status": "ACTIVE",
        "phase": "DISCOVERY",
        "current_goal": "",
        "active_tasks": [],
        "blocking_questions": [],
        "next_allowed_action": None,
    }

    (project_dir / "project.yaml").write_text(
        yaml.safe_dump(project, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )

    (project_dir / "state.yaml").write_text(
        yaml.safe_dump(state, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )

    typer.echo(f"Project created: {name}")


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