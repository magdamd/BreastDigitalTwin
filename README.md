# Breast Digital Twin: Towards simulation-guided acceleration of method development

This repository contains the phantoms and sequences necessary to recreate experiments from the article "Breast Digital Twin: Towards simulation-guided acceleration of method development". 

Phantom and sequences can be tested using the Any-Field scanner [1]. Some pre-defined expriences, that are also mentioned in the article, can be found under these links:
- 3T ideal phantom and FLASH in-phase sequence (Figure 3A.1): [FLASH IP](https://mrx-org.github.io/anyfield/#protocol_gz=H4sIAAAAAAAACrVWbW_bNhD-Kzf1g-3ClmInzlwBHlAULbChKIq-fYkCgZJONheKZEgqjRDkvw9HSrKTxti-TAkS8Xivzz1H6iG6i9LlPLrhsorSiMmu5iiqWBvlVKlENI9qLlCyBqM0ImmuW2HxNufSodEGHZpYd9E8KlVFOq8gSRKwpeHaZfIVGLxtuUG70J3bKwlbyKI_tufxmyyi7Qo1ygplydHCFq6ySLaN7rJoDlnUMKeFcoIXYa27EHy7Xcbr-CzWyrplFl1n8hX5unJKiXiogaTQ8NIozXUuVV6h7kMMfoIpJZxJelksFvBJOSyUugGLrtUwfacEKyCBv1rdOTSHt49e_OMrvFMVzsg2kzkfq9wJVTBhp7N4h2462aEbNidzEKwpKpbCJyVxNp0BEBAOSweyyCSvYXTELUjlvGKaSQAYt2LTylxwiXnDdrycTjTXkzlMuLSOCQGLW_BQwgFFeBHAyexE7SirUNaw_1Z2HwhaaNCxijkGBe647GsfgM__th4BM5lMMvlAWWeeYFmUUhN7amXRPGx5VtWtLA_7L5BsVCd5hTWX3HElgw2XBMQTlYNDJjuLt3GgpI1p81f36cviJy6V4TveR9w7p22aJDvu9m0Rl6pJGnO_UGaXDDgkhVBF0jAukwH3JOSSvBws9rwP8Z4Tl6I-Ze6QGG9awQYoHgJHsqhg5Q0OkDeqYiKnlHN30YfwyO-ZdKoJSoVBZt2ilyVhmZ9_y63gJeaa6REOsq3VXc7q2sOewtUqfnO5-X09hzP_u7w8iy83mzeri7Plxfpyc37uxcdaq15jtd5cnK0vN-uLwXgzh8XycliRt-snYRvmDL_3YZerzRzCn-vnZf1nPXWHxrJGi76UOaxIj9Qee5QNls8A_jfnDbq9qkYGekYsdCfbunZ09AE8ZvIxk35ITo3X0QTyRivj-pFmFqQeZQMpSKz14C3MBPhRwQos3rYoSwRWMe2wgtqoJoX_icd91hH9fFSsAgafQ440f0B3CjBZgUHXGgluj2OCMXy3CK0WZKYMIDkGBj8-fAXN3D75_uVjHDxnkooA12kud9Cj8VZK5ZjDilCrsIaXk5yGRvmjggtMD3ZX1hm6bUicRdf-xkLNc4u58ceHn4JZOnQ6ZELvTysdEfdJskPlMWVG-p-ZYQ0lY8N6MT5hPVy9kIJ1Bqa0noWtYO724JRH7wArD3DeceNaJrzMdtZhA1OMdzEkAVqb1EqR1ZFDRTgTvL4F5KVvQ9E6pyTtu06HHWrFWMgX38anVYz4QjoyNP7aY3KI-W2PQDGOKBr_iuwJpg8RtqD16HvaV-RMlx7iUHSDrJoOHe-18L5E7eC9_8eVJNd4ZGcYtwhfWul4g--NUQNzhqfOog-MC6yoFRThqBeThyHa4ySFB_zNPsYw1DQ8WUQYeP2GdVCMhKl4XaNB6QZG0TnFQx9ai1Ajc63B8IVQt0J0YFtNQGEFRQduz-0BsqLlooqPg89CoL4Z_SgSv_sThE6fU6dIfyodLv2CWcxLJgQrBML2xNQNM3nikn82lNssOrBVMLvP__ycr5er-_VyFQbxMIc3P5nZ0fedUGX47iqV7gYu9MWdSHf6-nUwn0WP_wDCyK_TEgsAAA) 
- 3T ideal phantom and TSE STIR sequence (Figure 3C.1): [TSE STIR ideal]()
- 3T inhomogeneous B1+ phantom and TSE STIR sequence (Figure 5C.1): [TSE STIR inhomogeneous B1+]()
- 3T inhomogeneous B1+ phantom and TSE STIR + asymmetric excitation sequence (Figure 5C.2): [TSE STIR and asymmetric excitation with inhomogeneous B1+]()

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

**Some notes on the use of the Any-Field scanner**

* The sequences with off-resonant RF pulses (sequences with FatSat) will not create the expected effect, because the Any-Field scanner currently does not support the extension of MR-zero to off-resonant behavior. Having that into account, no links with that same experiences are provided. 
* There is a default phantom resolution, simulation accuracy and PDG number of states being used in the Any-Field scanner that does not reflect the ones used for producing the figures in the article, so a complete correspondence is not expected. It is, however, a very convenient tool to experiment the simulation with the breast digital twin for the first time without having to build new scripts.
* The simulation of the links provided is expected to take approximately 5 minutes.
* Links to the simulation of the radial readout and CEST experiment are not provided because it has a very long execution time.
* Simulations with motion and dynamic B0 are also not supported currently in the Any-Field scanner.

 **References**
 
[1] S. Weinmüller et al., ‘Any-Field Scanner: A Virtual MRI Scanner for Rapid and Realistic Pulseq Sequence Validation in the Browser’, presented at the Acceepted at ESMRMB Annual Congress 2026,

[2] J. Endres, mrx-org/bifti-phantoms. (May 27, 2026). Python. MRX. Accessed: Jun. 01, 2026. [Online]. Available: https://github.com/mrx-org/bifti-phantoms

[3] K. J. Layton et al., ‘Pulseq: A rapid and hardware-independent pulse sequence prototyping framework’, Magnetic Resonance in Medicine, vol. 77, no. 4, pp. 1544–1552, 2017, doi: 10.1002/mrm.26235.



