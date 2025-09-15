# SQL – Guia Completo

## 📌 O que é SQL?
- **SQL (Structured Query Language)** é a linguagem padrão para **criar, manipular e consultar** bancos de dados relacionais.
- Base de sistemas como: **MySQL, PostgreSQL, SQL Server, Oracle, SQLite**.
- Foco em **dados estruturados** em tabelas.

---

## 🏗️ Tipos de Comandos SQL

### 1. DDL (Data Definition Language) – Definição de Estrutura
- `CREATE DATABASE nome;`
- `CREATE TABLE tabela (...);`
- `ALTER TABLE tabela ADD coluna tipo;`
- `DROP TABLE tabela;`

### 2. DML (Data Manipulation Language) – Manipulação de Dados
- `INSERT INTO tabela (col1, col2) VALUES (v1, v2);`
- `UPDATE tabela SET coluna = valor WHERE condição;`
- `DELETE FROM tabela WHERE condição;`

### 3. DQL (Data Query Language) – Consulta
- `SELECT colunas FROM tabela;`
- Permite uso de filtros, ordenação, agrupamento e joins.

### 4. DCL (Data Control Language) – Controle de Acesso
- `GRANT` → concede permissões.
- `REVOKE` → remove permissões.

### 5. TCL (Transaction Control Language) – Transações
- `BEGIN` / `START TRANSACTION`
- `COMMIT` → confirma mudanças.
- `ROLLBACK` → desfaz mudanças.
- `SAVEPOINT` → cria ponto de restauração.

---

## 🔎 SELECT – O coração do SQL
```sql
SELECT colunas
FROM tabela
WHERE condição
GROUP BY coluna
HAVING condição_agregada
ORDER BY coluna ASC|DESC
LIMIT n OFFSET m;
x