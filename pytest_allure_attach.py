# coding:utf-8
import allure


def test_attach_text():
    allure.attach("这是一个纯文本信息", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段html代码块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file(r"C:\Users\邱州炫\Desktop\study\fca\611.jpg", "这是一个图片", attachment_type=allure.attachment_type.JPG)
