.. _installation_setup:

----------------------
Installation and setup
----------------------

.. _installation_requirements:

Requirements
============

This package requires Python >= 3.8.

.. _installation_basic:

Basic installation
==================

Assuming you have the correct version of Python installed, you can install
`neuromaps-mouse` by opening a terminal and running the following:

.. code-block:: bash

   git clone https://github.com/netneurolab/neuromaps-mouse.git
   cd neuromaps-mouse
   pip install .

.. _installation_optional:

Optional dependencies
=====================

Some functionality in neuromaps-mouse requires additional dependencies.

Pyvista
-------

Pyvista is the plotting library used in the package for 3D surface visualization.
This will allow you to use functions like

* :func:`neuromaps_mouse.plotting.plot_allenccfv3_3d`

You will need a working Pyvista installation. We recommend using a clean conda
environment and installing Pyvista using the following commands:

.. code-block:: bash

   conda create -n plotting python=3.12
   conda activate plotting
   conda install -c conda-forge pyvista

Pyvista is actively maintained and generally installs without issues. Please
also check out their `detailed installation guide <https://docs.pyvista.org/getting-started/installation.html>`_.

Pyvista is built on top of VTK, which supports multiple OpenGL window backends
and you can choose one that fits your environment (see the `VTK runtime settings <https://docs.vtk.org/en/latest/advanced/runtime_settings.html>`_):

* **X11**: standard Linux display server (requires an active X server)
* **Win32**: native Windows OpenGL context
* **EGL**: offscreen GPU context (good for headless servers with GPUs)
* **OSMesa**: CPU-based software rendering (good for headless servers without GPUs)

For example, on a headless Linux server without a GPU you can request OSMesa by
setting the backend before importing PyVista/VTK:

.. code-block:: python

   import os
   os.environ["VTK_DEFAULT_OPENGL_WINDOW"] = "vtkOSOpenGLRenderWindow"
