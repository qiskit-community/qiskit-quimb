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


def quimb_circuit(circuit: QuantumCircuit) -> quimb.tensor.Circuit:
    quimb_circ = quimb.tensor.Circuit(circuit.num_qubits)
    for instruction in circuit.data:
        op = instruction.operation
        qubits = [circuit.find_bit(qubit).index for qubit in instruction.qubits]
        quimb_circ.apply_gates(list(quimb_gates(op, qubits)))
    return quimb_circ


def quimb_gates(op: Instruction, qubits: list[int]) -> Iterator[quimb.tensor.Gate]:
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
    else:
        raise ValueError(f"Unsupported gate: {op.name}.")
