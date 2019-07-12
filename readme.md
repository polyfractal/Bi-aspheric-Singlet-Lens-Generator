This translates the Mathematica code in *"General formula for bi-aspheric singlet lens design free of spherical aberration."* [1] to Python using [SymPy](https://www.sympy.org/en/index.html).  The intention was to reproduce the surfaces presented in the paper, and then use OpenSCAD (via [SolidPython](https://github.com/SolidCode/SolidPython/)) to model the lenses in 3D. 

Note this repo is in an unfinished, WIP state.  The basic equations have been converted and appear to work for the cases in the paper, but the OpenSCAD implementation is incomplete.  

The equations also do not appear to work quite correctly for the lenses presented in *"Single Lens Telescope"* [2].  This might be an artifact of incorrect translation of the original Mathematica code.  The lenses in [2] assume tₐ and tᵦ are infinite (collimated beams), so the code may also need to be adjusted using the equations in Figure 10 of [1] (e.g. calculating the limit when tₐ → −∞ for  fᵢ , rᵢ , zᵢ )


## Lenses from Table 1, González-Acuña et al. (2018)

| First Surface  | Plot |
| ------------- | ------------- |
| Table 1 Reference  | <a href="https://github.com/polyfractal/Bi-aspheric-Singlet-Lens-Generator/blob/master/images/table1.png"><img src="https://github.com/polyfractal/Bi-aspheric-Singlet-Lens-Generator/blob/master/images/table1.png" width="400"/></a>  |
| Flat  | <a href="https://github.com/polyfractal/Bi-aspheric-Singlet-Lens-Generator/blob/master/images/table1.1.png"><img src="https://github.com/polyfractal/Bi-aspheric-Singlet-Lens-Generator/blob/master/images/table1.1.png" width="400"/></a>  |
| Spherical  | <a href="https://github.com/polyfractal/Bi-aspheric-Singlet-Lens-Generator/blob/master/images/table1.2.png"><img src="https://github.com/polyfractal/Bi-aspheric-Singlet-Lens-Generator/blob/master/images/table1.2.png" width="400"/></a>  |
| Parabolic  | <a href="https://github.com/polyfractal/Bi-aspheric-Singlet-Lens-Generator/blob/master/images/table1.3.png"><img src="https://github.com/polyfractal/Bi-aspheric-Singlet-Lens-Generator/blob/master/images/table1.3.png" width="400"/></a>  |
| Cosine  | <a href="https://github.com/polyfractal/Bi-aspheric-Singlet-Lens-Generator/blob/master/images/table1.4.png"><img src="https://github.com/polyfractal/Bi-aspheric-Singlet-Lens-Generator/blob/master/images/table1.4.png" width="400"/></a>  |

---

## Lenses from Figure 4, González-Acuña et al. (2018)
![Figure 4](images/figure4.png?raw=true "Figure 4 from [1]")

**Figure 4.D**
![Figure 4.D](images/figure4.d.png?raw=true "Figure 4.D")

---

## References

[1] *González-Acuña, Rafael G., and Héctor A. Chaparro-Romo. "General formula for bi-aspheric singlet lens design free of spherical aberration." Applied optics 57.31 (2018): 9341-9345.* ([PDF](https://www.researchgate.net/publication/328536020_General_formula_for_bi-aspheric_singlet_lens_design_free_of_spherical_aberration))

[2] González-Acuña, Rafael Guillermo, Héctor Alejandro Chaparro-Romo, and Julio Cesar Gutíerrez-Vega. "Single lens telescope." arXiv preprint arXiv:1903.11129 (2019). ([PDF](https://arxiv.org/pdf/1903.11129.pdf))