# Chocobo's Sanctuary


## Parte 2

http://localhost:8000/api/navigator/get-route/
```json
{
    "from_station": 0,
    "to_station": 72
}
```
valores del kilometro de cada estación

http://localhost:8000/api/navigator/plan-route/
```json
{
    "from_station": 0,
    "to_station": 72,
    "number_plate": "AB-12-34"
}
```
# Para conocerte mejor

**1. Cuáles crees que son los aspectos más importantes al momento de hacer Code Review**

    R: Es muy importante no pasar alguna vulnerabilidad a producción, algo que pueda afectar lo que ya estaba funcionando bien. También creo que es importante mantener algun estilo y formato en cada proyecto, buenas prácticas y también aprender de los demás.

**2. Has trabajado con control de versiones? Cuál ha sido el flujo que has utilizado? Por favor explicar.**

    R: Si, principamente con git y gitFlow (a veces con algunas variaciones según la compañia o el proyecto)

**3. Cuál ha sido tu experiencia utilizando herramientas fuera de desarrollo del código mismo? (AWS, GCP, VPS, Docker, etc.)**

    R: No mucho más de lo que he necesitado para resolver tareas específicas, aunque con Docker he tenido que trabajar mucho más ya sea creando proyectos desde cero o dockerizando algunos ya existentes.

**4. Tienes algún servicio en la nube favorito? Cuál y por qué?**

    R: Aunque me gustan varios servicios de AWS puedo decir que en este momento DynamoDB y Lambda son mis preferidos, son los servicios que he usado últimamente y me parecen geniales para usos especícos donde se requiera.

**5. Has tenido experiencia con microservicios? En caso de que la tengas, podrías explicar por qué en ese caso fue mejor un microservicio que otro tipo de arquitectura?**

    R: Si, En las compañías donde he trabajado he tenido la oportunidad de mantener y/o desarrollar microservicios y siempre es mejor para separar responsabilidades en aplicaciones y no tener todo junto en un proyecto que finalmente se convierte en un dolor de cabeza ya que si pasa algún problema no cae toda la aplicación si no que sólo una parte.