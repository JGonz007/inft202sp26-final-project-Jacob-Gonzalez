#!/usr/bin/env python3
"""Docker-based setup check for the INFT202 final project.

This script keeps student setup small: repo + Docker + Codex. It checks Git,
checks Docker, starts the Docker Compose stack, verifies the PostgreSQL database
named "final", and writes short markdown notes for Codex to use later.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB_NAME = "final"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_PORT = "5432"
ADMINER_URL = "http://localhost:8080"


def run(command: list[str], timeout: int = 20) -> tuple[int, str, str]:
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        return completed.returncode, completed.stdout.strip(), completed.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"{command[0]} not found"
    except subprocess.TimeoutExpired:
        return 124, "", f"{' '.join(command)} timed out"


def has_command(name: str) -> bool:
    return shutil.which(name) is not None


def compose_command() -> list[str] | None:
    if not has_command("docker"):
        return None

    code, _, _ = run(["docker", "compose", "version"])
    if code == 0:
        return ["docker", "compose"]

    code, _, _ = run(["docker-compose", "version"])
    if code == 0:
        return ["docker-compose"]

    return None


def git_info() -> list[str]:
    notes: list[str] = []

    if not (ROOT / ".git").exists():
        return ["- [ ] Git repo found: no. Fork and clone the project repo first."]

    notes.append("- [x] Git repo found")

    code, origin, _ = run(["git", "remote", "get-url", "origin"])
    if code == 0 and origin:
        if "github.com" in origin and "YOUR_USERNAME" not in origin:
            notes.append(f"- [x] GitHub remote configured: `{origin}`")
        else:
            notes.append(f"- [ ] GitHub remote may need attention: `{origin}`")
    else:
        notes.append("- [ ] No GitHub remote named `origin` found. Add your fork as `origin`.")

    code, branch, _ = run(["git", "branch", "--show-current"])
    notes.append(f"- [x] Current Git branch: `{branch}`" if code == 0 and branch else "- [ ] Could not detect current Git branch.")

    code, name, _ = run(["git", "config", "user.name"])
    notes.append("- [x] Git user.name configured" if code == 0 and name else "- [ ] Set Git user.name.")

    code, email, _ = run(["git", "config", "user.email"])
    notes.append("- [x] Git user.email configured" if code == 0 and email else "- [ ] Set Git user.email.")

    return notes


def docker_info() -> tuple[list[str], bool, list[str] | None]:
    notes: list[str] = []

    if not has_command("docker"):
        notes.append("- [ ] Docker command not found. Install Docker Desktop, open it, then rerun this setup.")
        return notes, False, None

    notes.append("- [x] Docker command found")

    code, out, err = run(["docker", "info"], timeout=12)
    if code != 0:
        notes.append("- [ ] Docker is installed but not running.")
        notes.append("  - Open Docker Desktop and wait until it says Docker is running, then rerun setup.")
        if err:
            notes.append(f"  - Docker message: `{err.splitlines()[-1]}`")
        return notes, False, None

    notes.append("- [x] Docker is running")

    compose = compose_command()
    if compose is None:
        notes.append("- [ ] Docker Compose not found. Update Docker Desktop, then rerun setup.")
        return notes, False, None

    code, out, _ = run(compose + ["version"])
    notes.append(f"- [x] Docker Compose available: `{out.splitlines()[0] if out else 'installed'}`")
    return notes, True, compose


def start_stack(compose: list[str]) -> tuple[list[str], bool]:
    notes: list[str] = []

    code, out, err = run(compose + ["up", "-d", "postgres", "adminer"], timeout=120)
    if code != 0:
        notes.append("- [ ] Could not start the Docker database stack.")
        if err:
            notes.append(f"  - Docker message: `{err.splitlines()[-1]}`")
        return notes, False

    notes.append("- [x] Docker database stack started")

    for _ in range(20):
        code, out, _ = run(compose + ["exec", "-T", "postgres", "pg_isready", "-U", DB_USER, "-d", DB_NAME], timeout=10)
        if code == 0:
            notes.append(f"- [x] PostgreSQL database `{DB_NAME}` is ready")
            return notes, True
        time.sleep(2)

    notes.append(f"- [ ] PostgreSQL container started, but database `{DB_NAME}` was not ready in time.")
    notes.append("  - Wait a minute, then rerun setup.")
    return notes, False


def write_outputs(sections: list[tuple[str, list[str]]], ready: bool) -> None:
    lines = ["# Setup Check", ""]
    for title, notes in sections:
        lines.append(f"## {title}")
        lines.extend(notes)
        lines.append("")

    if ready:
        lines.extend(
            [
                "## Connection Info",
                f"- Database: `{DB_NAME}`",
                f"- User: `{DB_USER}`",
                f"- Password: `{DB_PASSWORD}`",
                f"- Host from your computer: `localhost`",
                f"- Port: `{DB_PORT}`",
                f"- Browser database tool: `{ADMINER_URL}`",
                "",
                "## Next Step",
                "Use this Docker PostgreSQL database for Beekeeper Studio, Adminer, imports, queries, and the Flask app.",
                "",
            ]
        )
        (ROOT / "database_setup.md").write_text(
            "\n".join(
                [
                    "# Database Setup",
                    "",
                    f"DB_NAME={DB_NAME}",
                    f"DB_USER={DB_USER}",
                    f"DB_PASSWORD={DB_PASSWORD}",
                    "DB_HOST=localhost",
                    f"DB_PORT={DB_PORT}",
                    f"ADMINER_URL={ADMINER_URL}",
                    "",
                    "Use this Docker PostgreSQL database for Beekeeper Studio, Adminer, imports, queries, and the Flask app.",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    else:
        lines.extend(
            [
                "## Next Step",
                "Fix the unchecked setup items above, then rerun this setup check.",
                "",
            ]
        )

    (ROOT / "setup_check.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


def main() -> int:
    sections: list[tuple[str, list[str]]] = []
    sections.append(("Git And GitHub", git_info()))

    docker_notes, docker_ready, compose = docker_info()
    sections.append(("Docker", docker_notes))

    stack_ready = False
    if docker_ready and compose is not None:
        stack_notes, stack_ready = start_stack(compose)
        sections.append(("Project Database Stack", stack_notes))
    else:
        sections.append(("Project Database Stack", ["- [ ] Not started because Docker is not ready."]))

    write_outputs(sections, stack_ready)
    return 0 if stack_ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
