# Proyecto de Descubrimiento del Conocimiento en Instagram

Este proyecto tiene como objetivo analizar y extraer conocimiento de perfiles de Instagram utilizando técnicas de minería de datos y aprendizaje automático.

## Estructura del Proyecto

El proyecto está dividido en cinco fases principales:

1. Recogida de datos
2. Análisis de datos
3. Minería de datos
4. Extracción del conocimiento
5. Presentación de resultados

## Motivación del Proyecto

El objetivo principal es realizar un análisis detallado del flujo temporal de publicaciones en un perfil de Instagram. Se busca extraer e inferir conocimiento tanto de las imágenes publicadas como de la metadata asociada a las publicaciones y al perfil en su conjunto. Utilizando modelos de machine learning, se pretende descubrir patrones ocultos en las imágenes y correlacionarlos con las interacciones de los usuarios y la naturaleza temporal de los posts.

## Requisitos

- Python 3.8+
- Bibliotecas adicionales listadas en `requirements.txt`

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/PedroOrtix/ddc_project.git
   cd ddc_project
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Uso

(Aquí puedes agregar instrucciones específicas sobre cómo ejecutar las diferentes partes del proyecto)

## Documentación de Metadatos

Los datos son extraídos directamente de Instagram utilizando la biblioteca Instaloader. Se recopilan datos de perfil de usuario y posts individuales con sus metadatos asociados. Estos datos son fundamentales para responder a las preguntas de investigación planteadas, permitiendo explorar las interacciones de los usuarios y la naturaleza temporal de las publicaciones.

## Proceso de Limpieza de Datos

El proceso de limpieza y transformación de los datos crudos tiene como objetivo obtener datos estructurados y relevantes que complementen el análisis de imágenes. La metadata limpia sirve como complemento crucial al análisis visual, proporcionando contexto, validación y enriquecimiento del análisis.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
