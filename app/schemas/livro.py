from pydantic import BaseModel, Field

# Schema base com os campos comuns de dados do livro
class LivroBase(BaseModel):
    titulo: str = Field(min_length=3, max_length=100)
    autor: str = Field(min_length=3, max_length=100)
    ano_publicacao: int

# Schema para CRIAR (POST): Não exige o ID, pois o banco gera sozinho
class LivroCreate(LivroBase):
    pass

# Schema para RESPONDER (GET, POST response): Inclui o ID gerado pelo banco
class LivroResponse(LivroBase):
    id: int

    class Config:
        from_attributes = True