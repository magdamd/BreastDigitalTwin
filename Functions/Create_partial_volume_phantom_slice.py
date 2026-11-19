"""
Auxiliary function: 2D breast phantom with partial volume effects.

Starting from a 3D proton-density (PD) phantom (X, Y, Z, tissues), a single 2D slice
is generated in two steps:
    1. In-plane Gaussian blurring of every tissue and slice.
    2. Weighted average of several slices to mimic the finite slice thickness. The tissue
       layout of each slice follows a reference slice; only voxels that are empty in the
       reference but occupied in the slice itself (e.g. fat/water entering from
       neighbouring slices) are taken from the slice itself.
"""

import os
import numpy as np
import nibabel as nib
from scipy.ndimage import gaussian_filter


def create_partial_volume_slice(
    data,
    slices,
    slices_reference,
    weights,
    silhouette_slice,
    water_idx=0,
    fat_idx=1,
    sigma=1.0,
    min_pd=1e-2,
    silhouette_pd=1e-1,
):
    """
    Parameters
    ----------
    data : (X, Y, Z, T) array
        PD of each tissue, no partial volume effects.
    slices : list[int]
        Slices that are averaged.
    slices_reference : list[int]
        Reference slice for each entry of `slices` (defines the tissue layout).
    weights : list[float]
        Weight of each slice; normalized to sum to 1.
    silhouette_slice : int
        Slice whose outline is imposed on the result.
    water_idx, fat_idx : int
        Channel indices of water and fat.
    sigma : float
        Standard deviation of the in-plane Gaussian kernel (voxels).
    min_pd : float
        Blurred values below this are set to 0 (removes the blur tails).
    silhouette_pd : float
        Threshold on the blurred PD that defines the silhouette of `silhouette_slice`.

    Returns
    -------
    (X, Y, 1, T) array
    """
    data = np.nan_to_num(np.asarray(data, dtype=float))

    # 1. In-plane blurring of each tissue
    for t in range(data.shape[3]):
        data[..., t] = gaussian_filter(data[..., t], sigma=sigma, axes=(0, 1))
    data[data < min_pd] = 0

    # Silhouette of the final slice: any tissue above threshold in the silhouette slice
    silhouette = np.any(data[:, :, silhouette_slice, :] > silhouette_pd, axis=-1)

    # 2. Weighted average of the slices
    weights = np.asarray(weights, dtype=float)
    weights = weights / weights.sum()

    result = np.zeros(data.shape[:2] + (data.shape[3],))
    for s, s_ref, w in zip(slices, slices_reference, weights):
        own = data[:, :, s, :]
        merged = data[:, :, s_ref, :].copy()

        # Voxels with water in this slice but not in the reference: keep own water,
        # fat is the complement (assumes water + fat fractions sum to 1).
        extra = (own[..., water_idx] > 0) & (merged[..., water_idx] == 0)
        merged[extra, water_idx] = own[extra, water_idx]
        merged[extra, fat_idx] = 1.0 - own[extra, water_idx]

        result += w * merged

    result *= silhouette[..., np.newaxis]
    return result[:, :, np.newaxis, :]


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    nifti = nib.load(os.path.join(
        dir_path, "../Phantoms/breast_3T_original_no_partial_volumes/breast_default_PD.nii.gz"))

    phantom_2d = create_partial_volume_slice(
        nifti.get_fdata(),
        slices=[3, 4, 6],
        slices_reference=[3, 4, 4],
        weights=[0.14, 0.42, 0.42],
        silhouette_slice=4,
    )

    out_path = os.path.join(dir_path, "out_phantom", "breast_2D_slice_partial_volume.nii.gz")
    nib.save(nib.Nifti1Image(phantom_2d, nifti.affine, header=nifti.header), out_path)

    # Optional: test import of the phantom with partial volume effects
    TEST_IMPORT = True
    if TEST_IMPORT:
        import MRzeroCore as mr0
        out_dir = os.path.join(dir_path, "out_phantom")
        phantom = mr0.TissueDict.load(os.path.join(out_dir, "test_phantom.json"))
        phantom.plot()    