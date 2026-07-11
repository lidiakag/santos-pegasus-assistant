🤖 Santos Pegasus Assistant

Agente inteligente desarrollado con Python, LangChain, Gemini, Streamlit y técnicas de RAG (Retrieval-Augmented Generation) para responder preguntas utilizando documentación interna de una empresa.

Características
- Consulta múltiples documentos PDF.
- Responde preguntas en lenguaje natural.
- Utiliza Gemini como modelo de lenguaje.
- Recupera información mediante RAG.
- Muestra las fuentes utilizadas.
- Interfaz desarrollada con Streamlit.

Tecnologías
- Python
- Streamlit
- LangChain
- Google Gemini
- BM25 Retriever
- PyPDF
- dotenv

Estructura
alura-agente/
│
├── documentos/
├── agente.py
├── app.py
├── requirements.txt
└── README.md

Cómo ejecutar
pip install -r requirements.txt
Crear un archivo
.env
con
GOOGLE_API_KEY=TU_API_KEY
Luego
streamlit run app.py

Ejemplos
Pregunta
¿Cuál es el objetivo del onboarding?
Respuesta
Al finalizar la primera semana el desarrollador debe tener su entorno configurado...

Pregunta
¿Qué es un post mortem?
Respuesta
Explica el procedimiento de análisis posterior a un incidente.

Arquitectura
Usuario
     │
     ▼
Streamlit
     │
     ▼
Retriever (BM25)
     │
     ▼
PDF
     │
     ▼
Gemini
     │
     ▼
Respuesta