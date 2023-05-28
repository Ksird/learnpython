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


practice_2_7()
