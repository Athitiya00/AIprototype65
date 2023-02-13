import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    ## basic
    subprocess.run(["ls", "-ltr"])
    subprocess.run(["python", "python_script101.py","--x","8"])

    ## use output of subprocess
    pro = subprocess.Popen(["python", "python_script101.py","--x","8"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = pro.communicate()
    print(out.decode('utf-8').split("\n")[-2])


    ##HW สั่งรัน print python_script101.py 50 รอบ โดย x = 1,3,5,7,....
    #แล้วให้เอา output ของ xt มารวมกันแล้ว print ออกมา 


    # for i in [2,5,6,8]:
    #     subprocess.run(["python", "python_script_101.py", "9", "--x", f"{i}", "--yval", "2"])
    

    # ## use output of subprocess
    # pro = subprocess.Popen(["ls", "-l"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # out, err = pro.communicate()
    # print(out.decode('utf-8'))


