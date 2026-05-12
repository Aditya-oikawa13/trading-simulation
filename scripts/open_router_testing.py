import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPEN_ROUTER_API_KEY"),
)

# First API call with reasoning
response = client.chat.completions.create(
  model="inclusionai/ring-2.6-1t:free",
  messages=[
          {
            "role": "user",
            "content": "How many r's are in the word 'strawberry'?"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)

print("--- First Response ---")
print(f"Content: {response.choices[0].message.content}")
if hasattr(response.choices[0].message, 'reasoning_details') and response.choices[0].message.reasoning_details:
    print("\nReasoning:")
    for detail in response.choices[0].message.reasoning_details:
        if isinstance(detail, dict) and 'text' in detail:
            print(detail['text'])
        elif hasattr(detail, 'text'):
            print(detail.text)

# Extract the assistant message with reasoning_details
assistant_message = response.choices[0].message

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "How many r's are in the word 'strawberry'?"},
  {
    "role": "assistant",
    "content": assistant_message.content,
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# If reasoning_details exists, we need to pass it back as per OpenRouter docs
if hasattr(assistant_message, 'reasoning_details') and assistant_message.reasoning_details:
    messages[1]["reasoning_details"] = assistant_message.reasoning_details

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="inclusionai/ring-2.6-1t:free",
  messages=messages,
  extra_body={"reasoning": {"enabled": True}}
)

print("\n--- Second Response ---")
print(f"Content: {response2.choices[0].message.content}")
if hasattr(response2.choices[0].message, 'reasoning_details') and response2.choices[0].message.reasoning_details:
    print("\nReasoning:")
    for detail in response2.choices[0].message.reasoning_details:
        if isinstance(detail, dict) and 'text' in detail:
            print(detail['text'])
        elif hasattr(detail, 'text'):
            print(detail.text)