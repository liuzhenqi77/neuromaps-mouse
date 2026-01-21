.. _api_ref:

.. currentmodule:: neuromaps_mouse

Reference API
=============

.. contents:: **List of modules**
   :local:

.. _ref_datasets:

:mod:`neuromaps_mouse.datasets` - Dataset fetchers
--------------------------------------------------
.. automodule:: neuromaps_mouse.datasets
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps_mouse.datasets

Functions to show all available annotations

.. autosummary::
   :template: function.rst
   :toctree: generated/

   available_annotations

Functions to fetch and describe the annotations

.. autosummary::
   :template: function.rst
   :toctree: generated/

   fetch_annotation

Functions to fetch the atlases

.. autosummary::
   :template: function.rst
   :toctree: generated/

   fetch_allenccfv3
   fetch_all_atlases

Support functions

.. autosummary::
   :template: function.rst
   :toctree: generated/

   get_data_dir
   get_atlas_dir
   get_annotation_dir

.. _ref_images:

:mod:`neuromaps_mouse.images` - Image and surface handling
----------------------------------------------------------
.. automodule:: neuromaps_mouse.images
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps_mouse.images

Functions to load the images and surfaces

.. autosummary::
   :template: function.rst
   :toctree: generated/

   load_region_data
   load_image_data

.. _ref_plotting:

:mod:`neuromaps_mouse.plotting` - Plotting functions
----------------------------------------------------
.. automodule:: neuromaps_mouse.plotting
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps_mouse.plotting

.. autosummary::
   :template: function.rst
   :toctree: generated/

   plot_allenccfv3_ortho
   plot_allenccfv3_ortho_asym
   plot_allenccfv3_lightbox
   plot_allenccfv3_3d

.. _ref_resampling:

:mod:`neuromaps_mouse.resampling` - Resampling workflows
--------------------------------------------------------
.. automodule:: neuromaps_mouse.resampling
    :no-members:
    :no-inherited-members:

.. currentmodule:: neuromaps_mouse.resampling

.. autosummary::
    :template: function.rst
    :toctree: generated/

    query_structure_graph_allenccfv3
    get_feature_allenccfv3
    align_structures_allenccfv3
    match_structures_fuzzy_allenccfv3
    visualize_structure_alignment_allenccfv3

.. _ref_stats:

:mod:`neuromaps_mouse.stats` - Statistical functions
----------------------------------------------------
.. automodule:: neuromaps_mouse.stats
    :no-members:
    :no-inherited-members:

.. currentmodule:: neuromaps_mouse.stats

.. autosummary::
    :template: function.rst
    :toctree: generated/

    correlation

.. _ref_transforms:

:mod:`neuromaps_mouse.transforms` - Transformations between spaces
------------------------------------------------------------------
.. automodule:: neuromaps_mouse.transforms
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps_mouse.transforms

.. autosummary::
   :template: function.rst
   :toctree: generated/

   allenccfv3_to_allenccfv3