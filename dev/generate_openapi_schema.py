# Copyright 2024 yu-iskw
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import textwrap

import click
import google.generativeai as genai
import requests


@click.command()
@click.option("--reference", type=str, default="https://raw.githubusercontent.com/lightdash/lightdash/main/packages/backend/src/generated/swagger.json")
# @click.option("--output", type=str, required=True)
def main(reference: str):
    print(f"Reference URL: {reference}")
    # print(f"Output Path: {output}")

    try:
        # Fetch the page
        html_content = fetch_page(reference)
        print(html_content[:100])
        # Generate schemas
        system_prompt = get_system_prompt()
        response = generate_schemas(
            model="gemini-1.5-flash",
            system_prompt=system_prompt,
            html_content=html_content,
        )
        print(response.text)
    except requests.RequestException as e:
        print(f"Failed to fetch the page: {e}")


def fetch_page(url: str, timeout: int = 10) -> str:
    """Fetch a page from the given URL."""
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()  # Ensure we raise an exception for HTTP errors
    return response.text


def get_system_prompt() -> str:
    return textwrap.dedent("""
    Can you break down the given swagger JSON object into smaller independent JSON objects each representing a single API endpoint?
    You don't have to share references of requests and response between objects.
    If you encounter infinite recursions in the swagger JSON object, you MUST handle them gracefully.

    The output format is a list of JSON objects each representing a single API endpoint.
    """).strip()


def generate_schemas(model: str, system_prompt: str, html_content: str):
    # Validate the environment variables
    if os.environ.get("GOOGLE_API_KEY") is None:
        raise ValueError("GOOGLE_API_KEY is not set")
    # Configure the client
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    # Generate content
    model = genai.GenerativeModel(model, system_instruction=system_prompt)
    response = model.generate_content(
        html_content,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json",
            temperature=0.0,
            candidate_count=1,
            max_output_tokens=2000,
        ),
    )
    return response


if __name__ == "__main__":
    main()
