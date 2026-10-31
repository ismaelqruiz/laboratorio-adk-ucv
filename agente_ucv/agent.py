
from google.adk.agents.llm_agent import Agent


def explicar_concepto(concepto: str) -> dict:
    """
    Explica conceptos relacionados con el curso de Sistemas Inteligentes.
    """

    conceptos = {
        "sistema inteligente": (
            "Un sistema inteligente es un sistema capaz de percibir información, "
            "procesarla y tomar decisiones para alcanzar determinados objetivos."
        ),
        "inteligencia artificial": (
            "La inteligencia artificial es una rama de la informática que desarrolla "
            "sistemas capaces de realizar tareas que requieren inteligencia humana."
        ),
        "agente inteligente": (
            "Un agente inteligente percibe su entorno mediante sensores y actúa "
            "sobre él mediante actuadores para cumplir un objetivo."
        ),
        "machine learning": (
            "Machine Learning es una rama de la inteligencia artificial que permite "
            "a los sistemas aprender patrones a partir de datos."
        ),
        "deep learning": (
            "Deep Learning es una técnica de aprendizaje automático que utiliza "
            "redes neuronales con múltiples capas."
        ),
        "red neuronal": (
            "Una red neuronal artificial es un modelo computacional inspirado "
            "en el funcionamiento de las neuronas biológicas."
        ),
        "algoritmo": (
            "Un algoritmo es un conjunto ordenado de instrucciones para resolver "
            "un problema o realizar una tarea."
        ),
        "minimax": (
            "Minimax es un algoritmo de búsqueda utilizado en juegos de dos "
            "jugadores para seleccionar movimientos óptimos."
        ),
        "big data": (
            "Big Data comprende el procesamiento y análisis de grandes volúmenes "
            "de datos para obtener información útil."
        ),
        "procesamiento de lenguaje natural": (
            "El procesamiento de lenguaje natural permite que las computadoras "
            "interpreten y procesen el lenguaje humano."
        )
    }

    concepto = concepto.lower().strip()

    if concepto in conceptos:
        return {
            "status": "success",
            "concepto": concepto,
            "explicacion": conceptos[concepto]
        }

    return {
        "status": "not_found",
        "concepto": concepto,
        "explicacion": (
            "El concepto no se encuentra registrado. "
            "Puedes consultar sobre inteligencia artificial, "
            "agentes inteligentes, Machine Learning o Minimax."
        )
    }


root_agent = Agent(
    model="gemini-3.5-flash-lite",
    name="agente_ucv",
    description=(
        "Agente académico especializado en el curso de Sistemas Inteligentes "
        "de la Universidad César Vallejo."
    ),
    instruction="""
    Eres un asistente académico especializado en el curso de Sistemas Inteligentes.

    Tus funciones son:
    1. Explicar conceptos de inteligencia artificial.
    2. Orientar sobre agentes inteligentes.
    3. Explicar Machine Learning y Deep Learning.
    4. Resolver dudas sobre algoritmos de búsqueda.
    5. Apoyar el aprendizaje de los estudiantes.

    Responde siempre en español.
    Utiliza explicaciones claras, sencillas y educativas.

    Cuando el estudiante consulte un concepto registrado,
    utiliza la herramienta explicar_concepto.

    Si el concepto no está registrado, intenta explicarlo
    utilizando tus conocimientos y aclara que no está en el diccionario.
    """,
    tools=[explicar_concepto]
)
