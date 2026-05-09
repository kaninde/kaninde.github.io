# Sobre o Social Media Safe Text (SMST)

Bem-vindo ao **Social Media Safe Text (SMST)** — um aplicativo para revisar e preparar textos antes de publicar nas redes sociais.

O SMST ajuda a substituir ou ofuscar palavras e expressões que você não quer expor literalmente, usando um **dicionário pessoal** (palavras-chave e substituições), **regras opcionais** de substituição de caracteres (estilo “leetspeak”) e um **editor** com modos automático ou manual. **Dicionário** e **histórico** ficam **localmente** no aparelho (SQLite).

---

## Destaques

- **Editor:** texto livre, realce de ocorrências dos dicionários ativos, substituição em massa ou passo a passo, copiar e compartilhar.
- **Dicionário:** entradas agrupadas por nome de grupo, várias substituições com prioridade, ativar/desativar grupos inteiros no editor, importar/exportar JSON (`smst.dictionary`) e, opcionalmente, instalar pacotes a partir de um **catálogo remoto** (HTTP).
- **Regras de leetspeak:** criar regras caractere a caractere, reordenar e aplicar em conjunto com o dicionário.
- **Histórico:** lista local de textos já preparados (toque para copiar).
- **Privacidade no núcleo do app:** dicionário, regras e histórico no dispositivo; não há conta obrigatória para o fluxo principal descrito no onboarding.

---

## Funcionalidades incluídas e limites (resumo)

O app pode oferecer acesso **gratuito**, **teste**, **premium** ou com **anúncios**, conforme a compilação e a loja. Exemplos de áreas sujeitas a limite (veja rótulos e paywalls **no app** para regras exatas na sua versão):

- **Dicionários:** limite de quantos grupos/dicionários no modo gratuito; **importação** pode ser limitada no gratuito e depois liberada via premium ou anúncio recompensado; **sincronização com catálogo remoto** costuma ser premium (ou desbloqueio por anúncio), conforme configuração.
- **Editor / histórico:** ações como **copiar**, **compartilhar**, **salvar no histórico** ou **histórico completo** podem exigir premium ou anúncio recompensado, conforme *feature flags*.
- **Anúncios e assinaturas:** redes de anúncios e/ou compras no app podem aparecer, alinhados ao `feature_config` e às políticas da loja.

Limites podem mudar com atualizações; prevalecem a experiência **no aplicativo** e a ficha na loja.

---

## Perguntas frequentes (FAQ)

**Preciso criar conta?**  
Não. O fluxo local principal pode ser usado sem criar conta.

**Preciso de internet?**  
Grande parte funciona **offline**. Internet é usada quando você opta por recursos que precisam dela (por exemplo **catálogo remoto de dicionários**, **anúncios** ou **compras no app**).

**Vou perder meus dados se desinstalar?**  
Dados locais (dicionário, histórico, configurações) ficam no aparelho. Desinstalar pode **apagar permanentemente** esses dados, salvo se você tiver exportado um backup.

**O app modera o que eu escrevo?**  
Não. Você define entradas e substituições do dicionário. O uso do texto preparado em cada rede e em lei aplicável é de sua responsabilidade.

---

## Contato

Para suporte ou feedback:

**E-mail:** samirtf.dev@gmail.com
