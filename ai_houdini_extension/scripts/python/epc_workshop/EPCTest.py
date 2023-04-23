"""

Quick test module to demonstrate a point.

"""

def test():
    print("Yes, this test seems to work just fine!")

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_gpt_code_from_prompt(prompt):
    openai.api_key = "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"
    wrapper = "Analyze the following VEX code from SideFX Houdini and add comments to explain it. Don't change the code, just add comment above. I only need the script body, do NOT explain the code body. The code: "
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "user", "content": f"{wrapper} {prompt}"}
        ],
        temperature=1.0,
        n=1
    )
    return completion.choices[0].message.content


def read_text_from_parameter_and_generate_gpt_code_from_prompt(prompt):
    openai.api_key = "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"
    pre_wrapper = "Write VEX code from SideFX Houdini that will: "
    post_wrapper = " Additionally add comments explaining it. Give me just the code and the comments, nothing else. I only need the script body, do NOT explain the code body."
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "user", "content": f"{pre_wrapper} {prompt} {post_wrapper}" }
        ],
        temperature=1.0,
        n=1
    )
    return completion.choices[0].message.content
