# Breast Digital Twin: Towards simulation-guided acceleration of method development

This repository contains the phantom and sequences necessary to recreate experiences from the article "Breast Digital Twin: Towards simulation-guided acceleration of method development". 

Phantom and sequences can be tested using the Any-Field scanner [1]. Some pre-defined expriences, that are also mentioned in the article, can be found under these links:
- placeholder
- placeholder

**Phantoms**

The phantoms are defined with the BIfTI format [2].
There are breast phantoms for 3T and 7T simulation. Both field-strength phantoms are prepared to be loaded without and with artefacts.
The 3T phantom can include inhomogeneous dB0, inhomogeneous B1+, inhomogeneous B1-.
The 7T phantom can include inhomogeneous B1+ and B1-. 

**Sequences**

 The sequences are written in the Pulseq .seq format [3]. The supplied sequences are FLASH and TSE sequences with various contrasts:
 - FLASH in-phase and opposed-phase
 - TSE in-phase and opposed-phase
 - TSE with fat saturation: STIR, STIR with AsymEx

 **References**
 
[1] S. Weinmüller et al., ‘Any-Field Scanner: A Virtual MRI Scanner for Rapid and Realistic Pulseq Sequence Validation in the Browser’, presented at the Acceepted at ESMRMB Annual Congress 2026,

[2] J. Endres, mrx-org/bifti-phantoms. (May 27, 2026). Python. MRX. Accessed: Jun. 01, 2026. [Online]. Available: https://github.com/mrx-org/bifti-phantoms

[3] K. J. Layton et al., ‘Pulseq: A rapid and hardware-independent pulse sequence prototyping framework’, Magnetic Resonance in Medicine, vol. 77, no. 4, pp. 1544–1552, 2017, doi: 10.1002/mrm.26235.



