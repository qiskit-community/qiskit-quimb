# qiskit-quimb

Simulate [Qiskit](https://www.ibm.com/quantum/qiskit) circuits using [quimb](https://quimb.readthedocs.io/en/latest/).

## Installation

```bash
pip install qiskit-quimb
```

## Usage

The `qiskit_quimb` module exposes two functions:

- `quimb_circuit`: Converts a Qiskit circuit to a quimb circuit. This is probably the function you want to use.
- `quimb_gates`: Converts a Qiskit circuit to a list of quimb gates, which is a bit more flexible.

## Example code

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
