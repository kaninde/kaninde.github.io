# Política de Privacidade – SafeText: Private Messages (STPM)

Última atualização: 5 de junho de 2026

---

## 1. Introdução

Esta Política de Privacidade descreve como o **SafeText: Private Messages** (“STPM”, “Aplicativo”) trata informações no seu dispositivo e, quando você usa certos recursos, interações limitadas pela internet.

Ao usar o Aplicativo, você concorda com as práticas descritas nesta Política de Privacidade.

Estamos comprometidos em proteger sua privacidade e ser transparentes sobre como os dados são tratados.

---

## 2. Coleta e armazenamento de dados

### 2.1 Armazenamento local

- O Aplicativo foi planejado para que o **conteúdo principal** — incluindo **registros de conversas seguras** (nomes locais de exibição, estados de chave, fingerprints, status de arquivo), **material criptográfico de chaves** (chaves privadas no armazenamento seguro do sistema; chaves públicas e metadados relacionados localmente), **metadados de mensagens e arquivos protegidos** (quando você ativa histórico local), **configurações** e registros relacionados — fique **localmente** no seu dispositivo (por exemplo em banco SQLite local denominado `stpm.db`).
- **Conteúdo de mensagens em texto claro** **não é persistido por padrão**; texto sensível só é exibido quando você escolhe revelar, conforme suas configurações.
- Quando disponível, você pode **exportar** um **backup criptografado**, **restaurar** um backup compatível ou **excluir** dados no Aplicativo (incluindo opções de apagar tudo, quando oferecidas).

### 2.2 Contas

- O Aplicativo **não exige** que você crie conta, telefone, e-mail ou login para o fluxo local principal.

### 2.3 Dados que não operamos como backend de mensagens

- O STPM **não** é mensageiro, servidor de chaves nem serviço de backup em nuvem operado por nós para seu conteúdo cifrado no uso diário. **Não** mantemos um serviço central cujo objetivo seja armazenar suas conversas, chaves privadas ou mensagens descriptografadas em **nossos** servidores como parte do uso normal.
- Quando você usa **compartilhar**, **exportar**, **copiar** ou abrir arquivo, o conteúdo é enviado pelo **seu** sistema operacional (por exemplo para WhatsApp, e-mail ou caminho que você escolher). Isso está sob **seu** controle.

### 2.4 Uso de rede (loja, anúncios, conteúdo remoto opcional)

Quando você escolhe recursos que precisam de conectividade, o Aplicativo pode acessar a internet, por exemplo para:

- **Compras no app / assinaturas / compra vitalícia:** processadas pela **Google Play** ou **App Store** da Apple, sob seus termos e políticas de privacidade.
- **Publicidade (se habilitada):** SDKs de anúncios podem processar **sinais de dispositivo e uso** conforme suas próprias políticas.
- **JSON ou links remotos opcionais:** por exemplo um carrossel leve de **“outros apps”** ou configuração similar hospedada em URL de **terceiros** incluída na compilação; essas requisições vão para quem opera esse host. Abrir **documentação**, **suporte** ou links da **loja** também usa a rede.

### 2.5 Permissões

Conforme os recursos e a plataforma, o Aplicativo pode solicitar acesso a:

- **Câmera:** para escanear QR Codes e trocar chaves públicas com contatos.
- **Fotos / galeria / arquivos (conforme exigido pelo SO):** para selecionar mídia ou documentos a proteger, abrir arquivos `.safe` ou salvar exportações, usando seletores do sistema quando disponíveis.
- **Microfone:** para gravar áudio a proteger como mídia criptografada quando você usar esse recurso.
- **Biometria / credenciais do dispositivo:** para **bloqueio do app** opcional, se você ativar.
- **Internet:** para **anúncios**, **cobrança**, configuração remota opcional ou abrir links.
- **Notificações (opcional):** somente se um recurso que você ativa usar notificações, conforme permissões declaradas na sua compilação.

O Aplicativo não acessa esses recursos sem **sua** ação quando o sistema exige consentimento explícito.

---

## 3. Uso dos dados

Os dados que você fornece são usados para:

- Executar **conversas seguras**, fluxos de **criptografar/descriptografar**, **troca de chaves por QR**, **verificação de fingerprint**, **backup/restauração** e **configurações**;
- Aplicar **histórico local de mensagens** opcional quando você ativar;
- Exibir **anúncios**, **assinatura premium** ou fluxos de compra **vitalícia** quando habilitados na sua compilação.

**Não** usamos o conteúdo das suas conversas ou mensagens para criar perfil publicitário **do nosso lado**; redes de anúncios de terceiros podem processar dados sob **suas** políticas quando anúncios são exibidos.

---

## 4. Compartilhamento de dados

- **Não vendemos** suas informações pessoais.
- Seu **conteúdo de conversas, chaves e mensagens** não é enviado para **nossos** servidores como parte do fluxo local padrão descrito acima.
- **Lojas de apps**, **redes de anúncios** e **hosts de URLs remotas opcionais** que você acessa podem processar dados conforme **suas** políticas quando você usa esses serviços.

Qualquer compartilhamento de payloads protegidos, arquivos `.safe`, backups ou capturas de tela ocorre somente quando **você** inicia compartilhar, exportar ou copiar.

---

## 5. Serviços de terceiros

O Aplicativo pode depender de terceiros, incluindo:

- **Publicidade:** pode coletar identificadores ou dados de uso para entrega e medição de anúncios.
- **Pagamentos:** processados pela loja da plataforma.
- **Hosts de JSON de configuração opcional:** quem opera a URL que você acessa pode ver **dados técnicos da requisição** (como endereço IP) como qualquer servidor web.
- **Apps de mensagem e arquivo que você escolher:** WhatsApp, e-mail, nuvem e similares processam conteúdo que **você** envia por eles sob **suas** políticas.

Esses serviços operam sob seus próprios termos e políticas de privacidade.

---

## 6. Retenção e exclusão de dados

- Dados locais permanecem no dispositivo até você excluí-los ou desinstalar o Aplicativo.
- Você pode usar opções no app para **limpar dados**, **excluir conversas** ou **apagar todos os dados do SafeText**, quando disponíveis.
- Desinstalar o Aplicativo normalmente **remove permanentemente** bancos locais e entradas de armazenamento seguro do dispositivo.

---

## 7. Segurança

Aplicamos práticas razoáveis no Aplicativo, incluindo manter chaves e dados de conversa **no dispositivo** por padrão, usar armazenamento seguro do sistema para chaves privadas e minimizar coleta desnecessária.

Você é responsável por proteger o dispositivo (PIN, senha, biometria), verificar contatos via QR e fingerprint e manter o SO atualizado.

---

## 8. Privacidade de crianças

O Aplicativo destina-se ao público em geral e **não** é direcionado a crianças menores de **13** anos.

Não coletamos intencionalmente informações pessoais de crianças de forma que viole essa intenção.

---

## 9. Alterações nesta política

Podemos atualizar esta Política de Privacidade periodicamente. A data “Última atualização” será alterada. O uso continuado do Aplicativo após atualizações constitui aceitação da política revisada.

---

## 10. Contato

Dúvidas sobre esta Política de Privacidade:

**E-mail:** samirtf.dev@gmail.com

---

## 11. Isenção de responsabilidade

O Aplicativo é fornecido **“como está”**, sem garantias de qualquer tipo. Você é o único responsável por **verificar contatos**, **proteger senhas de backup** e **decisões** ao compartilhar conteúdo cifrado ou descriptografado. O STPM não presta aconselhamento jurídico ou de segurança; nenhuma ferramenta garante confidencialidade se o dispositivo ou canal estiver comprometido.
