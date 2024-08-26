import os
from dotenv import load_dotenv
from your_clickhouse_script import get_client

load_dotenv()

def test_get_client():
    CLICKHOUSE_HOST = os.getenv('CLICKHOUSE_HOST')
    CLICKHOUSE_PORT = os.getenv('CLICKHOUSE_PORT')
    CLICKHOUSE_USER = os.getenv('CLICKHOUSE_USER')
    CLICKHOUSE_PASSWORD = os.getenv('CLICKHOUSE_PASSWORD')

    client = get_client()

    assert client.host == CLICKHOUSE_HOST
    assert client.port == int(CLICKHOUSE_PORT)
    assert client.user == CLICKHOUSE_USER
    assert client.password == CLICKHOUSE_PASSWORD