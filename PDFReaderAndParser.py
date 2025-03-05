from langchain_community.document_loaders import PyPDFium2Loader

class PDFReaderAndParser:
    def __init__(self, file_path):
        """
        初始化 PDF 解析器
        :param file_path: PDF 文件路径
        """
        self.file_path = file_path
        self.loader = PyPDFium2Loader(self.file_path)
        self.data = self.loader.load()

    def get_text(self):
        """
        提取 PDF 的文本内容
        :return: 解析出的文本内容（字符串列表，每页一个元素）
        """
        return [page.page_content for page in self.data]

    def get_metadata(self):
        """
        获取 PDF 的元数据
        :return: 解析出的元数据（字典）
        """
        return [page.metadata for page in self.data]

# 使用示例
if __name__ == "__main__":
    pdf_parser = PDFReaderAndParser("./VideoRAG.pdf")
    
    # 获取文本内容
    text_content = pdf_parser.get_text()
    print("\n".join(text_content))  # 打印所有页面的文本

    # 获取元数据
    metadata = pdf_parser.get_metadata()
    print(metadata)
