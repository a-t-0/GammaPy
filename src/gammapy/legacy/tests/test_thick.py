# Copyright 2020 Kilian Swannet, San Kilkis

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.

from math import pi

import numpy as np
import pytest
from pytest import approx

from gammapy.legacy.panel.thick import Solver, ThickPanelledAirfoil
from gammapy.geometry.airfoil import NACA4Airfoil
from tests.test_gammapy.helpers import ScenarioTestSuite


@pytest.fixture(scope="module")
def solver_obj():
    testfoil = ThickPanelledAirfoil(Naca="2412", n_panels=10)
    return Solver(testfoil.panels)


def test_A(solver_obj):
    calc = solver_obj.coefficients.A
    ref = -0.30074680202253584
    assert calc == approx(ref, rel=5e-5)


def test_B(solver_obj):
    calc = solver_obj.coefficients.B
    ref = 0.0904534136839456
    assert calc == approx(ref, rel=5e-5)


def test_C(solver_obj):
    calc = solver_obj.coefficients.C
    ref = -0.045227355204173834
    assert calc == approx(ref, rel=5e-5)


def test_D(solver_obj):
    calc = solver_obj.coefficients.D
    ref = 0.9989767196192489
    assert calc == approx(ref, rel=5e-5)


def test_E(solver_obj):
    calc = solver_obj.coefficients.E
    ref = 0.0021851217730942327
    assert calc == approx(ref, rel=5e-5)


def test_F(solver_obj):
    calc = solver_obj.coefficients.F
    ref = -3.6571407713042885
    assert calc == approx(ref, abs=5e-10)


def test_G(solver_obj):
    calc = solver_obj.coefficients.G
    ref = 0.03797726355934574
    assert calc == approx(ref, rel=5e-5)


def test_P(solver_obj):
    calc = solver_obj.coefficients.P
    ref = -0.015784868222446846
    assert calc == approx(ref, rel=5e-5)


def test_Q(solver_obj):
    calc = solver_obj.coefficients.Q
    ref = 0.30034022644185643
    assert calc == approx(ref, rel=5e-5)


def test_CN2(solver_obj):
    calc = solver_obj.coefficients.CN2
    ref = np.array(
        [
            [
                1.0,
                0.64921316,
                0.312088,
                0.16123912,
                0.05750833,
                0.05951267,
                0.18062465,
                0.38398089,
                1.05403062,
                -0.95201426,
            ],
            [
                -0.31212764,
                1.0,
                0.4945185,
                0.20897557,
                0.07086648,
                0.07357419,
                0.23729117,
                0.62807018,
                -0.71384956,
                -0.25548126,
            ],
            [
                -0.11071862,
                -0.56092105,
                1.0,
                0.40397767,
                0.11306947,
                0.11783988,
                0.43909266,
                -0.44858497,
                -0.38910077,
                -0.1029192,
            ],
            [
                -0.06752643,
                -0.24670092,
                -0.75116454,
                1.0,
                0.2791135,
                0.26966921,
                -0.20439362,
                -0.43849258,
                -0.20918952,
                -0.06455892,
            ],
            [
                -0.05061793,
                -0.17200097,
                -0.3770985,
                -1.10429254,
                1.0,
                0.26457871,
                -0.39990935,
                -0.26827688,
                -0.14905052,
                -0.04864378,
            ],
            [
                0.04566104,
                0.15048523,
                0.2972592,
                0.40552359,
                -0.79235766,
                1.0,
                0.61329673,
                0.28260727,
                0.14153538,
                0.04450794,
            ],
            [
                0.06566464,
                0.23292659,
                0.5356618,
                -0.33046439,
                -0.24890645,
                -0.33908425,
                1.0,
                0.4942742,
                0.20840228,
                0.06324438,
            ],
            [
                0.10896382,
                0.48935202,
                -0.25604628,
                -0.34522416,
                -0.10846826,
                -0.12043828,
                -0.56050784,
                1.0,
                0.40539968,
                0.10235303,
            ],
            [
                0.30124624,
                -0.27853112,
                -0.44124589,
                -0.19864065,
                -0.06899592,
                -0.07345868,
                -0.24570887,
                -0.74787363,
                1.0,
                0.25744373,
            ],
            [
                -0.31457691,
                -0.60262364,
                -0.29833553,
                -0.15560083,
                -0.05616256,
                -0.05910228,
                -0.18288653,
                -0.39702061,
                -1.1785747,
                1.0,
            ],
        ]
    )
    assert calc == approx(ref, rel=5e-5)


def test_CN1(solver_obj):
    calc = solver_obj.coefficients.CN1
    ref = np.array(
        [
            [
                -1.0,
                1.17573979,
                0.39466146,
                0.18068889,
                0.05968603,
                0.05770735,
                0.16187372,
                0.30529942,
                0.60985016,
                0.31826418,
            ],
            [
                -0.25820603,
                -1.0,
                0.74380362,
                0.24290143,
                0.07422604,
                0.07091835,
                0.20664984,
                0.451052,
                0.28575087,
                -0.30250645,
            ],
            [
                -0.10310336,
                -0.4071189,
                -1.0,
                0.55501213,
                0.12202563,
                0.111848,
                0.36042818,
                0.26647787,
                -0.49586545,
                -0.11007388,
            ],
            [
                -0.064609,
                -0.21171931,
                -0.49759995,
                -1.0,
                0.34279076,
                0.25469916,
                0.33722968,
                -0.55411285,
                -0.24011875,
                -0.06730658,
            ],
            [
                -0.04880709,
                -0.15279023,
                -0.29604105,
                -0.61673367,
                -1.0,
                0.79733565,
                -0.44572222,
                -0.32214977,
                -0.16470814,
                -0.05019485,
            ],
            [
                0.04418552,
                0.13561076,
                0.24548089,
                0.36646755,
                -0.27326007,
                -1.0,
                1.11313735,
                0.36333738,
                0.16037461,
                0.04627181,
            ],
            [
                0.06298858,
                0.20294518,
                0.42147547,
                0.19413339,
                -0.26534731,
                -0.27686458,
                -1.0,
                0.74541837,
                0.24293604,
                0.06611582,
            ],
            [
                0.10188392,
                0.38304241,
                0.44829642,
                -0.42300955,
                -0.11453002,
                -0.11162349,
                -0.40655653,
                -1.0,
                0.55778341,
                0.10987888,
            ],
            [
                0.25414746,
                0.71481955,
                -0.61632441,
                -0.22851892,
                -0.07172186,
                -0.07014711,
                -0.21082825,
                -0.49607887,
                -1.0,
                0.31100338,
            ],
            [
                0.95291173,
                -1.04319376,
                -0.37565468,
                -0.17386319,
                -0.05802286,
                -0.05694947,
                -0.16278176,
                -0.31329371,
                -0.64984215,
                -1.0,
            ],
        ]
    )
    assert calc == approx(ref, rel=5e-5)


def test_CT2(solver_obj):
    calc = solver_obj.coefficients.CT2
    ref = np.array(
        [
            [
                1.57079633e00,
                2.98904500e-03,
                3.83986703e-03,
                4.65851732e-03,
                3.70811255e-03,
                7.17522903e-03,
                3.37513319e-02,
                9.76941500e-02,
                4.37521286e-01,
                1.13522801e00,
            ],
            [
                3.50637404e-04,
                1.57079633e00,
                4.78453284e-03,
                6.11899675e-03,
                5.08726159e-03,
                1.04820418e-02,
                5.80511521e-02,
                3.07819262e-01,
                1.08051716e00,
                1.45734577e-02,
            ],
            [
                1.27701415e-03,
                2.63814831e-03,
                1.57079633e00,
                1.16143666e-02,
                1.03283830e-02,
                2.49390057e-02,
                2.39290199e-01,
                9.76214510e-01,
                6.71963169e-02,
                3.30754979e-03,
            ],
            [
                3.86943190e-03,
                1.18981245e-02,
                1.53865224e-02,
                1.57079633e00,
                3.33295394e-02,
                1.27957316e-01,
                8.86093371e-01,
                1.62383865e-01,
                2.78061790e-02,
                4.56089622e-03,
            ],
            [
                2.00920586e-02,
                6.50352064e-02,
                1.23553047e-01,
                1.69714237e-01,
                1.57079633e00,
                8.19006729e-01,
                4.33557131e-01,
                1.59972307e-01,
                6.83598489e-02,
                1.99794944e-02,
            ],
            [
                2.92321973e-02,
                1.03256172e-01,
                2.49208814e-01,
                7.94652164e-01,
                6.16153294e-01,
                1.57079633e00,
                1.91315662e-01,
                1.37401096e-01,
                8.21083923e-02,
                2.76454300e-02,
            ],
            [
                1.31581145e-02,
                6.35885297e-02,
                3.47945340e-01,
                8.49710599e-01,
                8.30658530e-02,
                2.69561149e-02,
                1.57079633e00,
                4.73202672e-02,
                3.23770248e-02,
                1.13939923e-02,
            ],
            [
                1.04975143e-02,
                1.61529536e-01,
                1.01300764e00,
                1.52759949e-01,
                2.70499803e-02,
                1.70994461e-02,
                2.59505570e-02,
                1.57079633e00,
                1.55555589e-02,
                6.14618225e-03,
            ],
            [
                3.90225562e-02,
                1.22202675e00,
                1.80878864e-01,
                5.73871575e-02,
                1.54316955e-02,
                1.13385362e-02,
                2.08317312e-02,
                2.03182748e-02,
                1.57079633e00,
                3.67730428e-03,
            ],
            [
                1.40670753e00,
                2.15809821e-01,
                8.77975122e-02,
                4.13454932e-02,
                1.26395904e-02,
                9.91690306e-03,
                1.94333084e-02,
                2.24517409e-02,
                2.39167311e-02,
                1.57079633e00,
            ],
        ]
    )
    assert calc == approx(ref, rel=5e-5)


def test_CT1(solver_obj):
    calc = solver_obj.coefficients.CT1
    ref = np.array(
        [
            [
                1.57079633e00,
                3.42384684e-03,
                3.65557421e-03,
                4.00759733e-03,
                2.98013255e-03,
                5.72194526e-03,
                2.64625818e-02,
                7.05855803e-02,
                1.99593147e-01,
                1.40537373e00,
            ],
            [
                5.31588963e-04,
                1.57079633e00,
                4.27593457e-03,
                5.18668854e-03,
                4.03138433e-03,
                8.14597834e-03,
                4.23633536e-02,
                1.65737211e-01,
                1.22143557e00,
                3.70715688e-02,
            ],
            [
                1.27523749e-03,
                3.32898215e-03,
                1.57079633e00,
                9.16549617e-03,
                7.97294996e-03,
                1.80908938e-02,
                1.36845288e-01,
                1.01609886e00,
                1.53784229e-01,
                5.78041440e-03,
            ],
            [
                3.77814986e-03,
                1.11068363e-02,
                1.71381759e-02,
                1.57079633e00,
                2.23615895e-02,
                7.72057300e-02,
                8.64401572e-01,
                3.28260529e-01,
                4.28172318e-02,
                5.53234816e-03,
            ],
            [
                1.94899733e-02,
                5.90911686e-02,
                1.03749473e-01,
                1.53193113e-01,
                1.57079633e00,
                6.31239562e-01,
                7.93379980e-01,
                2.21508897e-01,
                8.09418528e-02,
                2.10923617e-02,
            ],
            [
                2.80481015e-02,
                9.01316995e-02,
                1.87800468e-01,
                4.47754390e-01,
                8.10972914e-01,
                1.57079633e00,
                2.13582707e-01,
                1.58714309e-01,
                8.89059025e-02,
                2.83395634e-02,
            ],
            [
                1.21363972e-02,
                4.83132087e-02,
                1.86374667e-01,
                8.74301587e-01,
                1.32227916e-01,
                4.04474067e-02,
                1.57079633e00,
                4.23137106e-02,
                3.38378705e-02,
                1.15555808e-02,
            ],
            [
                8.13911613e-03,
                7.80921558e-02,
                9.64947195e-01,
                2.49741059e-01,
                3.35621831e-02,
                1.97200422e-02,
                3.27923519e-02,
                1.57079633e00,
                1.22977844e-02,
                6.06371593e-03,
            ],
            [
                1.76236224e-02,
                1.07296895e00,
                3.20187999e-01,
                7.15810347e-02,
                1.75970227e-02,
                1.25659471e-02,
                2.28541437e-02,
                2.26791858e-02,
                1.57079633e00,
                2.42311788e-03,
            ],
            [
                1.13124008e00,
                4.55010741e-01,
                1.14730774e-01,
                4.78295978e-02,
                1.39763092e-02,
                1.07702060e-02,
                2.07039132e-02,
                2.23626485e-02,
                2.08462691e-02,
                1.57079633e00,
            ],
        ]
    )
    assert calc == approx(ref, rel=5e-5)


def test_At(solver_obj):
    calc = solver_obj.coefficients.AT
    ref = np.array(
        [
            [
                1.57079633e00,
                1.57422017e00,
                6.64461921e-03,
                7.84746437e-03,
                7.63864987e-03,
                9.43005781e-03,
                3.36378108e-02,
                1.04336912e-01,
                2.97287297e-01,
                1.84289502e00,
                1.13522801e00,
            ],
            [
                5.31588963e-04,
                1.57114696e00,
                1.57507226e00,
                9.97122137e-03,
                1.01503811e-02,
                1.32332399e-02,
                5.28453954e-02,
                2.23788363e-01,
                1.52925483e00,
                1.11758873e00,
                1.45734577e-02,
            ],
            [
                1.27523749e-03,
                4.60599630e-03,
                1.57343448e00,
                1.57996182e00,
                1.95873166e-02,
                2.84192768e-02,
                1.61784294e-01,
                1.25538906e00,
                1.12999874e00,
                7.29767313e-02,
                3.30754979e-03,
            ],
            [
                3.77814986e-03,
                1.49762682e-02,
                2.90363004e-02,
                1.58618285e00,
                1.59315792e00,
                1.10535269e-01,
                9.92358888e-01,
                1.21435390e00,
                2.05201096e-01,
                3.33385272e-02,
                4.56089622e-03,
            ],
            [
                1.94899733e-02,
                7.91832272e-02,
                1.68784680e-01,
                2.76746159e-01,
                1.74051056e00,
                2.20203589e00,
                1.61238671e00,
                6.55066028e-01,
                2.40914160e-01,
                8.94522107e-02,
                1.99794944e-02,
            ],
            [
                2.80481015e-02,
                1.19363897e-01,
                2.91056640e-01,
                6.96963204e-01,
                1.60562508e00,
                2.18694962e00,
                1.78437903e00,
                3.50029970e-01,
                2.26306999e-01,
                1.10447956e-01,
                2.76454300e-02,
            ],
            [
                1.21363972e-02,
                6.14713232e-02,
                2.49963197e-01,
                1.22224693e00,
                9.81938515e-01,
                1.23513260e-01,
                1.59775244e00,
                1.61311004e00,
                8.11581377e-02,
                4.39326056e-02,
                1.13939923e-02,
            ],
            [
                8.13911613e-03,
                8.85896701e-02,
                1.12647673e00,
                1.26274870e00,
                1.86322132e-01,
                4.67700225e-02,
                4.98917981e-02,
                1.59674688e00,
                1.58309411e00,
                2.16192748e-02,
                6.14618225e-03,
            ],
            [
                1.76236224e-02,
                1.11199151e00,
                1.54221475e00,
                2.52459899e-01,
                7.49841802e-02,
                2.79976426e-02,
                3.41926799e-02,
                4.35109170e-02,
                1.59111460e00,
                1.57321944e00,
                3.67730428e-03,
            ],
            [
                1.13124008e00,
                1.86171828e00,
                3.30540595e-01,
                1.35627110e-01,
                5.53218025e-02,
                2.34097965e-02,
                3.06208163e-02,
                4.17959569e-02,
                4.32980100e-02,
                1.59471306e00,
                1.57079633e00,
            ],
            [
                0.00000000e00,
                0.00000000e00,
                0.00000000e00,
                0.00000000e00,
                0.00000000e00,
                0.00000000e00,
                0.00000000e00,
                0.00000000e00,
                0.00000000e00,
                0.00000000e00,
                0.00000000e00,
            ],
        ]
    )
    assert calc == approx(ref, rel=5e-5)


def test_AN(solver_obj):
    """..."""
    calc = solver_obj.coefficients.AN

    ref = np.array(
        [
            [
                -1.0,
                2.17573979,
                1.04387462,
                0.49277689,
                0.22092515,
                0.11521568,
                0.22138639,
                0.48592407,
                0.99383105,
                1.3722948,
                -0.95201426,
            ],
            [
                -0.25820603,
                -1.31212764,
                1.74380362,
                0.73741993,
                0.2832016,
                0.14178483,
                0.28022404,
                0.68834317,
                0.91382105,
                -1.01635601,
                -0.25548126,
            ],
            [
                -0.10310336,
                -0.51783752,
                -1.56092105,
                1.55501213,
                0.5260033,
                0.22491747,
                0.47826807,
                0.70557053,
                -0.94445042,
                -0.49917466,
                -0.1029192,
            ],
            [
                -0.064609,
                -0.27924573,
                -0.74430087,
                -1.75116454,
                1.34279076,
                0.53381266,
                0.60689889,
                -0.75850647,
                -0.67861133,
                -0.2764961,
                -0.06455892,
            ],
            [
                -0.04880709,
                -0.20340816,
                -0.46804202,
                -0.99383217,
                -2.10429254,
                1.79733565,
                -0.18114351,
                -0.72205913,
                -0.43298501,
                -0.19924536,
                -0.04864378,
            ],
            [
                0.04418552,
                0.1812718,
                0.39596611,
                0.66372675,
                0.13226352,
                -1.79235766,
                2.11313735,
                0.97663412,
                0.44298189,
                0.1878072,
                0.04450794,
            ],
            [
                0.06298858,
                0.26860981,
                0.65440206,
                0.72979519,
                -0.5958117,
                -0.52577104,
                -1.33908425,
                1.74541837,
                0.73721025,
                0.2745181,
                0.06324438,
            ],
            [
                0.10188392,
                0.49200623,
                0.93764844,
                -0.67905583,
                -0.45975418,
                -0.22009174,
                -0.5269948,
                -1.56050784,
                1.55778341,
                0.51527856,
                0.10235303,
            ],
            [
                0.25414746,
                1.01606579,
                -0.89485553,
                -0.66976481,
                -0.27036252,
                -0.13914304,
                -0.28428692,
                -0.74178775,
                -1.74787363,
                1.31100338,
                0.25744373,
            ],
            [
                0.95291173,
                -1.35777067,
                -0.97827832,
                -0.47219872,
                -0.21362369,
                -0.11311203,
                -0.22188404,
                -0.49618024,
                -1.04686276,
                -2.1785747,
                1.0,
            ],
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
        ]
    )

    assert calc == approx(ref, rel=5e-5)


def test_RHS(solver_obj):
    calc = solver_obj.get_RHS(alpha=8 / 180 * pi)
    ref = np.array(
        [
            0.06498711,
            0.07147468,
            0.0885728,
            0.14883974,
            0.48101857,
            0.38369263,
            -0.04156756,
            -0.20904692,
            -0.28724817,
            -0.33027553,
            0.0,
        ]
    )
    assert calc == approx(ref.reshape(ref.size, 1), rel=5e-5)


def test_Gamma(solver_obj):
    calc = solver_obj.solve_vorticity(alpha=8 / 180 * pi)
    ref = np.array(
        [
            -0.04925277,
            -0.13912607,
            -0.14202391,
            -0.13722209,
            -0.11395583,
            0.18838509,
            0.27053542,
            0.22651428,
            0.19311638,
            0.16234484,
            0.04925277,
        ]
    )
    assert calc == approx(ref.reshape(ref.size, 1), rel=5e-5)


def test_v_ind(solver_obj):
    calc = solver_obj.get_v_ind(
        alpha=8 / 180 * pi,
        Gamma=solver_obj.solve_vorticity(alpha=8 / 180 * pi),
    )
    ref = np.array(
        [
            -0.85013908,
            -0.89732153,
            -0.87555913,
            -0.78483922,
            -0.08752438,
            1.62253578,
            1.51914356,
            1.30421161,
            1.12729783,
            0.92407688,
        ]
    )
    assert calc == approx(ref.reshape(ref.size, 1), rel=5e-5)


def test_CP(solver_obj):
    calc = solver_obj.solve_Cp(alpha=8, plot=False)
    ref = np.array(
        [
            0.27726354,
            0.19481407,
            0.23339621,
            0.38402739,
            0.99233948,
            -1.63262237,
            -1.30779717,
            -0.70096792,
            -0.2708004,
            0.14608192,
        ]
    )
    assert calc == approx(ref.reshape(ref.size, 1), rel=5e-5)
