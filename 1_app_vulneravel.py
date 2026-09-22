import hashlib
import os
import pickle
import sqlite3
import subprocess
 
# --- VULNERABILIDADE 1: Credencial "hardcoded" no código ---
DB_PASSWORD = "admin123"
 
 
def conectar_banco():
    conn = sqlite3.connect("usuarios.db")
    return conn
 
 
# --- VULNERABILIDADE 2: SQL Injection (concatenação de string) ---
def buscar_usuario(nome_usuario):
    conn = conectar_banco()
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome = '" + nome_usuario + "'"
    cursor.execute(query)
    return cursor.fetchall()
 
 
# --- VULNERABILIDADE 3: Uso de algoritmo de hash fraco (MD5) ---
def gerar_hash_senha(senha):
    return hashlib.md5(senha.encode()).hexdigest()
 
 
# --- VULNERABILIDADE 4: Execução de comando de SO com entrada do usuário ---
def listar_arquivos(diretorio_usuario):
    comando = "ls " + diretorio_usuario
    resultado = os.popen(comando).read()
    return resultado
 
 
# --- VULNERABILIDADE 5: subprocess com shell=True ---
def ping_host(host):
    return subprocess.call("ping -c 1 " + host, shell=True)
 
 
# --- VULNERABILIDADE 6: Desserialização insegura (pickle) ---
def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, "rb") as f:
        return pickle.load(f)
 
 
if __name__ == "__main__":
    print(buscar_usuario("teste"))