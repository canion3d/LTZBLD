import streamlit as st
import pyvista as pv
import tempfile
import os

# Set Streamlit app title and layout
st.title("3D Model Viewer")

# Function to load and display 3D model
def load_model(file):
    try:
        # Save the uploaded file to a temporary directory
        temp_dir = tempfile.TemporaryDirectory()
        file_path = os.path.join(temp_dir.name, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        model = pv.read(file_path)
        st.write("Model loaded successfully!")
        st.write(model)

        # Display the 3D model using the PyVista plotter
        plotter = pv.Plotter(window_size=(800, 600))
        plotter.add_mesh(model, color='green')
        plotter.show()

    except Exception as e:
        st.write("Error loading the model:", e)

# Instructions and example models
st.sidebar.write("**Instructions:**")
st.sidebar.write("1. Upload a 3D model file (OBJ, STL, or VTK).")
st.sidebar.write("2. Wait for the model to load and display.")
st.sidebar.write("3. Use mouse controls to rotate, zoom, and pan the model.")
st.sidebar.write("---")
st.sidebar.write("**Example Models:**")
st.sidebar.write("- [Example OBJ model](https://github.com/pyvista/pyvista/blob/master/examples/examples/IO/test_obj.obj)")
st.sidebar.write("- [Example STL model](https://github.com/pyvista/pyvista/blob/master/examples/examples/IO/Bunny.vtp)")
