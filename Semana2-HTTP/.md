# Mensajes HTTP

Los mensajes HTTP, son los medios por los cuales se intercambian datos entre servidores y clientes. Hay dos tipos de mensajes: peticiones, enviadas por el cliente al servidor, para pedir el inicio de una acción; y respuestas, que son la respuesta del servidor.

Los desarrolladores de páginas Web, o administradores de sitios Web, desarrolladores... raramente codifican directamente estos mensajes HTTP. Normalmente especifican estos mensajes HTTP, mediante archivos de configuración (para proxies, y servidores), APIs (para navegadores) y otros medios.


Las peticiones y respuestas HTTP, comparten una estructura similar, compuesta de:

1. Una línea de inicio ('start-line' en inglés) describiendo la petición a ser implementada, o su estado, sea de éxito o fracaso. Esta línea de comienzo, es siempre una única línea. 

2. Un grupo opcional de cabeceras HTTP, indicando la petición o describiendo el cuerpo ('body' en inglés) que se incluye en el mensaje. 

3. Una línea vacía ('empty-line' en inglés) indicando toda la meta-información ha sido enviada.

4. Un campo de cuerpo de mensaje opcional ('body' en inglés) que lleva los datos asociados con la petición (como contenido de un formulario HTML), o los archivos o documentos asociados a una respuesta (como una página HTML, o un archivo de audio, vídeo ... ) . La presencia del cuerpo y su tamaño es indicada en la línea de inicio y las cabeceras HTTP.

# Peticiones

# Start-line
La primera linea de la petición en HTTP se compone por:
`<verbo> <recurso> <versión>`

#  Peticiones más comunes

`GET` Solicita una representación de un recurso específico.

`POST` Se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.

`PUT` Reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.


# Código de estado

La versión del protocolo, normalmente HTTP/1.1.
Un código de estado, indicando el éxito o fracaso de la petición. Códigos de estado muy comunes son:  200, 404, o 302
Un texto de estado, que es una breve descripción, en texto, a modo informativo, de lo que significa el código de estado, con el fin de que una persona pueda interpretar el mensaje HTTP.

`1XX` Información
`2XX` Éxito
`3XX` Redirección
`4XX` Error del Cliente
`5XX` Error del servidor