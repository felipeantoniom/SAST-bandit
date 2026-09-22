import hashlib
import json
import os
import re
import sqlite3
 
# CORREÇÃO 1: credencial não fica mais hardcoded, vem de variável de ambiente
DB_PASSWORD = os.environ.get("DB_PASSWORD")
 
 
def conectar_banco():
    conn = sqlite3.connect("usuarios.db")
    return conn
 
 
# CORREÇÃO 2: uso de query parametrizada (evita SQL Injection)
def buscar_usuario(nome_usuario):
    conn = conectar_banco()
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome = ?"
    cursor.execute(query, (nome_usuario,))
    return cursor.fetchall()
 
 
# CORREÇÃO 3: troca de MD5 por SHA-256 com salt (via hashlib.pbkdf2_hmac)
def gerar_hash_senha(senha, salt):
    return hashlib.pbkdf2_hmac("sha256", senha.encode(), salt, 100_000).hex()
 
 
# CORREÇÃO 4: sem shell=True, sem concatenação, e com validação do diretório
# antes de usá-lo (whitelist: apenas letras, números, "_", "-")
def listar_arquivos(diretorio_usuario):
    if not re.fullmatch(r"[\w\-]+", diretorio_usuario):
        raise ValueError("Nome de diretório inválido")
    diretorio_seguro = os.path.basename(diretorio_usuario)
    return os.listdir(diretorio_seguro)
 
 
# CORREÇÃO 5: elimina a chamada de processo externo; usa biblioteca nativa
# (socket) em vez de invocar o comando "ping" do sistema operacional
def ping_host(host):
    if not re.fullmatch(r"[a-zA-Z0-9.\-]+", host):
        raise ValueError("Host inválido")
    import socket
 
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False
 
 
# CORREÇÃO 6: pickle substituído por JSON (formato seguro para dados não confiáveis)
def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)
 
 
if __name__ == "__main__":
    print(buscar_usuario("teste"))
