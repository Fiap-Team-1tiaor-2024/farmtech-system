from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.get("/executar")
def rodar_script_r():
    try:
        # Executa o script R
        result = subprocess.run(['Rscript', 'src/backend/scripts/r/estatistica.R'], capture_output=True, text=True)
        # Verifica se houve erro na execução do script
        if result.returncode != 0:
            return {"error": "Erro ao executar o script R", "details": result.stderr}
        # Retorna a saída do script R
        return {"output": result.stdout}
    except Exception as e:
        return {"error": str(e)}