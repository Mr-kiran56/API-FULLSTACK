# from fastapi import FastAPI, status, HTTPException
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from pydantic import BaseModel
# from typing import Optional
# import time

# app = FastAPI()

# class Blog(BaseModel):
#     title: str
#     description: str
#     published: bool 

# # Database connection
# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost',
#             database='FastAPI',
#             user='postgres',
#             password='KIRAN5656@',
#             cursor_factory=RealDictCursor
#         )
#         cursor = conn.cursor()
#         print("Database connection successful")
#         break
#     except Exception as error:
#         print("Connection to the database failed!!")
#         print("Error:", error)
#         time.sleep(2)


# @app.post('/blogs', status_code=status.HTTP_201_CREATED)
# def Add_Post(request: Blog):
#     cursor.execute(
#         """INSERT INTO blogs(title, description, published) 
#            VALUES (%s, %s, %s) RETURNING *""",
#         (request.title, request.description, request.published)
#     )
#     new_post = cursor.fetchone()
#     conn.commit()

#     if not new_post:
#         raise HTTPException(
#             status_code=status.HTTP_406_NOT_ACCEPTABLE,
#             detail="Unable to post the data"
#         )
#     return new_post


# @app.get('/blogs', status_code=status.HTTP_200_OK)
# def Get_Posts():
#     cursor.execute("""SELECT * FROM blogs""")
#     posts = cursor.fetchall()

#     if not posts:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Data not found!"
#         )

#     return posts

# @app.get('/blogs{id}',status_code=status.HTTP_200_OK)
# def Get_Post_By_ID(id:int):
#     cursor.execute("""SELECT * FROM blogs where id=%s""",(str(id),))
#     posts = cursor.fetchone()

#     if not posts:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Data with id={id} not found!"
#         )

#     return posts



# @app.put('/blogs{id}',status_code=status.HTTP_200_OK)
# def Update_Post_By_ID(id:int,request:Blog):
#     cursor.execute("""update blogs set title=%s,description=%s where id=%s returning *""",(request.title,request.description,str(id)))
#     conn.commit()
#     posts = cursor.fetchone()


#     if not posts:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Data with id={id} not found!"
#         )

#     return posts


# @app.delete('/blogs{id}',status_code=status.HTTP_200_OK)
# def Delete_Post_By_ID(id:int):
#     cursor.execute("""delete from blogs where id=%s returning *""",(str(id),))
#     conn.commit()
#     posts = cursor.fetchone()


#     if not posts:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Data with id={id} not found!"
#         )

#     return posts




    
