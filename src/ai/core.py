from ai.core import streamText
from ai.model import google
import os
import json

async def generate_ai_content():
    os.environ["OPENAI_API_KEY"] = "your-api-key"

    async for chunk in streamText(
        model=google("gemini-2.0-flash-exp"),
        systemMessage="You are a creative writer.",
        prompt="Write a short story about a robot."
    ):
        # chunk format: "0:{"text content"}\n"
        if chunk.startswith("0:"):
            text = json.loads(chunk[2:])
            print(text, end="", flush=True)