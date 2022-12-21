import random
import string

def generate_random_str( length ):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length)).upper()

def generate_id():
    list = [] #リスト内にテーブル内容を読み込む
    while len( list ) < 10000000:
        リスト作成時生成文字列 =  generate_random_str(6)
        if リスト作成時生成文字列 not in list:
            list.append(リスト作成時生成文字列)

if __name__ == '__main__':
    generate_id()