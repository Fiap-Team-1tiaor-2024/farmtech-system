from fastapi import APIRouter

import subprocess

router = APIRouter()

R_EXECUTAVEL = "C:/Dev/Linguagens/R-4.4.3/bin/Rscript.exe"
R_SCRIPT = "C:/Dev/Projetos/FIAP/Fase 7/farmtech-system/src/estatistica/r/estatistica.r"

@router.post("/executar")
def rodar_script_r():
    try:
        result = subprocess.run(
            [R_EXECUTAVEL, R_SCRIPT],
            capture_output=True,
            text=True,
            check=True
        )
        print("Saída do R:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("R retornou erro:")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
