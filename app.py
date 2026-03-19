import streamlit as st
from rembg import remove
from PIL import Image
import io

# Configuración básica de la página web
st.set_page_config(page_title="Quita Fondos IA", page_icon="✂️", layout="centered")

# Títulos y descripción
st.title("✂️ Eliminador de Fondo Mágico")
st.write("Sube una imagen y nuestra Inteligencia Artificial eliminará el fondo en segundos.")

# 1. Crear el botón para subir la imagen
archivo_subido = st.file_uploader("Sube tu imagen aquí (JPG o PNG)", type=["jpg", "jpeg", "png"])

# 2. Si el usuario sube una imagen, empezamos a procesar
if archivo_subido is not None:
    
    # Mostrar la imagen original
    st.subheader("Imagen Original")
    imagen_original = Image.open(archivo_subido)
    st.image(imagen_original, use_container_width=True)
    
    # Botón para activar la IA
    if st.button("✨ Quitar Fondo Ahora"):
        
        # Mostrar un mensaje de carga mientras la IA trabaja
        with st.spinner("La IA está haciendo su magia... (puede tardar un poquito)"):
            try:
                # El código mágico que probaste en Colab
                imagen_sin_fondo = remove(imagen_original)
                
                st.success("¡Fondo eliminado con éxito!")
                
                # Mostrar el resultado
                st.subheader("Resultado")
                st.image(imagen_sin_fondo, use_container_width=True)
                
                # Preparar la imagen para poder descargarla
                buffer = io.BytesIO()
                imagen_sin_fondo.save(buffer, format="PNG")
                imagen_bytes = buffer.getvalue()
                
                # Crear el botón de descarga
                st.download_button(
                    label="⬇️ Descargar Imagen Transparente (PNG)",
                    data=imagen_bytes,
                    file_name="imagen_sin_fondo.png",
                    mime="image/png"
                )
                
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
