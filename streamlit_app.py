import streamlit as st
import cohere

# Inicializar el cliente de Cohere
cohere_api_key = 'KDhsUSaH5D01hlEWHEOfZvNhowIGPZC2cUcCP1sO'  # Reemplaza con tu clave API
co = cohere.Client(cohere_api_key)

# Aplicación Streamlit
def main():
    st.title("Preguntas y respuestas sobre las leyes de Guatemala")

    # Entrada del usuario
    pregunta_usuario = st.text_input("Haz una pregunta sobre las leyes de Guatemala:")

    if st.button("Obtener respuesta"):
        # Llamar a la API de Cohere
        respuesta = co.chat(
            model='command',
            message=pregunta_usuario,
            temperature=0.3,
            chat_history=[{"role": "User", "message": pregunta_usuario}],
            prompt_truncation='AUTO',
            stream=True,
            citation_quality='accurate',
            connectors=[{"id": "web-search"}],
            documents=[]
        )

        # Convertir la respuesta a cadena antes de mostrarla
        st.text("Respuesta completa de Cohere:")
        st.write(str(respuesta))

        # Mostrar las respuestas sugeridas al usuario
        if "suggestedUserResponses" in respuesta:
            st.text("Respuestas sugeridas:")
            st.write(respuesta["suggestedUserResponses"])

if __name__ == "__main__":
    main()
