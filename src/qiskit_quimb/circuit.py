# (C) Copyright IBM 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import math
from collections.abc import Iterator

import quimb.tensor
from qiskit.circuit import Instruction, QuantumCircuit


def quimb_circuit(
    circuit: QuantumCircuit,
    quimb_circuit_class: type[quimb.tensor.Circuit] = quimb.tensor.Circuit,
    **kwargs,
) -> quimb.tensor.Circuit:
    """Convert a Qiskit circuit to a quimb circuit."""
    return quimb_circuit_class.from_gates(
        quimb_gates(circuit), N=circuit.num_qubits, **kwargs
    )


def quimb_gates(circuit: QuantumCircuit) -> list[quimb.tensor.Gate]:
    """Convert a Qiskit circuit to a list of quimb gates."""
    gates = []
    for instruction in circuit.data:
        op = instruction.operation
        qubits = [circuit.find_bit(qubit)[0] for qubit in instruction.qubits]
        for gate in _gen_quimb_gates(op, qubits):
            gates.append(gate)
    return gates


def _gen_quimb_gates(op: Instruction, qubits: list[int]) -> Iterator[quimb.tensor.Gate]:
    """Convert a Qiskit gate to quimb gates."""
    if op.name == "x":
        yield quimb.tensor.Gate("X", params=[], qubits=qubits)
    elif op.name == "p":
        (theta,) = op.params
        yield quimb.tensor.Gate("RZ", params=[theta], qubits=qubits)
    elif op.name == "cp":
        (theta,) = op.params
        a, b = qubits
        yield quimb.tensor.Gate("RZZ", params=[-0.5 * theta], qubits=[a, b])
        yield quimb.tensor.Gate("RZ", params=[0.5 * theta], qubits=[a])
        yield quimb.tensor.Gate("RZ", params=[0.5 * theta], qubits=[b])
    elif op.name == "xx_plus_yy":
        theta, beta = op.params
        phi = beta + 0.5 * math.pi
        a, b = qubits
        yield quimb.tensor.Gate("RZ", params=[phi], qubits=[a])
        yield quimb.tensor.Gate("GIVENS", params=[0.5 * theta], qubits=[a, b])
        yield quimb.tensor.Gate("RZ", params=[-phi], qubits=[a])
    elif op.name == "barrier":
        return
    elif op.name == "measure":
        raise ValueError(
            "Encountered a measurement gate, which is not allowed. "
            "Remove the measurements from your circuit and try again."
        )
    else:
        raise ValueError(f"Unsupported gate: {op.name}.")
