import json
import os

# 保存数据的文件名
DATA_FILE = "shopping_cart.json"


def load_cart():
    """从文件读取购物车数据，文件不存在就返回空字典"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cart(cart):
    """把购物车数据写入文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cart, f, ensure_ascii=False, indent=4)


# 程序启动时，先把上次的数据读回来
shopping_cart = load_cart()

print("欢迎来到购物车管理系统")

while True:
    print(
        """
        #########################
        #       1.添加购物车      #
        #       2.修改购物车      #
        #       3.删除购物车      #
        #       4.查询购物车      #
        #       5.退出购物车      #
        #########################
        """
    )
    try:
        choice = int(input("请输入您的选择："))
    except ValueError:
        print("输入错误，请输入数字（1-5）！")
        continue

    match choice:
        case 1:
            goods_name = input("请输入商品的名称：")
            if goods_name in shopping_cart:
                print("商品已存在,请重新输入")
            else:
                goods_price = input("请输入商品的价格：")
                goods_num = input("请输入商品的数量：")
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                save_cart(shopping_cart)          # 保存到文件
                print("商品添加成功")

        case 2:
            print("修改购物车")
            goods_name = input("请输入要修改的商品的名称：")
            if goods_name not in shopping_cart:
                print("商品不存在,请重新输入")
                continue
            else:
                goods_price = input("请输入商品的价格：")
                goods_num = input("请输入商品的数量：")
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                save_cart(shopping_cart)          # 保存到文件
                print("商品修改成功")

        case 3:
            print("删除购物车")
            goods_name = input("请输入要删除的商品的名称：")
            if goods_name not in shopping_cart:
                print("商品不存在,请重新输入")
                continue
            else:
                del shopping_cart[goods_name]
                save_cart(shopping_cart)          # 保存到文件
                print("商品删除成功")

        case 4:
            print("查询购物车")
            print(shopping_cart)

        case 5:
            print("退出购物车")
            break

        case _:
            print("输入错误,请重新输入")
            continue