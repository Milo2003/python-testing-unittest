# Python Testing with Unittest

Este proyecto demuestra cómo realizar pruebas unitarias en Python utilizando los frameworks `unittest` y `pytest`. El objetivo principal es garantizar la fiabilidad de los componentes individuales mediante pruebas aisladas.

## Características

- **Pruebas Unitarias**: Pruebas aisladas utilizando la biblioteca `unittest` de Python.
- **Integración con Pytest**: Las pruebas también pueden ejecutarse con `pytest` para una salida más legible y flexible.
- **Manejo de Errores**: Se valida el manejo de excepciones personalizadas en las pruebas para asegurar la fiabilidad del sistema.

## Estructura del Proyecto

```
python-testing-unittest/
├── src/                    # Archivos fuente con la funcionalidad principal
│   └── bank_account.py     # Ejemplo de archivo con la clase 'BankAccount' a probar
├── tests/                  # Archivos de pruebas unitarias
│   └── test_bank_account.py # Pruebas unitarias para la clase 'BankAccount'
├── requirements.txt        # Dependencias (por ejemplo, pytest)
└── README.md               # Documentación del proyecto
```

## Configuración

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/python-testing-unittest.git
   cd python-testing-unittest
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Instala `pytest` (opcional)**:
   Si deseas ejecutar las pruebas con `pytest`, asegúrate de que esté incluido en `requirements.txt` o instálalo directamente:
   ```bash
   pip install pytest
   ```

## Ejecución de Pruebas

### Usando `unittest`
Para ejecutar las pruebas con `unittest`, navega al directorio raíz y ejecuta el siguiente comando:

```bash
python -m unittest discover -s tests
```

### Usando `pytest`
Alternativamente, puedes ejecutar las pruebas usando `pytest`:

```bash
pytest
```

Esto descubrirá y ejecutará automáticamente las pruebas, proporcionando una salida más detallada y permitiendo opciones adicionales.

## Excepciones Personalizadas

El proyecto incluye manejo de excepciones personalizadas para garantizar que se arrojen y manejen correctamente ciertos errores en diferentes escenarios, como:

- **WithdrawTimeRestrictionError**: Se lanza si se intenta hacer un retiro fuera del horario permitido.
- **WithdrawDayRestrictionError**: Se lanza si se intenta hacer un retiro en un día restringido.
- **InsufficientFundsError**: Se lanza si el saldo de la cuenta es insuficiente para realizar un retiro.

## Ejemplo de Prueba

A continuación se muestra un ejemplo de prueba unitaria que verifica el comportamiento del método `withdraw` de la clase `BankAccount`:

```python
import unittest
from src.bank_account import BankAccount, WithdrawTimeRestrictionError

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(balance=100)

    def test_withdraw_success(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_time_restriction(self):
        with self.assertRaises(WithdrawTimeRestrictionError):
            self.account.withdraw(50, time="23:00")

if __name__ == '__main__':
    unittest.main()
```

¡Todas las contribuciones son bienvenidas!
