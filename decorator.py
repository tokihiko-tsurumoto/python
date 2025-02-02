import time
from datetime import datetime


# funcには、decoratorでラップされた関数自体が入る
def decorator(func):
    def wrapper(*args, **kwargs):
        print(datetime.now())
        # ラップされた関数を実行
        # *args, **kwargsはラップされた関数に渡す任意の位置引数とキーワード引数
        func(*args, **kwargs)
        print(datetime.now())

    return wrapper


# decoratorを使ってfuncをラップ
@decorator
def func():
    print("func start")
    time.sleep(2)
    print("func end")


# スクリプトが直接実行された場合、__name__は"__main__"になる
# 以下のようにすることで、他のスクリプトからimportされた際に勝手に実行されることを防げる
if __name__ == "__main__":
    func()
