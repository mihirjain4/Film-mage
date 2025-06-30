import streamlit as st
import os
import zipfile
from PIL import Image
import PIL.Image
from presets import * # Assuming preset.py contains the filter functions

def preset_app(c):
    """Applies image presets to selected images."""
    st.title("Preset Application App")
    c.execute("SELECT title FROM events")
    ev = c.fetchall()
    ev = [item for sublist in ev for item in sublist]
    option1 = st.selectbox("Where to try Presets?", ["Events", "Your Images"])
    if option1 == "Events":
        selected_ev = st.selectbox("Which Event?", ev)
        input_folder = os.path.join("uploads",selected_ev)
    elif  option1 == "Your Images":
        selected_ev = st.selectbox("Which Event?", ev)
        input_folder = os.path.join("output", selected_ev, st.session_state.username)

    if os.path.isdir(input_folder):
        st.write("Images in the directory:")
        image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG'))]
        selected_image = st.selectbox("Select an image:", image_files)
        image_path = os.path.join(input_folder, selected_image)
        image = PIL.Image.open(image_path)
        st.image(image, caption="Original Image", use_column_width=True)

        filter_option = st.selectbox("Select a filter:",
                                     ["None", "Inkwell", "XPro", "Lark", "Hudson", "1977", "Aden", "Branan", "Brooklyn",
                                      "Clarendon", "Earlybird", "Gingham", "Kelvin", "Lofi", "Maven", "Mayfair",
                                      "Willow",
                                      "Moon", "Nashville", "Slumber", "Reyes", "Rise", "Valencia", "Perpetua",
                                      "Stinson",
                                      "Toaster"])
        if filter_option != "None":
            # Apply filter to single image
            filter_func_map = {
                "Inkwell": apply_inkwell, "XPro": apply_xpro, "Lark": apply_lark, "Hudson": apply_hudson,
                "1977": apply_1977, "Aden": apply_aden, "Branan": apply_brannan, "Brooklyn": apply_brooklyn,
                "Clarendon": apply_clarendon, "Earlybird": apply_earlybird, "Gingham": apply_gingham,
                "Kelvin": apply_kelvin, "Lofi": apply_lofi, "Maven": apply_maven, "Mayfair": apply_mayfair,
                "Willow": apply_willow, "Moon": apply_moon, "Nashville": apply_nashville, "Slumber": apply_slumber,
                "Reyes": apply_reyes, "Rise": apply_rise, "Valencia": apply_valencia, "Perpetua": apply_perpetua,
                "Stinson": apply_stinson, "Toaster": apply_toaster
            }
            
            if filter_option in filter_func_map:
                filter_func_map[filter_option](image_path)
                st.write(f"Applied {filter_option} filter.")
                edited_image_path = os.path.join(input_folder, f'{filter_option.lower()}_{selected_image}')
                edited_image = PIL.Image.open(edited_image_path)
                st.image(edited_image, caption="Edited Image", use_column_width=True)
                os.remove(edited_image_path) # Clean up the temporary edited image

            if st.button("Apply it to all images"):
                if filter_option in filter_func_map:
                    filter_func_map[filter_option](input_folder) # Apply to folder
                    st.write(f"Filter applied to all images in the directory.")
                    
                    f = filter_option.lower()
                    output_path = os.path.join(input_folder,f) # This path might be incorrect if filters create subfolders
                    
                    # Assuming filters save processed images in a subfolder named after the filter
                    # You might need to adjust this based on how your `preset.py` functions work.
                    # If they overwrite the original, this part needs rethinking.
                    
                    if os.path.exists(output_path):
                        image_files = os.listdir(output_path)
                        num_images = len(image_files)
                        num_cols = 5
                        cols = st.columns(num_cols)
                        st.write(f"Found {len(image_files)} images.")

                        selected_images = []
                        for i, image_file in enumerate(image_files):
                            image_path = os.path.join(output_path, image_file)
                            img = Image.open(image_path)
                            checkbox = cols[i % num_cols].checkbox(label=f"Image {i + 1}", key=f"checkbox_{i}")
                            if checkbox:
                                selected_images.append(image_path)
                            cols[i % num_cols].image(img, caption=f"Image {i + 1}")
                        with zipfile.ZipFile(f"{f}_selected.zip", "w") as zipf:
                            for image_path in selected_images:
                                zipf.write(image_path, os.path.basename(image_path))
                        with open(f"{f}_selected.zip", "rb") as f:
                            st.download_button(label="Download All Selected Images", data=f,
                                               file_name=f"{f}_selected.zip")
                    else:
                        st.warning(f"Output folder for {filter_option} filter not found: {output_path}")
    else:
        st.warning("Please select a valid directory path.")
