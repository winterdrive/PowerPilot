from openai import OpenAI
from prompt import (commit_message_generator_role,
                    commit_message_generator_guidelines,
                    commit_message_generator_demo_input,
                    commit_message_generator_demo_output,
                    commit_message_generator_test_input)
from dotenv import load_dotenv
from os import environ

def commit_message_generator(git_diff_content: str) -> str:
    """
    Generates a commit message based on the provided git diff content.

    Args:
        git_diff_content (str): The content of the git diff.

    Returns:
        str: The generated commit message.
    """

    # Check git diff content validity
    if not is_valid_git_diff(git_diff_content):
        return "Invalid git diff content."

    # Point to the local server
    client = OpenAI(base_url=environ.get("model_url"), api_key=environ.get("api_key"))

    conversation_history = [
        {"role": "system",
         "content": commit_message_generator_role},
        {"role": "user",
         "content": "How will you generate the commit message?"},
        {"role": "system",
         "content": commit_message_generator_guidelines},
        {"role": "user",
         "content": "Can you show me an example input?"},
        {"role": "system",
         "content": commit_message_generator_demo_input},
        {"role": "user",
         "content": "Can you show me an example output?"},
        {"role": "system",
         "content": commit_message_generator_demo_output},
    ]

    conversation_history.append({"role": "user", "content":
        """
        give me the commit message base on the following git diff content
        
        ### git diff content
        
        """
        + git_diff_content})

    completion = client.chat.completions.create(
        model="TheBloke/CodeLlama-7B-Instruct-GGUF/codellama-7b-instruct.Q5_K_M.gguf",
        messages=conversation_history,
        temperature=1,
    )

    return completion.choices[0].message.content


def is_valid_git_diff(git_diff_content: str) -> bool:
    """
    Validates the git diff content.

    Args:
        git_diff_content (str): The content of the git diff.

    Returns:
        bool: True if the git diff content is valid, False otherwise.
    """
    if git_diff_content is None or not 10 <= len(git_diff_content) <= 20000:
        print(f"Invalid git diff content length.{len(git_diff_content)}")
        return False

    if not all(tag in git_diff_content for tag in ["diff --git", "index", "---", "+++", "@@", "+", "-"]):
        print("Invalid git diff content format.")
        return False

    return True


if __name__ == "__main__":
    result = commit_message_generator(commit_message_generator_test_input)
    print(result)
