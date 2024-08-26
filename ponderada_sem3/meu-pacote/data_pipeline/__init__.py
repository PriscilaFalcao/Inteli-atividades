import random
from api import get_dog_facts
from data_processing import process_data, prepare_dataframe_for_insert

if __name__ == "__main__":
    # Gerar um número aleatório de 1 a 10
    random_number = random.randint(1, 10)

    # Obter os dados da API de fatos sobre cachorros
    dog_facts = get_dog_facts(random_number)

    # Processar os dados
    filename = process_data(dog_facts)
    print(f"Arquivo Parquet criado: {filename}")

    # Preparar o DataFrame para inserção
    df_prepared = prepare_dataframe_for_insert(dog_facts)
    print(df_prepared)