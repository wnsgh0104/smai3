from io import BytesIO
from PIL import Image
from myllm.MyApi import geminiModel
import requests

def test(prompt,img):
    model = geminiModel()
    response = model.generate_content([prompt,img])
    print(response.text)

if __name__ == '__main__':
    image_url = "https://www.coca-cola.com/content/dam/onexp/kr/ko/home-images/brands/coca-cola-brand/kr_coca-cola_prod_coca-cola%20original%20taste%20250ml_750x750.jpg"
    response_image = requests.get(image_url)
    img = Image.open(BytesIO(response_image.content))
    prompt="이 이미지가 어떤 성분으로 이루어져 있는지 알려줘"
    test(prompt,img)