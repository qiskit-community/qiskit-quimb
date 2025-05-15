# (C) Copyright IBM 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import Any, Callable

import quimb.tensor
from qiskit.circuit import Instruction, QuantumCircuit

_gate_func: dict[
    str,
    Callable[[Instruction, Sequence[int], dict[str, Any]], quimb.tensor.Gate | None],
] = {}

SUPPORTED_GATES = _gate_func.keys()


def _register_gate_func(name: str):
    def g(f):
        _gate_func[name] = f
        return f

    return g


@_register_gate_func("barrier")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return None


@_register_gate_func("ccx")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("CCX", params=[], qubits=qubits, **kwargs)


@_register_gate_func("ccz")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("CCZ", params=[], qubits=qubits, **kwargs)


@_register_gate_func("cp")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (theta,) = op.params
    return quimb.tensor.Gate("CPHASE", params=[theta], qubits=qubits, **kwargs)


@_register_gate_func("cx")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("CX", params=[], qubits=qubits, **kwargs)


@_register_gate_func("cy")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("CY", params=[], qubits=qubits, **kwargs)


@_register_gate_func("cz")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("CZ", params=[], qubits=qubits, **kwargs)


@_register_gate_func("h")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("H", params=[], qubits=qubits, **kwargs)


@_register_gate_func("id")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("IDEN", params=[], qubits=qubits, **kwargs)


@_register_gate_func("iswap")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("ISWAP", params=[], qubits=qubits, **kwargs)


@_register_gate_func("measure")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    raise ValueError(
        "Encountered a measurement gate, which is not allowed. "
        "Remove the measurements from your circuit and try again."
    )


@_register_gate_func("p")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (theta,) = op.params
    return quimb.tensor.Gate("PHASE", params=[theta], qubits=qubits, **kwargs)


@_register_gate_func("rx")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (theta,) = op.params
    return quimb.tensor.Gate("RX", params=[theta], qubits=qubits, **kwargs)


@_register_gate_func("rxx")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (theta,) = op.params
    return quimb.tensor.Gate("RXX", params=[theta], qubits=qubits, **kwargs)


@_register_gate_func("ry")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (theta,) = op.params
    return quimb.tensor.Gate("RY", params=[theta], qubits=qubits, **kwargs)


@_register_gate_func("ryy")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (theta,) = op.params
    return quimb.tensor.Gate("RYY", params=[theta], qubits=qubits, **kwargs)


@_register_gate_func("rz")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (theta,) = op.params
    return quimb.tensor.Gate("RZ", params=[theta], qubits=qubits, **kwargs)


@_register_gate_func("rzz")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (theta,) = op.params
    return quimb.tensor.Gate("RZZ", params=[theta], qubits=qubits, **kwargs)


@_register_gate_func("s")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("S", params=[], qubits=qubits, **kwargs)


@_register_gate_func("sdg")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("SDG", params=[], qubits=qubits, **kwargs)


@_register_gate_func("sx")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("SX", params=[], qubits=qubits, **kwargs)


@_register_gate_func("sxdg")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("SXDG", params=[], qubits=qubits, **kwargs)


@_register_gate_func("swap")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("SWAP", params=[], qubits=qubits, **kwargs)


@_register_gate_func("t")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("T", params=[], qubits=qubits, **kwargs)


@_register_gate_func("tdg")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("TDG", params=[], qubits=qubits, **kwargs)


@_register_gate_func("u1")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (theta,) = op.params
    return quimb.tensor.Gate("U1", params=[theta], qubits=qubits, **kwargs)


@_register_gate_func("u2")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (phi, lam) = op.params
    return quimb.tensor.Gate("U2", params=[phi, lam], qubits=qubits, **kwargs)


@_register_gate_func("u3")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    (theta, phi, lam) = op.params
    return quimb.tensor.Gate("U3", params=[theta, phi, lam], qubits=qubits, **kwargs)


@_register_gate_func("x")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("X", params=[], qubits=qubits, **kwargs)


@_register_gate_func("xx_minus_yy")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    theta, beta = op.params
    return quimb.tensor.Gate("XXMINUSYY", params=[theta, beta], qubits=qubits, **kwargs)


@_register_gate_func("xx_plus_yy")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    theta, beta = op.params
    return quimb.tensor.Gate("XXPLUSYY", params=[theta, beta], qubits=qubits, **kwargs)


@_register_gate_func("y")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("Y", params=[], qubits=qubits, **kwargs)


@_register_gate_func("z")
def _(op: Instruction, qubits: Sequence[int], kwargs: dict[str, Any]):
    return quimb.tensor.Gate("Z", params=[], qubits=qubits, **kwargs)


def quimb_gate(
    op: Instruction, qubits: Sequence[int], **kwargs
) -> quimb.tensor.Gate | None:
    """Convert a Qiskit gate to a quimb gate, or ``None`` in case of a barrier."""
    try:
        func = _gate_func[op.name]
    except KeyError:
        raise ValueError(f"Unsupported gate: {op.name}.") from None
    else:
        return func(op, qubits, kwargs)


def quimb_gates(circuit: QuantumCircuit) -> list[quimb.tensor.Gate]:
    """Convert a Qiskit circuit to a list of quimb gates."""
    gates = []
    for instruction in circuit.data:
        op = instruction.operation
        qubits = [circuit.find_bit(qubit).index for qubit in instruction.qubits]
        for gate in _gen_quimb_gates(op, qubits):
            gates.append(gate)
    return gates


def _gen_quimb_gates(
    op: Instruction, qubits: Sequence[int], **kwargs
) -> Iterator[quimb.tensor.Gate]:
    """Convert a Qiskit gate to quimb gates."""
    name = op.name
    if name == "barrier":
        pass
    else:
        yield quimb_gate(op, qubits, **kwargs)
