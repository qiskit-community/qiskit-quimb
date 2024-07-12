# (C) Copyright IBM 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import cmath

import numpy as np


def match_global_phase(a: np.ndarray, b: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Phase the given arrays so that their phases match at one entry.

    Args:
        a: A Numpy array.
        b: Another Numpy array.

    Returns:
        A pair of arrays (a', b') that are equal if and only if a == b * exp(i phi)
        for some real number phi.
    """
    if a.shape != b.shape:
        return a, b
    # use the largest entry of one of the matrices to maximize precision
    index = max(np.ndindex(*a.shape), key=lambda i: abs(b[i]))
    phase_a = cmath.phase(a[index])
    phase_b = cmath.phase(b[index])
    return a * cmath.rect(1, -phase_a), b * cmath.rect(1, -phase_b)


def assert_allclose_up_to_global_phase(
    actual: np.ndarray,
    desired: np.ndarray,
    rtol: float = 1e-7,
    atol: float = 0,
    equal_nan: bool = True,
    err_msg: str = "",
    verbose: bool = True,
):
    """Check if a == b * exp(i phi) for some real number phi.

    Args:
        actual: A Numpy array.
        desired: Another Numpy array.
        rtol: Relative tolerance.
        atol: Absolute tolerance.
        equal_nan: If True, NaNs will compare equal.
        err_msg: The error message to be printed in case of failure.
        verbose: If True, the conflicting values are appended to the error message.

    Raises:
        AssertionError: If a and b are not equal up to global phase, up to the
            specified precision.
    """
    actual, desired = match_global_phase(actual, desired)
    np.testing.assert_allclose(
        actual,
        desired,
        rtol=rtol,
        atol=atol,
        equal_nan=equal_nan,
        err_msg=err_msg,
        verbose=verbose,
    )
