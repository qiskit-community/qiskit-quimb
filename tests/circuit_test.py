# (C) Copyright IBM 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Tests for gates."""

import numpy as np
from qiskit.circuit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import CPhaseGate, PhaseGate, XGate, XXPlusYYGate
from qiskit.quantum_info import Statevector
from qiskit_quimb import quimb_circuit
from qiskit_quimb.testing import assert_allclose_up_to_global_phase


def test_quimb_circuit():
    """Test quimb circuit."""
    rng = np.random.default_rng(3377)
    qubits = QuantumRegister(4)
    circuit = QuantumCircuit(qubits)
    a, b, c, d = qubits

    circuit.append(XGate(), [a])
    circuit.append(XGate(), [b])
    circuit.append(XXPlusYYGate(rng.uniform(-10, 10), rng.uniform(-10, 10)), [b, c])
    circuit.append(XXPlusYYGate(rng.uniform(-10, 10), rng.uniform(-10, 10)), [a, b])
    circuit.append(XXPlusYYGate(rng.uniform(-10, 10), rng.uniform(-10, 10)), [c, d])
    circuit.append(CPhaseGate(rng.uniform(-10, 10)), [b, c])
    circuit.append(CPhaseGate(rng.uniform(-10, 10)), [a, b])
    circuit.append(CPhaseGate(rng.uniform(-10, 10)), [c, d])
    circuit.append(PhaseGate(rng.uniform(-10, 10)), [a])
    circuit.append(PhaseGate(rng.uniform(-10, 10)), [b])
    circuit.append(PhaseGate(rng.uniform(-10, 10)), [c])
    circuit.append(PhaseGate(rng.uniform(-10, 10)), [d])

    quimb_circ = quimb_circuit(circuit)
    qiskit_vec = np.array(Statevector(circuit))
    quimb_vec = quimb_circ.to_dense(reverse=True).reshape(-1)
    assert_allclose_up_to_global_phase(quimb_vec, qiskit_vec)
