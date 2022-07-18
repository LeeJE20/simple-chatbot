# 프로젝트 이름
Simple Chatbot

## 프로젝트 목적
<!--
프로젝트에 대해 간단하게 설명하는 내용을 포함하는 것이 좋다.

이 프로젝트는 무엇을 위한 것인가
어떤 문제를 해결할 수 있는가
왜 이 프로젝트가 유용한가
어떤 사람들이 이 프로젝트를 사용하면 좋은가
이 프로젝트는 어떻게 작동하는가
-->

fastapi를 이용해 간단한 챗봇 구현
참고: https://github.com/ukairia777/tensorflow-nlp-tutorial
사용 데이터: https://github.com/songys/Chatbot_data

## 동작 과정
1.  학습시킬 질문(Q)과 응답(A) 데이터셋을 준비한다.
2.  Q와 A에 대해 임베딩(Q를 벡터화한것)을 구해둔다.
3.  입력값의 임베딩을 구한다.
4.  Q와 입력값의 임베딩을 비교(코사인 유사도) -> 입력값과 가장 비슷한 Q에 해당하는 A를 출력

## 기능 설명
1. [POST] /insert
    - db에 데이터 저장
2. [GET] /chat/simple?question={}
    - 질문을 보내면 응답받을 수 있음
<!--
## 결과 화면
-->

## 환경
<!-- 기술 스택 -->
### 주요 내역
- Ubuntu 20.04.4 LTS
- Python 3.8.10
    - sentence-transformers==2.2.2
        - 사용 모델: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
    - fastapi==0.78.0
    - SQLAlchemy==1.4.39
- mysql 8.0.29

### pip freeze 내역
```
absl-py==1.0.0
anyio==3.6.1
argon2-cffi==21.3.0
argon2-cffi-bindings==21.2.0
asttokens==2.0.5
astunparse==1.6.3
attrs==21.4.0
backcall==0.2.0
beautifulsoup4==4.11.1
bleach==5.0.0
cachetools==5.1.0
certifi==2019.11.28
cffi==1.15.0
chardet==3.0.4
click==8.1.3
cryptography==37.0.4
cycler==0.11.0
dbus-python==1.2.16
debugpy==1.6.0
decorator==5.1.1
defusedxml==0.7.1
entrypoints==0.4
executing==0.8.3
fastapi==0.78.0
fastjsonschema==2.15.3
filelock==3.7.1
flatbuffers==1.12
fonttools==4.33.3
gast==0.4.0
google-auth==2.6.6
google-auth-oauthlib==0.4.6
google-pasta==0.2.0
greenlet==1.1.2
grpcio==1.46.3
h11==0.13.0
h5py==3.6.0
huggingface-hub==0.8.1
idna==2.8
importlib-metadata==4.11.4
importlib-resources==5.7.1
ipykernel==5.1.1
ipython==8.3.0
ipython-genutils==0.2.0
ipywidgets==7.7.0
jedi==0.17.2
Jinja2==3.1.2
joblib==1.1.0
jsonschema==4.5.1
jupyter==1.0.0
jupyter-client==7.3.1
jupyter-console==6.4.3
jupyter-core==4.10.0
jupyter-http-over-ws==0.0.8
jupyterlab-pygments==0.2.2
jupyterlab-widgets==1.1.0
keras==2.9.0
Keras-Preprocessing==1.1.2
kiwisolver==1.4.2
libclang==14.0.1
Markdown==3.3.7
MarkupSafe==2.1.1
matplotlib==3.5.2
matplotlib-inline==0.1.3
mistune==0.8.4
nbclient==0.6.3
nbconvert==6.5.0
nbformat==4.4.0
nest-asyncio==1.5.5
nltk==3.7
notebook==6.4.11
numpy==1.22.4
oauthlib==3.2.0
opt-einsum==3.3.0
packaging==21.3
pandas==1.4.3
pandocfilters==1.5.0
parso==0.7.1
pexpect==4.8.0
pickleshare==0.7.5
Pillow==9.1.1
prometheus-client==0.14.1
prompt-toolkit==3.0.29
protobuf==3.19.4
psutil==5.9.1
ptyprocess==0.7.0
pure-eval==0.2.2
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.21
pydantic==1.9.1
Pygments==2.12.0
PyGObject==3.36.0
PyMySQL==1.0.2
pyparsing==3.0.9
pyrsistent==0.18.1
python-apt==2.0.0+ubuntu0.20.4.7
python-dateutil==2.8.2
pytz==2022.1
PyYAML==6.0
pyzmq==23.0.0
qtconsole==5.3.0
QtPy==2.1.0
regex==2022.7.9
requests==2.22.0
requests-oauthlib==1.3.1
requests-unixsocket==0.2.0
rsa==4.8
scikit-learn==1.1.1
scipy==1.8.1
Send2Trash==1.8.0
sentence-transformers==2.2.2
sentencepiece==0.1.96
six==1.14.0
sniffio==1.2.0
soupsieve==2.3.2.post1
SQLAlchemy==1.4.39
stack-data==0.2.0
starlette==0.19.1
tensorboard==2.9.0
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
tensorflow==2.9.1
tensorflow-estimator==2.9.0
tensorflow-io-gcs-filesystem==0.26.0
termcolor==1.1.0
terminado==0.15.0
threadpoolctl==3.1.0
tinycss2==1.1.1
tokenizers==0.12.1
torch==1.7.1+cu110
torchaudio==0.7.2
torchvision==0.8.2+cu110
tornado==6.1
tqdm==4.64.0
traitlets==5.2.1.post0
transformers==4.20.1
typing_extensions==4.2.0
urllib3==1.25.8
uvicorn==0.18.2
wcwidth==0.2.5
webencodings==0.5.1
Werkzeug==2.1.2
widgetsnbextension==3.6.0
wrapt==1.14.1
zipp==3.8.0
```

## 실행/설치 방법
- 도커 이미지 만들기 (GPU)
    - 파이토치 버전은 환경에 맞게 해야함
    - `docker create fastapi-tf-torch-gpu`

- 도커 실행
    - `docker compose up`

- /app/conn에 secrets.json 만들기
```json
{
    "DB":{
        "name": "mysql+pymysql",
        "user": "root",
        "password": "1234",
        "host": "cb_db",
        "port": 3306,
        "dbconn":"test_db"
    }
}
```

- mysql에 접속해서 test_db 만들기

- test_db에 테이블 만들기
```ddl
-- test_db.small_talk definition

CREATE TABLE `small_talk` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Q` text NOT NULL,
  `A` text NOT NULL,
  `embedding` json NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47302 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

```ddl
CREATE TABLE `test` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `number` int NOT NULL,
  `json_data` json DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

- 명령어 실행
    - `uvicorn --host=0.0.0.0 --port 8000 main:app`

- [POST] localhost:8000/insert 로 데이터 학습
- [GET] localhost:8000/chat/simple?question={} 로 질의
    + Request URL: `http://localhost:8000/chat/simple?question=점심 뭐먹지`
    + Response body: `"맛있는 거 드세요."`


<!--
프로젝트를 설치, 사용하기 위해 필요한 전제조건이 있는가
어떻게 설치, 사용, 테스트하는가
설치 가이드 문서는 어디에 있는가
-->

<!--
## 저작권/라이선스

어떤 라이선스로 배포되는가?
상세한 라이선스 정보는 어디에서 확인할 수 있는가
프로젝트를 사용함에 있어 제약 조건이 있는가(특허, 상업적 사용)
-->

<!--
## 외부 리소스 정보

프로젝트 내에 포함된 외부의 코드나 리소스의 정보
각각의 출처 및 배포 라이선스는 무엇인가
-->

<!--
## 이슈사항
버그 등-->


