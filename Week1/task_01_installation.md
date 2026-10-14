# Task 01 — Installation

## Tools to Download and Install

### 1. Anaconda3
- Download from: https://www.anaconda.com/products/distribution
- Choose the version for your OS (Linux/Windows/macOS)
- Anaconda includes Python, Jupyter Notebook, NumPy, Pandas, Matplotlib, and more
- Install using the installer (.sh on Linux, .exe on Windows)

### 2. PyTorch
- After Anaconda is installed, open terminal/Anaconda Prompt
- Install command:
  ```
  pip install torch torchvision torchaudio
  ```
- Or with conda:
  ```
  conda install pytorch torchvision -c pytorch
  ```

### 3. TensorFlow 2.0
- Install using pip:
  ```
  pip install tensorflow
  ```
- Verify installation:
  ```
  python -c "import tensorflow as tf; print(tf.__version__)"
  ```

### 4. VSCode (Visual Studio Code)
- Download from: https://code.visualstudio.com/
- Install the Python extension from the Extensions tab
- Set the Python interpreter to your Anaconda environment

### 5. PyCharm
- Download from: https://www.jetbrains.com/pycharm/
- Community edition is free
- Configure the project interpreter to point to Anaconda Python
