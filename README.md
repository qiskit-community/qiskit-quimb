# qiskit-quimb

Simulate [Qiskit](https://www.ibm.com/quantum/qiskit) circuits using [quimb](https://quimb.readthedocs.io/en/latest/).

## Example code

```python
import quimb.tensor
from qiskit.circuit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import CPhaseGate, PhaseGate, XGate, XXPlusYYGate
from qiskit_quimb import quimb_circuit

# Build a Qiskit circuit
qubits = QuantumRegister(3)
circuit = QuantumCircuit(qubits)
a, b, c = qubits
circuit.append(XGate(), [a])
circuit.append(XXPlusYYGate(0.5, 0.5), [a, b])
circuit.append(CPhaseGate(0.1), [b, c])
circuit.append(PhaseGate(0.1), [c])
circuit.append(XXPlusYYGate(0.5, 0.5), [a, b])

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
['100', '010', '010', '100', '100', '100', '010', '100', '100', '100']
['100', '100', '100', '100', '100', '100', '010', '100', '010', '100']
```
