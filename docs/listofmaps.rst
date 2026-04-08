.. _listofmaps:

------------
List of Maps
------------
This is a complete list of maps available in the `neuromaps_mouse` package.

----

Psychedelic drug activation maps (aboharb2025)
==============================================

Regional brain activation maps following administration of various
psychedelic compounds and controls, measured via whole-brain imaging.

Each file contains activation values for a single treatment condition:
psychedelics (5-MeO, 6-F-DET, Ketamine, MDMA, Psilocybin),
antidepressant controls (ASSRI, CSSRI), and saline control.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - 5-MeO
     - tabular
     - ``('aboharb2025', '5meo', 'allenccfv3', 'region')``
   * - 6-F-DET
     - tabular
     - ``('aboharb2025', '6fdet', 'allenccfv3', 'region')``
   * - ASSRI
     - tabular
     - ``('aboharb2025', 'assri', 'allenccfv3', 'region')``
   * - CSSRI
     - tabular
     - ``('aboharb2025', 'cssri', 'allenccfv3', 'region')``
   * - Ketamine
     - tabular
     - ``('aboharb2025', 'ket', 'allenccfv3', 'region')``
   * - MDMA
     - tabular
     - ``('aboharb2025', 'mdma', 'allenccfv3', 'region')``
   * - Psilocybin
     - tabular
     - ``('aboharb2025', 'psi', 'allenccfv3', 'region')``
   * - Saline
     - tabular
     - ``('aboharb2025', 'sal', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('aboharb2025', '5meo', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/aboharb2025

    # region mapping files
    # source-aboharb2025_regionmapping.csv


----

Cell type density atlas (ero2018)
=================================

A Cell Atlas for the Mouse Brain (Ero et al., 2018).

Provides density estimates of major cell types across
Allen CCFv3 brain regions, derived from single-cell RNA sequencing
and in situ hybridization data.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Density of cell types
     - tabular
     - ``('ero2018', 'celldensity', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('ero2018', 'celldensity', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/ero2018

    # region mapping files
    # source-ero2018_regionmapping.csv


----

IBL behavioral and electrophysiology maps (ibl2025)
===================================================

Regional brain maps from the International Brain Laboratory (IBL)
reproducible brain-wide mapping pipeline.

Includes behavioral task performance metrics and electrophysiology
summary statistics mapped to Allen CCFv3 regions.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Behavioral task
     - tabular
     - ``('ibl2025', 'behtask', 'allenccfv3', 'region')``
   * - Electrophysiology
     - tabular
     - ``('ibl2025', 'ephys', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('ibl2025', 'behtask', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/ibl2025

    # region mapping files
    # source-ibl2025_regionmapping.csv


----

Brain microvasculature (ji2021)
===============================

Brain microvasculature has a common topology with local differences
in geometry that match metabolic load (Ji et al., 2021).

Whole mouse brain microvasculature imaged, reconstructed,
and analyzed at sub-micrometer resolution. Includes data from
Ji et al. (2021), Kirst et al. (2020), and Todorov et al. (2020).

Each file contains region-level tabular data characterizing
microvascular network properties across Allen CCFv3 regions.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Ji 2021
     - tabular
     - ``('ji2021', 'ji2021', 'allenccfv3', 'region')``
   * - Kirst 2020
     - tabular
     - ``('ji2021', 'kirst2020', 'allenccfv3', 'region')``
   * - Todorov 2020
     - tabular
     - ``('ji2021', 'todorov2020', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('ji2021', 'ji2021', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/ji2021

    # region mapping files
    # source-ji2021_regionmapping.csv


----

High-resolution connectome model (knox2018)
===========================================

A high-resolution data-driven model of the mouse connectome
(Knox et al., 2018).

Provides region-by-region connectivity matrices at the Allen CCFv3
parcellation. Each matrix is asymmetric: rows are source regions and
columns are target regions. Available for both ipsi- and contralateral
projections, in connection density and connection strength variants,
each with normalized versions.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Connection density (contralateral)
     - matrix
     - ``('knox2018', 'conndencontra', 'allenccfv3', 'region')``
   * - Connection density (ipsilateral)
     - matrix
     - ``('knox2018', 'conndenipsi', 'allenccfv3', 'region')``
   * - Connection strength (contralateral)
     - matrix
     - ``('knox2018', 'connstrcontra', 'allenccfv3', 'region')``
   * - Connection strength (ipsilateral)
     - matrix
     - ``('knox2018', 'connstripsi', 'allenccfv3', 'region')``
   * - Normalized connection density (contralateral)
     - matrix
     - ``('knox2018', 'normconndencontra', 'allenccfv3', 'region')``
   * - Normalized connection density (ipsilateral)
     - matrix
     - ``('knox2018', 'normconndenipsi', 'allenccfv3', 'region')``
   * - Normalized connection strength (contralateral)
     - matrix
     - ``('knox2018', 'normconnstrcontra', 'allenccfv3', 'region')``
   * - Normalized connection strength (ipsilateral)
     - matrix
     - ``('knox2018', 'normconnstripsi', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('knox2018', 'conndencontra', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/knox2018

    # region mapping files
    # source-knox2018_regionmapping.csv


----

Allen Mouse Brain Atlas gene expression (lein2006amba)
======================================================

Allen Mouse Brain Atlas (Lein et al., 2006) — regional gene
expression data aggregated across sagittal and coronal sections.

For each section type (sagittal, coronal), three expression metrics
are provided: energy, density, and intensity. Each file is a
region-by-gene matrix where rows are Allen CCFv3 regions and columns
are genes (see feature mapping file for gene names).

This is a large dataset; files are compressed (.csv.gz).

.. warning:: This is a very large dataset, and may take a long time to download.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Expression energy of sagittal slices
     - tabular
     - ``('lein2006amba', 'sagittalenergy', 'allenccfv3', 'region')``
   * - Expression energy of coronal slices
     - tabular
     - ``('lein2006amba', 'coronalenergy', 'allenccfv3', 'region')``
   * - Expression density of sagittal slices
     - tabular
     - ``('lein2006amba', 'sagittaldensity', 'allenccfv3', 'region')``
   * - Expression density of coronal slices
     - tabular
     - ``('lein2006amba', 'coronaldensity', 'allenccfv3', 'region')``
   * - Expression intensity of sagittal slices
     - tabular
     - ``('lein2006amba', 'sagittalintensity', 'allenccfv3', 'region')``
   * - Expression intensity of coronal slices
     - tabular
     - ``('lein2006amba', 'coronalintensity', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('lein2006amba', 'sagittalenergy', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/lein2006amba

    # region mapping files
    # source-lein2006amba_regionmapping.csv

    # feature mapping files
    # source-lein2006amba_genemapping.csv


----

Cell-type-specific functional connectivity (mandino2025)
========================================================

Cell-type-specific functional connectivity matrices from
Mandino et al. (2025), combining calcium imaging and fMRI.

Files are organized by modality (calcium imaging: ``cal`` prefix,
fMRI: ``fmri`` prefix), cell type (PV, VIP, SLC, SOM, glia),
and whether global signal regression was applied
(``gsr`` = with GSR, ``nogsr`` = without GSR).

For example, ``calpvallgsr`` is the calcium imaging PV cell matrix
with GSR. Each file is a region-by-region connectivity matrix.
Region mappings differ between modalities.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Calcium imaging PV with GSR
     - matrix
     - ``('mandino2025', 'calpvallgsr', 'allenccfv3', 'region')``
   * - Calcium imaging PV without GSR
     - matrix
     - ``('mandino2025', 'calpvallnogsr', 'allenccfv3', 'region')``
   * - Calcium imaging VIP with GSR
     - matrix
     - ``('mandino2025', 'calvipallgsr', 'allenccfv3', 'region')``
   * - Calcium imaging VIP without GSR
     - matrix
     - ``('mandino2025', 'calvipallnogsr', 'allenccfv3', 'region')``
   * - Calcium imaging SLC with GSR
     - matrix
     - ``('mandino2025', 'calslcallgsr', 'allenccfv3', 'region')``
   * - Calcium imaging SLC without GSR
     - matrix
     - ``('mandino2025', 'calslcallnogsr', 'allenccfv3', 'region')``
   * - Calcium imaging SOM with GSR
     - matrix
     - ``('mandino2025', 'calsomallgsr', 'allenccfv3', 'region')``
   * - Calcium imaging SOM without GSR
     - matrix
     - ``('mandino2025', 'calsomallnogsr', 'allenccfv3', 'region')``
   * - Calcium imaging glia with GSR
     - matrix
     - ``('mandino2025', 'calgliaallgsr', 'allenccfv3', 'region')``
   * - Calcium imaging glia without GSR
     - matrix
     - ``('mandino2025', 'calgliaallnogsr', 'allenccfv3', 'region')``
   * - fMRI PV with GSR
     - matrix
     - ``('mandino2025', 'fmripvallgsr', 'allenccfv3', 'region')``
   * - fMRI PV without GSR
     - matrix
     - ``('mandino2025', 'fmripvallnogsr', 'allenccfv3', 'region')``
   * - fMRI VIP with GSR
     - matrix
     - ``('mandino2025', 'fmrivipallgsr', 'allenccfv3', 'region')``
   * - fMRI VIP without GSR
     - matrix
     - ``('mandino2025', 'fmrivipallnogsr', 'allenccfv3', 'region')``
   * - fMRI SLC with GSR
     - matrix
     - ``('mandino2025', 'fmrislcallgsr', 'allenccfv3', 'region')``
   * - fMRI SLC without GSR
     - matrix
     - ``('mandino2025', 'fmrislcallnogsr', 'allenccfv3', 'region')``
   * - fMRI SOM with GSR
     - matrix
     - ``('mandino2025', 'fmrisomallgsr', 'allenccfv3', 'region')``
   * - fMRI SOM without GSR
     - matrix
     - ``('mandino2025', 'fmrisomallnogsr', 'allenccfv3', 'region')``
   * - fMRI glia with GSR
     - matrix
     - ``('mandino2025', 'fmrigliaallgsr', 'allenccfv3', 'region')``
   * - fMRI glia without GSR
     - matrix
     - ``('mandino2025', 'fmrigliaallnogsr', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('mandino2025', 'calpvallgsr', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/mandino2025

    # region mapping files
    # source-mandino2025_cal_regionmapping.csv
    # source-mandino2025_fmri_regionmapping.csv


----

Homogeneous and voxel-scale connectivity models (nathan2026)
============================================================

Connectivity matrices from Nathan et al. (2026) providing two
complementary models of mouse brain connectivity.

The homogeneous model (``hom``) is a linear connectivity model via
constrained optimization and linear regression, similar to
Oh et al. (2014).

The voxel-scale model (``vox``) from Knox et al. (2018) performs
Nadaraya-Watson regression to infer voxel-to-voxel connectivity,
splitting the source space into 12 major brain divisions to prevent
influence from adjacent divisions. The voxel-scale results are then
regionalized into Allen CCFv3 regions.

Files are further organized by:

- Laterality: ``ipsi`` (ipsilateral) or ``contra`` (contralateral)
- Quality: ``orig`` (original methods) or ``qc`` (carefully QC-ed
  experiments providing a refined connectome)
- Resolution: ``211`` (regions from Oh et al., 2014) or ``291``
  (regions from Knox et al., 2018)

Each resolution has its own region mapping file (``r211``, ``r291``).

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Homotopic ipsilateral QC at 211 region resolution
     - matrix
     - ``('nathan2026', 'homipsiqc211', 'allenccfv3', 'region')``
   * - Homotopic ipsilateral QC at 291 region resolution
     - matrix
     - ``('nathan2026', 'homipsiqc291', 'allenccfv3', 'region')``
   * - Homotopic ipsilateral original at 211 region resolution
     - matrix
     - ``('nathan2026', 'homipsiorig211', 'allenccfv3', 'region')``
   * - Homotopic ipsilateral original at 291 region resolution
     - matrix
     - ``('nathan2026', 'homipsiorig291', 'allenccfv3', 'region')``
   * - Homotopic contralateral QC at 211 region resolution
     - matrix
     - ``('nathan2026', 'homcontraqc211', 'allenccfv3', 'region')``
   * - Homotopic contralateral QC at 291 region resolution
     - matrix
     - ``('nathan2026', 'homcontraqc291', 'allenccfv3', 'region')``
   * - Homotopic contralateral original at 211 region resolution
     - matrix
     - ``('nathan2026', 'homcontraorig211', 'allenccfv3', 'region')``
   * - Homotopic contralateral original at 291 region resolution
     - matrix
     - ``('nathan2026', 'homcontraorig291', 'allenccfv3', 'region')``
   * - Voxelwise ipsilateral QC at 211 region resolution
     - matrix
     - ``('nathan2026', 'voxipsiqc211', 'allenccfv3', 'region')``
   * - Voxelwise ipsilateral QC at 291 region resolution
     - matrix
     - ``('nathan2026', 'voxipsiqc291', 'allenccfv3', 'region')``
   * - Voxelwise ipsilateral original at 211 region resolution
     - matrix
     - ``('nathan2026', 'voxipsiorig211', 'allenccfv3', 'region')``
   * - Voxelwise ipsilateral original at 291 region resolution
     - matrix
     - ``('nathan2026', 'voxipsiorig291', 'allenccfv3', 'region')``
   * - Voxelwise contralateral QC at 211 region resolution
     - matrix
     - ``('nathan2026', 'voxcontraqc211', 'allenccfv3', 'region')``
   * - Voxelwise contralateral QC at 291 region resolution
     - matrix
     - ``('nathan2026', 'voxcontraqc291', 'allenccfv3', 'region')``
   * - Voxelwise contralateral original at 211 region resolution
     - matrix
     - ``('nathan2026', 'voxcontraorig211', 'allenccfv3', 'region')``
   * - Voxelwise contralateral original at 291 region resolution
     - matrix
     - ``('nathan2026', 'voxcontraorig291', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('nathan2026', 'homipsiqc211', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/nathan2026

    # region mapping files
    # source-nathan2026_r211_regionmapping.csv
    # source-nathan2026_r291_regionmapping.csv


----

Mesoscale structural connectome (oh2014)
========================================

A mesoscale connectome of the mouse brain (Oh et al., 2014).

Provides weighted connectivity strength, p-values, and projection
distances for both ipsi- and contralateral projections across
Allen CCFv3 regions.

Original source: Supplementary Table 3.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Weighted ipsilateral strength index
     - matrix
     - ``('oh2014', 'wipsi', 'allenccfv3', 'region')``
   * - P values for wipsi
     - matrix
     - ``('oh2014', 'pvalipsi', 'allenccfv3', 'region')``
   * - Weighted contralateral strength index
     - matrix
     - ``('oh2014', 'wcontra', 'allenccfv3', 'region')``
   * - P values for wcontra
     - matrix
     - ``('oh2014', 'pvalcontra', 'allenccfv3', 'region')``
   * - Distance (mm) for ipsilateral projections
     - matrix
     - ``('oh2014', 'distipsi', 'allenccfv3', 'region')``
   * - Distance (mm) for contralateral projections
     - matrix
     - ``('oh2014', 'distcontra', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('oh2014', 'wipsi', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/oh2014

    # region mapping files
    # source-oh2014_regionmapping.csv


----

ABC Atlas MERFISH cell types and gene expression (yao2023abca)
==============================================================

Mouse whole-brain transcriptomic cell type atlas from the
Allen Brain Cell Atlas (Yao et al., 2023), MERFISH dataset
(C57BL6J-638850).

Gene expression files (``*mean``) are region-by-gene matrices
averaged at three hierarchical levels: division (``divi``),
structure (``stru``), and substructure (``subs``).
``imp`` prefix indicates imputed expression values.

Cell type files (``*ct*``) are region-by-cell-type matrices
at four classification levels: class, subclass, supertype, cluster,
each at the three hierarchical region levels.

Each hierarchical level uses its own region mapping file.
Separate feature mapping files are provided for measured and
imputed gene sets.

This is a large dataset; files may take a long time to download.

.. warning:: This is a very large dataset, and may take a long time to download.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Average regional gene expressions at the division level
     - tabular
     - ``('yao2023abca', 'divimean', 'allenccfv3', 'region')``
   * - Average regional gene expressions at the structure level
     - tabular
     - ``('yao2023abca', 'strumean', 'allenccfv3', 'region')``
   * - Average regional gene expressions at the substructure level
     - tabular
     - ``('yao2023abca', 'subsmean', 'allenccfv3', 'region')``
   * - Average imputed regional gene expressions at the division level
     - tabular
     - ``('yao2023abca', 'impdivimean', 'allenccfv3', 'region')``
   * - Average imputed regional gene expressions at the structure level
     - tabular
     - ``('yao2023abca', 'impstrumean', 'allenccfv3', 'region')``
   * - Average imputed regional gene expressions at the substructure level
     - tabular
     - ``('yao2023abca', 'impsubsmean', 'allenccfv3', 'region')``
   * - Cell type (class) at the division level
     - tabular
     - ``('yao2023abca', 'divictclass', 'allenccfv3', 'region')``
   * - Cell type (class) at the structure level
     - tabular
     - ``('yao2023abca', 'structclass', 'allenccfv3', 'region')``
   * - Cell type (class) at the substructure level
     - tabular
     - ``('yao2023abca', 'subsctclass', 'allenccfv3', 'region')``
   * - Cell type (subclass) at the division level
     - tabular
     - ``('yao2023abca', 'divictsubclass', 'allenccfv3', 'region')``
   * - Cell type (subclass) at the structure level
     - tabular
     - ``('yao2023abca', 'structsubclass', 'allenccfv3', 'region')``
   * - Cell type (subclass) at the substructure level
     - tabular
     - ``('yao2023abca', 'subsctsubclass', 'allenccfv3', 'region')``
   * - Cell type (supertype) at the division level
     - tabular
     - ``('yao2023abca', 'divictsupertype', 'allenccfv3', 'region')``
   * - Cell type (supertype) at the structure level
     - tabular
     - ``('yao2023abca', 'structsupertype', 'allenccfv3', 'region')``
   * - Cell type (supertype) at the substructure level
     - tabular
     - ``('yao2023abca', 'subsctsupertype', 'allenccfv3', 'region')``
   * - Cell type (cluster) at the division level
     - tabular
     - ``('yao2023abca', 'divictcluster', 'allenccfv3', 'region')``
   * - Cell type (cluster) at the structure level
     - tabular
     - ``('yao2023abca', 'structcluster', 'allenccfv3', 'region')``
   * - Cell type (cluster) at the substructure level
     - tabular
     - ``('yao2023abca', 'subsctcluster', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('yao2023abca', 'divimean', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/yao2023abca

    # region mapping files
    # source-yao2023abca_division_regionmapping.csv
    # source-yao2023abca_structure_regionmapping.csv
    # source-yao2023abca_substructure_regionmapping.csv

    # feature mapping files
    # source-yao2023abca_merfish_genemapping.csv
    # source-yao2023abca_imputed_genemapping.csv


----

ABC Atlas Zhuang-ABCA gene expression (zhang2023abca)
=====================================================

A molecularly defined and spatially resolved cell atlas of the
whole mouse brain (Zhang et al., 2023, Zhuang-ABCA MERFISH).

Gene expression files are region-by-gene matrices averaged at
three hierarchical levels: division (``divi``), structure
(``stru``), and substructure (``subs``). Each level uses its own
region mapping file.

This is a large dataset; files may take a long time to download.

.. warning:: This is a very large dataset, and may take a long time to download.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Average regional gene expressions at the division level
     - tabular
     - ``('zhang2023abca', 'divimean', 'allenccfv3', 'region')``
   * - Average regional gene expressions at the structure level
     - tabular
     - ``('zhang2023abca', 'strumean', 'allenccfv3', 'region')``
   * - Average regional gene expressions at the substructure level
     - tabular
     - ``('zhang2023abca', 'subsmean', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('zhang2023abca', 'divimean', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/zhang2023abca

    # region mapping files
    # source-zhang2023abca_division_regionmapping.csv
    # source-zhang2023abca_structure_regionmapping.csv
    # source-zhang2023abca_substructure_regionmapping.csv

    # feature mapping files
    # source-zhang2023abca_merfish_genemapping.csv


----

Brain synaptome architecture (zhu2018)
======================================

Architecture of the Mouse Brain Synaptome (Zhu et al., 2018).

Provides synaptic type density measurements across Allen CCFv3
brain regions, characterizing the molecular and cellular
composition of synapses throughout the mouse brain.

**Available files**

.. list-table::
   :header-rows: 1

   * - Description
     - Format
     - Key
   * - Synaptic type density
     - tabular
     - ``('zhu2018', 'typedensity', 'allenccfv3', 'region')``

**How to use**

.. code:: python

    # fetch a specific annotation
    fetch_annotation(('zhu2018', 'typedensity', 'allenccfv3', 'region'))

    # file location
    # $MOUSEMAPS_DATA/zhu2018

    # region mapping files
    # source-zhu2018_regionmapping.csv

