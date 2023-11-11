from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import produto,camisa,caneca,quadrinho

app = FastAPI()


@app.get('/')
async def mensagem():
    return {'msg': 'Trabalho de Programação(API) - UNIMA'}


@app.get('/produtos')
async def get_produtos():
    return produtos


@app.get('/produtos/{produto_id}')
async def get_produtos(produto_id: int):
    try:
        produto = produtos[produto_id]
        return produto
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Produto não cadastrado.")
    
    
@app.post('/produtos/caneca')
async def post_produto(produto: caneca):
    next_id: int = len(produtos)+1
    produtos[next_id] = produto
    del produto.id
    return produto

@app.post('/produtos/camisa')
async def post_produto(produto: camisa):
    next_id: int = len(produtos)+1
    produtos[next_id] = produto
    del produto.id
    return produto

@app.post('/produtos/quadrinho')
async def post_produto(produto: quadrinho):
    next_id: int = len(produtos)+1
    produtos[next_id] = produto
    del produto.id
    return produto



produtos = {
    1: {
        "nome": "Caneca do Batman",
        "preco": 35,
        "material": "Porcelana",
        "capacidade": "350 ml"
    },
}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='127.0.0.1', port=8000,
                log_level='info', reload=True)
