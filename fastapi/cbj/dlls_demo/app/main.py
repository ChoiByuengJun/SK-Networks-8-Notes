from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os

from config.cors_config import CorsConfig
from ensemble_method.controller.ensemble_method_controller import ensembleMethodRouter
from feature_engineering.controller.feature_engineering_controller import featureEngineeringRouter
from kmeans.controller.kmeans_controller import kMeansRouter
from mnist.controller.mnist_controller import mnistRouter
from model_regulation.controller.model_regulation_controller import modelRegulationRouter

load_dotenv()

app = FastAPI()

CorsConfig.middlewareConfig(app)

# APIRouter로 작성한 Router를 실제 main에 맵핑
# 결론적으로 다른 도메인에 구성한 라우터를 연결하여 사용할 수 있음
app.include_router(featureEngineeringRouter)
app.include_router(ensembleMethodRouter)
app.include_router(kMeansRouter)
app.include_router(mnistRouter)
app.include_router(modelRegulationRouter)

# HOST는 모두에 열려 있고
# FASTAPI_PORT를 통해서 이 서비스가 구동되는 포트 번호를 지정
if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
