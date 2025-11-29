from tensorflow.keras import models, layers

def build_mlp(input_dim):
    """Crea un semplice modello MLP."""
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=(input_dim,)),
        layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model
