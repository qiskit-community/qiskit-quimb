# qiskit-quimb

<!-- start introduction -->

Simulate [Qiskit](https://www.ibm.com/quantum/qiskit) circuits using [quimb](https://quimb.readthedocs.io/en/latest/).

<!-- end introduction -->

## Documentation

Documentation is located at the [project website](https://qiskit-community.github.io/qiskit-quimb/).

## Installation

<!-- start installation -->

```bash
pip install qiskit-quimb
```

<!-- end installation -->

## Usage

The `qiskit_quimb` module exposes three functions:

- `quimb_circuit`: Converts a Qiskit circuit to a quimb circuit.
- `quimb_gates`: Converts a Qiskit circuit to a list of quimb gates, which is a bit more flexible.
- `quimb_gate`: Converts a Qiskit gate to a quimb gate.

For details, refer to the [API documentation](https://qiskit-community.github.io/qiskit-quimb/api/qiskit_quimb.html).

## Code example

<!-- start code-example -->

```python
import quimb.tensor
from qiskit.circuit import QuantumCircuit, QuantumRegister
from qiskit_quimb import quimb_circuit

# Build a Qiskit circuit
qubits = QuantumRegister(2)
circuit = QuantumCircuit(qubits)
a, b = qubits
circuit.h(a)
circuit.cx(a, b)

# Convert it to a quimb circuit
quimb_circ = quimb_circuit(circuit)

# Sample 10 bitstrings
samples = list(quimb_circ.sample(10, seed=1234))
print(samples)

# You can specify the quimb Circuit subclass and keyword arguments for the constructor
quimb_circ = quimb_circuit(
    circuit, quimb_circuit_class=quimb.tensor.CircuitMPS, max_bond=20
)
samples = list(quimb_circ.sample(10, seed=1234))
print(samples)
```

```text
['00', '00', '11', '00', '11', '00', '11', '00', '11', '11']
['11', '11', '00', '00', '11', '00', '11', '11', '11', '00']
```

<!-- end code-example -->
