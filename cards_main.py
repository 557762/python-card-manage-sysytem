import cards_tools
while True:

    cards_tools.show_menu()
    action_str = input("请选择希望进行的操作: ")
    # print("您选择的操作是[%s]" % action_str)

    #针对名片的操作
    if action_str in ["1", "2", "3"]:
        #新增名片
        if action_str == "1":
            cards_tools.new_card()

        #显示全部
        elif action_str == "2":
            cards_tools.show_all()

        #搜索名片
        elif action_str == "3":
            cards_tools.search_card()

    #退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")

        break
