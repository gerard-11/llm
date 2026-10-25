import os

import streamlit as st
from openai import OpenAI


MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def generar_respuesta(client: OpenAI, instrucciones: str, solicitud: str) -> str:
    """Envía una solicitud al modelo y devuelve únicamente el texto generado."""
    respuesta = client.responses.create(
        model=MODEL,
        instructions=instrucciones,
        input=solicitud,
    )
    return respuesta.output_text.strip()


def main() -> None:
    st.set_page_config(
        page_title="Asistente de escritura",
        page_icon="✍️",
        layout="centered",
    )

    st.title("✍️ Asistente de escritura automática")
    st.write(
        "Corrige textos, continúa ideas o genera contenido desde cero con ayuda "
        "de un modelo de lenguaje."
    )

    clave_guardada = os.getenv("OPENAI_API_KEY", "")
    if clave_guardada:
        api_key = clave_guardada
        st.success("Clave de OpenAI cargada desde la variable de entorno.")
    else:
        api_key = st.text_input(
            "Ingresa tu clave de OpenAI para comenzar:",
            type="password",
            help="También puedes definir OPENAI_API_KEY antes de ejecutar la aplicación.",
        )

    if not api_key:
        st.info("Necesitas una clave de OpenAI para utilizar el asistente.")
        return

    client = OpenAI(api_key=api_key)
    tarea = st.selectbox(
        "¿En qué te puedo ayudar hoy?",
        (
            "Mejorar redacción y ortografía",
            "Sugerir continuación",
            "Escribir un texto desde cero",
        ),
    )

    if tarea == "Mejorar redacción y ortografía":
        texto = st.text_area("Pega aquí tu texto:", height=180)
        if st.button("Mejorar texto", type="primary"):
            if not texto.strip():
                st.warning("Por favor, ingresa un texto para mejorar.")
                return
            with st.spinner("Revisando tu texto..."):
                try:
                    resultado = generar_respuesta(
                        client,
                        "Eres un editor experto de español. Conserva el significado "
                        "original, corrige ortografía y gramática, y mejora la claridad "
                        "sin agregar información. Devuelve solo el texto corregido.",
                        texto,
                    )
                    st.subheader("Texto mejorado")
                    st.write(resultado)
                except Exception as error:
                    st.error(f"No se pudo consultar OpenAI: {error}")

    elif tarea == "Sugerir continuación":
        texto = st.text_area("Escribe el inicio de tu texto:", height=180)
        if st.button("Sugerir continuación", type="primary"):
            if not texto.strip():
                st.warning("Por favor, ingresa el inicio de un texto.")
                return
            with st.spinner("Pensando en ideas..."):
                try:
                    resultado = generar_respuesta(
                        client,
                        "Eres un asistente de escritura creativo. Continúa el texto de "
                        "forma coherente, respeta su tono y agrega un solo párrafo. "
                        "Devuelve únicamente la continuación.",
                        texto,
                    )
                    st.subheader("Sugerencia")
                    st.write(resultado)
                except Exception as error:
                    st.error(f"No se pudo consultar OpenAI: {error}")

    else:
        tema = st.text_input(
            "¿Sobre qué tema quieres escribir?",
            placeholder="Ejemplo: un correo para solicitar vacaciones",
        )
        tono = st.selectbox(
            "Elige el tono del texto:",
            ("Profesional", "Casual", "Creativo", "Persuasivo"),
        )
        if st.button("Generar texto", type="primary"):
            if not tema.strip():
                st.warning("Por favor, ingresa un tema.")
                return
            with st.spinner("Escribiendo..."):
                try:
                    resultado = generar_respuesta(
                        client,
                        f"Eres un escritor experto. Redacta un texto en español sobre el "
                        f"tema indicado con un tono {tono.lower()}. Entrega un texto claro, "
                        "bien estructurado y listo para usar.",
                        tema,
                    )
                    st.subheader("Texto generado")
                    st.write(resultado)
                except Exception as error:
                    st.error(f"No se pudo consultar OpenAI: {error}")


if __name__ == "__main__":
    main()
