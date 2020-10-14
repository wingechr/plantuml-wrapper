"""Plantuml wrapper script
"""

import os
import sys
import shutil
from subprocess import Popen

JARFILE = "plantuml.jar"


def find_plantuml():
    """Return path to plantuml executable."""
    path = shutil.which("plantuml")
    return path


def find_java():
    """Return path to java executable."""
    path = shutil.which("java")
    if not path:
        raise FileNotFoundError("java executable not found in PATH")
    return path


def find_plantuml_jar():
    """Return path to java plantuml.jar."""
    for path in os.environ.get("PATH", "").split(os.pathsep):
        path = os.path.join(path, JARFILE)
        if os.path.isfile(path):
            return path
    raise FileNotFoundError("%s not found in PATH" % JARFILE)


def main():
    """Script entry point."""
    plantuml = find_plantuml()
    if plantuml:
        cmd = [plantuml]
    else:
        java = find_java()
        plantuml_jar = find_plantuml_jar()
        cmd = [java, "-jar", plantuml_jar]
    cmd += sys.argv[1:]
    proc = Popen(cmd, stdin=sys.stdin.buffer, stdout=sys.stdout.buffer)
    proc.communicate()
    if proc.returncode:
        raise Exception("plantuml failed")


if __name__ == "__main__":
    main()
