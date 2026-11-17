# Versão corrigida: consulta parametrizada.
import sqlite3


def login(usuario, senha):
    conn = sqlite3.connect("usuarios.db")
    cur = conn.cursor()
    # Os valores vão como parâmetros, nunca concatenados ao SQL
    cur.execute(
        "SELECT 1 FROM usuarios WHERE usuario = ? AND senha = ?",
        (usuario, senha),
    )
    resultado = cur.fetchone()
    conn.close()
    return resultado is not None


if __name__ == "__main__":
    u = input("Usuário: ")
    s = input("Senha: ")
    print("Login OK" if login(u, s) else "Login negado")
