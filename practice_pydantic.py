from typing import ClassVar

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    # インスタンス変数
    id: int
    name: str
    age: int

    # クラス変数
    user_count: ClassVar[int] = 0

    # カスタムの処理を追加したい場合は__init__()をオーバーライド
    def __init__(self, **data):
        # BaseModelのコンストラクタ（バリデーションやデフォルト値の適用などを行う）を呼び出す
        super().__init__(**data)
        User.user_count += 1
        print(f"user_count: {User.user_count}")


# 正しいデータでインスタンスを作成
try:
    user = User(id=1, name="Alice", age=20)
    print(user)
except ValidationError as e:
    print(e)

# 自動変換可能なデータでインスタンスを作成
try:
    # 以下のように可変長引数でデータを渡すこともできる
    data = {"id": "2", "name": "John", "age": "20"}
    user = User(**data)
    print(user)
except ValidationError as e:
    print(e)

# 不正なデータでインスタンスを作成
try:
    user = User(id="3", name="Bob", age="twenty")
    print(user)
except ValidationError as e:
    print(e)
