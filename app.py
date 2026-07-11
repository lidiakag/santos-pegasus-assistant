import streamlit as st

from agente import crear_agente


st.set_page_config(
    page_title="Santos Pegasus Assistant",
    page_icon="🤖",
    layout="centered",
)


@st.cache_resource
def cargar_agente():
    return crear_agente("documentos")


st.title("🤖 Santos Pegasus Assistant")

st.write(
    """
    Agente inteligente para consultar la documentación interna
    de Santos Pegasus Soluciones.
    """
)

st.info(
    "Las respuestas se generan utilizando exclusivamente "
    "el contenido de los documentos PDF."
)

try:
    responder = cargar_agente()

    pregunta = st.text_input(
        "Escribe una pregunta sobre los documentos:",
        placeholder=(
            "Ejemplo: ¿Cómo debe actuar el equipo "
            "frente a un incidente?"
        ),
    )

    if st.button("Consultar", type="primary"):
        if not pregunta.strip():
            st.warning(
                "Escribe una pregunta antes de continuar."
            )

        else:
            with st.spinner(
                "Buscando información en los documentos..."
            ):
                resultado = responder(pregunta)

            st.subheader("Respuesta")
            st.write(resultado["respuesta"])

            documentos = resultado["documentos"]

            if documentos:
                fuentes = sorted(
                    {
                        (
                            doc.metadata.get(
                                "archivo",
                                "Documento desconocido",
                            ),
                            doc.metadata.get("page", 0) + 1,
                        )
                        for doc in documentos
                    }
                )

                st.subheader("Fuentes consultadas")

                for archivo, pagina in fuentes:
                    st.caption(
                        f"📄 {archivo} — página {pagina}"
                    )

except Exception as error:
    st.error(
        f"No fue posible cargar el agente: {error}"
    )