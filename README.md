# SkyZero

SkyZero é uma aplicação para registro e cálculo de emissões de carbono com base em voos. Este projeto integra back-end
em Python, banco de dados Oracle.

## 🌐 Link do Front-End

Acesse o front-end do projeto em: [SkyZero](https://fiap-gs-skyzero.vercel.app/)

## Equipe

| **Nome**                | **RM**   |
|-------------------------|----------|
| **Allan Brito Moreira** | RM558948 |
| **Caio Liang**          | RM558868 |
| **Levi Magni**          | RM98276  |

## Estrutura do Projeto

- `main.py`: Arquivo principal do projeto.
- `scripts_sql/`: Pasta contendo os scripts SQL necessários para a configuração do banco de dados.
- `requirements.txt`: Arquivo contendo todas as dependências do projeto.

## Instruções de Configuração

1. **Instalação das Dependências**:
    Certifique-se de ter todas as dependências necessárias instaladas. Utilize o seguinte comando para instalar as dependências listadas no arquivo `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

2. **Configuração do Banco de Dados**:
    Certifique-se de que seu banco de dados está configurado corretamente. Se você não possui as tabelas da SkyZero, utilize os scripts SQL disponíveis na pasta `scripts_sql`.

    **Atenção**: Caso não possua as tabelas da SkyZero, utilize os scripts disponíveis na pasta `scripts_sql` para criá-las.

3. **Execução do Projeto**:
    Após configurar o banco de dados e instalar as dependências, execute o projeto com o seguinte comando:
    
    Verifique se o caminho do terminal está na raiz do projeto (SkyZero-Python)

    ```sh
    python main.py
    ```

3. **API**:
    API: https://deividfortuna.github.io/fipe/
    Autor: https://github.com/deividfortuna/fipe

## Instruções para Rodar o Projeto

1. **Clone o repositório**

  ```bash
  git clone https://github.com/CaioLiang/SkyZero-Python
  ```

  ```bash
  cd SkyZero-Python
  ```

## Contato

Para mais informações, acesse https://github.com/CaioLiang/SkyZero-Python