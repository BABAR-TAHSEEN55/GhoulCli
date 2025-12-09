import json

from openai import OpenAI

from .prompt import SYSTEM_PROMPT
from .tools import available_tools


def setup():
    client = OpenAI()
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        print("Enter your query")
        query = input("> ")

        while True:
            messages.append({"role": "user", "content": query})

            res = client.chat.completions.create(
                model="gpt-4.1-nano",
                response_format={"type": "json_object"},
                messages=messages,
            )

            messages.append(
                {"role": "assistant", "content": res.choices[0].message.content}
            )

            parsed_response = json.loads(res.choices[0].message.content)

            if parsed_response.get("step") == "start":
                print(f"{parsed_response.get('content')}")
                continue

            if parsed_response.get("step") == "plan":
                print(f"{parsed_response.get('content')}")
                continue

            if parsed_response.get("step") == "action":
                tool_name = parsed_response.get("function")
                tool_input = parsed_response.get("input")

                print(f"Calling {tool_name} with input as {tool_input}")

                if available_tools.get(tool_name):
                    observe_output = available_tools[tool_name](tool_input)

                    messages.append(
                        {
                            "role": "user",
                            "content": json.dumps(
                                {"step": "observe", "output": observe_output}
                            ),
                        }
                    )

                    continue

            if parsed_response.get("step") == "result":
                print(f"{parsed_response.get('content')}")
                break
