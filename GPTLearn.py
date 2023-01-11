import openai
import time

def configure():
    openai.api_key = "API_KEY"

def create_completion(model, organization, prompt, temperature):
    completion = openai.Completion.create(engine=model, prompt=prompt, temperature=temperature, max_tokens=1024, top_p=1, frequency_penalty=0, presence_penalty=0, organization=organization)
    return completion["choices"][0]["text"]

if __name__ == '__main__':
    pass
