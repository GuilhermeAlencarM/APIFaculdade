from pydantic import BaseModel
from typing import Optional

class produto(BaseModel):
  id: Optional[int] = None
  nome: str
  preco: float
  
  
class camisa(produto):
  tamanho: str
  estampa: bool
  
  
class caneca(produto):
  material: str
  capacidade: str
  

class quadrinho(produto):
  marca: str
  distribuidora: str
  
  
  
  
  