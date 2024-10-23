# Documentación de Metadatos - Recopilación de Datos de Instagram

> **Observación importante**: La mayoría de los metadatos extraídos no aportarán valor al análisis final. Durante la fase de limpieza de datos se seleccionarán únicamente las variables relevantes para el estudio, descartando aquellas que no contribuyan significativamente al análisis.

## Fuente de los Datos
Los datos son extraídos directamente de Instagram utilizando la biblioteca Instaloader. Se recopilan dos tipos principales de datos:
- Datos de perfil de usuario
- Posts individuales y sus metadatos asociados

## Fecha de Recogida
La recopilación de datos es un proceso continuo que registra la fecha UTC específica para cada post descargado en su metadata correspondiente.

## Formato de los Datos
Los datos se almacenan en los siguientes formatos:

### Datos de Perfil
- **Formato**: JSON
- **Ubicación**: `data/{username}/raw/{username}_metadata.json`

### Posts
- **Metadatos**: Archivos JSON
- **Ubicación**: `data/{username}/raw/metadata/{fecha_UTC}.json`
- **Medios**: Imágenes en formato JPG/JPEG

## Licencia de Uso
Los datos recopilados están sujetos a los términos de servicio de Instagram y deben utilizarse de acuerdo con sus políticas de uso.

## Descripción de las Variables

### Metadatos de Perfil
| Variable | Descripción |
|----------|-------------|
| username | Nombre de usuario en Instagram |
| full_name | Nombre completo del usuario |
| biography | Descripción biográfica del perfil |
| external_url | URL externa vinculada al perfil |
| followers | Número de seguidores |
| followees | Número de usuarios seguidos |
| mediacount | Cantidad total de publicaciones |
| is_verified | Estado de verificación del perfil |
| is_private | Estado de privacidad del perfil |
| is_business_account | Indica si es una cuenta comercial |
| business_category_name | Categoría del negocio (si aplica) |
| profile_pic_url | URL de la foto de perfil |
| biography_hashtags | Hashtags en la biografía |
| biography_mentions | Menciones en la biografía |

### Metadatos de Posts
| Variable | Descripción |
|----------|-------------|
| __typename | Tipo de publicación (GraphImage, GraphSidecar, GraphVideo) |
| accessibility_caption | Descripción de accesibilidad de la imagen |
| dimensions | Dimensiones de la imagen (altura y ancho) |
| display_url | URL de la imagen |
| edge_liked_by | Contador de "me gusta" |
| edge_media_to_caption | Texto de la publicación |
| edge_media_to_comment | Número de comentarios |
| edge_sidecar_to_children | Lista de medios en publicaciones múltiples |
| location | Información de ubicación (nombre, id) |
| owner | Información del propietario del post |
| taken_at_timestamp | Fecha y hora de publicación en timestamp |
| is_video | Indica si es un video |
| edge_media_to_tagged_user | Lista de usuarios etiquetados |
| thumbnail_resources | Lista de miniaturas en diferentes resoluciones |

## Notas Adicionales
- Los datos se organizan en una estructura de directorios específica para cada usuario
- Se mantiene una copia raw (sin procesar) de todos los datos descargados
- Las imágenes y videos se almacenan en sus formatos originales
- Los metadatos incluyen información temporal precisa para cada elemento
