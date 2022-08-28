
"""
EasyDL 图像分类 调用模型公有云API Python3实现
"""

from PIL import Image
import json
import base64
import requests

# 目标图片的 本地文件路径，支持jpg/png/bmp格式
IMAGE_FILEPATH = "./test_image/30.jpg"

# 可选的请求参数
# top_num: 返回的分类数量，不声明的话默认为 6 个
PARAMS = {"top_num": 3}

# 服务详情 中的 接口地址
MODEL_API_URL = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/segmentation/roadsegimage"

# 调用 API 需要 ACCESS_TOKEN。若已有 ACCESS_TOKEN 则于下方填入该字符串
# 否则，留空 ACCESS_TOKEN，于下方填入 该模型部署的 API_KEY 以及 SECRET_KEY，会自动申请并显示新 ACCESS_TOKEN
ACCESS_TOKEN = ""
API_KEY = "FE9tGvcQrwwhKSnYrKh0GDBT"
SECRET_KEY = "LZfG8M0XzeXY6gyvzyh6TH4YP9ewlGuW"


print("1. 读取目标图片 '{}'".format(IMAGE_FILEPATH))
with open(IMAGE_FILEPATH, 'rb') as f:
    base64_data = base64.b64encode(f.read())
    base64_str = base64_data.decode('UTF8')
print("将 BASE64 编码后图片的字符串填入 PARAMS 的 'image' 字段")
PARAMS["image"] = base64_str


if not ACCESS_TOKEN:
    print("2. ACCESS_TOKEN 为空，调用鉴权接口获取TOKEN")
    auth_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"               "&client_id={}&client_secret={}".format(API_KEY, SECRET_KEY)
    auth_resp = requests.get(auth_url)
    auth_resp_json = auth_resp.json()
    ACCESS_TOKEN = auth_resp_json["access_token"]
    print("新 ACCESS_TOKEN: {}".format(ACCESS_TOKEN))
else:
    print("2. 使用已有 ACCESS_TOKEN")


print("3. 向模型接口 'MODEL_API_URL' 发送请求")
request_url = "{}?access_token={}".format(MODEL_API_URL, ACCESS_TOKEN)
response = requests.post(url=request_url, json=PARAMS)
response_json = response.json()
response_str = json.dumps(response_json, indent=4, ensure_ascii=False)
print(type(response_str))
print("结果:{}".format(response_str))


