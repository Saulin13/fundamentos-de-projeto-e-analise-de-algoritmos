# KaratsubaMultiplication

**Disciplina:** Fundamentos de Projeto e Análise de Algoritmos  
**Objetivo:** Implementar o algoritmo de Karatsuba para multiplicação eficiente de inteiros, com documentação, execução local e relatório técnico (complexidade assintótica e ciclomática).

---

## O que é o algoritmo de Karatsuba

O algoritmo de **Karatsuba** (1960) reduz o número de multiplicações recursivas ao calcular o produto de dois inteiros grandes.  
Em vez de 4 multiplicações do método tradicional (dividir-alto/baixo), ele faz **apenas 3** e usa somas/subtrações para recompor o resultado.

Para `x` e `y`:

- Escrevemos `x = a·B + b` e `y = c·B + d`, com `B = 10^m` (m ≈ metade dos dígitos).
- Calculamos:
  - `z2 = a*c`
  - `z0 = b*d`
  - `z1 = (a+b)*(c+d) - z2 - z0`
- Resultado: `x*y = z2·B² + z1·B + z0`.

**Vantagem:** Complexidade temporal **O(n^log₂3) ≈ O(n^1,585)**, melhor que o método quadrático **O(n²)** (n = nº de dígitos).

---

## Estrutura do repositório

```
karatsuba/
├─ README.md
└─ main.py
```

- `main.py`: implementação do Karatsuba + CLI para rodar no terminal.

---

## Requisitos

- Python **3.10+** (recomendado **3.13**).
- (Opcional) Ambiente virtual `venv`.

---

##  Como rodar localmente

### 1) Criar e ativar um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv .venv
```

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

> Para sair depois: `deactivate`

### 2) Executar a aplicação (CLI)

No diretório do projeto, rode:

```bash
python main.py
```

Você verá um prompt pedindo dois inteiros. Exemplo:

```
Karatsuba CLI
Informe dois inteiros (p.ex.: 1234 e 5678).
x = 1234
y = 5678

Resultado: 7006652
Confere com x*y nativo? SIM
```

---

## Explicação da implementação (resumo)

Trechos de `main.py` (descrição por blocos):

- **Normalização de sinal**: calcula o sinal final e trabalha com valores absolutos durante a recursão.
- **Caso base**: se um operando tem 1 dígito, multiplica diretamente (encerra a recursão).
- **Divisão**: calcula `n` (nº de dígitos), escolhe `m = n//2`, define `base = 10**m` e separa `x = a·base + b` e `y = c·base + d` via `divmod`.
- **3 multiplicações recursivas**: `z2 = a*c`, `z0 = b*d`, `z1 = (a+b)*(c+d) - z2 - z0`.
- **Recomposição**: `z2·base² + z1·base + z0` e aplica o sinal calculado no início.
- **CLI**: lê `x` e `y`, imprime o produto e confere com `x*y` do Python.

---

## Complexidade assintótica

- **Tempo:** A recorrência é `T(n) = 3T(n/2) + O(n)`. Pela Master Theorem,  
  `T(n) = O(n^log₂3) ≈ O(n^1,585)`.
- **Espaço:** `O(n)` no total, considerando profundidade de recursão e temporários.

---

## Complexidade ciclomática (McCabe)

A função `karatsuba` possui essencialmente **1 decisão** (o caso base).  
Assim, a complexidade ciclomática é **M = decisões + 1 = 2**.  
Isso implica em dois caminhos principais para testes: (i) caso base; (ii) caminho recursivo.

---
