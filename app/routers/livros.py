from fastapi import APIRouter, HTTPException
from app.schemas.livro import LivroSchema
from app.database.connection import SessionLocal
from app.database.models import LivroModel
from app.schemas.livro import LivroCreate

from app.database.connection import get_db
from app.services import livro_service

router = APIRouter(
    prefix="/livros",
    tags=["livros"],
)

#listar-livros
@router.get("/")
async def listar_livros(
    db:Session = Depends(get_db)
):
  return livro_service.listar_livros(db)
 

#Adicionar Livros
@router.post("/")
async def adicionar_livro(livro: LivroCreate):
    db = SessionLocal()
    novo_livro = LivroModel(
        titulo = livro.titulo,
        autor = livro.autor,
        ano_publicacao = livro.ano_publicacao
    )
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    db.close()
    return{"message": "Livro adicionado com sucesso"}



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