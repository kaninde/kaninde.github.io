# Acerca de SafeText: Private Messages (STPM)

Bienvenido a **SafeText: Private Messages (STPM)** — una aplicación que añade una capa extra de privacidad a las conversaciones que ya usas a diario.

STPM **no** es un mensajero completo. Cifras mensajes y archivos **en tu teléfono** y envías el contenido protegido por WhatsApp, Telegram, SMS, correo electrónico u otra app — como texto `SAFE://` o archivo `.safe`. **No hay registro**, **inicio de sesión**, **teléfono**, **correo** ni **servidor central** que guarde tus claves.

STPM te ayuda a gestionar **conversaciones seguras** (nombres locales de contacto, intercambio de claves por código QR, verificación de huella digital), **mensajes protegidos**, **archivos `.safe`** (fotos, vídeos, audio, documentos), **ajustes de privacidad** (ocultar texto sensible, bloqueo de la app, limpieza del portapapeles, límite de captura de pantalla) y **copia de seguridad cifrada** (exportar/restaurar). **Metadatos de conversaciones**, **claves públicas**, **ajustes** e **historial local** opcional (si lo activas) se guardan **localmente** en el dispositivo (base SQLite `stpm.db`).

---

## Destacados

- **Conversaciones seguras:** Crear conversaciones, intercambiar claves por QR, verificar el código de seguridad (huella), archivar o revocar acceso, renovar la clave local cuando haga falta.
- **Mensajes protegidos:** Escribir texto, generar payload cifrado, copiar o compartir; abrir contenido `SAFE://` recibido con comprobación de firma e integridad.
- **Archivos `.safe`:** Cifrar medios y documentos; abrir archivos compartidos en la app; previsualizar contenido descifrado; aviso explícito antes de compartir en texto claro.
- **Abrir mensaje:** Pegar o recibir texto protegido desde otras apps y descifrar localmente.
- **Privacidad por defecto:** El texto sensible permanece oculto hasta que lo reveles; las claves privadas usan almacenamiento seguro del sistema; el texto claro no se persiste por defecto.
- **Ajustes:** Bloqueo de la app (biometría o PIN), limpieza automática del portapapeles, historial local opcional, detalles técnicos avanzados, copia de seguridad cifrada, guía de introducción.
- **Privacidad en el núcleo:** Tus claves y datos de conversación permanecen en el dispositivo salvo que exportes una copia de seguridad o uses funciones que requieran internet (consulta la Política de privacidad).

---

## Funcionalidades incluidas y límites (resumen)

La app puede ofrecer acceso **gratuito**, **suscripción premium**, **compra vitalicia offline** o con **anuncios**, según la compilación y la tienda. En el nivel gratuito pueden aplicarse límites (por ejemplo anuncios recompensados antes de cifrar/descifrar o ajustes premium bloqueados). **Premium** o **vitalicio** amplían el acceso, incluidos flujos de cifrado sin anuncios y funciones avanzadas de privacidad, según la ficha en la tienda y el paywall en la app.

Los límites pueden cambiar con actualizaciones; prevalecen la experiencia **en la aplicación** y la ficha en la tienda.

---

## Preguntas frecuentes (FAQ)

**¿Necesito crear una cuenta?**  
No. Puedes usar STPM sin crear cuenta.

**¿Necesito internet?**  
El cifrado y descifrado principal funcionan **sin conexión**. Internet se usa cuando eliges funciones que la requieren (por ejemplo **anuncios**, **compras en la app** o **suscripciones**, carga opcional de **configuración remota** como un carrusel de otras apps, o abrir enlaces externos).

**¿Perderé mis datos si desinstalo?**  
Los datos locales están en el dispositivo. Desinstalar puede **eliminar permanentemente** conversaciones, claves y ajustes, salvo que hayas exportado una **copia de seguridad cifrada**.

**¿STPM es un servicio de mensajería?**  
No. STPM es una **herramienta de cifrado local**. No entrega mensajes, no aloja chats ni sustituye WhatsApp u otros mensajeros. Sigues siendo responsable de cómo compartes contenido protegido y de verificar contactos mediante QR y huella.

---

## Contacto

Para soporte o comentarios:

**Correo electrónico:** samirtf.dev@gmail.com
