# Modelli

Questa cartella è dedicata ai modelli addestrati del progetto.

⚠️ Nota: i file di grandi dimensioni (es. `.h5`, `.pt`, `.onnx`) non vengono caricati su GitHub.  
Usa storage esterni come Google Drive, Kaggle o Hugging Face per salvarli e condividerli.

## Come ottenere i modelli
- Dopo l’addestramento, salva i modelli su Drive o Kaggle.
- Documenta qui il percorso o il link per recuperarli.
- Esempio di caricamento in Colab:
```python
from tensorflow.keras.models import load_model
model = load_model('/content/drive/MyDrive/models/mlp_pima.h5')
