# Como buscar candidatos com sua própria IA via MCP

O Graviola, produto da Heuv Technologies, permite que um assistente compatível com MCP consulte perfis profissionais, organize pessoas em projetos e execute operações autorizadas. O assistente ajuda a interpretar a vaga e revisar evidências; o Graviola fornece os dados disponíveis e os recursos da conta.

Este roteiro serve para uma busca inicial de recrutamento. O resultado esperado é uma lista pequena com evidências profissionais e lacunas explícitas. Uma pessoa encontrada não é automaticamente candidata interessada na vaga.

## 1. Conecte a conta correta

Crie sua conta no [Graviola](https://graviola.dev) e siga as [instruções de conexão](https://graviola.dev/docs/connect-your-ai). Em Claude Code, a conexão remota pode ser adicionada assim:

```sh
claude mcp add --transport http graviola https://mcp.graviola.dev/api/mcp
```

Complete a autenticação e confira a conta e o workspace usados pelo assistente. Antes de buscar, peça a leitura das permissões e dos limites atuais. Não coloque chaves de API em arquivos públicos ou em exemplos compartilhados.

## 2. Transforme a vaga em critérios verificáveis

Descreva as responsabilidades e a experiência necessária. Separe filtros de busca suportados de requisitos que precisam de conversa ou pesquisa adicional. Um título parecido não comprova experiência em uma responsabilidade específica.

Exemplo de pedido para preparar a busca:

> Quero pesquisar lideranças de engenharia para uma vaga. Converta meu briefing em filtros suportados pelo Graviola e uma lista de critérios profissionais para revisão. Indique os requisitos que não podem ser confirmados pelos perfis. Proponha uma busca de até cinco pessoas, sem executar ainda.

Use localização como critério operacional quando necessário. Não deduza características pessoais sensíveis a partir de nome, foto ou formação.

## 3. Execute uma busca limitada e revise a evidência

Depois de aprovar os critérios e solicitar a execução, revise o histórico profissional retornado. Para cada pessoa, registre o requisito, a informação que o sustenta e o que permanece desconhecido. Se o perfil não mencionar uma habilidade, marque como desconhecida em vez de concluir que a pessoa não a possui.

Salve os perfis relevantes em um projeto. Ao retomar a revisão, use os resultados salvos quando disponíveis para evitar consumir outra busca apenas para reabrir informações.

## 4. Selecione antes de revelar contatos

A busca de perfis e a recuperação de contatos têm limites distintos. Escolha quem merece uma conversa antes de solicitar dados de contato. Um email ausente deve continuar ausente; não gere endereços por adivinhação.

Peça uma mensagem que explique a vaga e a relevância do histórico profissional. Revise destinatário, remetente e texto antes de autorizar envio. O envio depende do plano, das permissões e de uma caixa autorizada conectada.

## Como avaliar o resultado

Conte perfis revisados, pessoas selecionadas, contatos disponíveis, respostas e entrevistas realizadas separadamente. Não transforme uma correspondência na busca em uma contratação prevista.

Leia também o [tutorial de sourcing](https://graviola.dev/blog/ai-recruiting-sourcing-shortlist), o [guia de revisão de perfis](https://graviola.dev/docs/review-profiles) e as [comparações com ferramentas de recrutamento](https://graviola.dev/compare).
