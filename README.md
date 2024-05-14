<h1> Simple Todo </h1> 📋✏️

Bem-vindo ao meu primeiro projeto *CRUD*.  
Aqui pude estudar mais sobre a criação do *backend* de uma aplicação *web*.  
Utilizei o *framework Django* da linguagem *Python*.  
___
Fiz uso do protocolo *HTTP* com um conjunto de métodos de requisição para funções como  
adicionar, editar e remover conteúdo dentro de um banco de dados.
![Captura de tela 2024-05-12 235326](https://github.com/eniocharles/simple_todo/assets/120492104/0b002169-7563-4fdc-b500-9d725139a609)
> Imagem da tabela do *crud*.
___
<h2> Passo a passo do uso de métodos no Crud</h2>  
Bem, para iniciar vamos explicar sobre o padrão de arquitetura de software do django...  
A princípio o framework usa o padrão MVT derivado do MVC.  
Ele separa a lógica de negócios e a manipulação de dados (Model), a apresentação de dados e interação com o usuário (View) e a lógica de controle (Controller) em componentes distintos.  
A principal diferença entre o MVT e o MVC está na separação entre View e Template.  
No MVT, a View lida com a lógica de controle e a preparação dos dados, enquanto o Template é responsável pela apresentação visual desses dados.  
![Captura de tela 2024-05-13 223153](https://github.com/eniocharles/simple_todo/assets/120492104/d2fd9278-1e0d-4888-8be8-e2a22790b1ed)

+Model.
  -Representa a camada de acesso aos dados, semelhante ao Modelo no MVC. Ele define a estrutura 
  -dos dados e as operações que podem ser realizadas sobre eles, como consultas ao banco de dados.  
+Template.
  -Corresponde à camada de visualização, semelhante à View no MVC.Os templates no Django são  
  -arquivos HTML que incorporam código Python, permitindo que os dados do aplicativo sejam renderizados dinamicamente.
+View:
  -Representa a camada de lógica de controle, semelhante ao Controlador no MVC. As views no  
  -Django são funções ou classes que processam as requisições HTTP, interagem com o modelo para 
  -recuperar os dados necessários e renderizam os templates apropriados para criar a resposta HTTP.
