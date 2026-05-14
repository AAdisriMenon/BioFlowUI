"""
Checks whether Docker, Nextflow, Java, and Singularity are available on the system.
"""

import shutil
import subprocess
from dataclasses import dataclass


@dataclass
class EnvCheck:
    name: str
    available: bool
    version: str
    install_url: str
    required: bool


def check_tool(cmd: list[str]) -> tuple[bool, str]:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        version_line = (result.stdout + result.stderr).strip().split("\n")[0]
        return True, version_line
    except Exception:
        return False, ""


def run_environment_check() -> list[EnvCheck]:
    checks = []

    # Java
    ok, ver = check_tool(["java", "-version"])
    checks.append(
        EnvCheck(
            name="Java (JDK ≥ 11)",
            available=ok,
            version=ver,
            install_url="https://adoptium.net/",
            required=True,
        )
    )

    # Nextflow
    ok, ver = check_tool(["nextflow", "-version"])
    checks.append(
        EnvCheck(
            name="Nextflow",
            available=ok,
            version=ver,
            install_url="https://www.nextflow.io/docs/latest/install.html",
            required=True,
        )
    )

    # Docker
    ok, ver = check_tool(["docker", "--version"])
    checks.append(
        EnvCheck(
            name="Docker",
            available=ok,
            version=ver,
            install_url="https://docs.docker.com/get-docker/",
            required=False,
        )
    )

    # Singularity
    ok, ver = check_tool(["singularity", "--version"])
    checks.append(
        EnvCheck(
            name="Singularity",
            available=ok,
            version=ver,
            install_url="https://docs.sylabs.io/guides/3.0/user-guide/installation.html",
            required=False,
        )
    )

    # Git
    ok, ver = check_tool(["git", "--version"])
    checks.append(
        EnvCheck(
            name="Git",
            available=ok,
            version=ver,
            install_url="https://git-scm.com/downloads",
            required=True,
        )
    )

    return checks


def get_available_profiles() -> list[str]:
    profiles = []
    ok_docker, _ = check_tool(["docker", "--version"])
    ok_singularity, _ = check_tool(["singularity", "--version"])
    if ok_docker:
        profiles.append("docker")
    if ok_singularity:
        profiles.append("singularity")
    profiles.append("conda")
    return profiles if profiles else ["conda"]
