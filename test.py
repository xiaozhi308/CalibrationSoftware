# 原码转化为补码
def true2complement(str_bin):
    str_new = ""
    if str_bin[0] == "0":
        str_flash = str_bin
    else:
        for i in str_bin[1:]:
            if i == "0":
                str_new += "1"
            else:
                str_new += "0"
        str_flash = '0' + str_new  # 反码
    return str_flash
def number_handle():
    # infile = r'../DataVisualization/test.txt'
    infile = r'G:\pycharm_project\CalibrationSoftware\DataVisualization\test.txt'
    with open(infile) as f:
        s = f.read()
        for number in range(30, len(s) - 24, 6):
            # 字符串的处理
            m = s[number:number + 6]
            new_str_two = str.strip(m)
            new_str = new_str_two.split(" ")
            new_str = new_str[1] + new_str[0]
            # 转化成
            complement_binary = int(new_str, 16) - 1
            com_str = bin(complement_binary)
            com_bin_str = com_str[2:]
            bin_handle = true2complement(com_bin_str)
            bin_int_handle = int(bin_handle, 2) / 10
            bin_int_handle = - bin_int_handle
            print(bin_int_handle)

if __name__ == '__main__':
    number_handle()




