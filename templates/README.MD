# 🚗 Simulador de Sensor de Estacionamento

Simulador web de um **sensor de estacionamento** inspirado no funcionamento de um sistema embarcado com ESP32 e sensor ultrassônico.

O projeto utiliza **Flask (Python)** no backend e **HTML + CSS + JavaScript** no frontend para simular:

* 📏 Medição de distância
* 💡 LEDs indicadores (verde, amarelo, vermelho)
* 🔊 Buzzer de alerta
* 💥 Detecção de colisão

---

## 📌 Funcionalidades

* Movimento interativo do carro (arrastar com o mouse)
* Cálculo automático da distância simulada
* Comunicação em tempo real com o servidor Flask
* Ativação de LEDs conforme a distância
* Alerta visual de perigo
* Animação de colisão

---

## 🧠 Regras de Funcionamento

| Distância (cm) | LED Verde | LED Amarelo | LED Vermelho | Buzzer | Status     |
| -------------- | --------- | ----------- | ------------ | ------ | ---------- |
| > 50           | ✅         | ❌           | ❌            | ❌      | Seguro     |
| 21 – 50        | ❌         | ✅           | ❌            | ❌      | Atenção    |
| 11 – 20        | ❌         | ❌           | ✅            | ❌      | Perigo     |
| ≤ 10           | ❌         | ❌           | ✅            | ✅      | Pare       |
| ≤ 2.5          | ❌         | ❌           | ✅            | ✅      | 💥 Colisão |

---

## 🏗️ Estrutura do Projeto

```
projeto/
│
├── app.py
└── templates/
    └── index.html
```

---

## 🐍 Backend (Flask)

Responsável por:

* Receber a distância simulada via requisição POST
* Processar a lógica de decisão
* Retornar o estado dos atuadores em JSON

Rota principal:

```
GET /
```

Rota de atualização:

```
POST /atualizar_sensor
```

---

## 🌐 Frontend

Responsável por:

* Interface visual
* Movimento do carro
* Cálculo da distância
* Comunicação com o backend via `fetch()`
* Atualização dinâmica dos LEDs e alertas

---

## ▶️ Como Executar

### 1️⃣ Instalar dependências

```bash
pip install flask
```

### 2️⃣ Organizar a estrutura

Certifique-se de que o arquivo `index.html` esteja dentro da pasta `templates`.

### 3️⃣ Executar o projeto

```bash
python app.py
```

### 4️⃣ Acessar no navegador

```
http://127.0.0.1:5000/
```

---

## 🎯 Objetivo Educacional

Este projeto é ideal para:

* Aprender integração entre backend e frontend
* Entender comunicação via JSON
* Simular lógica de sistemas embarcados
* Estudar arquitetura cliente-servidor
* Praticar manipulação de DOM e eventos JavaScript

---

## 🚀 Melhorias Futuras

* Adicionar som real ao buzzer
* Tornar interface responsiva
* Implementar gráfico de distância em tempo real
* Adaptar para controle por teclado
* Conectar com hardware real (ESP32)
