import openai
import yaml


def gpt_prompt(question):
    with open("API.yaml", "r") as yaml_conf:
        conf = yaml.safe_load(yaml_conf)
        openai.api_key = conf["OPENAI"]["API"]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"You are MBTIGPT produced by gangjoohyeong. Answer in Korean",
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )
    answer = completion["choices"][0]["message"]["content"]
    return answer