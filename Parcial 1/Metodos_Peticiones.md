# Los códigos de estado de respuesta HTTP indican si se ha completado satisfactoriamente una solicitud HTTP específica. Las respuestas se agrupan en cinco clases:

## Respuestas informativas (100–199),
## Respuestas satisfactorias (200–299),
## Redirecciones (300–399),
## Errores de los clientes (400–499),
## y errores de los servidores (500–599).
## Los códigos de estado se definen en la sección 10 de RFC 2616. Puedes obtener las especificaciones actualizadas en RFC 7231.
## 100 Continue
## Esta respuesta provisional indica que todo hasta ahora está bien y que el cliente debe continuar con la solicitud o ignorarla si ya está terminada.
## 101 Switching Protocol
## Este código se envía en respuesta a un encabezado de solicitud Upgrade (en-US) por el cliente e indica que el servidor acepta el cambio de protocolo propuesto por el agente de usuario.
## 102 Processing (WebDAV (en-US))
## Este código indica que el servidor ha recibido la solicitud y aún se encuentra procesandola, por lo que no hay respuesta disponible.
## 103 Early Hints (en-US)
## Este código de estado está pensado principalmente para ser usado con el encabezado Link, permitiendo que el agente de usuario empiece a pre-cargar recursos mientras el servidor prepara una respuesta.
## Respuestas satisfactorias
## GET: El recurso se ha obtenido y se transmite en el cuerpo del mensaje.
## HEAD: Los encabezados de entidad están en el cuerpo del mensaje.
## PUT o POST: El recurso que describe el resultado de la acción se transmite en el cuerpo del mensaje.
## TRACE: El cuerpo del mensaje contiene el mensaje de solicitud recibido por el servidor.
## 200 OK
## La solicitud ha tenido éxito. El significado de un éxito varía dependiendo del método HTTP:
## 201 Created
## La solicitud ha tenido éxito y se ha creado un nuevo recurso como resultado de ello. Ésta es típicamente la respuesta enviada después de una petición PUT.
## 202 Accepted
## La solicitud se ha recibido, pero aún no se ha actuado. Es una petición "sin compromiso", lo que significa que no hay manera en HTTP que permite enviar una respuesta asíncrona que indique el resultado del procesamiento de la solicitud. Está pensado para los casos en que otro proceso o servidor maneja la solicitud, o para el procesamiento por lotes.
## 203 Non-Authoritative Information
## La petición se ha completado con éxito, pero su contenido no se ha obtenido de la fuente originalmente solicitada, sino que se recoge de una copia local o de un tercero. Excepto esta condición, se debe preferir una respuesta de 200 OK en lugar de esta respuesta.
## 204 No Content (en-US)
## La petición se ha completado con éxito pero su respuesta no tiene ningún contenido, aunque los encabezados pueden ser útiles. El agente de usuario puede actualizar sus encabezados en caché para este recurso con los nuevos valores.
## 205 Reset Content (en-US)
## La petición se ha completado con éxito, pero su respuesta no tiene contenidos y además, el agente de usuario tiene que inicializar la página desde la que se realizó la petición, este código es útil por ejemplo para páginas con formularios cuyo contenido debe borrarse después de que el usuario lo envíe.
## 206 Partial Content
## La petición servirá parcialmente el contenido solicitado. Esta característica es utilizada por herramientas de descarga como wget para continuar la transferencia de descargas anteriormente interrumpidas, o para dividir una descarga y procesar las partes simultáneamente.
## 207 Multi-Status (WebDAV (en-US))
## Una respuesta Multi-Estado transmite información sobre varios recursos en situaciones en las que varios códigos de estado podrían ser apropiados. El cuerpo de la petición es un mensaje XML.
## 208 Multi-Status (WebDAV (en-US))
## El listado de elementos DAV ya se notificó previamente, por lo que no se van a volver a listar.
## 226 IM Used (HTTP Delta encoding)
## El servidor ha cumplido una petición GET para el recurso y la respuesta es una representación del resultado de una o más manipulaciones de instancia aplicadas a la instancia actual.