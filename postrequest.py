import requests
import json

if __name__ == "__main__":

    url = 'http://127.0.0.1:5000/postrequest' #ของเรา
    myobj = {'message_key': 'message_val'}

    # url = 'http://10.71.160.33:5001/postrequest'#ของอาจารย์
    # myobj = {'name': 'Athitiya'}
    
    # url = 'http://192.168.205.233:8080/postrequest'#ของเพิ่อนแต่ติดไฟล์วอร์
    # myobj = {'Hi': 'Wanita'}

    x = requests.post(url, data = json.dumps(myobj))

    print(x.text)
 