import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread

from skimage.transform import (
    radon,
    iradon,
    iradon_sart
)
from skimage.transform import resize


# 1. IMAGEM ORIGINAL

image = imread("ct_teste.png", as_gray=True)

image = resize(
    image,
    (256, 256),
    anti_aliasing=True
)

# 2. GERAR DADOS BRUTOS (SINOGRAMA)

theta = np.linspace(
    0.,
    180.,
    max(image.shape),
    endpoint=False
)

sinogram = radon(
    image,
    theta=theta,
    circle=True
)

# 3. RETROPROJEÇÃO SIMPLES

backprojection = iradon(
    sinogram,
    theta=theta,
    filter_name=None
)

# 4. RETROPROJEÇÃO FILTRADA

filtered_backprojection = iradon(
    sinogram,
    theta=theta,
    filter_name='ramp'
)

# 5. RECONSTRUÇÃO ITERATIVA (SART)

iterative = iradon_sart(
    sinogram,
    theta=theta
)

# 6. EXIBIÇÃO

fig, axes = plt.subplots(
    1,
    5,
    figsize=(18, 4)
)

axes[0].imshow(image, cmap="gray")
axes[0].set_title("Original")

axes[1].imshow(sinogram, cmap="gray", aspect="auto")
axes[1].set_title("Sinograma")

axes[2].imshow(backprojection, cmap="gray")
axes[2].set_title("Retroprojeção Simples")

axes[3].imshow(filtered_backprojection, cmap="gray")
axes[3].set_title("Retroprojeção Filtrada")

axes[4].imshow(iterative, cmap="gray")
axes[4].set_title("Reconstrução Iterativa")

for ax in axes:
    ax.axis("off")

plt.tight_layout()
plt.show()