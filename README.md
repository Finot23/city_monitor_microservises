# city_monitor_microservises
Proyecto de Sistemas distribuidos
Nombre del los autores: [Andres Mateo Dorantes, Jose Abraham Marin Sanchez, Luis Antonio Salinas Mata]
 Fecha: [27/062025]
UEA: [Sistemas distribuidos]

Objetivo del Proyecto


El propósito de este sistema es monitorear variables ambientales (temperatura, humedad y calidad del aire) en tiempo real en diferentes barrios de una ciudad mediante una arquitectura de microservicios. La solución utiliza Python, Flask, JSON y Docker para simular sensores, almacenar datos, detectar alertas y permitir consultas a través de una API.
Arquitectura General


La arquitectura está compuesta por cinco microservicios que se comunican vía HTTP REST con formato JSON, orquestados mediante Docker Compose. A continuación se resumen:
sensor_service: Simula sensores ambientales por barrio y envía datos periódicamente.


collector_service: Recibe datos de sensores y los reenvía a los servicios correspondientes.


storage_service: Guarda las mediciones por barrio y expone una API para consultarlas.


alert_service: Detecta valores extremos y registra alertas.


(Insertar diagrama aquí: arquitectura de microservicios, nombres de servicios, flujos HTTP)

Tecnologías Utilizadas


Lenguaje: Python 3.10+


Framework web: Flask


Comunicación: HTTP REST (requests + Flask)


Orquestación: Docker y Docker Compose


Formato de datos: JSON




Generación de Alertas


El servicio alert_service evalúa las mediciones y genera una alerta si se detecta alguna condición crítica, como:
Temperatura > 35 °C


Humedad < 20% o > 80%


Calidad del aire > 90 (escala arbitraria)


Las alertas se imprimen por consola y se almacenan para su consulta.
Ejemplo de alerta generada:
[ALERTA] Barrio: Centro — Temperatura crítica: 38.2 °C
(Captura de pantalla de consola o registro .log aquí)
API de Consulta


El servicio storage_service expone los siguientes endpoints:
GET /barrio/<nombre>: Devuelve las últimas mediciones del barrio.


GET /promedio/<nombre>: Devuelve el promedio de cada variable del barrio.


GET /todos (opcional): Devuelve todos los datos almacenados.


Ejemplo de respuesta:
{
 "barrio": "Centro",
 "promedios": {
 "temperatura": 26.8,
 "humedad": 58.2,
 "calidad_aire": 43.5
 }
 }
Conclusiones


La solución propuesta permite simular un sistema distribuido funcional, modular y escalable. Se puede extender fácilmente para soportar nuevos barrios, almacenamiento persistente y visualización en tiempo real. Docker permite levantar todo el ecosistema rápidamente, ideal para entornos de desarrollo y pruebas.
