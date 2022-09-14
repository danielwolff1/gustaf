"""gustaf/gustaf/edges.py

Edges. Also known as 
"""

import numpy as np

from gustaf import settings
from gustaf import utils
from gustaf import helpers
from gustaf.vertices import Vertices


class Edges(Vertices):

    kind = "edge"

    __slots__ = (
        "_edges",
        "_const_edges",
    )

    def __init__(
            self,
            vertices=None,
            edges=None,
            elements=None,
    ):
        """
        Edges. It has vertices and edges. Also known as lines.

        Parameters
        -----------
        vertices: (n, d) np.ndarray
        edges: (n, 2) np.ndarray
        """
        super().__init__(vertices=vertices)

        if edges is not None:
            self.edges = edges

        elif elements is not None:
            self.edges = elements

    @property
    def edges(self):
        """
        Returns edges. If edges is not its original property

        Parameters
        -----------
        None

        Returns
        --------
        edges: (n, 2) np.ndarray
        """
        self._logd("returning edges")
        return self._edges

    @edges.setter
    def edges(self, es):
        """
        Edges setter. Similar to vertices, this is a tracked array.

        Parameters
        -----------
        es: (n, 2) np.ndarray

        Returns
        --------
        None
        """
        self._logd("setting edges")
        self._edges = helpers.data.make_tracked_array(
            es,
            settings.INT_DTYPE
        )
        # same, but non-writeable view of tracked array
        self._const_edges = self._edges.view()
        self._const_edges.flags.writeable = False

    @property
    def const_edges(self):
        """
        Returns non-writeable version of edges.

        Parameters
        -----------
        None

        Returns
        --------
        const_edges (n, 2) np.ndarray
        """
        return self._const_edges

    @property
    def whatami(self):
        """
        whatami?

        Parameters
        -----------
        None

        Returns
        --------
        whatami: str
        """
        return "edges"

    @helpers.data.ComputedMeshData.depends_on(["elements"])
    def sorted_edges(self):
        """
        Sort edges along axis=1.

        Parameters
        -----------
        None

        Returns
        --------
        edges_sorted: (n_edges, 2) np.ndarray
        """
        edges = self._get_attr("edges")

        return np.sort(edges, axis=1)

    @helpers.data.ComputedMeshData.depends_on(["elements"])
    def unique_edges(self):
        """
        Returns a named tuple of unique edge info.
        Info includes unique values, ids of unique edges, inverse ids,
        count of each unique values. 

        Parameters
        -----------
        None

        Returns
        --------
        unique_info: Unique2DIntegers
          valid attributes are {values, ids, inverse, counts}
        """
        unique_info = utils.connec.sorted_unique(
            self.sorted_edges(),
            sorted_=True
        )

        edges = self._get_attr("edges")

        # tuple is not assignable, but entry is mutable...
        unique_info.values[:] = edges[unique_info.ids]

        return unique_info

    @property
    def elements(self):
        """
        Returns current connectivity. A short cut in FE friendly term.
        Elements mean different things for different classes:
          Vertices -> vertices
          Edges -> edges
          Faces -> faces
          Volumes -> volumes

        Parameters
        -----------
        None

        Returns
        --------
        elements: (n, d) np.ndarray
          int. iff elements=None
        """
        elem_name = type(self).__qualname__.lower()
        self._logd(f"returning {elem_name}")

        return getattr(self, elem_name)

    @elements.setter
    def elements(self, elems):
        """
        Calls corresponding connectivity setter.
        A short cut in FEM friendly term.
          Vertices -> vertices
          Edges -> edges
          Faces -> faces
          Volumes -> volumes

        Parameters
        -----------
        elems: (n, d) np.ndarray

        Returns
        --------
        None
        """
        # naming rule in gustaf
        elem_name = type(self).__qualname__.lower()
        self._logd(f"seting {elem_name}'s connectivity.")

        return setattr(self, elem_name, elems)

    @property
    def const_elements(self):
        """
        Returns non-mutable version of elements

        Parameters
        -----------
        None

        Returns
        --------
        non_mutable_elements: (n, d) TrackedArray
        """
        self._logd("returning const_elements")
        return getattr(self, "const_" + type(self).__qualname__.lower())

    @helpers.data.ComputedMeshData.depends_on(["vertices", "elements"])
    def centers(self):
        """
        Center of elements.

        Parameters
        -----------
        None

        Returns
        --------
        centers: (n_elements, d) np.ndarray
        """
        self._logd("computing centers")

        return self.const_vertices[self.const_elements].mean(axis=1)

    @helpers.data.ComputedMeshData.depends_on(["vertices", "elements"])
    def referenced_vertices(self,):
        """
        Returns mask of referenced vertices.

        Parameters
        -----------
        None

        Returns
        --------
        referenced: (n,) np.ndarray
        """
        referenced = np.zeros(len(self.const_vertices), dtype=bool)
        referenced[self.const_elements] = True

        return referenced

    def remove_unreferenced_vertices(self):
        """
        Remove unreferenced vertices.
        Adapted from `github.com/mikedh/trimesh`

        Parameters
        -----------
        None

        Returns
        --------
        new_self: type(self)
        """
        referenced = self.referenced_vertices()

        inverse = np.zeros(len(self.vertices), dtype=settings.INT_DTYPE)
        inverse[referenced] = np.arange(referenced.sum())

        return self.update_vertices(
            mask=referenced,
            inverse=inverse,
        )

    def update_elements(self, mask):
        """
        Similar to update_vertices, but for elements.

        Parameters
        -----------
        inplace: bool

        Returns
        --------
        new_self: type(self)
        """
        self.elements = self.elements[mask]

        return self.elements.remove_unreferenced_vertices()

    def update_edges(self, *args, **kwargs):
        """
        Alias to update_elements.
        """
        return self.update_elements(*args, **kwargs)

    def dashed(self, spacing=None):
        """
        Turn edges into dashed edges(=lines).
        Given spacing, it will try to chop edges as close to it as possible.
        Pattern should look:

        ``dashed edges``

        .. code-block::

             o--------o    o--------o    o--------o
             |<------>|             |<-->|
                (chop length)         (chop length / 2)

        Parameters
        -----------
        spacing: float
          Default is None and it will use self.bounds_diagonal_norm() / 50

        Returns
        --------
        dashing_edges: Edges
        """
        if self.kind != "edge":
            raise NotImplementedError("dashed is only for edges.")

        if spacing is None:
            # apply "automatic" spacing
            spacing = self.bounds_diagonal_norm() / 50

        v0s = self.vertices[self.edges[:,0]]
        v1s = self.vertices[self.edges[:,1]]

        distances = np.linalg.norm(v0s - v1s, axis=1)
        linspaces = (((distances // (spacing * 1.5)) + 1) * 3).astype(np.int32)

        # chop vertices!
        new_vs = []
        for v0, v1, lins in zip(v0s, v1s, linspaces):
            new_vs.append(np.linspace(v0, v1, lins))

        # we need all choped vertices.
        # there might be duplicating vertices. you can use merge_vertices
        new_vs = np.vstack(new_vs)
        # all mid points are explicitly defined, but they aren't required
        # so, rm. 
        mask = np.ones(len(new_vs), dtype=bool)
        mask[1::3] = False
        new_vs = new_vs[mask]

        # prepare edges
        tmp_es = utils.connec.range_to_edges((0, len(new_vs)), closed=False)
        new_es = tmp_es[::2]

        return Edges(vertices=new_vs, edges=new_es)

    def shrink(self, ratio=.8, map_vertexdata=True):
        """
        Returns shrunk elements.

        Parameters
        -----------
        ratio: float
          Default is 0.8
        map_vertexdata: bool
          Default is True. Maps all vertexdata.

        Returns
        --------
        s_elements: Elements
          shrunk elements
        """
        elements = self.const_elements
        vs = np.vstack(self.vertices[elements])
        es = np.arange(len(vs))

        nodes_per_element = elements.shape[1]
        es = es.reshape(-1, nodes_per_element)

        mids = np.repeat(self.centers(), nodes_per_element, axis=0)

        vs -= mids
        vs *= ratio
        vs += mids

        s_elements = type(self)(vertices=vs, elements=es)

        if map_vertexdata:
            elements_flat = elements.ravel()
            for key, value in self.vertexdata.items():
                s_elements.vertexdata[key] = value[elements_flat]

            # probably wanna take visulation options too
            s_elements.vis_dict = self.vis_dict

        return s_elements

    def tovertices(self):
        """
        Returns Vertices obj.

        Parameters
        -----------
        None

        Returns
        --------
        vertices: Vertices
        """
        return Vertices(self.vertices)

    def _get_attr(self, attr):
        """
        Internal function to get attribute that maybe property or callable.
        Some properties are replaced by callable in subclasses as it may depend
        on other properties of subclass.

        Parameters
        -----------
        attr: str

        Returns
        --------
        attrib: Any
        """
        attrib = getattr(self, attr)

        return attrib() if callable(attrib) else attrib


