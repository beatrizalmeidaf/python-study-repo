import subprocess
import sys

result = subprocess.run([sys.executable, "-c", "print('olá')"])
print("\n")
#sys.executable é o caminho absoluto para o executável Python com o qual o programa foi originalmente invocado
#-c é um argumento que permite que passe uma string com um script Python para ser executado
#O script Python passado para -c é print('olá')

test = subprocess.run([sys.executable,"-c", "print('tudo bem?')"], capture_output=True, text=True)
print("stdout:", test.stdout)
print("stderr:", test.stderr)
print("\n")

erro = subprocess.run(
    [sys.executable, "-c", "raise ValueError('oops')"], capture_output=True, text=True
)
print("stdout:", erro.stdout)
print("\n")
print("stderr:", erro.stderr)