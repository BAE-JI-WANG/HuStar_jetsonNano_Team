import pymysql
import plate_recognition

db_addr = pymysql.connect(
    user='team', 
    passwd='1234', 
    host='hustar-jetsonnano.crrje0xrfk2b.ap-northeast-2.rds.amazonaws.com', 
    db='Team1', 
    charset='utf8'
)

cursor = db_addr.cursor(pymysql.cursors.DictCursor)

insert = "insert into parkin_info(car_num,ent_date) values (%s,now(),%s)"
car_num = plate_recognition.result_chars
# img_name = plate_recognition.img_ori
cursor.execute(insert,car_num)
db_addr.commit()

result = cursor.fetchall()
result