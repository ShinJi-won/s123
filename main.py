from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from db import engine
from models import Base
from routers import predict

app = FastAPI()

@app.get("/health", status_code=status.HTTP_200_OK, tags=["Health"])
def health_check():
    """
    ALB 헬스체크용 기본 엔드포인트
    단순히 서버가 살아있는지 확인
    """
    return {"status": "healthy", "service": "AI Image Classifier API"}
