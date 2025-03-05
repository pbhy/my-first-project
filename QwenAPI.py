import os
import dashscope

class QwenAPI:
    def __init__(self, api_key=None, model="qwen-turbo", temperature=0.7, punishment=1.0, max_tokens=512, top_p=0.9, n=1):
        """
        Qwen API 封装类

        :param api_key: 阿里云 DashScope API Key（可从环境变量 ALIYUN_API_KEY 读取）
        :param model: 选择的 Qwen 模型（如 "qwen-turbo"）
        :param temperature: 控制生成文本的随机性（值越大，随机性越高）
        :param punishment: 惩罚参数，控制重复度
        :param max_tokens: 最大输出 token 数
        :param top_p: nucleus sampling（保留概率最高的 top_p 部分）
        :param n: 生成的输出数量
        """
        self.api_key = api_key or os.getenv("ALIYUN_API_KEY")
        self.model = model
        self.temperature = temperature
        self.punishment = punishment
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.n = n

        if not self.api_key:
            raise ValueError("请提供 API Key，可以通过参数传入或设置环境变量 ALIYUN_API_KEY")

        dashscope.api_key = self.api_key

    def __call__(self, prompt):
        """
        调用 Qwen API 进行文本生成

        :param prompt: 需要输入的大模型提示词
        :return: 生成的文本结果
        """
        response = dashscope.Generation.call(
            model=self.model,
            prompt=prompt,
            result_format="text",
            temperature=self.temperature,
            top_p=self.top_p,
            max_tokens=self.max_tokens,
            n=self.n,
        )
        return response

# 示例用法
if __name__ == "__main__":
    qwen = QwenAPI(temperature=0.8, punishment=1.2, max_tokens=256, top_p=0.85, n=1)
    result = qwen("如何用 Python 进行数据分析？")
    print(result)
