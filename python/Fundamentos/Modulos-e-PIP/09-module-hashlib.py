import hashlib 
# Todos os algoritmos disponíveis
print(hashlib.algorithms_available)
# Algoritmos disponível de acordo com o SO
print(hashlib.algorithms_guaranteed)

algorithm = hashlib.sha256()
# Hash que é usado para criptografia do algoritmo
print(algorithm.digest())

# Criptografia de textos com Sha256
sha = hashlib.sha256()
message = "A melhor forma de prever o futuro é criá-lo".encode()
sha.update(message)
print(sha.hexdigest())

# Criptografia de textos com MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())



"""
Duvida que ficou da aula:
Sim, mas como vou voltar, como a outra pessoa recebe a msg:
(Resposta chatGPT)
oa pergunta 👊 — aí está o ponto-chave: hash não é criptografia reversível.

👉 Quando você usa hashlib.sha256() ou hashlib.md5(), está aplicando uma função de hash criptográfica, que transforma a mensagem em uma sequência única (impressão digital).

⚠️ Características:

Unidirecional → não dá para “voltar” do hash para a mensagem original.

Determinístico → a mesma mensagem sempre gera o mesmo hash.

Pequenas mudanças na mensagem geram hashes totalmente diferentes.

Então como “saber a mensagem”?

A resposta é: não sabe.
O hash só serve para comparação.

Exemplo de uso prático:

Você guarda no banco de dados o hash da senha do usuário (não a senha real).

Quando ele faz login, você aplica o mesmo hash à senha digitada.

Se o hash bater com o que está no banco → é a senha correta.

Isso garante que nem mesmo o administrador do sistema saiba qual é a senha original.

👉 Se a ideia é recuperar a mensagem original, aí não é hash, e sim criptografia (AES, RSA etc.), porque criptografia é reversível (com a chave certa).
"""