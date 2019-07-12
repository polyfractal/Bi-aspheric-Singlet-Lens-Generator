#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import sympy
import numpy;

from solid import *
from solid.utils import *
from sympy import *
from sympy.plotting import plot, plot_parametric


def main():
    phi, phi_top, phi_middle, phi_bottom, ra, ta, za, df_za, ri, ri_top, ri_bottom = symbols('phi phi_top phi_middle phi_bottom ra ta za df_za ri ri_top ri_bottom')
    zi, zi_top, zi_bottom, fi, h0, h1, zb, rb = symbols('zi zi_top zi_bottom fi h0 h1 zb rb')

    

    # Flat surface, Table 1.1
    #za = 0
    #
    #s1 = 1
    #n = 1.5
    #t = 10
    #ta = -70
    #tb = 75
   
    # Spherical surface, Table 1.2
    #za = 100 - sqrt(100**2 - ra**2)
    #
    #s1 = 1
    #n = 1.5
    #t = 8
    #ta = -70
    #tb = 80

    # Parabolic surface, Table 1.3
    #za = ra**2 / 200
    #
    #s1 = 1
    #n = 1.5
    #t = 10
    #ta = -80
    #tb = 100

    # Cosine surface, Table 1.4
    #za = cos(ra/3)
    #
    #s1 = 1
    #n = 1.5
    #t = 8
    #ta = -70
    #tb = 80

    # Bessel surface, Figure 4.d
    za = besselj(0, ra/2)

    s1 = 1
    n = 1.5
    t = 5
    ta = -30
    tb = 75


    # Parabolic from "Single Lens Telescope"
    #za = -ra**2 / 4
    
    rmax = 50
    precision = 50

    
    df_za = diff(za, ra)

    phi_top = (ra + (-ta + za) * df_za)**2
    phi_middle = n**2 * (ra**2 + (ta - za)**2) * (1 + df_za**2)
    phi_bottom = sqrt(1 + df_za**2)
    phi = sqrt(1 - (phi_top / phi_middle)) / phi_bottom
    #phi = sqrt(1 - ((ra + (-ta + za) * df_za)**2 / (n**2 * (ra**2 + (ta - za)**2) * (1 + df_za**2)))) / sqrt(1 + df_za**2)

    ri_top = ra + (-ta + za) * df_za
    ri_bottom = n * sqrt(ra**2 + (ta - df_za)**2) * (1 + df_za**2)
    ri = (ri_top / ri_bottom) - df_za * phi
    #ri = ((ra + (-ta + za) * df_za) / (n * sqrt(ra**2 + (ta - za)**2) * (1 + df_za**2))) - (df_za * phi)

    zi_top = df_za * (ra + (-ta + za) * df_za)
    zi_bottom = n * sqrt(ra**2 + (ta - za)**2) * (1 + df_za**2)
    zi = (zi_top / zi_bottom) + phi
    #zi = ((df_za * (ra + (-ta + za) * df_za)) / ((n * sqrt(ra**2 + (ta - za)**2)) * (1 + df_za**2))) + phi

    fi = ta - tb - sign(ta) * sqrt(ra**2 + (ta - za)**2)
    h0 = ri**2 * za + fi * n * zi - ra * ri * zi + (t + tb) * zi**2 - n**2 * (za + t * zi)
    h1 = ra**2 + 2 * ra * ri * t + (tb - za)**2 + t**2 * (ri**2 + (-1 + zi)**2) - 2 * t * (tb - za) * (-1 + zi)
    zb = (h0 + s1 * sqrt(zi**2 * (fi**2 - 2 * fi * n * (ra * ri + ri**2 * t + zi * (t * (zi -1) - tb + za)) + h1 * n**2 - (ra * zi + ri * (t + tb - za))**2))) / (-n**2 + 1)
    rb = ra + (ri * (-za + zb)) / zi

    p = plot_parametric((ra, za), (rb, zb), (ra, -rmax, rmax), xlim=(-30,30), ylim=(-30,30))

    #foo = solveset(Eq(ra/za, rb/zb), ra)
    #print(foo)

    ras = numpy.linspace(0, rmax, precision)
    f_za = lambdify(ra, za, "numpy")
    f_rb = lambdify(ra, rb, "numpy")
    f_zb = lambdify(ra, zb, "numpy")

    #for i, (x1, y1, x2, y2) in enumerate(zip(ras, f_za(ras), f_rb(ras), f_zb(ras))):
    #    if (x1 > x2 and y1 < y2):
    #        print("Intersection at i: %2d [(%5.2f, %5.2f), (%5.2f,%5.2f)]" % (i, x1, y1, x2, y2))
    #        break
 
    

if __name__ == "__main__":
    main()

