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
    """Convert a Qiskit circuit to a quimb circuit.

    The quimb circuit is constructed using the ``from_gates`` method of the quimb
    circuit class (``quimb.tensor.Circuit`` by default), passing along the keyword
    arguments from ``kwargs``.

    Args:
        circuit: The Qiskit circuit.
        quimb_circuit_class: The ``quimb.tensor.Circuit`` subclass to use.

    Returns:
        The quimb circuit.
    """
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


def _gen_quimb_gates(op: Instruction, qubits: list[int], **kwargs) -> Iterator[quimb.tensor.Gate]:
    """Convert a Qiskit gate to quimb gates."""
    match op.name:
        case "barrier":
            pass
        case "ccx":
            yield quimb.tensor.Gate("CCX", params=[], qubits=qubits, **kwargs)
        case "ccz":
            yield quimb.tensor.Gate("CCZ", params=[], qubits=qubits, **kwargs)
        case "cp":
            (theta,) = op.params
            yield quimb.tensor.Gate("CU1", params=[theta], qubits=qubits, **kwargs)
        case "cx":
            yield quimb.tensor.Gate("CX", params=[], qubits=qubits, **kwargs)
        case "cy":
            yield quimb.tensor.Gate("CY", params=[], qubits=qubits, **kwargs)
        case "cz":
            yield quimb.tensor.Gate("CZ", params=[], qubits=qubits, **kwargs)
        case "h":
            yield quimb.tensor.Gate("H", params=[], qubits=qubits, **kwargs)
        case "id":
            yield quimb.tensor.Gate("IDEN", params=[], qubits=qubits, **kwargs)
        case "iswap":
            yield quimb.tensor.Gate("ISWAP", params=[], qubits=qubits, **kwargs)
        case "measure":
            raise ValueError(
                "Encountered a measurement gate, which is not allowed. "
                "Remove the measurements from your circuit and try again."
            )
        case "p":
            (theta,) = op.params
            yield quimb.tensor.Gate("U1", params=[theta], qubits=qubits, **kwargs)
        case "rx":
            (theta,) = op.params
            yield quimb.tensor.Gate("RX", params=[theta], qubits=qubits, **kwargs)
        case "rxx":
            (theta,) = op.params
            yield quimb.tensor.Gate("RXX", params=[theta], qubits=qubits, **kwargs)
        case "ryy":
            (theta,) = op.params
            yield quimb.tensor.Gate("RYY", params=[theta], qubits=qubits, **kwargs)
        case "rzz":
            (theta,) = op.params
            yield quimb.tensor.Gate("RZZ", params=[theta], qubits=qubits, **kwargs)
        case "ry":
            (theta,) = op.params
            yield quimb.tensor.Gate("RY", params=[theta], qubits=qubits, **kwargs)
        case "rz":
            (theta,) = op.params
            yield quimb.tensor.Gate("RZ", params=[theta], qubits=qubits, **kwargs)
        case "s":
            yield quimb.tensor.Gate("S", params=[], qubits=qubits, **kwargs)
        case "sdg":
            yield quimb.tensor.Gate("SDG", params=[], qubits=qubits, **kwargs)
        case "swap":
            yield quimb.tensor.Gate("SWAP", params=[], qubits=qubits, **kwargs)
        case "t":
            yield quimb.tensor.Gate("T", params=[], qubits=qubits, **kwargs)
        case "tdg":
            yield quimb.tensor.Gate("TDG", params=[], qubits=qubits, **kwargs)
        case "u1":
            (theta,) = op.params
            yield quimb.tensor.Gate("U1", params=[theta], qubits=qubits, **kwargs)
        case "u2":
            (phi, lam) = op.params
            yield quimb.tensor.Gate("U2", params=[phi, lam], qubits=qubits, **kwargs)
        case "u3":
            (theta, phi, lam) = op.params
            yield quimb.tensor.Gate("U3", params=[theta, phi, lam], qubits=qubits, **kwargs)
        case "x":
            yield quimb.tensor.Gate("X", params=[], qubits=qubits, **kwargs)
        case "xx_plus_yy":
            theta, beta = op.params
            phi = beta + 0.5 * math.pi
            a, b = qubits
            yield quimb.tensor.Gate("RZ", params=[phi], qubits=[a], **kwargs)
            yield quimb.tensor.Gate("GIVENS", params=[0.5 * theta], qubits=[a, b], **kwargs)
            yield quimb.tensor.Gate("RZ", params=[-phi], qubits=[a], **kwargs)
        case "y":
            yield quimb.tensor.Gate("Y", params=[], qubits=qubits, **kwargs)
        case "z":
            yield quimb.tensor.Gate("Z", params=[], qubits=qubits, **kwargs)
        case _:
            raise ValueError(f"Unsupported gate: {op.name}.")
