import os
import subprocess

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse

router = APIRouter()

script_path = '/app/estatistica/r/estatistica.r'

R_SCRIPT_WORKING_DIR = '/app/estatistica'

CSV_OUTPUT_DIR_RELATIVE_TO_APP = (
    'estatistica/r/csv'  # Usado para servir os arquivos via GET
)
ABSOLUTE_CSV_OUTPUT_DIR = os.path.join('/app', CSV_OUTPUT_DIR_RELATIVE_TO_APP)


@router.post('/executar')
def rodar_script_r():
    try:
        result = subprocess.run(
            ['Rscript', script_path],
            capture_output=True,
            text=True,
            check=True,
            cwd=R_SCRIPT_WORKING_DIR,  # Define o diretório de trabalho para o script R
        )
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stdout': e.stdout, 'stderr': e.stderr}
    except FileNotFoundError:   # Caso Rscript não seja encontrado
        return {
            'status': 'error',
            'stderr': 'Comando Rscript não encontrado. Verifique se R está instalado no container backend e no PATH.',
        }


@router.get('/csv/{filename}')
def get_csv(filename: str):
    # Os arquivos CSV são gerados pelo script R em R_SCRIPT_WORKING_DIR/r/csv/
    # que corresponde a ABSOLUTE_CSV_OUTPUT_DIR
    file_path = os.path.join(ABSOLUTE_CSV_OUTPUT_DIR, filename)
    if not os.path.exists(file_path):
        # Adiciona mais detalhes ao log para depuração
        print(f'Tentativa de acesso ao arquivo: {file_path}')
        print(
            f"Conteúdo de {ABSOLUTE_CSV_OUTPUT_DIR}: {os.listdir(ABSOLUTE_CSV_OUTPUT_DIR) if os.path.exists(ABSOLUTE_CSV_OUTPUT_DIR) else 'Diretório não existe'}"
        )
        raise HTTPException(
            status_code=404,
            detail=f"Arquivo '{filename}' não encontrado em '{ABSOLUTE_CSV_OUTPUT_DIR}'. Verifique se o script R foi executado e gerou os arquivos.",
        )
    return FileResponse(file_path, media_type='text/csv', filename=filename)
