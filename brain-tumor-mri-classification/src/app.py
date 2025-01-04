from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
import cv2
import os

# Load the trained model
model = load_model(r'C:\Users\berka\OneDrive\Masaüstü\yapay_zeka_proje\brain-tumor-mri-classification\src\model\best_model.keras')

# Define the labels
labels_map = {0: "Healthy", 1: "Glioma", 2: "Meningioma", 3: "Pituitary"}

def preprocess_image(image):
    # Resize the image to the target size
    image = cv2.resize(image, (200, 200))
    # Normalize the image
    image = image / 255.0
    # Expand dimensions to match the model input
    image = np.expand_dims(image, axis=0)
    return image

def main():
    st.title("MRI Görüntüleri ile Beyin Tümörü Sınıflandırma: Sağlıklı, Glioma, Meningioma, Hipofiz")
    st.image("https://storage.googleapis.com/kaggle-datasets-images/1608934/2645886/44583c7826d1bdea68598f0eef8e6cfc/dataset-cover.jpg?t=2021-09-25-22-03-08", width=450)
    st.write("MRI görüntülerini yapay zeka tabanlı algoritmalar kullanarak analiz eden bu sistem, potansiyel tümörlerin sınıflandırılmasını gerçekleştirir. Tümör tespiti ve sınıflandırılması için hızlı, doğru ve güvenilir sonuçlar elde edilebilir. Bu modül, hastalıkların erken teşhisini desteklemek ve tedavi süreçlerini iyileştirmek amacıyla kullanıma sunulmuştur.")

    # File uploader for image
    uploaded_file = st.file_uploader("Lütfen bir görsel yükleyin...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
        st.image(image, channels="BGR", caption="Uploaded Image", width=200)

        # Preprocess the image
        processed_image = preprocess_image(image)

    # Prediction button
    if st.button("Tahmin Et"):
        if uploaded_file is not None:
            prediction = model.predict(processed_image)
            predicted_class = np.argmax(prediction, axis=1)[0]
            st.write(f"Tahmin Edilen Sınıf: {labels_map[predicted_class]}")
        else:
            st.warning("Lütfen ilk önce görsel yükleyin")
    
    st.write("Bu uygulamada kullanılan model hata yapabilir. Bu nedenle, bu uygulamayı kullanarak kesin bir teşhis koymayın. Kesin bir teşhis için bir doktora başvurun.")



if __name__ == "__main__":
    main()