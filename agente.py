from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.retrievers import BM25Retriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()


def crear_agente(ruta_carpeta: str):
    carpeta = Path(ruta_carpeta)

    if not carpeta.exists():
        raise FileNotFoundError(
            f"No se encontró la carpeta: {carpeta.resolve()}"
        )

    archivos_pdf = sorted(carpeta.glob("*.pdf"))

    if not archivos_pdf:
        raise ValueError(
            "No se encontraron archivos PDF en la carpeta documentos."
        )

    documentos = []

    # Leer todos los PDF
    for archivo_pdf in archivos_pdf:
        loader = PyPDFLoader(str(archivo_pdf))
        paginas = loader.load()

        for pagina in paginas:
            pagina.metadata["archivo"] = archivo_pdf.name

        documentos.extend(paginas)

    if not documentos:
        raise ValueError(
            "Los documentos PDF no contienen texto procesable."
        )

    # Dividir el contenido en fragmentos
    divisor = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=200,
    )

    fragmentos = divisor.split_documents(documentos)

    # Buscador local BM25: no consume la API de Gemini
    retriever = BM25Retriever.from_documents(fragmentos)
    retriever.k = 5

    # Gemini solo redacta la respuesta final
    modelo = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_template(
        """
Eres un asistente especializado en responder preguntas sobre la
documentación interna de Santos Pegasus Soluciones.

Responde exclusivamente con la información entregada en el contexto.

No inventes información ni utilices conocimientos externos.

Si la respuesta no aparece en los documentos, responde exactamente:

"No encontré esa información en los documentos."

Contexto:
{contexto}

Pregunta:
{pregunta}

Respuesta:
"""
    )

    cadena = prompt | modelo

    def responder(pregunta: str):
        documentos_relevantes = retriever.invoke(pregunta)

        contexto = "\n\n".join(
            f"Documento: {doc.metadata.get('archivo', 'Desconocido')}\n"
            f"Página: {doc.metadata.get('page', 0) + 1}\n"
            f"Contenido:\n{doc.page_content}"
            for doc in documentos_relevantes
        )

        respuesta = cadena.invoke(
            {
                "contexto": contexto,
                "pregunta": pregunta,
            }
        )

        # Obtener solo el texto de Gemini
        if hasattr(respuesta, "text"):
            texto = respuesta.text()

        elif isinstance(respuesta.content, list):
            partes = []

            for parte in respuesta.content:
                if isinstance(parte, dict):
                    partes.append(parte.get("text", ""))

            texto = "".join(partes)

        else:
            texto = str(respuesta.content)

        return {
            "respuesta": texto.strip(),
            "documentos": documentos_relevantes,
            "cantidad_archivos": len(archivos_pdf),
        }

    return responder