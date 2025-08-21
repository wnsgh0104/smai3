from myllm.MyApi import geminiModel

def test(prompt):
    model = geminiModel()
    response = model.generate_content(prompt)
    print(response.text)

if __name__ == '__main__':
    question = "시스템반도체란 무엇인가요?"

    prompt = f"{question}에 대해서 설명해줘."

    test(prompt)