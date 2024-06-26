<h1 align='Center'>meme-aleatorio</h1>

<div align="Center">
    <img src="https://img.shields.io/github/license/ericshantos/meme-aleatorio.svg" alt="Bagde LISENCE">
    <img src="https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg" alt="Bagde MarkDown">
    <a href = "https://github.com/pre-commit/pre-commit" >
        <img src ="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=​​​ pré-commit" alt ="pré-commit" style = "max-width:100%;" />
    </a>
    <img src="https://img.shields.io/github/commits-since/ericshantos/meme-aleatorio/e6910d9.svg" alt="Bagde Commits">
</div>

<br>

Esta é uma API Rest Flask que fornece acesso a memes aleatórios do site Memedroid. A API possui apenas um endpoint GET, que retorna um meme aleatório. Os memes são selecionados aleatoriamente do Memedroid e são fornecidos em formato JPEG.

<details>

<summary>Instalação</summary>

<br>

**IMPORTANTE**: É necessário Python 3.12 ou superior.

Para começar a desfrutar do meme-aleatorio, siga estas simples etapas de instalação:

1. **Clone o repositório:**
   Execute o seguinte comando para obter os arquivos do projeto em seu ambiente local:

```
git clone https://github.com/ericshantos/meme-aleatorio.git
```

2. **Crie um ambiente virtual:**
Utilize o seguinte comando para criar um ambiente virtual na pasta do projeto:

```
python -m venv venv
```

3. **Ative o ambiente virtual:**
Dependendo do seu sistema operacional, ative o ambiente virtual usando um dos seguintes comandos:
- Para Linux/Mac:
  ```
  source venv/bin/activate
  ```
- Para Windows:
  ```
  venv\Scripts\activate
  ```

4. **Instale as dependências:**
Utilize o seguinte comando para instalar as bibliotecas necessárias:

```
pip install -r requirements.txt
```

</details>

<details>

<summary>Convenções</summary>

## Conventional Commits 1.0.0

Esse projeto segue as diretrizes da [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). Para sabar mais, acesse o site.

</details>

<details>

<summary>Configurações</summary>


## Pré-commit

Após instalar as dependências do projeto, execulte o seguinte script para configurar o pre-commit
no seu ambiente local:

```
pre-commit install
```

Caso receba o seguinte retorno, é sinal que a instalação do pre-commit foi realizada com exito:

```
pre-commit installed at .git\hooks\pre-commit
```

## Execulção do projeto

Para rodar a API em sua máquina, no terminal, execulte o seguinte script no diretório raiz do projeto:

```
python run.py
```

</details>

<details>

<summary>Contribuições</summary>

<br>

Agradeço seu interesse em contribuir para este projeto! Por favor, leia as diretrizes de contribuição
abaixo antes de enviar sua contribuição. Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para
entrar em contato comigo.

### Como Contribuir

1. **Abra uma issue**: Se você encontrar um problema ou tiver uma ideia para uma nova funcionalidade, abra uma
issue descrevendo o problema ou a proposta. Isso me ajuda a manter o controle das alterações e a discutir
possíveis soluções.

2. **Trabalhe em uma branch**: Se você deseja contribuir com código, crie uma branch para sua alteração a partir
do branch principal (main, master ou outro). Isso ajuda a manter o código base limpo e facilita a revisão
de código.

  ```
  git checkout -b minha-contribuicao
  ```

3. **Faça suas alterações**: Faça as alterações necessárias no código, documentação ou outros recursos.

4. **Teste suas alterações**: Certifique-se de que suas alterações não quebraram o código existente.
Execute testes unitários, se disponíveis, e verifique se tudo funciona conforme o esperado.

5. **Envie um Pull Request (PR)**: Quando estiver pronto para enviar suas alterações, envie um PR para revisão.
Certifique-se de incluir uma descrição clara das alterações que você fez e quais problemas eles abordam.

6. **Revisão de código**: As contribuições serão revisadas por mim. Fique atento ao feedback e esteja disposto
a fazer alterações conforme necessário.

7. **Merge do PR**: Após a revisão e aprovação, seu PR será mesclado ao branch principal e suas alterações serão
incorporadas ao projeto.

### Diretrizes de Contribuição
- Siga os padrões de codificação do projeto.
- Mantenha as alterações focadas e concisas.
- Documente suas alterações, especialmente se afetarem a API pública ou a experiência do usuário.
- Se estiver adicionando novos recursos, forneça testes apropriados para eles.
- Se estiver resolvendo problemas, forneça uma descrição clara do problema e da solução proposta.
- Se estiver adicionando dependências, verifique se elas são necessárias e se estão de acordo com as políticas do projeto.
- Agradecemos sua contribuição para tornar este projeto ainda melhor!

### Problemas

Se você encontrar algum problema com o projeto ou tiver uma sugestão para melhorias, por favor
[abra uma issue](https://github.com/ericshantos/meme-aleatorio/issues) neste repositório.

</details>

<details>

<summary>Tecnologias utilizadas</summary>

- Linguagens de Programação:
  - Python

- Frameworks e Bibliotecas:
  - [Flask](https://flask.palletsprojects.com/en/3.0.x/): framework web.
  - [Pre-commit](docs/_source/pre-commit.rst): autoamtização de commits.
  - [Black](docs/_source/black.rst): formatação de código.
  - [Pylint](docs/_source/pylint.rst): conformidade do código com diretrizes estatísticas.
  - [Requests](docs/_source/requests.rst): requisições HTTP.
  - [Commitizen](docs/_source/commitizen.rst): customização de commits.
  - [PIL](docs/_source/PIL.rst): manipulação de imagens.
  - [Sphinx](docs/_source/sphinx.rst): documentação.
  - [BS4](docs/_source/bs4.rst):extrai dados de arquivos HTML e XML.
  - [Os](docs/_source//os.rst): Manipulação de arquivos e funcionalidades dependentes do sistema operacional.
  - [Io](docs/_source/io.rst): Manipulação de entrada/saída (I/O) em Python.
  - [Typing](docs/_source/typing.rst): Adição de anotações de tipo opcional ao código Python.

- Ferramentas de Desenvolvimento:
  - Visual Studio Code
  - Git

</details>

<details>

<summary>Contato</summary>

Para qualquer dúvida ou sugestão, entre em contato através do email ericshantos13@gmail.com.

</details>

<details>

<summary>Lincença</summary>

Este projeto é distribuído sob [MIT License](https://opensource.org/license/mit). Consulte o arquivo
[LICENSE](LICENSE) para obter mais informações.

</details>
