from fastapi import APIRouter
from fastapi.responses import JSONResponse
from infra.database.database import SessionLocal    
import subprocess

router = APIRouter()

@router.post("/executar")
def rodar_script_r():
    try:
        result = subprocess.run(['Rscript', 'src/estatistica/r/estatistica.R'], capture_output=True, text=True)
        if result.returncode != 0:
            return JSONResponse(
                status_code=500,
                content={"error": "Erro ao executar o script R", "details": result.stderr}
            )
        return JSONResponse(content={"output": result.stdout})
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
