import subprocess
import sys
import os

test_file = sys.argv[1]

main_sub = subprocess.Popen([r"ans\main.exe"], stdin = subprocess.PIPE, stdout=subprocess.PIPE)
test_sub = subprocess.Popen([test_file], stdin = subprocess.PIPE, stdout=subprocess.PIPE)

with open("input.txt", "r", encoding = 'utf8') as file:
    for s in file.readlines():
        main_sub = subprocess.Popen([r"ans\main.exe"], stdin = subprocess.PIPE, stdout=subprocess.PIPE)
        test_sub = subprocess.Popen([test_file], stdin = subprocess.PIPE, stdout=subprocess.PIPE)

        print("===============================================")

        ans_out, ans_err = main_sub.communicate(s.encode())
        test_out, tes_err = test_sub.communicate(s.encode())
        ans_out = ans_out.decode('big5')
        test_out = test_out.decode('big5')
        
        while ans_out[-1] == "\n":
            ans_out = ans_out.removesuffix("\n")

        while test_out[-1] == "\n":
            test_out = test_out.removesuffix("\n")

        if ans_out != test_out:
            print("錯誤")
            print(f"測資： {s}")
            print(f"正確為：{ans_out}")
            print(f"您的輸入為：{test_out}")

        else:
            print("正確")
            print(f"測資： {s}")
            print(f"正確為：{ans_out}")
            print(f"您的輸入為：{test_out}")
        
        print("===============================================")
        print()

os.system("pause")