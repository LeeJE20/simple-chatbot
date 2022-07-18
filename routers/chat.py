"""
유저의 채팅 입력에 대한 응답 반환
"""

from fastapi import APIRouter, Depends, HTTPException, Request
from conn.db_class import SmallTalk
from pydantic import BaseModel

import numpy as np
import pandas as pd
from numpy import dot
from numpy.linalg import norm
import urllib.request
from sentence_transformers import SentenceTransformer

class Question(BaseModel):
    question : str

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)

# 모델 불러오기
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')


global train_data
train_data = pd.DataFrame()

# 두 개의 벡터로부터 코사인 유사도를 구하는 함수 cos_sim
def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))


@router.get("/simple")
async def return_answer(request: Request, question: str):
    global train_data

    # 유저 입력 확인
    print(question)

    # DB 세션
    session = request.state.db_conn

    # train_data가 없으면 DB에서 불러오기   
    if (train_data.empty):
        contents = session.query(SmallTalk).all()

        Q = []
        A = []
        embedding = []

        for i in range(len(contents)):
            Q.append(contents[i].Q)
            A.append(contents[i].A)
            embedding.append(list(contents[i].embedding))
            
        train_data = pd.DataFrame({"Q":Q,
                        "A":A,
                        "embedding":embedding})
    # 유저 입력에 대한 임베딩 계산
    q_embedding = model.encode(question)

    # 기존 임베딩과 비교하여 가장 유사한 응답 출력
    train_data['score'] = train_data.apply(lambda x: cos_sim(x['embedding'], q_embedding), axis=1)
    answer = train_data.loc[train_data['score'].idxmax()]['A']
    print(answer)
    return answer