card_list = []


def show_menu():
    """显示菜单"""
    menu = '''欢迎使用【名片管理系统】V 1.0
    1.新增名片
    2.显示全部
    3.搜索名片
    
    0.退出系统
    '''
    print(menu)




def new_card():
    """新增名片"""
    # print("新增名片")
    #1.提示用户输入名片详细信息
    name_str = input("请输入姓名: ")
    phone_str = input("请输入电话号码: ")
    qq_str = input("请输入QQ: ")
    email_srt = input("请输入邮箱: ")
    #2.使用用户的信息建立一个字典
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_srt
    }
    #3.将名片字典添加到列表中
    card_list.append(card_dict)
    # print(card_list)

    #4.提示用户添加成功
    print("添加 %s 的名片成功" % name_str)



def show_all():
    """显示全部"""
    # print("显示全部")
    #1.判断是否存在名片
    if len(card_list) == 0:
        print("当前没有任何名片，请使用后新增名片功能添加名片")
        return
    print("=" * 50)
    #2.打印表头
    for card in ["姓名", "电话", "QQ", "邮箱"]:
        print(card, end="\t\t\t")


    print("")
    #3.打印分隔线
    #4.遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))
    print("=" * 50)



def search_card():
    """搜索名片"""
    # print("搜索名片")
    #1. 提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名: ")



    #2. 遍历名片列表，查询要搜索的姓名，如果没有找到，要告诉用户
    for card_dict in card_list:

        if card_dict["name"] == find_name:
            print("搜索到包含 %s 信息的如下名片: " % find_name)
            print("=" * 50)
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            print("=" * 50)
            deal_card(card_dict)
            break
    else:
        print("抱歉没有找到 %s " % find_name)

def deal_card(find_dict):
    """

    @param find_dict: 传递了card_dict实参
    """
    # print(find_dict)
    action_str = input("请选择要执行的操作 "
                       "[1]修改"
                       "[2]删除"
                       "[0]返回上级菜单: " )
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名: ")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话: ")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ:")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱:")
        print("修改名片成功！！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！！")

def input_card_info(idct_value, tip_message):
    """

    @param idct_value:字典中原有的值
    @param tip_message:输入的提示文字
    @return:如果用户输入了内容就返回输入的内容，否则返回原有的值
    """
    #1. 提示用户输入内容
    result_str = input(tip_message)
    #2.根据用户输入内容进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:

        return result_str
    #3. 如果用户没有输入内容，则直接返回字典中原有的值
    else:
        return idct_value

