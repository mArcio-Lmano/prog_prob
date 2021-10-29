import logging
import pymc4 as pm # Têm que instalar
import numpy as np
import arviz as az

import tensorflow as tf # Têm que instalar
import tensorflow_probability as tfp # Têm que instalar
import matplotlib.pyplot as plt

#%matplotlib inline

# Print das versões
print(pm.__version__)
print(tf.__version__)
print(tfp.__version__)

# Mute Tensorflow warnings ...
logging.getLogger('tensorflow').setLevel(logging.ERROR)

# Defenição de um modelo
@pm.model
def model(x):
    # prior for the mean of a normal distribution
    loc = yield pm.Normal('loc', loc=0, scale=10) # loc = centro
    
    # likelihood of observed data
    obs = yield pm.Normal('obs', loc=loc, scale=1, observed=x)


# Criação de 30 pontos de "data", gerados segundo uma distribuição noraml centrada em 3
x = np.random.randn(30) + 3

# Inferencia
trace = pm.sample(model(x)) # NUTS- No-U-Turn-Sampler

# PLot do gráfico
az.plot_posterior(trace, var_names=["model/loc"])

