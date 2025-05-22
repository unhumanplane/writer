from abc import ABC, abstractmethod
import os
import openai # This line might require 'pip install openai' in the environment

class LLMService(ABC):
    @abstractmethod
    def edit(self, text: str) -> str:
        pass

class MockLLMService(LLMService):
    def edit(self, text: str) -> str:
        # Simulate an LLM edit
        return f"{text}\n--- Edited by Mock LLM ---"

class OpenAILLMService(LLMService):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            # Option 1: Raise an error (commented out as per instructions to log a warning)
            # raise ValueError("OPENAI_API_KEY environment variable not set.")
            # Option 2: Log a warning and the service won't work
            print("Warning: OPENAI_API_KEY environment variable not set. OpenAILLMService will not work.")
            # A more sophisticated logging mechanism could be used in a real application.
        # It's important to set openai.api_key only if the key exists, 
        # or handle it in the edit method to avoid errors if the key is missing.
        # For this implementation, we'll proceed to set it and let the edit method handle the absence.
        openai.api_key = self.api_key

    def edit(self, text: str) -> str:
        if not self.api_key:
            return "Error: OpenAI API key not configured."

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo", # Or another suitable model
                messages=[
                    {"role": "system", "content": "You are a helpful editor. Lightly edit the provided text for clarity and grammar."},
                    {"role": "user", "content": text}
                ]
            )
            # Correct way to access the content from the response object
            if response.choices and len(response.choices) > 0:
                # Check if the message content is not None
                if response.choices[0].message and response.choices[0].message.content:
                    return response.choices[0].message.content.strip()
                else:
                    return "Error: No content in OpenAI response."
            else:
                return "Error: No response choices from OpenAI."
        except Exception as e:
            # Log the exception e
            print(f"OpenAI API call failed: {e}")
            # It's good practice to not expose raw exception messages to the client if they might contain sensitive info.
            return "Error processing text with OpenAI."
