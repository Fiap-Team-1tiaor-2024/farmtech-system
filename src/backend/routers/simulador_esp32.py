import json
import random
import time

import boto3
from decouple import config
from fastapi import APIRouter, HTTPException, Request

QUEUE_URL = config('AWS_SQS_QUEUE_URL')
REGIAO = config('AWS_REGION', 'us-east-1')

sqs = boto3.client(
    'sqs',
    region_name=REGIAO,
    aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
)

router = APIRouter()


@router.post('/simulador')
def simulador_esp32():
    dados = gerar_dados()
    enviar_mensagem(dados)
    time.sleep(3)

    return {
        'status': 'success',
        'message': 'Simulador de ESP32 iniciado. Dados serão enviados para a fila SQS.',
    }


def gerar_dados():
    return {
        'sensor_id': 'esp32-001',
        'temperatura': round(random.uniform(18.0, 35.0), 2),
        'umidade': round(random.uniform(40.0, 85.0), 2),
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
    }


def enviar_mensagem(dados):
    response = sqs.send_message(
        QueueUrl=QUEUE_URL, MessageBody=json.dumps(dados)
    )
    print(f"✅ Mensagem enviada! ID: {response['MessageId']}")
