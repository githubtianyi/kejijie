#请使用UTF-8编码打开和运行
print("欢迎使用此小工具","\n")
#小工具内容
print("可以使用的功能:")
print("1:计算n个数的平均数")
print("2:计算n个数中的最大值")
print("3:计算n个数中的最小值")
print("4:对n个数进行排序")
print("5:计算前3(10)名")
print("6:彩蛋")
print("7:简单计算器")
print("\n","输入数据不得超过10000000")
#内容打印结束
lines = []
#功能实现



#前十名
def ten(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]: # 如果前面的数大于后面的数，就交换位置
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
#前三名
def third(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]: # 如果前面的数大于后面的数，就交换位置
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
#排序,从大到小
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] < nums[j + 1]: # 如果前面的数小于后面的数，就交换位置
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
#排序,从小到大
def bubble(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]: # 如果前面的数大于后面的数，就交换位置
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
#输入数据是不是str
def check_input_type_str(input_value):
    if not isinstance(input_value, (str)):
        return False
    else:
        return True
#输入数据是不是int
def check_input_type_int(input_value):
    if not isinstance(input_value, (int)):
        return False
    else:
        return True







while True:
    indoor = input("输入功能前数字即可,输入exit即可以退出,输入'help'显示功能列表:")
    
    #help函数        
    if indoor == "help":
        print("\n")
        print("可以使用的功能:")
        print("1:计算n个数的平均数")
        print("2:计算n个数中的最大值")
        print("3:计算n个数中的最小值")
        print("4:对n个数进行排序")
        print("5:计算前3(10)名")
        print("6:彩蛋")
        print("7:简单计算器")
    #退出程序   
    if indoor == "exit":
        break
    
    if check_input_type_str(indoor):
        if indoor == "1":
            c = 0
            n = int(input("请输入有共几个数字:"))
            for i in range(n):
                p = str(i + 1)
                d = "请输入第" + p + "个数字:"
                print(d)
                a = int(input())
                if check_input_type_int(a):
                    c = a + c
            n = c / n
            print("以上数据的平均数是:",n)
        if indoor == "2":
            c = 0
            n = int(input("请输入有共几个数字:"))
            for i in range(n):
                p = str(i + 1)
                d = "请输入第" + p + "个数字:"
                print(d)
                a = int(input())
                if check_input_type_int(a):
                    if c < a:
                        c = a
            print("这些数字的最大值是:",c)
        if indoor == "3":
            c = 0
            n = int(input("请输入有共几个数字:"))
            for i in range(n):
                p = str(i + 1)
                d = "请输入第" + p + "个数字:"
                print(d)
                a = int(input())
                if check_input_type_int(a):
                    if i == 0:
                        c = a
                    elif c > a:
                        c = a
                else:
                    print("谁让你这么输入的,数据不对o((>ω< ))o")
            print("这些数字的最小值是:",c)
        if indoor == "4":
            print("从大到小为'big',从小到大为'small'")
            s = input()
            if check_input_type_str(s):
                if s == "big":
                    d = "请输入一组数字，用空格隔开:"
                    print(d)
                    lines = input()
                    a = len(lines)
                    lines = [int(num) for num in lines.split(" ")]
                    sorted_list = bubble_sort(lines)
                    print("从大到小排列的结果是：", sorted_list)
                if s == "small":
                    d = "请输入一组数字，用空格隔开:"
                    print(d)
                    lines = input()
                    a = len(lines)
                    num_list = [int(num) for num in lines.split(" ")]
                    sorted_list = bubble(num_list)
                    print("从小到大排列的结果是：", sorted_list)
            if not check_input_type_str(s):
                print("谁让你这么输入的,数据不对o((>ω< ))o")
        if indoor == "5":
            print("计算前三名请输入'three',计算前十名请输入'ten'")
            li = input("请输入:")
            if li == "three":
                d = "请输入一组数字，用空格隔开:"
                print(d)
                lines = input()
                a = len(lines)
                if a >= 3:
                    num_list = [int(num) for num in lines.split(" ")]
                    sorted_list = third(num_list)
                    top_three = sorted_list[-3:]
                    print("前三名是：", top_three)
                else:
                    print("输入数量不够,再试试吧")
            elif li == "ten":
                d = "请输入一组数字，用空格隔开（必须有十个以上）:"
                print(d)
                lines = input()
                a = len(lines)
                if a >= 10:
                    num_list = [int(num) for num in lines.split(" ")]
                    sorted_list = bubble_sort(num_list)
                    top_ten = sorted_list[-10:]
                    print("前十名是：", top_ten)
                else:
                    print("输入数量不够,再试试吧")
        #菜单,550W
        if indoor == "6":
            password = input("请输入密码(输入'h'获取密码提示):")
            if password == "password":
                print("======   ======      ===     ==         ====        ==")
                print("=        =          =   =     =          ==         =")   
                print("=        =         =     =    =         =  =        =")
                print("==       ==        =     =     =       =    =      =")
                print("    ==       ==    =     =     =       =    =      =")
                print("    ==       ==    =     =       =    =      =    = ")
                print("   =         =     =     =       =    =      =    =")
                print("  =         =       =   =         =  =        =  =")
                print("==       ==          ===           ==         == ")
                print("            550W智能量子计算机[MOSS]")
            elif password == "h":
                print("偷偷的告诉你:密码是'password'")

        if indoor == "7":
            symbol = input("请输入运算符号(输入'加 减 乘 除'即可):")
            if symbol == "加":
                n1 = int(input("请输入第一个加数:"))
                n2 = int(input("请输入第二个加数:"))
                print(n1 + n2)
            elif symbol == "减":
                n1 = int(input("请输入第一个减数:"))
                n2 = int(input("请输入第二个减数:"))
                print(n1 - n2)
            elif symbol == "乘":
                n1 = int(input("请输入第一个乘数:"))
                n2 = int(input("请输入第二个乘数:"))
                print(n1 * n2)
            elif symbol == "除":
                n1 = int(input("请输入第一个除数:"))
                n2 = int(input("请输入第二个除数:"))
                print(n1 / n2)
            else:
                print("手滑了么，输错了，再试一次吧(●'◡'●)")
    if not check_input_type_str(indoor):
        print("输错了,输错了(* ￣︿￣)")
    
    
print("再见了ヾ(￣▽￣)Bye~Bye~")