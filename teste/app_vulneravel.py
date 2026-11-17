# Código DIDÁTICO com falha proposital (SQL Injection). Use só em laboratório.
import sqlite3


def login(usuario, senha):
    conn = sqlite3.connect("usuarios.db")
    cur = conn.cursor()
    # VULNERÁVEL: entrada do usuário concatenada na consulta
    query = f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND senha = '{senha}'"
    cur.execute(query)
    resultado = cur.fetchone()
    conn.close()
    return resultado is not None


if __name__ == "__main__":
    u = input("Usuário: ")
    s = input("Senha: ")
    print("Login OK" if login(u, s) else "Login negado")
