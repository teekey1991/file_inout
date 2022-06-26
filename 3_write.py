def main():
    # ファイルオブジェクトを生成
    with open(file="users.csv", mode="r") as f:
        text = f.read()
            #text=readlines()
        users = text.split('\n')

     for user in users:
        name, age = user.split(',') #分割代入
        print(f'Name: {name} Age : {age}')
        
    print(users)

if __name__ == "__main__":
    # read01()
    main()