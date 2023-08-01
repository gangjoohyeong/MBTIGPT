import openai
import yaml


def gpt_prompt(question, title, mbti):
    with open("API.yaml", "r") as yaml_conf:
        conf = yaml.safe_load(yaml_conf)
        openai.api_key = conf["OPENAI"]["API"]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f'''
                    Your name is {title}. 
                    You will answer like an {mbti}.
                    Answer in Korean.
                    ''',
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )
    answer = completion["choices"][0]["message"]["content"]
    return answer