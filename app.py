import streamlit as st
from rembg import remove
from PIL import Image
import io

# Configuración de la página
st.set_page_config(page_title="Quita Fondos IA", page_icon="✂️", layout="centered")

st.title("✂️ Eliminador de Fondo Mágico")
st.write("Sube una imagen y nuestra Inteligencia Artificial eliminará el fondo automáticamente.")

# Cargar el archivo
archivo_subido = st.file_uploader("Sube tu imagen (JPG, JPEG o PNG)", type=["jpg", "jpeg", "png"])

if archivo_subido is not None:
    # Abrir la imagen subida
    imagen_original = Image.open(archivo_subido)
    
    # Mostrar la imagen original
    st.image(imagen_original, caption="Imagen Original", use_container_width=True)
    
    # Botón para accionar la IA
    if st.button("✨ Quitar Fondo Ahora"):
        with st.spinner("La IA está haciendo su magia... (puede tardar unos segundos)"):
            try:
                # Procesar la imagen
                imagen_sin_fondo = remove(imagen_original)
                
                # Mostrar el resultado
                st.success("¡Fondo eliminado con éxito!")
                st.image(imagen_sin_fondo, caption="Resultado sin fondo", use_container_width=True)
                
                # Preparar la imagen para descargarla
                buffer = io.BytesIO()
                imagen_sin_fondo.save(buffer, format="PNG")
                imagen_bytes = buffer.getvalue()
                
                # Botón de descarga
                st.download_button(
                    label="⬇️ Descargar Imagen en PNG",
                    data=imagen_bytes,
                    file_name="imagen_sin_fondo.png",
                    mime="image/png"
                )
            except Exception as e:
                st.error(f"Ocurrió un error al procesar la imagen: {e}")