import os
import dashscope

# 从环境变量获取 API Key
dashscope.api_key = os.getenv("ALIYUN_API_KEY")

response = dashscope.Generation.call(
    model="qwen-turbo",
    prompt="如何用 Python 进行数据分析？",
    result_format="text"
)

print(response)
