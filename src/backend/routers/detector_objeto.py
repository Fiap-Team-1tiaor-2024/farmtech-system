# filepath: c:\Dev\Projetos\FIAP\Fase 7\farmtech-system\src\backend\routers\detector_objeto.py
import os
import subprocess
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse # Importar FileResponse
import glob # Para listar arquivos

router = APIRouter()

YOLOV5_DIR = "/main/yolov5"
YOLO_EXAMPLE_IMAGES_DIR = os.path.join(YOLOV5_DIR, "data", "images")
# Caminho base onde os resultados da detecção dos exemplos são salvos
YOLO_EXAMPLE_RESULTS_BASE_DIR = os.path.join(YOLOV5_DIR, "runs", "detect")
YOLO_EXAMPLE_RUN_NAME = "api_example_detection_run" # Deve ser o mesmo --name usado no detect.py

@router.get('/detector_objeto_exemplos_yolo')
def executar_exemplos_yolo():
    # ... (código existente do endpoint, sem alterações aqui) ...
    weights_name = "yolov5s.pt"
    detect_script_path = os.path.join(YOLOV5_DIR, "detect.py")

    if not os.path.exists(YOLO_EXAMPLE_IMAGES_DIR) or not os.listdir(YOLO_EXAMPLE_IMAGES_DIR):
        raise HTTPException(status_code=404, detail=f"Diretório de imagens de exemplo do YOLOv5 '{YOLO_EXAMPLE_IMAGES_DIR}' está vazio ou não encontrado no container.")

    command = [
        "python", detect_script_path,
        "--weights", weights_name,
        "--img", "640",
        "--conf-thres", "0.25",
        "--source", YOLO_EXAMPLE_IMAGES_DIR,
        "--project", YOLO_EXAMPLE_RESULTS_BASE_DIR,
        "--name", YOLO_EXAMPLE_RUN_NAME,
        "--exist-ok"
    ]
    
    try:
        process = subprocess.run(command, capture_output=True, text=True, check=False, cwd=YOLOV5_DIR)
        output_dir = os.path.join(YOLO_EXAMPLE_RESULTS_BASE_DIR, YOLO_EXAMPLE_RUN_NAME)

        if process.returncode != 0:
            return {
                "status": "error",
                "message": "Erro durante a detecção YOLOv5 nos exemplos.",
                "command_executed": " ".join(command),
                "stdout": process.stdout,
                "stderr": process.stderr,
                "returncode": process.returncode,
                "results_expected_in": output_dir
            }
        
        # Listar as imagens processadas para retornar ao frontend
        processed_images = []
        if os.path.exists(output_dir):
            # Lista apenas arquivos .jpg e .png (YOLOv5 geralmente salva como .jpg)
            processed_images = [f for f in os.listdir(output_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        return {
            "status": "success",
            "message": "Detecção YOLOv5 nos exemplos concluída.",
            "command_executed": " ".join(command),
            "stdout": process.stdout,
            "stderr": process.stderr,
            "results_saved_to_container_path": output_dir,
            "processed_image_filenames": processed_images # Nova chave
        }
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail=f"Erro: 'python' ou '{detect_script_path}' não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")


@router.get("/yolo_example_image/{image_name}")
async def get_imagem_yolo_processada(image_name: str):
    """
    Serve uma imagem processada da pasta de resultados dos exemplos YOLO.
    """
    image_path = os.path.join(YOLO_EXAMPLE_RESULTS_BASE_DIR, YOLO_EXAMPLE_RUN_NAME, image_name)
    
    if not os.path.isfile(image_path):
        raise HTTPException(status_code=404, detail="Imagem não encontrada.")
    
    # Determinar o media type com base na extensão do arquivo
    media_type = "image/jpeg"
    if image_name.lower().endswith(".png"):
        media_type = "image/png"
    
    return FileResponse(image_path, media_type=media_type)