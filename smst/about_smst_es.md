# Acerca de Social Media Safe Text (SMST)

Te damos la bienvenida a **Social Media Safe Text (SMST)** — una app para revisar y preparar textos antes de publicarlos en redes sociales.

SMST te ayuda a reemplazar u ofuscar palabras y frases que no quieras mostrar literalmente, usando un **diccionario personal** (palabras clave y sustituciones), **reglas opcionales** de sustitución de caracteres (estilo “leetspeak”) y un **editor** con modos automático o manual. Tu **diccionario** e **historial** se guardan **localmente** en el dispositivo (SQLite).

---

## Lo esencial

- **Editor:** texto libre, resaltado de coincidencias de los diccionarios activos, sustitución masiva o paso a paso, copiar y compartir.
- **Diccionario:** entradas agrupadas por nombre de grupo, varias sustituciones con prioridad, activar/desactivar grupos enteros en el editor, importar/exportar JSON (`smst.dictionary`) e, opcionalmente, instalar paquetes desde un **catálogo remoto** (HTTP).
- **Reglas leetspeak:** definir reglas carácter a carácter, reordenarlas y aplicarlas junto con el diccionario.
- **Historial:** lista local de textos ya preparados (toca para copiar).
- **Privacidad en el núcleo de la app:** diccionario, reglas e historial en el dispositivo; no hay cuenta obligatoria para el flujo principal del onboarding.

---

## Funciones incluidas y límites (resumen)

La app puede ofrecer acceso **gratis**, **de prueba**, **premium** o con **anuncios**, según la compilación y la tienda. Ejemplos de límites (consulta **en la app** los textos y paywalls exactos de tu versión):

- **Diccionarios:** límite de grupos en modo gratuito; la **importación** puede estar limitada en gratuito y luego desbloquearse con premium o anuncio recompensado; la **sincronización con catálogo remoto** suele ser premium (o desbloqueo por anuncio), según configuración.
- **Editor / historial:** acciones como **copiar**, **compartir**, **guardar en historial** o **historial completo** pueden requerir premium o anuncio recompensado, según *feature flags*.
- **Anuncios y suscripciones:** redes de anuncios y/o compras in-app pueden mostrarse, alineadas con `feature_config` y las políticas de la tienda.

Los límites pueden cambiar con actualizaciones; prevalecen la experiencia **en la aplicación** y la ficha de la tienda.

---

## Preguntas frecuentes (FAQ)

**¿Necesito crear una cuenta?**  
No. El flujo local principal se puede usar sin crear cuenta.

**¿Necesito internet?**  
Gran parte funciona **sin conexión**. Internet se usa cuando eliges funciones que lo requieren (por ejemplo **catálogo remoto de diccionarios**, **anuncios** o **compras in-app**).

**¿Perderé mis datos si desinstalo?**  
Los datos locales (diccionario, historial, ajustes) están en el dispositivo. Desinstalar puede **borrarlos permanentemente**, salvo que hayas exportado una copia de seguridad.

**¿La app modera lo que escribo?**  
No. Tú defines entradas y sustituciones del diccionario. El uso del texto preparado en cada red y ante la ley aplicable es tu responsabilidad.

---

## Contacto

Para soporte o comentarios:

**Email:** samirtf.dev@gmail.com
