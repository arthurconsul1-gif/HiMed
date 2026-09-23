# Fluxo de publicação do conteúdo

## Papéis de GitHub e Supabase

O GitHub e o Supabase não são alternativas concorrentes:

- o **GitHub é a fonte editorial de verdade**: guarda o legado, o Banco V2,
  referências, relatórios, versões e histórico das mudanças;
- o **Supabase é a base de execução**: entrega ao aplicativo somente as versões
  aprovadas e armazena contas, tentativas, favoritos e progresso dos alunos.

Uma questão não deve ser editada diretamente no Supabase. A correção nasce em um
arquivo V2 no GitHub, passa por revisão e testes e, somente depois, é sincronizada
com o Supabase. Assim, toda publicação pode ser explicada e revertida.

## Fluxo de um lote

1. preservar a questão original em `banco_completo.json`;
2. corrigir o lote em arquivo separado do Banco V2;
3. obter verificação independente e adjudicar divergências;
4. executar a validação automática do lote;
5. aprovar e integrar o lote ao arquivo consolidado V2;
6. gerar uma prévia das inserções e alterações no Supabase;
7. sincronizar pelo servidor, usando segredo armazenado no ambiente protegido;
8. conferir contagem, IDs e amostra diretamente no Supabase;
9. alterar o status para `published` apenas depois da conferência;
10. registrar resultado, versão e possibilidade de reversão.

## O que muda no protótipo

O aplicativo atual consulta a tabela `questions` do Supabase; portanto, o Supabase
continua necessário enquanto essa arquitetura estiver em uso. Enviar um JSON ao
GitHub, sozinho, **não atualiza o conteúdo exibido aos alunos**.

As páginas públicas `importar.html` e `atualizar.html` não serão o mecanismo
definitivo. Elas pedem credenciais no navegador e fazem alterações diretamente na
tabela, sem uma etapa robusta de prévia, aprovação, auditoria e reversão. Devem ser
substituídas por uma sincronização administrativa executada no servidor.

## Segurança

- nunca incluir `service_role`, senha ou token no GitHub ou no navegador;
- guardar segredos somente no cofre de variáveis do ambiente de implantação;
- validar a identidade e a autorização administrativas no servidor;
- publicar por ID e versão, sem apagar silenciosamente questões ausentes;
- registrar quem publicou, quando, qual commit e o resultado por questão;
- manter o lote como `draft` até a verificação pós-sincronização.

## Situação do LOTE-001

O teste termina primeiro como artefato V2 revisado no GitHub. Ele **não será enviado
automaticamente ao Supabase de produção**. Depois da validação do lote, será criada
e testada a sincronização segura em ambiente de homologação; somente então Arthur
receberá, se ainda houver alguma ação inevitável, uma orientação clique a clique.
