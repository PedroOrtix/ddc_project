# Motivación del Proyecto

## Objetivo General del Proyecto
El objetivo principal de este proyecto es realizar un análisis detallado del flujo temporal de publicaciones en un perfil de Instagram. Se busca extraer e inferir conocimiento tanto de las imágenes publicadas como de la metadata asociada a las publicaciones y al perfil en su conjunto. Utilizando modelos de machine learning (ML), se pretende descubrir patrones ocultos en las imágenes (como captions, etiquetas, colores, composición, calidad técnica, etc.) y correlacionarlos con las interacciones de los usuarios (likes, comentarios) y la naturaleza temporal de los posts.

## Preguntas de Investigación o Hipótesis
- ¿Qué patrones visuales y de contenido se correlacionan con un mayor engagement en las publicaciones de Instagram?
- ¿Cómo influye la temporalidad de las publicaciones en el comportamiento de los usuarios?
- ¿Existen características específicas en las imágenes que predicen el éxito de una publicación?
- ¿Qué rol juegan las descripciones y hashtags en la visibilidad y popularidad de los posts?

> **Nota**: Las preguntas de investigación pueden variar a medida que el proyecto se desarrolle, especialmente al utilizar determinados modelos de machine learning que puedan revelar nuevas perspectivas o requerir ajustes en las hipótesis iniciales.

## Justificación de los Datos Seleccionados
Los datos seleccionados para este análisis incluyen las imágenes publicadas en el perfil de Instagram, así como la metadata asociada a los posts (fecha de publicación, likes, comentarios) y la metadata del perfil en su conjunto. Estos datos son fundamentales para responder a las preguntas de investigación planteadas. Las imágenes aportan una gran cantidad de información visual, que puede ser analizada mediante técnicas de ML para extraer detalles sobre su contenido, estética y composición. Al combinar estos insights con la metadata del perfil y de los posts, es posible explorar las interacciones de los usuarios y la naturaleza temporal de las publicaciones, lo cual es clave para comprender el impacto y la evolución del contenido publicado.

## Desafíos Potenciales con los Datos Limpiados
El principal desafío potencial con los datos limpiados es la posibilidad de insuficiencia o sesgo en los datos recopilados. La calidad y cantidad de las imágenes y la metadata pueden no ser suficientes para extraer inferencias sólidas, especialmente si el perfil analizado tiene un número limitado de posts o interacciones. Además, la metadata disponible puede no reflejar completamente la actividad del usuario, lo que podría introducir sesgos en el análisis. Otro desafío significativo es la limitación impuesta por los rate limits y las restricciones de la API de Instagram, así como de la librería utilizada para la extracción de datos, lo que puede impedir obtener toda la información deseada. Esto puede limitar el acceso a ciertas publicaciones o interacciones, afectando la completitud del análisis. Por último, la falta de consistencia en las imágenes, en términos de calidad visual o estilo, podría complicar el proceso de inferencia mediante técnicas de ML, y se debe considerar la posibilidad de errores en la generación automática de captions o etiquetas, lo cual podría impactar la precisión de los resultados.
