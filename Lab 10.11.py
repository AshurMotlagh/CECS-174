empty_dic = {}
file_name = input("Enter the input file name: ")
file = open(file_name)
line = file.readline()
num = 0
while line != '':
    for wd in line:
        if wd.upper().isalpha():
            num += 1
            if wd.upper() in empty_dic:
                empty_dic[wd.upper()] += 1
            else:
                empty_dic[wd.upper()] = 1
    line = file.readline()

for wd2 in sorted(empty_dic):
    number = (empty_dic[wd2]/num) * 100
    print(wd, '%.2f' % number, '%')