import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    ## basic
    # subprocess.run(["ls", "-ltr"])
    # subprocess.run(["python", "python_script101.py","--x","8"])

    ## use output of subprocess
    # pro = subprocess.Popen(["python", "python_script101.py","--x","8"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # out, err = pro.communicate()
    # print(out.decode('utf-8').split("\n")[-2])


    ##HW สั่งรัน print python_script101.py 50 รอบ โดย x = 1,3,5,7,....
    #แล้วให้เอา output ของ xt มารวมกันแล้ว print ออกมา 

    sum = 0 
    round = 0
    for i in range(1, 100, 2):
            round +=1
            process1 = subprocess.Popen(["python", "python_script101.py", "--x",f'{i}'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process1.communicate()
            print(f"({round}) x = {i}")
            print(out.decode('utf-8'))
            sum += (i)
            
    print(f'   sum of xt = {(sum)*2}')



