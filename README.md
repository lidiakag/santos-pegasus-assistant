# 🤖 Santos Pegasus Assistant

Agente inteligente desarrollado con Python, LangChain, Gemini, Streamlit y técnicas de RAG (Retrieval-Augmented Generation) para responder preguntas utilizando documentación interna de una empresa.

## Características
- Consulta múltiples documentos PDF.
- Responde preguntas en lenguaje natural.
- Utiliza Gemini como modelo de lenguaje.
- Recupera información mediante RAG.
- Muestra las fuentes utilizadas.
- Interfaz desarrollada con Streamlit.

## Tecnologías
- Python
- Streamlit
- LangChain
- Google Gemini
- BM25 Retriever
- PyPDF
- dotenv

## Cómo ejecutar
pip install -r requirements.txt
Crear un archivo .env con GOOGLE_API_KEY=TU_API_KEY
Luego streamlit run app.py

## Ejemplos
### Pregunta
¿Cuál es el objetivo del onboarding?
### Respuesta
De acuerdo con el documento onboarding.pdf, el objetivo de la primera semana es tener el entorno configurado y conocer el equipo. Además, el plan de 30/60/90 días se define como una guía de rampaje progresiva, donde se espera alcanzar la productividad plena aproximadamente al tercer mes, dependiendo del nivel de seniority.
### Pregunta
¿Qué tecnologías utiliza el equipo backend?
### Respuesta
Basado en los documentos proporcionados, el equipo utiliza las siguientes tecnologías y herramientas:
Spring: Específicamente ApplicationEventPublisher para gestionar comunicaciones asíncronas y el patrón Observer.
AWS SES y SQS: Utilizados por el microservicio de integración con servicios de notificación.
IA Generativa y LLM: Integrados en los back-ends, utilizando la arquitectura RAG (Retrieval-Augmented Generation).
GitHub: Para el manejo de código, comentarios, commits y Pull Requests.
Slack: Para comunicación interna y recepción de notificaciones de GitHub (canal #code-reviews).
Pipelines CI/CD: Para la automatización de despliegues.
Estrategias de despliegue: Blue-Green y Canary Releases.

## Arquitectura
Usuario -> Streamlit -> Retriever (BM25) -> PDF -> Gemini -> Respuesta