from connection import s3_connection
from config import BUCKET_NAME

s3 = s3_connection()
s3.put_object(
    Bucket = BUCKET_NAME,
    Body = 'test',
    Key = 'test_img.jpg',
    ContentType = 'image/jpg'
)