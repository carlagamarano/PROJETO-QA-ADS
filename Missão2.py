import pytest

# Funções que serão testadas
def soma(a, b):
  return a + b

def subtracao(a, b):
  return a - b

def multiplicacao(a, b):
  return a * b

def divisao(a, b):
  if b == 0:
    raise ValueError("Não pode dividir por zero!")
  return a / b


# Testes
def test_soma():
  assert soma(3, 2) == 5
  assert soma(-1, 1) == 0

def test_subtracao():
  assert subtracao(5, 3) == 2
  assert subtracao(10, 10) == 0

def test_multiplicacao():
  assert multiplicacao(3, 3) == 9
  assert multiplicacao(4, -2) == -8

def test_divisao():
  assert divisao(10, 2) == 5
  with pytest.raises(ValueError):
    divisao(10, 0)

