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

import quimb.tensor
from qiskit.circuit import QuantumCircuit

from qiskit_quimb.gate import quimb_gates


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
