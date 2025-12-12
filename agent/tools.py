import os
import subprocess
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather(city: str):
    try:
        url = os.getenv("WEATHER_API")
        contructed_url = f"{url}&q={city}&aqi=no"
        response = requests.get(contructed_url, timeout=30).json()
        return response
    except requests.Timeout:
        return {
            "error": "Command timed out after 30 seconds",
            "success": False,
        }


def run_terminal_cmd(args: str) -> Dict:
    try:
        if args.startswith("git commit -m"):
            result = subprocess.run(
                args,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30,
                cwd=os.getcwd(),
            )
        else:
            split_text = args.split(" ")
            result = subprocess.run(
                split_text, capture_output=True, text=True, timeout=30, cwd=os.getcwd()
            )

        return {
            "command": args,
            "return_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": result.returncode == 0,
            "working_directory": os.getcwd(),
        }

    except subprocess.TimeoutExpired:
        return {
            "command": args,
            "error": "Command timed out after 30 seconds",
            "success": False,
        }
    except Exception as e:
        return {
            "command": args,
            "error": f"Failed to execute command: {str(e)}",
            "success": False,
        }


def read_file(file_name: str) -> dict:
    proc = subprocess.run(["cat", file_name], capture_output=True, text=True)
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def grep_search(pattern: str):
    cmd = ["grep", "-r", pattern]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    print(proc.stdout)
    return {"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}


def docker_orchestrationOrCheckContainerStatus():
    return "Docker Orchestration"


def commit_generate(filename: str):
    res = read_file(filename)
    return res


available_tools = {
    "get_weather": get_weather,
    "run_terminal_cmd": run_terminal_cmd,
    "read_file": read_file,
    # "edit_file": edit_file,
    "grep_search": grep_search,
    # "codebase_search": codebase_search,
    "commit_generate": commit_generate,
}
