from functions.movie.search_movies.function import search_movies
from functions.movie.search_movies.types import FunctionInput
import os

params = FunctionInput(title="Interstellar")
print(search_movies(params=params))

import json
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_KEY"),
    base_url=os.environ.get("OPENAI_URL"),
)

kwargs = {
    "messages": [
        {"role": "user", "content": "近期上映电影有？"},
        # {
        #     "role": "assistant",
        #     "content": None,
        #     "function_call": {
        #         "name": "get_current_weather",
        #         "arguments": '{\n  "location": "Toronto"\n}',
        #     },
        # },
        # {
        #     "role": "function",
        #     "name": "get_current_weather",
        #     "content": '{\n "degree": "22" \n}',
        # },
    ],
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_playing_movies",
                "description": "Get a list of movies that are playing in theatres.",
                "parameters": {
                    "type": "object",
                    "properties": {"limit": {"type": "integer", "description": ""}},
                    "required": [],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_popular_movies",
                "description": "Get a list of popular movies.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "limit": {
                            "type": "integer",
                            "description": "The limit number of popular movies.",
                        }
                    },
                    "required": [],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "search_people",
                "description": "Search for people by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The name of the person to search for.",
                        }
                    },
                    "required": ["query"],
                },
            },
        },
    ],
    "model": "gpt-3.5-turbo-0613",
}

kwargs = dict(
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_playing_movies",
                "description": "Get a list of movies that are playing in theatres.",
                "parameters": {
                    "type": "object",
                    "properties": {"limit": {"type": "integer", "description": ""}},
                    "required": [],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_popular_movies",
                "description": "Get a list of popular movies.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "limit": {
                            "type": "integer",
                            "description": "The limit number of popular movies.",
                        }
                    },
                    "required": [],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "search_people",
                "description": "Search for people by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The name of the person to search for.",
                        }
                    },
                    "required": ["query"],
                },
            },
        },
    ]
)

args = {
    "model": "gpt-3.5-turbo-0613",
    "messages": [{"role": "user", "content": "近期上映电影有？"}],
}
response = client.chat.completions.create(**args, **kwargs)

print(response)
