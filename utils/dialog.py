from qfluentwidgets import MessageBox


def functions_not_open(instance):
    """
    弹出一个对话框：该功能暂不开放
    """
    message = MessageBox(title="友好提示",
                         content="该功能暂不开放,可以加入开发加速功能开放",
                         parent=instance)
    message.show()
