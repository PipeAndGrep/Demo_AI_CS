import streamlit as st
import openai


import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Aplicación Streamlit
st.title("Pregúntame algo")
st.write("Introduce un prompt a continuación y obtén una respuesta del modelo GPT de OpenAI:")

# Crea un área de texto para que el usuario ingrese su input
user_input = st.text_area("Introduce tu prompt:", placeholder="Escribe tu mensaje aquí...")

# Agrega un botón para enviar el input
if st.button("Obtener respuesta"):
    if user_input.strip():
        try:
            # Llamada a la nueva API de OpenAI con el modelo GPT-3.5 o GPT-4
            response = client.chat.completions.create(
                model=model_name,  # Puedes usar el modelo que prefieras aquí
                messages=[{"role": "user", "content": user_input}],
                top_p=1.0,
                max_tokens=1000,
                temperature=1.0,
            )
 
            # Extrae la respuesta de GPT
            #output = response['choices'][0]['message']['content'].strip()
            output = response.choices[0].message.content.strip()

            # Muestra la respuesta
            st.subheader("Respuesta de OpenAI:")
            st.write(output)
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
    else:
        st.warning("Por favor, introduce un prompt válido antes de enviar.")

# Pie de página opcional
st.write("---")
st.write("Un App de prueba conectando al API de OpenAI .")
