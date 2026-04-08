"""Functions for resampling and aligning structures."""

from pathlib import Path
import subprocess
import pandas as pd
import shutil
from neuromaps_mouse.datasets import fetch_allenccfv3


def query_structure_graph_allenccfv3(
    data, in_col="acronym", out_col="all", data_dir=None, verbose=1
):
    """Query the Allen CCFv3 structure graph.

    Parameters
    ----------
    data : array-like
        Input values to query (e.g., region acronyms or IDs).
    in_col : str, optional
        Column to index by. Default is 'acronym'.
    out_col : str or list of str, optional
        Column(s) to return. Use 'all' to return all columns. Default is 'all'.
    data_dir : str or Path, optional
        Base data directory. If None, uses the default. Default is None.
    verbose : int, optional
        Verbosity level. Default is 1.

    Returns
    -------
    pandas.DataFrame or pandas.Series
        Queried structure graph data.
    """
    # this directly returns the dataframe by indexing, so no none/null input
    df_struct = pd.read_csv(
        fetch_allenccfv3(
            which="structure-graph-csv", data_dir=data_dir, verbose=verbose
        )
    )
    if out_col == "all":
        return df_struct.set_index(in_col).loc[data, :].reset_index()
    else:
        return df_struct.set_index(in_col).loc[data, :].reset_index()[out_col]


def get_feature_allenccfv3(
    data, in_col="acronym", out_col="id", data_dir=None, verbose=1
):
    """Get a feature value for each region from the Allen CCFv3 structure graph.

    Unlike ``query_structure_graph_allenccfv3``, this function accepts None/NaN
    values and returns None for those entries.

    Parameters
    ----------
    data : array-like
        Input values (may include None/NaN).
    in_col : str, optional
        Column to index by. Default is 'acronym'.
    out_col : str, optional
        Column to return values from. Default is 'id'.
    data_dir : str or Path, optional
        Base data directory. If None, uses the default. Default is None.
    verbose : int, optional
        Verbosity level. Default is 1.

    Returns
    -------
    list
        Feature values, with None for any None/NaN inputs.
    """
    # this allows none/null input and returns a list
    df_struct = pd.read_csv(
        fetch_allenccfv3(
            which="structure-graph-csv", data_dir=data_dir, verbose=verbose
        )
    ).set_index(in_col)
    out_values = []
    for value in data:
        if pd.isna(value):  # or value is None:
            out_values.append(None)
        else:
            out_values.append(df_struct.loc[value, out_col])
    return out_values


def _get_nearest_ancestor_region_allenccfv3(
    source_structure_id_paths, target_region_ids, include_self=True
):
    matched_region_ids = []
    for p in source_structure_id_paths:
        if p is None:
            matched_region_ids.append(None)
            continue
        if include_self:
            p_list = list(map(int, p.split("/")[2:-1]))[
                ::-1
            ]  # reversed to get the nearest
        else:
            p_list = list(map(int, p.split("/")[2:-2]))[::-1]
        # print(p_list, target_region_ids)
        p_in_target = [_ in target_region_ids for _ in p_list]
        if any(p_in_target):
            _matched_id = p_list[p_in_target.index(True)]  # first match (nearest)
            matched_region_ids.append(_matched_id)
        else:
            # print(p)
            matched_region_ids.append(None)
    # print(matched_region_ids)
    return matched_region_ids


def _get_nearest_descendant_region_allenccfv3(
    source_region_ids, target_structure_id_paths, include_self=True
):
    matched_region_ids = []

    if include_self:
        tp_list = [
            list(map(int, tp.split("/")[2:-1])) for tp in target_structure_id_paths
        ]
    else:
        tp_list = [
            list(map(int, tp.split("/")[2:-2])) for tp in target_structure_id_paths
        ]

    for p in source_region_ids:
        if p is None:
            matched_region_ids.append([])
            continue
        p_in_tp = [_[-1] for _ in tp_list if p in _]

        matched_region_ids.append(p_in_tp)

    return matched_region_ids


def align_structures_allenccfv3(acronyms_fixed, acronyms_moving, debug=False):
    """Align moving structures to fixed structures via ancestor matching.

    For each region in ``acronyms_moving``, finds its nearest ancestor that
    exists in ``acronyms_fixed``.

    Parameters
    ----------
    acronyms_fixed : array-like of str
        Target region acronyms (the fixed reference set).
    acronyms_moving : array-like of str
        Source region acronyms to align to the fixed set.
    debug : bool, optional
        If True, also compute descendant mappings and add them to the
        returned DataFrame. Default is False.

    Returns
    -------
    pandas.DataFrame
        DataFrame for moving regions with an added 'id_ancestor_fixed' column.
    """
    df_fixed = query_structure_graph_allenccfv3(
        acronyms_fixed,
        in_col="acronym",
        out_col=["acronym", "id", "structure_id_path"],
        verbose=0,
    )
    df_moving = query_structure_graph_allenccfv3(
        acronyms_moving,
        in_col="acronym",
        out_col=["acronym", "id", "structure_id_path"],
        verbose=0,
    )

    df_moving["id_ancestor_fixed"] = _get_nearest_ancestor_region_allenccfv3(
        df_moving["structure_id_path"].to_list(),
        df_fixed["id"].to_list(),
        include_self=True,
    )
    df_moving["id_ancestor_fixed"] = df_moving["id_ancestor_fixed"].astype("Int64")

    if debug:
        df_moving["id_ancestor_fixed_acronym"] = get_feature_allenccfv3(
            df_moving["id_ancestor_fixed"].tolist(),
            in_col="id",
            out_col="acronym",
            verbose=0,
        )
        # also get descendant
        df_moving["id_descendant_fixed"] = _get_nearest_descendant_region_allenccfv3(
            df_moving["id"].tolist(),
            df_fixed["structure_id_path"].tolist(),
            include_self=True,
        )
        df_moving["id_descendant_fixed_acronym"] = df_moving.apply(
            lambda x: get_feature_allenccfv3(
                x["id_descendant_fixed"], in_col="id", out_col="acronym", verbose=0
            )
            if len(["id_descendant_fixed"]) > 0
            else [],
            axis=1,
        )

    return df_moving


def match_structures_fuzzy_allenccfv3():
    """Match structures using fuzzy string matching."""
    pass


def visualize_structure_alignment_allenccfv3(
    acronyms_fixed, acronyms_moving, save_path=Path("./"), save_name="graphviz"
):
    """Visualize the alignment between two sets of brain structures as a graph.

    Generates a Graphviz SVG diagram showing the hierarchical relationship
    between fixed and moving region sets. Requires Graphviz to be installed.

    Parameters
    ----------
    acronyms_fixed : array-like of str
        Fixed (reference) region acronyms, marked with a stop symbol in the graph.
    acronyms_moving : array-like of str
        Moving (source) region acronyms, marked with an arrow in the graph.
    save_path : str or Path, optional
        Directory to save output files. Default is current directory.
    save_name : str, optional
        Base filename (without extension) for the output files. Default is 'graphviz'.
    """
    graphviz_path = shutil.which("dot")
    if graphviz_path is None:
        raise ValueError("Graphviz executable not found, please install graphviz")

    if not isinstance(save_path, Path):
        save_path = Path(save_path)

    struct_csv = pd.read_csv(fetch_allenccfv3(which="structure-graph-csv"))

    df_fixed = query_structure_graph_allenccfv3(
        acronyms_fixed,
        in_col="acronym",
        out_col=["acronym", "id", "structure_id_path"],
        verbose=0,
    )
    df_moving = query_structure_graph_allenccfv3(
        acronyms_moving,
        in_col="acronym",
        out_col=["acronym", "id", "structure_id_path"],
        verbose=0,
    )

    all_regions = [
        _.strip("/").split("/")
        for _ in df_fixed["structure_id_path"].tolist()
        + df_moving["structure_id_path"].tolist()
    ]
    all_regions = list(
        map(int, list(set([r for regions in all_regions for r in regions])))
    )

    struct_csv_filtered = struct_csv[struct_csv["id"].isin(all_regions)]
    struct_csv_filtered["parent_structure_id"] = struct_csv_filtered[
        "parent_structure_id"
    ].astype("Int64")

    graphviz_script = [
        "digraph G {",
        'rankdir="LR";',
        'node [shape=box, fontname="Arial", fontsize=12];',
        'edge [fontname="Arial", fontsize=10];',
    ]

    for _i, row in struct_csv_filtered.iterrows():
        curr_label = row["acronym"]
        if row["acronym"] in df_fixed["acronym"].tolist():
            curr_label += " ⏹️"
        if row["acronym"] in df_moving["acronym"].tolist():
            curr_label += " ⬅️"
        graphviz_script.append(f'{row["id"]} [label="{curr_label}"]')

    for _i, row in struct_csv_filtered.iterrows():
        if row["acronym"] == "root":
            continue
        graphviz_script.append(f"    {row['parent_structure_id']} -> {row['id']}")
    graphviz_script += ["}"]

    with open(save_path / f"{save_name}.txt", "w", encoding="utf-8") as f:
        f.writelines("\n".join(graphviz_script))

    subprocess.run(
        [
            graphviz_path,
            "-Tsvg",
            f"{save_path / save_name}.txt",
            "-o",
            f"{save_path / save_name}.svg",
        ]
    )
