from fastapi import APIRouter, HTTPException
from app.schemas.livro import LivroSchema


router = APIRouter(
    prefix="/livros",
    tags=["livros"],
)

#Banco de Dados em memória
Livros = [
    LivroSchema(id=1, titulo="O Senhor dos Anéis", autor="J.R.R. Tolkien", ano_publicacao=1954),
    LivroSchema(id=2, titulo="1984", autor="George Orwell", ano_publicacao=1949),
]

#listar-livros
@router.get("/")
async def listar_livros():
    return {"livros": Livros}

#adicionar-livro
@router.post("/")
async def adicionar_livro(livro: LivroSchema):
    Livros.append(livro)
    return {"message":"Livro adicionado com Sucesso"}

#atualizar-livro
@router.put("/{index}")
async def atualizar_livro(index: int, livro: LivroSchema):
    if index > len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    Livros[index] = livro
    return {"message": "Livro atualizado com sucesso"}


#delete-livro
@router.delete("/{index}")
async def deletar_livro(index: int):
    if index > len(Livros) or index < 0:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    Livros.pop(index)
    return {"message": "Livro deletado com sucesso"}