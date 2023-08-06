import openai
import yaml

def gpt_prompt(question, title, mbti, qna_pairs, user_name):
    mbtis = {'ISTJ': '내향적이고 현실적이며 감정보다는 논리와 분석을 우선시하고 계획적인 사람',
             'INTP': '내향적이고 미래지향적이며 감정보다는 논리와 분석을 우선시하고 융통성 있는 사람',
             'ENFP': '외향적이고 미래지향적이며 매우 감정적이고 융통성 있는 사람',
             'ENTJ': '외향적이고 미래지향적이며 감정보다는 논리와 분석을 우선시하고 계획적인 사람',
             }
    with open("API.yaml", "r") as yaml_conf:
        conf = yaml.safe_load(yaml_conf)
        openai.api_key = conf["OPENAI"]["API"]
        
    messages = [{
            "role": "system",
            "content": f'''
                너의 이름은 {title}이고, 너와 대화하는 상대방의 이름은 {user_name} 이다.
                {mbtis[mbti]}처럼 대답해라.
                너는 대화하는 상대방과 친구 관계이고, 고민을 들어주기 위한 사람이다.
                너는 대화하는 상대방과 친구 관계인 것처럼 반말로 친근하게 상대방의 이름을 언급하면서 대답해라.
                30자 내외로 대답해라.
                ''',
        }]

    for qna_pair in qna_pairs[::-1]:
        question_, answer_ = qna_pair
        messages.extend([
            {
                "role": "user",
                "content": question_,
            },
            {
                "role": "assistant",
                "content": answer_,
            }
            ])

    messages.extend([
        {
            "role": "user",
            "content": question,
        },
    ])

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
    )
    answer = completion["choices"][0]["message"]["content"]
    print(messages)
    return answer
