def practice_2_1():
    """
    简单消息：
    将一条消息赋给变量，并将其打印出来
    """
    mesage = "What are you doing?"
    print(mesage)


def practice_2_2():
    """
    多条简单消息：
    将一条变量赋给变量，并将其打印出来；
    再将变量的值修改为一条新消息，并将其打印出来
    """
    mesage = "This is the first message, then it will change!"
    print(mesage)
    mesage = "It was changed already!"
    print(mesage)


def practice_2_3():
    """
    个性化消息：
    用变量表示一个人的名字，并向其显示一条消息。
    显示的消息应非常简单，下面是一个例子。
    Hello Eric, would you like to learn some Python today?
    """
    name = "Eric"
    message = "would you like to learn some Python today?"
    print(f"Hello {name}, {message}")


def practice_2_4():
    """
    调整名字的大小写：
    用变量表示一个人的名字，在以小写、大写和首字母大写的方式显示这个人名。
    """
    name = "wANg zI Hao"
    print(f"{name.lower()}\n{name.upper()}\n{name.title()}")


def practice_2_5_6():
    """
    名言，名言2：
    找一句你钦佩的名人说的名言，将其姓名和名言打印出来。
    输出应该类似于下面这样（包括引号）。
    Albert Einstein once said, "A person who never made a mistake never tried
    anything new.
    """
    famous_person = "Albert Einstein"
    message = "A person who never made a mistake never tried anything new."
    print(f'{famous_person} once said, "{message}"')


def practice_2_7():
    """
    剔除人名中的空白：
    用变量表示一个人的名字，并在其开头和末尾都包含一些空白字符。
    务必至少使用字符组合"\t"和"\n"各一次。
    打印这个人名，显示其开头和末尾的空白。
    然后，分别使用剔除函数lstrip()、rstrip()和strip()对人名进行处理，并将结果打印出来。
    """
    name = "\twang z\ni hao\t"
    print("原字符串：\n", name, "end")
    print("去除开头空白：\n", name.lstrip(), "(end)", sep="")
    print("去除末尾空白：\n", name.rstrip(), "(end)", sep="")
    print("去除两边空白：\n", name.strip(), "(end)", sep="")


def practice_2_8():
    """
    数字8：
    编写四个表达式，分别使用加法、减法、乘法和除法运算，但结果都是数字8.
    为使用函数调用print()来显示结果，务必将这些表达式用圆括号括起来。
    也就是说，你应该编写四行类似于下面的代码：
    print(5+3)
    输出应为四行，其中每行都只包含数字。
    """
    print(5 + 3)
    print(9 - 1)
    print(2 * 4)
    print(16 / 2)


def practice_2_9():
    """
    最喜欢的数：
    用一个变量来表示你最喜欢的数，再使用这个变量创建一条消息，指出你最喜欢的数是什么，然后
    将这条消息打印出来。
    """
    number = 100
    print(f"最喜欢的数是{number}")


def practice_3_1():
    """
    姓名：
    将一些朋友的姓名储存在一个列表中，并将其命名为names。
    依次访问该列表中的每个元素，从而将每个朋友的姓名打印出来。
    """
    names = ['xiuzui', 'abin', 'daot']
    print(names[0])
    print(names[1])
    print(names[-1])


def practice_3_2():
    """
    问候语：
    继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。
    每条消息都包含相同的问候语，但抬头为相应朋友的姓名
    """
    names = ['xiuzui', 'abin', 'daot']
    print(f"Hello, {names[0]}")
    print(f"Hello, {names[1]}")
    print(f"Hello, {names[-1]}")


def practice_3_3():
    """
    自己的列表：
    想想你喜欢的通勤方式。如骑摩托车或开汽车，并创建一个包含多种方式的列表。
    根据该列表打印一系列有关这些通勤方式的宣言，下面是一个例子。
    I would like to own a Honda motorcycle.
    """
    commute = ['walk', 'car', 'motorcycle', 'bus', 'subway']
    for i in commute:
        print(f"I would like to {i}")


practice_3_3()
