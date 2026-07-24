# Breast Digital Twin: Towards simulation-guided acceleration of method development

This repository contains the phantoms and sequences necessary to recreate experiments from the article "Breast Digital Twin: Towards simulation-guided acceleration of method development". 

**Phantoms**

The phantoms are defined with the BIfTI format [2].
There are breast phantoms for 3T and 7T simulation. Both field-strength phantoms are prepared to be loaded without and with artefacts.
The 3T phantom can include inhomogeneous dB0, inhomogeneous B1+, inhomogeneous B1-.
The 7T phantom can include inhomogeneous B1+ and B1-. 

For each field strength two phantoms are defined: one with 8 slices and one with just one slice, which is the one used in the article.

**Sequences**

 The sequences are written in the Pulseq .seq format [3]. The supplied sequences are FLASH and TSE sequences with various contrasts:
 - FLASH in-phase and opposed-phase, cartesian readout
 - TSE in-phase and opposed-phase
 - TSE with fat saturation: STIR, STIR with asymmetric excitation, FatSat, FatSat with asymmetric excitation
 - FLASH opposed-phase, radial readout

**Simulation with the Any-Field scanner**

Phantom and sequences can be tested using the Any-Field scanner [1]. Some pre-loaded sequences can be found under these links:
1) FLASH in-phase sequence: [FLASH IP](https://mrx-org.github.io/anyfield/?seq_url=https://raw.githubusercontent.com/magdamd/BreastDigitalTwin/refs/heads/main/Sequences/flash_IP_512x512.seq)
2) TSE STIR sequence: [TSE STIR ideal](https://mrx-org.github.io/anyfield/?seq_url=https://raw.githubusercontent.com/magdamd/BreastDigitalTwin/refs/heads/main/Sequences/tse_IP_STIR_512x512.seq)

For the anyfield scanner, the phantom can be selected from the Phantom menu as shown below
<p align="center">
<img width="1000" height="500" alt="Bild2" src="https://github.com/user-attachments/assets/d7690f42-91d0-4218-83c6-79cb4af6f4a5" />
</p>


**Some notes on the use of the Any-Field scanner**

* The sequences with off-resonant RF pulses (sequences with FatSat) will not create the expected effect, because the Any-Field scanner currently does not support the extension of MR-zero to off-resonant behavior. Having that into account, no links with that same experiences are provided. 
* There is a default phantom resolution, simulation accuracy and PDG number of states being used in the Any-Field scanner that does not reflect the ones used for producing the figures in the article, so a complete correspondence is not expected. It is, however, a very convenient tool to experiment the simulation with the breast digital twin for the first time without having to build new scripts.
* The simulation of the links provided is expected to take approximately 5 minutes due to the high resolution of the sequences (512x512).
* Links to the simulation of the radial readout and CEST experiment are not provided because it has a very long execution time.
* Simulations with motion and dynamic B0 are also not supported currently in the Any-Field scanner.

 **References**
 
[1] S. Weinmüller et al., ‘Any-Field Scanner: A Virtual MRI Scanner for Rapid and Realistic Pulseq Sequence Validation in the Browser’, presented at the Acceepted at ESMRMB Annual Congress 2026,

[2] J. Endres, mrx-org/bifti-phantoms. (May 27, 2026). Python. MRX. Accessed: Jun. 01, 2026. [Online]. Available: https://github.com/mrx-org/bifti-phantoms

[3] K. J. Layton et al., ‘Pulseq: A rapid and hardware-independent pulse sequence prototyping framework’, Magnetic Resonance in Medicine, vol. 77, no. 4, pp. 1544–1552, 2017, doi: 10.1002/mrm.26235.



