# 2.3.2 在字符串中使用变量
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"  # f字符串 format，通过吧或括号内的变量替换为其值来设置字符串的格式 ver>=3.6
print(full_name)
print(f"Hello, {full_name.title()}")

# 2.3.3 使用制表符或换行符来添加空白
print("Languages:\n\tPython\n\tC\n\tJavascript")  # \t 制表符输出八个字符

# 2.3.4 删除空白(不会改变原字符串)
favorite_language = " pyt hon "
favorite_language.rstrip()  # rstrip()，去除字符串末尾空白
favorite_language.lstrip()  # lstrip()，去除字符串开头空白
favorite_language.strip()  # strip()，去除字符串两边空白
