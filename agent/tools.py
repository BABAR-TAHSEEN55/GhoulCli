import os
import subprocess
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather(city: str):
    url = os.getenv("WEATHER_API")
    contructed_url = f"{url}&q={city}&aqi=no"
    response = requests.get(contructed_url).json()
    return response


def run_terminal_cmd(args: str) -> Dict:
    splitText = args.split(" ")
    result = subprocess.run(splitText, capture_output=True, text=True)
    return {"cmd": args, "stderr": result.stderr, "stdout": result.stdout}


def read_file(file_name: str) -> dict:
    proc = subprocess.run(["cat", file_name], capture_output=True, text=True)

    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def edit_file(file_name: str, content: str):
    with open(file_name, "w") as f:
        f.write(content)


def grep_search(pattern: str):
    cmd = ["grep", "-r", pattern]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    print(proc.stdout)
    return {"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}


def commit_generate(filename: str):
    pass


def docker_orchestration():
    print("docker done NLP")


available_tools = {
    "get_weather": get_weather,
    "run_terminal_cmd": run_terminal_cmd,
    "read_file": read_file,
    "edit_file": edit_file,
    "grep_search": grep_search,
    # "codebase_search": codebase_search,
    # "commit_generate": commit_generate,
    # "repo_analyzer": repo_analyzer,
}
