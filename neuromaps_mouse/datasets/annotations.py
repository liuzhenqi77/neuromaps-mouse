"""Functions for annotation data fetching and loading."""

from neuromaps_mouse.datasets.utils import (
    MOUSEMAPS_ANNOTS,
    MOUSEMAPS_ANNOTS_META,
    get_data_dir,
    fetch_files,
    _annot_full_to_tuple,
    _filter_annots_by_keys,
    _match_annots_by_tuple
)


def get_annotation_dir(data_dir=None):
    """Get the annotations data directory path.

    Retrieves the path to the directory where annotation files are stored.
    If no data directory is specified, uses the default neuromaps-mouse data directory.

    Parameters
    ----------
    data_dir : str or Path, optional
        Path to the base neuromaps-mouse data directory. If None, uses the default
        directory determined by `get_data_dir()`. Default is None.

    Returns
    -------
    pathlib.Path
        Path to the annotations subdirectory.

    See Also
    --------
    neuromaps_mouse.datasets.get_data_dir : Get the base neuromaps-mouse data directory.

    Examples
    --------
    >>> annot_dir = get_annotation_dir()
    >>> print(annot_dir)
    /home/user/neuromaps-mouse-data/annotations

    >>> custom_annot_dir = get_annotation_dir(data_dir='/custom/data')
    >>> print(custom_annot_dir)
    /custom/data/annotations
    """
    data_dir = get_data_dir(data_dir=data_dir)
    return data_dir / "annotations"


def available_annotations(
    source=None, desc=None, space=None, res=None, tag=None, format=None
):
    """List available annotations with optional filtering.

    Returns a list of available annotation datasets that can be fetched,
    optionally filtered by various metadata attributes.

    See :doc: `/listofmaps` for details on available annotations.

    Parameters
    ----------
    source : str, optional
        Filter by data source. If 'all', returns all
        available annotations without filtering. Default is None.
    desc : str, optional
        Filter by description. Default is None.
    space : str, optional
        Filter by anatomical space. Default is None.
    res : int or float, optional
        Filter by resolution. Default is None.
    tag : str, optional
        Filter by annotation tag or keyword. Default is None.
    format : str, optional
        Filter by file format. Default is None.

    Returns
    -------
    list of tuple
        List of tuples representing available annotations. Each tuple contains
        annotation metadata (source, desc, space, res).
        If source='all', returns all available annotations.

    See Also
    --------
    neuromaps_mouse.datasets.fetch_annotation : Download and load annotation files.

    Examples
    --------
    >>> # Get all available annotations
    >>> all_annots = available_annotations(source='all')
    >>> print(f"Found {len(all_annots)} annotations")

    >>> # Filter by specific source
    >>> lein2006amba = available_annotations(source='lein2006amba')

    >>> # Filter by multiple criteria
    >>> annots = available_annotations(source='lein2006amba', desc='sagittalenergy')
    """
    if source == "all":
        return _annot_full_to_tuple(MOUSEMAPS_ANNOTS)
    else:
        return _annot_full_to_tuple(_filter_annots_by_keys(locals()))


def fetch_annotation(annotations, data_dir=None, return_single=False, verbose=1):
    """Download and cache annotation files.

    Fetches annotation data files from the neuromaps-mouse repository and caches them
    locally. Also downloads related metadata files such as region mappings.

    Parameters
    ----------
    annotations : str, tuple, or list of str/tuple
        Annotation(s) to fetch. Can be specified as:
        - A single annotation tuple from `available_annotations()`
        - A list of annotation tuples
        - A string identifier for a specific annotation
        - A list of string identifiers
    data_dir : str or Path, optional
        Path to the base neuromaps-mouse data directory where files will be cached.
        If None, uses the default directory. Default is None.
    return_single : bool, optional
        If True and only one annotation is requested, returns a tuple of
        (annotation_id, file_path). If False, always returns lists.
        Default is False.
    verbose : int, optional
        Verbosity level for download progress (0=silent, 1=verbose).
        Default is 1.

    Returns
    -------
    annotations : list of str or str
        Input annotation identifier(s). Returned as single string if
        return_single=True and one annotation was requested.
    file_paths : list of str or str
        Path(s) to the downloaded annotation file(s). Returned as single
        string if return_single=True and one annotation was requested.

    Notes
    -----
    This function automatically downloads related metadata files (such as
    regionmapping files) for each annotation source. Files are cached locally
    to avoid re-downloading on subsequent calls.

    See Also
    --------
    neuromaps_mouse.datasets.available_annotations : List available annotations.
    neuromaps_mouse.datasets.get_annotation_dir : Get the annotations directory path.

    Examples
    --------
    >>> # Fetch a single annotation
    >>> annot_id, annot_path = fetch_annotation(
    ...     ('lein2006amba', 'sagittalenergy', 'allenccfv3', 'region'),
    ...     return_single=True
    ... )
    >>> print(f"Downloaded to: {annot_path}")

    >>> # Fetch multiple annotations
    >>> annot_ids, annot_paths = fetch_annotation([
    ...     ('lein2006amba', 'sagittalenergy', 'allenccfv3', 'region'),
    ...     ('yao2023abca', 'divimean', 'allenccfv3', 'region')
    ... ])
    """
    data_dir = get_data_dir(data_dir=data_dir)

    if not isinstance(annotations, list):
        annotations = [annotations]
    annotations_full = _match_annots_by_tuple(annotations)

    targ_fname_list = fetch_files(
        annotations_full, file_type="annotations", data_dir=data_dir, verbose=verbose
    )

    # also download the related aux files, regionmapping, for now
    source_list = list(set([annot["source"] for annot in annotations_full]))

    if verbose:
        print(f"Downloading regionmapping files for {source_list}")
    targ_annot_meta_fname_list = _fetch_annotation_meta_files(
        list(set([annot["source"] for annot in annotations_full])),
        which="regionmapping",
        data_dir=data_dir,
        verbose=verbose,
    )

    if len(annotations_full) == 1 and return_single:
        return annotations[0], targ_fname_list[0]
    else:
        return annotations, targ_fname_list


def _fetch_annotation_meta_files(
    sources, which="regionmapping", data_dir=None, verbose=1
):
    data_dir = get_data_dir(data_dir=data_dir)

    if not isinstance(sources, list):
        sources = [sources]

    filtered_annot_meta_list = [
        annot_meta["aux_files"][which]
        for annot_meta in MOUSEMAPS_ANNOTS_META
        if annot_meta["source"] in sources
    ]
    filtered_annot_meta_list = [
        item
        for sublist in filtered_annot_meta_list
        for item in (
            sublist if isinstance(sublist, list) else [sublist]
        )
    ]

    targ_fname_list = fetch_files(
        filtered_annot_meta_list,
        file_type="annotations-meta",
        data_dir=data_dir,
        verbose=verbose,
    )

    return targ_fname_list
