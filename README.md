# README - Sistema de Atletas

## 📝 Descrição
Este projeto implementa um sistema de classes para modelar diferentes tipos de atletas, com foco especial em um triatleta que combina habilidades de corredor, nadador e ciclista.

## 🚀 Funcionalidades Principais

### 🏗️ Classes Implementadas:

#### `Atleta` (Classe Base)
- `aposentar()`: marca o atleta como aposentado
- `aquecer()`: prepara o atleta para atividades

#### 🏃 `Corredor`, 🏊 `Nadador`, 🚴 `Ciclista` (Classes Especializadas)
- Cada uma adiciona métodos específicos:
  - `correr()`, `nadar()`, `pedalar()`
- Verificam estado do atleta antes de executar ações

#### 🏅 `TriAtleta` (Herança Múltipla)
- Implementa polimorfismo para evitar conflitos entre atividades
- Verifica se o atleta já está em outra atividade antes de executar
- Combina habilidades das três especializações

## 💻 Como Usar

1. Instancie um objeto:
```python
triatleta = TriAtleta(peso)  # Ex: TriAtleta(78)

Métodos disponíveis:

triatleta.aquecer()   # Prepara o atleta
triatleta.correr()    # Inicia corrida
triatleta.nadar()     # Inicia nado
triatleta.pedalar()   # Inicia pedalada
triatleta.aposentar() # Aposenta o atleta

⚠️ Observações Importantes
❌ Sistema previne ações inválidas (ex: nadar sem aquecer)

🔄 Triatleta não pode executar múltiplas atividades simultaneamente

🏷️ Estado do atleta é controlado automaticamente

🧠 Demonstração de polimorfismo e herança múltipla em Python

▶️ Execução
Execute o arquivo main.py para testar as funcionalidades:

bash
python main.py
