def write01():
    # ファイルオブジェクトを生成
    f = open("fruits.txt", mode="a", encoding='utf-8')

    f.write("リンゴ")
    f.write("ミカン")
    f.write("メロン")

    # データが破損したりする場合があるので忘れない！
    f.close()


if __name__ == "__main__":
    write01()
