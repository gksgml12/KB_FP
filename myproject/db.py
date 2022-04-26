import pymysql

db=None
try:
    #DB 호스트 정보에 맞게 입력해주세요.
    db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='ab97826431',
            db='kb_finaldb',
            charset='utf8'
    )
    print("DB connection success")
    
except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()
        print("DB close success")
