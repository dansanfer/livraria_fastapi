from fastapi import FastAPI, HTTPException

#Lista, Dicionários, Bancos de Dados, etc
Livros = ["Hobbit", "O Senhor dos Anéis", "O Código Da Vinci"]

app = FastAPI()

#rota-inicial
@app.get("/")
async def home():
    return {"message": "Bem-vindo à API de Livros!"}

#listar-livros
@app.get("/livros")
async def listar_livros():
    return {"livros": Livros}

#adicionar-livro
@app.post("/livros")
async def adicionar_livro(livro: str):
    Livros.append(livro)
    return {"message":"Livro adicionado com Sucesso"}

#atualizar-livro
@app.put("/livros/{index}")
async def atualizar_livro(index: int, new_livro: str):
    if index > len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    Livros[index] = new_livro
    return {"message": "Livro atualizado com sucesso"}


#delete-livro
@app.delete("/livros/{index}")
async def deletar_livro(index: int):
    if index > len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    Livros.pop(index)
    return {"message": "Livro deletado com sucesso"}