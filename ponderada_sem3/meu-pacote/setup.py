import subprocess
import sys

def setup_project():
    try:
        subprocess.check_call([sys.executable, "-m", "poetry", "install"])
        subprocess.check_call(["docker-compose", "up", "-d"])

        print("Projeto configurado e em execução!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar o projeto: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_project()