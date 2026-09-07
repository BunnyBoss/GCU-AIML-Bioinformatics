# Unit 3: Deep Learning for Biological Data

**Course Code:** `02BMSBI24365` — AI & ML in Bioinformatics  
**Target Audience:** M.Sc. Bioinformatics (Semester III)  

---

## Unit Overview

When biological data scales to millions of sequences, entire whole-slide histopathology images, or complex 3D protein structures, classical machine learning models struggle due to manual feature engineering constraints.

Unit 3 introduces **Deep Learning (DL)** architectures that learn hierarchical feature representations directly from raw biological inputs. You will master Multilayer Perceptrons (ANNs), 2D Convolutional Neural Networks (CNNs) for medical imaging, 1D-CNNs and LSTMs for genomic sequence analysis, and explore the revolutionary impact of **Transformers, Protein Large Language Models (pLLMs), and AlphaFold**.

---

## Core Topics & Syllabus Breakdown

### 3.1 Artificial Neural Networks (ANNs) & Backpropagation
* **The Biological vs. Artificial Neuron:** Dendrites, soma, axon vs. inputs $\mathbf{x}$, weights $\mathbf{w}$, bias $b$, and activation function $f(z)$.
* **Activation Functions:** Sigmoid, Tanh, Rectified Linear Unit (ReLU), Leaky ReLU, and Softmax for multi-class probabilities.
* **Forward Propagation & Loss Functions:** Binary Cross-Entropy for disease presence; Categorical Cross-Entropy for multi-class classification; Mean Squared Error for continuous biophysical predictions.
* **Backpropagation & Optimization:** The Chain Rule of calculus for computing error gradients; Gradient Descent, Stochastic Gradient Descent (SGD), and Adam optimizer.
* **Regularization in Deep Networks:** Dropout, Batch Normalization, and Early Stopping to prevent memorization of small clinical cohorts.

### 3.2 Deep Learning Frameworks (TensorFlow & Keras)
* **Framework Architecture:** Tensors, computation graphs, and GPU acceleration.
* **Building Sequential & Functional Models:** Stacking layers, defining input shapes, compiling models with optimizers and losses, and monitoring validation loss curves.

### 3.3 Convolutional Neural Networks (CNNs) & Sequence Models (RNN/LSTM)
* **2D-CNNs for Biomedical Image Analysis:**
  * Convolutional filters/kernels for edge, texture, and cellular feature extraction.
  * Receptive fields, padding, stride, and MaxPooling.
  * Applications: Automated detection of malignant cells in Whole Slide Images (WSI) and histopathology slides.
* **1D-CNNs for Genomic Motifs:**
  * Applying 1D spatial filters over one-hot encoded DNA sequences to discover transcription factor binding motifs.
* **Recurrent Neural Networks (RNNs) & Long Short-Term Memory (LSTM):**
  * Sequential dependencies in biological polymers (DNA, RNA, proteins).
  * The vanishing gradient problem in vanilla RNNs.
  * LSTM gates: Forget gate, Input gate, and Output gate for capturing long-range genomic dependencies.

### 3.4 Transformers, Generative AI & Agentic AI in Biology
* **The Attention Mechanism:** Why recurrent models struggle over long biological sequences; Self-Attention formulation ($Q, K, V$).
* **Transformers in Genomics & Proteomics:** Multi-Head Attention; Positional encoding of amino acid sequences.
* **Protein Language Models (pLLMs):** ESM (Evolutionary Scale Modeling), ProtBERT, and zero-shot variant effect prediction.
* **AlphaFold & Structural Biology:** How deep attention architectures revolutionized 3D protein structure prediction from 1D sequence alone.
* **Generative & Agentic AI in Drug Discovery:** Molecular generative models (diffusion models, VAEs) and autonomous AI agents for automated bioinformatic workflow orchestration.

---

## Associated Laboratory Practicals

* **[Lab 06](../../labs/lab_06_ann_keras_workflow/):** Multi-layer Perceptron (ANN) with TensorFlow/Keras for Patient Biomarker Panel Classification.
* **[Lab 07](../../labs/lab_07_histopathology_cnn/):** Automated Histopathology Biopsy Classification using 2D Convolutional Neural Networks.
* **[Lab 08](../../labs/lab_08_sequence_classification_1dcnn_lstm/):** Genomic Sequence Motif Detection using 1D-CNN and Bidirectional LSTM Architectures.

---

## Computational Setup & Hardware Recommendations

* Deep learning experiments in this unit require `tensorflow` ($\ge 2.12$) or `pytorch`.
* While small models can run on modern CPUs, training CNNs on image patches or LSTMs on long sequences benefits significantly from GPU acceleration (NVIDIA CUDA or Apple Silicon Metal Performance Shaders via `tensorflow-metal`).
* Cloud alternative: Google Colab (Free T4 GPU runtime) is fully supported for all unit notebooks.
