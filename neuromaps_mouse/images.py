"""Functions for image data fetching and loading."""


def parcellate_image(image, annotation, **kwargs):
    """Parcellate an image using an annotation.

    Parameters
    ----------
    image :
        Input image data.
    annotation :
        Annotation to use for parcellation.
    **kwargs :
        Additional keyword arguments.

    Returns
    -------
    parcellated :
        Parcellated image data.
    """
    pass


def register_image(image, target, **kwargs):
    """Register an image to a target space.

    Parameters
    ----------
    image :
        Input image data.
    target :
        Target space or image for registration.
    **kwargs :
        Additional keyword arguments.

    Returns
    -------
    registered :
        Registered image data.
    """
    pass


def transform_image(image, transform, **kwargs):
    """Transform an image using a spatial transform.

    Parameters
    ----------
    image :
        Input image data.
    transform :
        Transform to apply.
    **kwargs :
        Additional keyword arguments.

    Returns
    -------
    transformed :
        Transformed image data.
    """
    pass
