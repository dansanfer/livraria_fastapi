const API_URL = "http://localhost:8030/livros/";

const listaLivros = document.getElementById("LivrosList");
const formLivro = document.getElementById("formLivro");

async function carregarLivros() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error("Erro ao buscar livros");
    
    const livros = await response.json();
    listaLivros.innerHTML = "";

    livros.forEach((livro) => {
      listaLivros.innerHTML += `
        <div class="livro">
          <div>
            <strong>Título:</strong> ${livro.titulo}<br>
            <strong>Autor:</strong> ${livro.autor}<br>
            <strong>Ano de Publicação:</strong> ${livro.ano_publicacao}
          </div>

          <div class="acoes">
            <button onclick="removerLivro(${livro.id})">
              Remover
            </button>
          </div>
        </div>
      `;
    });
  } catch (error) {
    console.error("Erro ao carregar livros:", error);
  }
}

async function removerLivro(id) {
  try {
    const response = await fetch(`${API_URL}${id}`, {
      method: "DELETE",
    });

    if (!response.ok) throw new Error("Erro ao remover o livro");
    carregarLivros();
  } catch (error) {
    console.error("Erro ao remover:", error);
  }
}

if (formLivro) {
  formLivro.addEventListener("submit", async (event) => {
    event.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;
    const ano = Number(document.getElementById("ano_publicacao").value);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          titulo: titulo,
          autor: autor,
          ano_publicacao: ano,
        }),
      });

      if (!response.ok) {
        const erroDetalhe = await response.text();
        console.error("Erro retornado pela API:", erroDetalhe);
        throw new Error("Erro ao cadastrar o livro");
      }

      formLivro.reset();
      carregarLivros();
    } catch (error) {
      console.error("Erro no envio:", error);
    }
  });
}

carregarLivros();