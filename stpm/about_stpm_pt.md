# Sobre o SafeText: Private Messages (STPM)

Bem-vindo ao **SafeText: Private Messages (STPM)** — um aplicativo que adiciona uma camada extra de privacidade às conversas que você já usa no dia a dia.

O STPM **não** é um mensageiro completo. Você criptografa mensagens e arquivos **no celular** e envia o conteúdo protegido pelo WhatsApp, Telegram, SMS, e-mail ou qualquer outro app — como texto `SAFE://` ou arquivo `.safe`. **Não há cadastro**, **login**, **telefone**, **e-mail** nem **servidor central** guardando suas chaves.

O STPM ajuda a gerir **conversas seguras** (nomes locais de contato, troca de chaves por QR Code, verificação de fingerprint), **mensagens protegidas**, **arquivos `.safe`** (fotos, vídeos, áudio, documentos), **configurações de privacidade** (ocultar texto sensível, bloqueio do app, limpeza da área de transferência, limite de captura de tela) e **backup criptografado** (exportar/restaurar). **Metadados das conversas**, **chaves públicas**, **configurações** e **histórico local** opcional (ativado por você) ficam **localmente** no aparelho (base SQLite `stpm.db`).

---

## Destaques

- **Conversas seguras:** Criar conversas, trocar chaves por QR Code, verificar o código de segurança (fingerprint), arquivar ou revogar acesso, renovar a chave local quando necessário.
- **Mensagens protegidas:** Escrever texto, gerar payload criptografado, copiar ou compartilhar; abrir conteúdo `SAFE://` recebido com verificação de assinatura e integridade.
- **Arquivos `.safe`:** Criptografar mídia e documentos; abrir arquivos compartilhados no app; visualizar conteúdo descriptografado; aviso explícito antes de compartilhar em texto claro.
- **Abrir mensagem:** Colar ou receber texto protegido de outros apps e descriptografar localmente.
- **Privacidade por padrão:** Texto sensível permanece oculto até você revelar; chaves privadas usam armazenamento seguro do sistema; texto claro não é persistido por padrão.
- **Configurações:** Bloqueio do app (biometria ou PIN), limpeza automática da área de transferência, histórico local opcional, detalhes técnicos avançados, backup criptografado, guia de introdução.
- **Privacidade no núcleo:** Suas chaves e dados de conversa permanecem no dispositivo, salvo se exportar backup ou usar funções que precisem de internet (veja a Política de privacidade).

---

## Funcionalidades incluídas e limites (resumo)

O app pode oferecer acesso **gratuito**, **assinatura premium**, **compra vitalícia offline** ou com **anúncios**, conforme a compilação e a loja. No gratuito podem aplicar-se limites (por exemplo anúncios recompensados antes de criptografar/descriptografar ou configurações premium bloqueadas). **Premium** ou **vitalício** ampliam o acesso, incluindo fluxos de criptografia sem anúncios e recursos avançados de privacidade, conforme a ficha na loja e o paywall no app.

Os limites podem mudar com atualizações; prevalecem a experiência **no aplicativo** e a ficha na loja.

---

## Perguntas frequentes (FAQ)

**Preciso criar conta?**  
Não. Você pode usar o STPM sem criar conta.

**Preciso de internet?**  
A criptografia e descriptografia principais funcionam **offline**. A internet é usada quando você opta por recursos que precisam dela (por exemplo **anúncios**, **compras no app** ou **assinaturas**, carregamento opcional de **configuração remota** como um carrossel de outros apps, ou abrir links externos).

**Vou perder meus dados se desinstalar?**  
Os dados locais ficam no aparelho. Desinstalar pode **apagar permanentemente** conversas, chaves e configurações, salvo se tiver exportado um **backup criptografado**.

**O STPM é um serviço de mensagens?**  
Não. O STPM é uma **ferramenta de criptografia local**. Não entrega mensagens, não hospeda chats nem substitui WhatsApp ou outros mensageiros. Você continua responsável por como compartilha conteúdo protegido e por verificar contatos via QR e fingerprint.

---

## Contato

Para suporte ou feedback:

**E-mail:** samirtf.dev@gmail.com
