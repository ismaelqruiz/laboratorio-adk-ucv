# Laboratorio 8: Agente Inteligente con Google ADK

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de un agente inteligente académico utilizando Google Agent Development Kit (ADK) y Python, orientado al curso de Sistemas Inteligentes de la Universidad César Vallejo.

El agente utiliza el modelo Gemini 3.5 Flash Lite para interpretar consultas de los estudiantes y proporcionar explicaciones sobre conceptos relacionados con inteligencia artificial, agentes inteligentes, Machine Learning, Deep Learning y algoritmos de búsqueda.

Además, incorpora una herramienta denominada `explicar_concepto`, que permite consultar un diccionario de conceptos previamente registrados.

## 2. Objetivos

- Implementar un agente inteligente utilizando Google ADK.
- Integrar un modelo de lenguaje de Gemini.
- Gestionar las dependencias mediante Poetry.
- Implementar pruebas automatizadas utilizando Pytest.
- Configurar integración continua mediante GitHub Actions.
- Analizar la calidad del código mediante SonarQube Cloud.

## 3. Tecnologías utilizadas

| Tecnología | Descripción |
|---|---|
| Python 3.13 | Lenguaje de programación |
| Google ADK | Desarrollo del agente inteligente |
| Gemini 3.5 Flash Lite | Modelo de inteligencia artificial |
| Poetry | Gestión de dependencias |
| Pytest | Pruebas automatizadas |
| Git y GitHub | Control de versiones |
| GitHub Actions | Integración continua |
| SonarQube Cloud | Análisis estático de código |
| python-dotenv | Gestión de variables de entorno |

## 4. Estructura del proyecto

```text
laboratorio-adk-ucv/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── agente_ucv/
│   ├── __init__.py
│   └── agent.py
│
├── tests/
│   └── test_agent.py
│
├── .env
├── .gitignore
├── README.md
├── pyproject.toml
└── poetry.lock
```

## 5. Funcionalidades del agente

El agente académico permite:

- Explicar qué es un sistema inteligente.
- Definir conceptos de inteligencia artificial.
- Explicar el funcionamiento de los agentes inteligentes.
- Describir Machine Learning y Deep Learning.
- Explicar las redes neuronales.
- Definir algoritmos.
- Explicar el algoritmo Minimax.
- Describir conceptos relacionados con Big Data.
- Explicar el procesamiento de lenguaje natural.
- Identificar conceptos que no se encuentran registrados en el diccionario.

## 6. Requisitos previos

Para ejecutar el proyecto se necesita:

- Python 3.13.
- Poetry.
- Una API Key de Google AI Studio.
- Git.

## 7. Instalación y configuración

**Paso 1. Clonar el repositorio**

```bash
git clone https://github.com/ismaelqruiz/laboratorio-adk-ucv.git
```

**Paso 2. Ingresar a la carpeta**

```bash
cd laboratorio-adk-ucv
```

**Paso 3. Instalar las dependencias**

```bash
poetry install
```

**Paso 4. Configurar las variables de entorno**

Crear un archivo `.env` en la raíz del proyecto:

```env
GOOGLE_API_KEY=TU_API_KEY
```

Reemplazar `TU_API_KEY` por una clave válida de Google AI Studio.

**Importante:** el archivo `.env` está excluido del repositorio mediante `.gitignore` para proteger las credenciales.

## 8. Ejecución del agente

Para iniciar el agente desde la terminal:

```bash
poetry run adk run agente_ucv
```

También se puede iniciar la interfaz web de ADK:

```bash
poetry run adk web --port 8000
```

Una vez iniciado, el estudiante puede realizar preguntas relacionadas con Sistemas Inteligentes.

## 9. Pruebas automatizadas

El proyecto utiliza Pytest para verificar el funcionamiento de la herramienta `explicar_concepto`.

Para ejecutar las pruebas:

```bash
poetry run pytest
```

Las pruebas verifican:

1. Explicación de un sistema inteligente.
2. Explicación de Machine Learning.
3. Identificación de conceptos no registrados.
4. Normalización de conceptos mediante espacios y mayúsculas.

**Resultado obtenido durante el desarrollo:**

```text
4 passed in 0.77s
```

## 10. Integración continua con GitHub Actions

Se configuró un flujo de integración continua en:

`.github/workflows/ci.yml`

El flujo se ejecuta automáticamente cuando se realizan cambios en la rama `main` o se crea una solicitud de incorporación de cambios.

Sus principales actividades son:

- Descargar el repositorio.
- Configurar Python 3.13.
- Instalar Poetry.
- Instalar las dependencias.
- Ejecutar las pruebas automatizadas con Pytest.

La ejecución del flujo fue completada satisfactoriamente en GitHub Actions.

## 11. Análisis de calidad con SonarQube Cloud

Se integró el repositorio con SonarQube Cloud para realizar un análisis estático del código fuente.

El análisis permitió identificar métricas de seguridad, fiabilidad y mantenibilidad, además de detectar tres alertas de seguridad relacionadas con la configuración de dependencias y scripts de instalación.

Estos resultados permiten identificar oportunidades de mejora en el proyecto.

## 12. Repositorio

El código fuente se encuentra disponible en GitHub:

https://github.com/ismaelqruiz/laboratorio-adk-ucv

## 13. Autoría

**Proyecto académico:** Laboratorio 8 - Sistemas Inteligentes.

**Universidad:** Universidad César Vallejo.

**Autor:** Ismael Quispe.

**Curso:** Sistemas Inteligentes.
