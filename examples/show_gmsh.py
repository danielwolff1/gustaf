"""Example showing the import of a gmsh file via meshio.

This example shows how a gmsh file can be imported into gustaf with the meshio
io module.
"""
import pathlib

import load_sample_file

from gustaf import io

if __name__ == "__main__":
    mesh_file_tri = pathlib.Path("faces/tri/2DChannelTria.msh")
    mesh_file_quad = pathlib.Path("faces/quad/2DChannelQuad.msh")

    base_samples_path = pathlib.Path(__file__).parent / "samples"
    load_sample_file.load_sample_file(str(mesh_file_tri))
    load_sample_file.load_sample_file(str(mesh_file_quad))

    # load the .msh file directly with the correct io module (meshio)
    loaded_mesh_tri = io.meshio.load(base_samples_path / mesh_file_tri)

    loaded_mesh_tri.show()

    # load the .msh file directly with the correct io module (meshio)
    loaded_mesh_quad = io.meshio.load(base_samples_path / mesh_file_quad)

    loaded_mesh_quad.show()

    # load the .msh file with the default load function which needs to find out
    # it self which module is the correct one.
    loaded_mesh_default = io.load(base_samples_path / mesh_file_tri)

    loaded_mesh_default.show()
