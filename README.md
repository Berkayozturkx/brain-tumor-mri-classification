# MRI Görüntüleri ile Beyin Tümörü Sınıflandırma

Bu proje, beyin MR görüntülerini farklı kategorilerde sınıflandırmak için tasarlanmış bir Streamlit uygulamasıdır: sağlıklı beyin, iyi huylu tümör, kötü huylu tümör ve hipofiz tümörü. Uygulama, kullanıcı tarafından yüklenen görüntülere dayalı tahminler yapmak için önceden eğitilmiş bir Evrişimsel Sinir Ağı (CNN) modeli kullanır.

## Uygulama Özellikleri

- **MRI Görüntüsü Yükle**: Kullanıcılar JPG, JPEG veya PNG formatında bir MRI görüntüsü yükleyebilir.
- **Görüntü Görüntüleme**: Yüklenen görüntü arayüzde görüntülenir.
- **Tahmin**: Bir “Tahmin Et” düğmesi, kullanıcıların yüklenen görüntünün tahminini almalarını sağlar. Herhangi bir resim yüklenmemişse, bir uyarı mesajı görüntülenir.
- **Sonuç Gösterimi**: MRI görüntüsünün tahmin edilen sınıfı arayüzde görüntülenir.

## Proje Yapısı

```
brain-tumor-mri-classification
├── src
│   ├── app.py               # Streamlit uygulamasına ait kodların bulunduğu dosya
│   ├── model
│   │   └── best_model.keras # Eğitilmiş modelin .keras uzantılı hali
│   ├── utils
│       └── preprocess.py    # Görüntü ön işleme için yardımcı fonksiyonlar
└── requirements.txt         # Bağımlılıkların listesi
```

## Kurulum

Bu projeyi çalıştırmak için Python'un makinenizde kurulu olması gerekir. Ortamı ayarlamak için aşağıdaki adımları izleyin:

1. Depoyu klonlayın:
   ```
   git clone <repository-url>
   cd brain-tumor-mri-classification
   ```

2. Sanal bir ortam oluşturun (isteğe bağlı ancak önerilir):
   ```
   python -m venv venv
   source venv/bin/activate  # Windows'ta `venv\Scripts\activate` kullanın
   ```

3. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```

## Kullanım

1. Streamlit uygulamasını çalıştırın:
   ```
   streamlit run src/app.py
   ```

2. Web tarayıcınızı açın ve `http://localhost:8501` adresine gidin.

3. Sağlanan arayüzü kullanarak bir beyin MRI görüntüsü yükleyin.

4. Görüntüyü sınıflandırmak için “Tahmin Et” düğmesine tıklayın. Tahmin edilen sınıf ekranda görüntülenecektir.

## Model

Bu uygulamada kullanılan model, beyin MRI görüntülerinden oluşan bir veri kümesi üzerinde eğitilmiş bir Evrişimsel Sinir Ağıdır (CNN). Eğitilen model `src/model/best_model.keras` dosyasında saklanmaktadır.