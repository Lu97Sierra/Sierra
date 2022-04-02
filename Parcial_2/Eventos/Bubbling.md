# Propagacion y captura

- El flujo de eventos de OM tiene tres etapas:Etapa de captura de eventos, en la etapa de destino, etapa de burbujeo de eventos.

- Captura de eventos（event  capturing）：El entendimiento popular es que cuando el mouse hace clic o activa el evento dom, el navegador se iniciará desde el nodo raíz.De afuera hacia adentroPara la propagación de eventos, es decir, si se hace clic en el elemento secundario, si el elemento principal registra el evento correspondiente a través de la captura de eventos, el evento vinculado al elemento principal se activará primero.

- Evento burbujeante（dubbed  bubbling）：A diferencia de la captura de eventos, la secuencia de propagación de eventos consiste en propagar eventos de adentro hacia afuera hasta el nodo raíz.

- Ya sea captura de eventos o propagación de eventos, todos tienen un comportamiento común, que esPropagación de eventos, Es como una mecha, solo a través de la mecha se pueden detonar los petardos (oyentes de eventos) atados a la mecha. Imagínense, si la mecha no enciende el fuego, ¡entonces los petardos solo se apagarán! ! !

- La secuencia de activación del flujo de eventos estándar de dom es:Atrapa primero y luego burbujea, Es decir, cuando se activa el evento dom, el evento se capturará primero y el evento se propagará a través de la propagación del evento después de que se capture el origen del evento.Los diferentes navegadores tienen diferentes implementaciones de esto. IE10 y los siguientes no admiten eventos de captura.Entonces hay una etapa de captura de eventos menos, IE11, Chrome, Firefox, Safari y otros navegadoresEntonces exista al mismo tiempo.

- Cuando se trata de la captura y propagación de eventos, debo mencionar dos métodos para el enlace de eventos, addEventListener y attachEvent. Por supuesto, hay otros métodos de enlace de eventos que no se presentan aquí.

　　addEventListener(event, listener, useCapture)　　

- Definición de parámetros:evento --- (nombre del evento, como clic, sin encendido), oyente --- función de monitoreo de eventos,useCapture---Ya sea para utilizar la captura de eventos para la captura de eventos,

- El valor predeterminado es falso, es decir, se adopta el método de propagación de eventos.

- AddEventListener es compatible con IE11, Chrome, Firefox, Safari y otros navegadores.

　　attachEvent(event,listener)　　

- Definición de parámetros: Evento --- (nombre del evento, como onclick, con on), escucha --- función de escucha del evento.

- AttachEvent se utiliza principalmente en los navegadores IE, y solo es compatible con IE10 y versiones anteriores. IE11 ha abandonado este método (Microsoft sigue siendo bastante interesante y se está acercando lentamente al estándar).