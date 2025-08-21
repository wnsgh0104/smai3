from numpy.f2py.crackfortran import endifs
from openai import chat

from myllm.MyApi import geminiModel

def test(chat):
    model = geminiModel()
    chat = model.start_chat(history=[])
    print("\n--- Gemini 챗 봇 시작 ---")

if __name__ == '__main__':
    while True:
        user_message=input("나:")
        if user_message.lower()=='종료':
            break
        response=chat.send_message(user_message)

        print("Gemini:", response.text)
    print("--- 챗 봇 종료 ---")
    print(chat.history)