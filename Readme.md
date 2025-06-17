# 🧠 Classificação de Frutas Boas e Podres com Redes Neurais Convolucionais

Este repositório contém uma aplicação baseada em Redes Neurais Convolucionais (CNNs) para classificar imagens de frutas como **"boas"** ou **"podres"**. A solução inclui:

- Treinamento do modelo
- Busca de hiperparâmetros
- Interface web simples para testes manuais

---

## 🌱 Visão Geral do Projeto

O objetivo principal deste projeto é oferecer uma ferramenta automatizada para inspeção e classificação de frutas, contribuindo para **redução de desperdícios** na cadeia de suprimentos.

A inteligência artificial é utilizada para analisar **características visuais** das frutas, como:
- Textura  
- Coloração  
- Presença de manchas  

Esses fatores são indicadores de frescor ou deterioração.

---

## 👥 Equipe

- Rafael Pascoali Czerniej  
- Gabriel Yudi  
- Nathan Oliboni  
- André Henrique  

---

## 🧠 Arquitetura da Rede Neural

A CNN foi desenvolvida utilizando a API `Sequential` do **TensorFlow**, com a seguinte estrutura:

### 🔹 Camadas Convolucionais
- **Camada 1**: 16 filtros `3x3`, ativação ReLU  
- **Camada 2**: 32 filtros `3x3`, ativação ReLU  
- **Camada 3**: 16 filtros `3x3`, ativação ReLU  

A função ReLU introduz **não-linearidade**, essencial para o aprendizado de padrões complexos.

### 🔹 Camadas de Pooling
- Após cada convolução, é aplicada uma camada `MaxPooling2D` com janela `2x2`  
- Essa etapa reduz a dimensionalidade, mantendo as características mais relevantes

### 🔹 Camadas Fully Connected (Flatten + Dense)
- `Flatten`: transforma os dados em vetor unidimensional  
- `Dense 1`: 96 neurônios com ativação ReLU  
- `Dense 2`: 1 neurônio com ativação **sigmoide**  
  - Saída entre 0 e 1  
  - Próximo de 0 → fruta **boa**  
  - Próximo de 1 → fruta **podre**

---

## ⚙️ Parâmetros de Treinamento

| Parâmetro           | Valor                                      |
|---------------------|--------------------------------------------|
| Função de Custo     | Binary Crossentropy                        |
| Otimizador          | Adam                                       |
| Métrica             | Acurácia                                   |
| Dimensão da Entrada | 256x256x3 (RGB, normalizada para [0,1])     |
| Saída               | Valor contínuo entre 0 e 1                 |
| Taxa de Aprendizado | 0.001                                      |
| Épocas              | 10                                         |
| Divisão dos Dados   | 70% treino, 20% validação, 10% teste       |

---

## 🔍 Busca de Hiperparâmetros

A otimização foi feita com **Hyperband** (Keras Tuner), usando **early stopping** com `patience=5` para interromper treinos improdutivos.

### 🔧 Melhores Resultados:
- **Neurônios na camada densa**: 96  
- **Taxa de aprendizado**: 0.001  

---

## 📈 Resultados

- **Acurácia treino**: ~95%  
- **Acurácia validação**: ~90%  

Gráficos de perda e acurácia confirmam a capacidade de **aprendizado e generalização** do modelo.

### 🧪 Teste com imagens reais
Total de 150 imagens (75 boas e 75 podres):

| Tipo         | Acertos | Erros |
|--------------|---------|-------|
| Frutas boas  | 71      | 4     |
| Frutas podres| 68      | 7     |

### 📊 Matriz de Confusão
A matriz de confusão mostra **baixa taxa de falsos positivos e falsos negativos**, indicando alta confiabilidade do modelo.

---

## 🚀 Como Rodar o Projeto

### 🔧 Requisitos
Certifique-se de ter o Python instalado e, em seguida, instale as dependências:

```bash
pip install flask flask-cors tensorflow numpy opencv-python
