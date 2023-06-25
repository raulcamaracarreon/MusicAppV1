import streamlit as st
from blues_page import show_blues_page
from modal_chord_page import show_modal_chord_page

# Definir las páginas en tu aplicación
paginas = {
    "Progresiones de blues": show_blues_page,
    "Progresiones modales de acordes": show_modal_chord_page,
    # Aquí puedes agregar más páginas según lo necesites...
}

# Crear un menú de selección en la barra lateral
pagina_seleccionada = st.sidebar.radio("Selecciona una función", list(paginas.keys()))

# Mostrar la página seleccionada
paginas[pagina_seleccionada]()

