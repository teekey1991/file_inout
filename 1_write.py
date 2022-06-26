def main():
    f = open(file='users.csv', mode='w', encoding='utf-8')

    f.write('Bob,79\n')
    f.write('tom,59\n')
    f.write('tom,59')

    print('close前', f.closed)
    f.close()
    print('close後', f.closed)

if __name__ == '__main__':
    main()