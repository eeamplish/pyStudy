money = 500000
name = input("请输入您的姓名\n")


def query():
    """
    查询账户余额
    :return: 当前余额
    """
    print(f"您的余额为{money}")
    return money


def save(save_money):
    """
    存款
    :return: 存款之后余额
    """
    cur_money = query()
    cur_money += save_money
    print(f"存入{save_money}元，当前余额为{cur_money}元")
    return cur_money


def withdraw(withdraw_money):
    """
    取钱
    :return: 取款之后余额
    """
    cur_money = query()
    cur_money -= withdraw_money
    print(f"取出{withdraw_money}元，当前余额为{cur_money}元")
    return cur_money


def main_menu():
    global money
    mode = input("请选择想要进行的操作：\n1，查询余额 \n2，存款 \n3，取款\n")
    if mode == "1":
        query()
    elif mode == "2":
        save_money = float(input("请输入存款金额 "))
        money = save(save_money)
    elif mode == "3":
        withdraw_money = float(input("请输入取款金额 "))
        money = withdraw(withdraw_money)
    else:
        print("操作错误，程序结束运行")
        return
    main_menu()


main_menu()
