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
from qiskit.circuit.library import (
    Barrier,
    CCXGate,
    CCZGate,
    CPhaseGate,
    CXGate,
    CYGate,
    CZGate,
    HGate,
    IGate,
    PhaseGate,
    RXGate,
    RXXGate,
    RYGate,
    RYYGate,
    RZGate,
    RZZGate,
    SdgGate,
    SGate,
    SwapGate,
    TdgGate,
    TGate,
    U1Gate,
    U2Gate,
    U3Gate,
    XGate,
    XXPlusYYGate,
    YGate,
    ZGate,
    iSwapGate,
)
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
    circuit.append(RXGate(rng.uniform(-10, 10)), [a])
    circuit.append(RYGate(rng.uniform(-10, 10)), [b])
    circuit.append(RZGate(rng.uniform(-10, 10)), [c])
    circuit.append(RXXGate(rng.uniform(-10, 10)), [a, b])
    circuit.append(RYYGate(rng.uniform(-10, 10)), [b, c])
    circuit.append(RZZGate(rng.uniform(-10, 10)), [c, d])
    circuit.append(YGate(), [b])
    circuit.append(YGate(), [c])
    circuit.append(ZGate(), [b])
    circuit.append(ZGate(), [c])
    circuit.append(HGate(), [b])
    circuit.append(HGate(), [c])
    circuit.append(IGate(), [c])
    circuit.append(SGate(), [a])
    circuit.append(TGate(), [b])
    circuit.append(SdgGate(), [c])
    circuit.append(TdgGate(), [d])
    circuit.append(U1Gate(rng.uniform(-10, 10)), [d])
    circuit.append(U2Gate(rng.uniform(-10, 10), rng.uniform(-10, 10)), [d])
    circuit.append(
        U3Gate(rng.uniform(-10, 10), rng.uniform(-10, 10), rng.uniform(-10, 10)), [d]
    )
    circuit.append(CCXGate(), [a, b, c])
    circuit.append(CCZGate(), [a, b, c])
    circuit.append(CXGate(), [a, b])
    circuit.append(CYGate(), [a, b])
    circuit.append(CZGate(), [a, b])
    circuit.append(SwapGate(), [a, b])
    circuit.append(iSwapGate(), [b, c])
    circuit.append(Barrier(4), [a, b, c, d])
    circuit.append(Barrier(3), [a, b, d])

    quimb_circ = quimb_circuit(circuit)
    qiskit_vec = np.array(Statevector(circuit))
    quimb_vec = quimb_circ.to_dense(reverse=True).reshape(-1)
    assert_allclose_up_to_global_phase(quimb_vec, qiskit_vec)
