# Política de Privacidad – SafeText: Private Messages (STPM)

Última actualización: 5 de junio de 2026

---

## 1. Introducción

Esta Política de Privacidad describe cómo **SafeText: Private Messages** (“STPM”, “Aplicación”) trata la información en tu dispositivo y, cuando usas ciertas funciones, interacciones limitadas por internet.

Al usar la Aplicación, aceptas las prácticas descritas en esta Política de Privacidad.

Estamos comprometidos con proteger tu privacidad y ser transparentes sobre el tratamiento de datos.

---

## 2. Recopilación y almacenamiento de datos

### 2.1 Almacenamiento local

- La Aplicación está diseñada para que el **contenido principal** — incluidos **registros de conversaciones seguras** (nombres locales de visualización, estados de clave, huellas digitales, estado de archivo), **material criptográfico de claves** (claves privadas en almacenamiento seguro del sistema; claves públicas y metadatos relacionados localmente), **metadatos de mensajes y archivos protegidos** (cuando activas el historial local), **ajustes** y registros relacionados — se guarde **localmente** en tu dispositivo (por ejemplo en una base SQLite local denominada `stpm.db`).
- El **contenido de mensajes en texto claro** **no se persiste por defecto**; el texto sensible solo se muestra cuando eliges revelarlo, según tus ajustes.
- Cuando esté disponible, puedes **exportar** una **copia de seguridad cifrada**, **restaurar** una copia compatible o **eliminar** datos en la Aplicación (incluidas opciones de borrado total cuando se ofrezcan).

### 2.2 Cuentas

- La Aplicación **no exige** crear cuenta, teléfono, correo electrónico ni inicio de sesión para el flujo local principal.

### 2.3 Datos que no operamos como backend de mensajería

- STPM **no** es un mensajero, servidor de claves ni servicio de copia de seguridad en la nube operado por nosotros para tu contenido cifrado en el uso diario. **No** mantenemos un servicio central cuyo objetivo sea almacenar tus conversaciones, claves privadas o mensajes descifrados en **nuestros** servidores como parte del uso normal.
- Cuando usas **compartir**, **exportar**, **copiar** o abrir un archivo, el contenido se envía a través del **sistema operativo de tu dispositivo** (por ejemplo a WhatsApp, correo o una ruta que elijas). Eso está bajo **tu** control.

### 2.4 Uso de red (tienda, anuncios, contenido remoto opcional)

Cuando eliges funciones que requieren conectividad, la Aplicación puede conectarse a internet, por ejemplo para:

- **Compras en la app / suscripciones / compra vitalicia:** gestionadas por **Google Play** o **App Store** de Apple, bajo sus términos y políticas de privacidad.
- **Publicidad (si está habilitada):** los SDK de anuncios pueden procesar **señales de dispositivo y uso** según sus propias políticas.
- **JSON o enlaces remotos opcionales:** por ejemplo un carrusel ligero de **“otras apps”** u otra configuración alojada en una URL de **terceros** incluida en la compilación; esas solicitudes van al operador de ese host. Abrir **documentación**, **soporte** o enlaces de la **tienda** también usa la red.

### 2.5 Permisos

Según las funciones y la plataforma, la Aplicación puede solicitar acceso a:

- **Cámara:** para escanear códigos QR e intercambiar claves públicas con contactos.
- **Fotos / galería / archivos (según exija el SO):** para seleccionar medios o documentos a proteger, abrir archivos `.safe` o guardar exportaciones, usando selectores del sistema cuando estén disponibles.
- **Micrófono:** para grabar audio a proteger como medio cifrado cuando uses esa función.
- **Biometría / credenciales del dispositivo:** para **bloqueo de la app** opcional si lo activas.
- **Internet:** para **anuncios**, **facturación**, configuración remota opcional o abrir enlaces.
- **Notificaciones (opcional):** solo si una función que activas usa notificaciones, conforme a los permisos declarados en tu compilación.

La Aplicación no accede a estos recursos sin **tu** acción cuando el sistema exige consentimiento explícito.

---

## 3. Uso de los datos

Los datos que proporcionas se usan para:

- Ejecutar **conversaciones seguras**, flujos de **cifrar/descifrar**, **intercambio de claves por QR**, **verificación de huella**, **copia de seguridad/restauración** y **ajustes**;
- Aplicar **historial local de mensajes** opcional cuando lo actives;
- Mostrar **anuncios**, **suscripción premium** o flujos de compra **vitalicia** cuando estén habilitados en tu compilación.

**No** usamos el contenido de tus conversaciones o mensajes para crear un perfil publicitario **de nuestro lado**; las redes de anuncios de terceros pueden procesar datos bajo **sus** políticas cuando se muestran anuncios.

---

## 4. Compartición de datos

- **No vendemos** tu información personal.
- Tu **contenido de conversaciones, claves y mensajes** no se sube a **nuestros** servidores como parte del flujo local predeterminado descrito arriba.
- **Tiendas de apps**, **redes de anuncios** y **hosts de URLs remotas opcionales** que consultes pueden procesar datos según **sus** políticas cuando uses esos servicios.

Cualquier compartición de payloads protegidos, archivos `.safe`, copias de seguridad o capturas ocurre solo cuando **tú** inicias compartir, exportar o copiar.

---

## 5. Servicios de terceros

La Aplicación puede depender de terceros, incluidos:

- **Publicidad:** puede recopilar identificadores o datos de uso para entrega y medición de anuncios.
- **Pagos:** procesados por la tienda de la plataforma.
- **Hosts de JSON de configuración opcional:** quien opere la URL que consultes puede ver **datos técnicos de la solicitud** (como dirección IP) como cualquier servidor web.
- **Apps de mensajería y archivos que elijas:** WhatsApp, correo, nube y similares procesan contenido que **tú** envías por ellos bajo **sus** políticas.

Esos servicios operan bajo sus propios términos y políticas de privacidad.

---

## 6. Retención y eliminación de datos

- Los datos locales permanecen en el dispositivo hasta que los elimines o desinstales la Aplicación.
- Puedes usar opciones en la app para **borrar datos**, **eliminar conversaciones** o **borrar todos los datos de SafeText**, cuando estén disponibles.
- Desinstalar la Aplicación normalmente **elimina permanentemente** bases locales y entradas de almacenamiento seguro del dispositivo.

---

## 7. Seguridad

Aplicamos prácticas razonables en la Aplicación, incluido mantener claves y datos de conversación **en el dispositivo** por defecto, usar almacenamiento seguro del sistema para claves privadas y minimizar la recopilación innecesaria.

Eres responsable de proteger tu dispositivo (PIN, contraseña, biometría), verificar contactos mediante QR y huella, y mantener el SO actualizado.

---

## 8. Privacidad de menores

La Aplicación está destinada al público general y **no** está dirigida a menores de **13** años.

No recopilamos intencionalmente información personal de menores de forma que viole esta intención.

---

## 9. Cambios en esta política

Podemos actualizar esta Política de Privacidad periódicamente. La fecha “Última actualización” cambiará. El uso continuado de la Aplicación tras las actualizaciones constituye aceptación de la política revisada.

---

## 10. Contacto

Preguntas sobre esta Política de Privacidad:

**Correo electrónico:** samirtf.dev@gmail.com

---

## 11. Descargo de responsabilidad

La Aplicación se proporciona **“tal cual”**, sin garantías de ningún tipo. Eres el único responsable de **verificar contactos**, **proteger contraseñas de copia de seguridad** y **decisiones** al compartir contenido cifrado o descifrado. STPM no ofrece asesoramiento legal o de seguridad; ninguna herramienta garantiza confidencialidad si el dispositivo o el canal están comprometidos.
