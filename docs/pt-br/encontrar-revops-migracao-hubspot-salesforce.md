# Como encontrar líderes de RevOps para oferecer uma migração de HubSpot para Salesforce com IA e MCP

Este tutorial mostra como usar o Graviola, produto da Heuv Technologies, para montar uma lista pequena de profissionais de operações de receita, revisar evidências e preparar uma abordagem relevante. O exemplo é uma consultoria que oferece mapeamento de campos, revisão de duplicados e validação de pipeline durante uma migração de CRM.

O resultado esperado é uma lista de pesquisa e rascunhos de mensagens. Experiência com dois CRMs não comprova que a empresa esteja migrando ou comprando uma consultoria. Este é um fluxo ilustrativo, não um caso de cliente com resultado medido.

## O que preparar

- Uma conta Graviola e uma conexão MCP em um cliente compatível.
- Uma lista curta de empresas B2B que você consegue atender.
- Uma oferta real: entregáveis, escopo e próximo passo que sua equipe consegue executar.
- Um projeto para guardar a pesquisa e limites claros de busca e contatos.

Consulte o [guia de conexão](https://graviola.dev/docs/connect-your-ai). O endpoint MCP é `https://mcp.graviola.dev/api/mcp`. Para integrações REST, use o [OpenAPI atual](https://api.graviola.dev/api/v1/openapi.json), sem copiar parâmetros de exemplos antigos.

## 1. Transforme o serviço em um briefing pesquisável

Descreva quem normalmente cuida do problema: Revenue Operations, Sales Operations ou operações de CRM. Defina as empresas-alvo antes de procurar pessoas. Se tamanho da empresa ou tecnologia atual forem essenciais, verifique se o esquema oferece o filtro; quando não oferecer, trate essa informação como pesquisa externa.

Prompt:

```text
Minha oferta é mapear campos de ciclo de vida, revisar duplicados e validar
pipeline em projetos de mudança de CRM de empresas B2B SaaS.
Mostre meu workspace Graviola e os limites atuais.
Proponha filtros suportados de cargo e empresa para encontrar até cinco
profissionais de RevOps ou Sales Operations nesta lista de empresas: [lista].
Não execute a busca ainda. Separe filtros disponíveis de fatos que precisamos verificar.
```

Troque `[lista]` pelas empresas que você verificou. Consultar workspace e uso não deve iniciar uma pesquisa de profissionais.

## 2. Faça uma busca pequena e registre os critérios

Depois de revisar a proposta, peça uma busca de até cinco perfis. Use os filtros que o esquema atual realmente aceita. Caso o resultado seja estreito demais, teste um cargo adjacente antes de remover simultaneamente todos os critérios.

```text
Execute uma busca com os critérios revisados, limitada a cinco perfis.
Guarde a referência da busca para revisar os mesmos resultados depois.
Quando houver competências HubSpot ou Salesforce, considere-as sinais de
experiência profissional. Não infira stack atual, orçamento ou intenção de migração.
Não revele contatos nem envie mensagens nesta etapa.
```

Uma pessoa com ambas as ferramentas no histórico pode ter usado cada uma em empregadores diferentes. Essa distinção evita transformar uma correspondência de palavras em uma falsa oportunidade comercial.

## 3. Construa uma tabela de evidências

Revise cargo, vínculo profissional disponível, histórico e fontes. Uma vaga pública mencionando Salesforce pode ajudar na pesquisa da empresa, mas não prova uma decisão de compra. Registre a data da fonte e o que ela sustenta.

| Campo | O que registrar |
| --- | --- |
| Empresa e pessoa | Referências retornadas pela pesquisa |
| Cargo atual | Evidência disponível e sua data |
| Experiência CRM | Ferramentas e atividades documentadas |
| Stack da empresa | Fonte pública atual ou “não confirmado” |
| Intenção de migração | “Não confirmada” sem fonte explícita |
| Próxima pergunta | Informação que uma conversa precisa esclarecer |

```text
Revise os perfis retornados e monte a tabela acima com links de fonte.
Diferencie experiência pessoal, tecnologia do empregador e intenção de compra.
Marque dados ausentes como não confirmados. Não invente emails nem projetos.
```

Se o carregamento de um perfil falhar, siga o [diagnóstico documentado](https://graviola.dev/docs/troubleshooting); um erro de carregamento não significa ausência de experiência.

## 4. Prepare uma pergunta de descoberta

Selecione as pessoas cuja função combina com o serviço. Só então solicite os contatos disponíveis, com um limite explícito e após conferir os créditos. Um endereço retornado não garante entrega nem interesse.

Modelo editável:

> Olá, [nome]. Sou [nome real], da [empresa]. Ajudamos equipes B2B a mapear campos e validar registros de pipeline durante mudanças de CRM. Seu trabalho em [evidência profissional verificada] parece relacionado à operação desses processos. Sua equipe está avaliando algum projeto desse tipo, ou existe outra pessoa responsável por sistemas comerciais?

Não escreva “vi que vocês estão migrando” sem uma fonte que confirme isso. Personalize pela responsabilidade documentada e mantenha a pergunta aberta.

## 5. Salve a pesquisa e acompanhe respostas reais

Guarde evidências e rascunhos no projeto. Se for exportar CSV ou sincronizar contatos com HubSpot, confira o esquema de registros e as duplicatas antes da atualização. Não sobrescreva propriedades confirmadas do CRM com hipóteses da pesquisa.

Separe os estados pesquisado, abordado, respondeu, projeto confirmado e reunião qualificada. Uma busca bem-sucedida não equivale a uma reunião marcada.

O envio de sequências exige plano pago e mailbox autorizada. Confira [configuração e limites de email](https://graviola.dev/docs/email-sequences) antes de executar uma solicitação de envio. O Graviola não automatiza mensagens de LinkedIn ou SMS.

## Próximos passos

- [Criar conta no Graviola](https://data.graviola.dev/signup)
- [Tutorial equivalente em inglês](https://graviola.dev/blog/find-revops-leaders-hubspot-salesforce-migration)
- [Busca e revisão de perfis](https://graviola.dev/docs/review-profiles)
- [Outros guias em português](prospectar-clientes-com-ia.md)

Produto: Graviola, da Heuv Technologies. Contato: Toni — [toni@graviola.dev](mailto:toni@graviola.dev).
