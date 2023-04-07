"""Python bindings to GEMMI - a library used in macromolecular
crystallography and related fields"""
from __future__ import annotations

import pathlib
import typing

import gemmi
import numpy

_Shape = ...

__all__ = ...

class Addends:
    def add_cl_fprime(self, energy: float) -> None: ...
    def clear(self) -> None: ...
    def get(self, arg0: Element) -> float: ...
    def set(self, arg0: Element, arg1: float) -> None: ...
    def subtract_z(self, except_hydrogen: bool = False) -> None: ...

class AlignmentResult:
    def add_gaps(self, s: str, which: int) -> str: ...
    def calculate_identity(self, which: int = 0) -> float: ...
    def cigar_str(self) -> str: ...
    def formatted(self, arg0: str, arg1: str) -> str: ...
    @property
    def match_count(self) -> int:
        """
        :type: int
        """
    @property
    def match_string(self) -> str:
        """
        :type: str
        """
    @property
    def score(self) -> int:
        """
        :type: int
        """

class AlignmentScoring:
    def __init__(self) -> None: ...
    @property
    def gape(self) -> int:
        """
        :type: int
        """
    @gape.setter
    def gape(self, arg0: int) -> None:
        pass
    @property
    def gapo(self) -> int:
        """
        :type: int
        """
    @gapo.setter
    def gapo(self, arg0: int) -> None:
        pass
    @property
    def match(self) -> int:
        """
        :type: int
        """
    @match.setter
    def match(self, arg0: int) -> None:
        pass
    @property
    def mismatch(self) -> int:
        """
        :type: int
        """
    @mismatch.setter
    def mismatch(self, arg0: int) -> None:
        pass

class Assembly:
    class Gen:
        def __init__(self) -> None: ...
        @property
        def chains(self) -> list[str]:
            """
            :type: typing.List[str]
            """
        @chains.setter
        def chains(self, arg0: list[str]) -> None:
            pass
        @property
        def operators(self) -> Assembly.OperatorList:
            """
            :type: Assembly.OperatorList
            """
        @property
        def subchains(self) -> list[str]:
            """
            :type: typing.List[str]
            """
        @subchains.setter
        def subchains(self, arg0: list[str]) -> None:
            pass

    class GenList:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Assembly.Gen:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Assembly.GenList: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Assembly.GenList) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator[Assembly.Gen]: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Assembly.Gen) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Assembly.GenList) -> None: ...
        def append(self, x: Assembly.Gen) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Assembly.GenList) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Assembly.Gen) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Assembly.Gen:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Assembly.Gen: ...

    class Operator:
        def __init__(self) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @name.setter
        def name(self, arg0: str) -> None:
            pass
        @property
        def transform(self) -> Transform:
            """
            :type: Transform
            """
        @transform.setter
        def transform(self, arg0: Transform) -> None:
            pass
        @property
        def type(self) -> str:
            """
            :type: str
            """
        @type.setter
        def type(self, arg0: str) -> None:
            pass

    class OperatorList:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Assembly.Operator:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Assembly.OperatorList: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Assembly.OperatorList) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator[Assembly.Operator]: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Assembly.Operator) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Assembly.OperatorList) -> None: ...
        def append(self, x: Assembly.Operator) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Assembly.OperatorList) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Assembly.Operator) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Assembly.Operator:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Assembly.Operator: ...

    def __init__(self, arg0: str) -> None: ...
    @property
    def author_determined(self) -> bool:
        """
        :type: bool
        """
    @author_determined.setter
    def author_determined(self, arg0: bool) -> None:
        pass
    @property
    def generators(self) -> Assembly.GenList:
        """
        :type: Assembly.GenList
        """
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def oligomeric_details(self) -> str:
        """
        :type: str
        """
    @oligomeric_details.setter
    def oligomeric_details(self, arg0: str) -> None:
        pass
    @property
    def software_determined(self) -> bool:
        """
        :type: bool
        """
    @software_determined.setter
    def software_determined(self, arg0: bool) -> None:
        pass
    @property
    def special_kind(self) -> AssemblySpecialKind:
        """
        :type: AssemblySpecialKind
        """
    @special_kind.setter
    def special_kind(self, arg0: AssemblySpecialKind) -> None:
        pass

class AssemblyList:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Assembly:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> AssemblyList: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: AssemblyList) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator[AssemblyList]: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Assembly) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: AssemblyList) -> None: ...
    def append(self, x: Assembly) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: AssemblyList) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Assembly) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Assembly:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Assembly: ...

class AssemblySpecialKind:
    """
    Members:

      NA

      CompleteIcosahedral

      RepresentativeHelical

      CompletePoint
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    CompleteIcosahedral: gemmi.AssemblySpecialKind  # value = <AssemblySpecialKind.CompleteIcosahedral: 1>
    CompletePoint: gemmi.AssemblySpecialKind  # value = <AssemblySpecialKind.CompletePoint: 3>
    NA: gemmi.AssemblySpecialKind  # value = <AssemblySpecialKind.NA: 0>
    RepresentativeHelical: gemmi.AssemblySpecialKind  # value = <AssemblySpecialKind.RepresentativeHelical: 2>

class Asu:
    """
    Members:

      Same

      Different

      Any
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Any: gemmi.Asu  # value = <Asu.Any: 2>
    Different: gemmi.Asu  # value = <Asu.Different: 1>
    Same: gemmi.Asu  # value = <Asu.Same: 0>

class AsuBrick:
    def get_extent(self) -> FractionalBox: ...
    def str(self) -> str: ...
    @property
    def incl(self) -> list[bool]:
        """
        :type: typing.List[bool]
        """
    @property
    def size(self) -> list[int]:
        """
        :type: typing.List[int]
        """

class Atom:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def b_eq(self) -> float: ...
    def clone(self) -> Atom: ...
    def has_altloc(self) -> bool: ...
    def is_hydrogen(self) -> bool: ...
    def padded_name(self) -> str: ...
    @property
    def altloc(self) -> str:
        """
        :type: str
        """
    @altloc.setter
    def altloc(self, arg0: str) -> None:
        pass
    @property
    def aniso(self) -> SMat33f:
        """
        :type: SMat33f
        """
    @aniso.setter
    def aniso(self, arg0: SMat33f) -> None:
        pass
    @property
    def b_iso(self) -> float:
        """
        :type: float
        """
    @b_iso.setter
    def b_iso(self, arg0: float) -> None:
        pass
    @property
    def calc_flag(self) -> CalcFlag:
        """
        :type: CalcFlag
        """
    @calc_flag.setter
    def calc_flag(self, arg0: CalcFlag) -> None:
        pass
    @property
    def charge(self) -> int:
        """
        :type: int
        """
    @charge.setter
    def charge(self, arg0: int) -> None:
        pass
    @property
    def element(self) -> Element:
        """
        :type: Element
        """
    @element.setter
    def element(self, arg0: Element) -> None:
        pass
    @property
    def flag(self) -> str:
        """
        :type: str
        """
    @flag.setter
    def flag(self, arg0: str) -> None:
        pass
    @property
    def fraction(self) -> float:
        """
        :type: float
        """
    @fraction.setter
    def fraction(self, arg0: float) -> None:
        pass
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def occ(self) -> float:
        """
        :type: float
        """
    @occ.setter
    def occ(self, arg0: float) -> None:
        pass
    @property
    def pos(self) -> Position:
        """
        :type: Position
        """
    @pos.setter
    def pos(self, arg0: Position) -> None:
        pass
    @property
    def serial(self) -> int:
        """
        :type: int
        """
    @serial.setter
    def serial(self, arg0: int) -> None:
        pass
    @property
    def tls_group_id(self) -> int:
        """
        :type: int
        """
    @tls_group_id.setter
    def tls_group_id(self, arg0: int) -> None:
        pass

class AtomAddress:
    def __eq__(self, arg0: AtomAddress) -> bool: ...
    def __getstate__(self) -> tuple: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, chain: str, seqid: SeqId, resname: str, atom: str, altloc: str = "\x00") -> None: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    def __str__(self) -> str: ...
    @property
    def altloc(self) -> str:
        """
        :type: str
        """
    @altloc.setter
    def altloc(self, arg0: str) -> None:
        pass
    @property
    def atom_name(self) -> str:
        """
        :type: str
        """
    @atom_name.setter
    def atom_name(self, arg0: str) -> None:
        pass
    @property
    def chain_name(self) -> str:
        """
        :type: str
        """
    @chain_name.setter
    def chain_name(self, arg0: str) -> None:
        pass
    @property
    def res_id(self) -> ResidueId:
        """
        :type: ResidueId
        """
    @res_id.setter
    def res_id(self, arg0: ResidueId) -> None:
        pass
    __hash__ = None

class AtomGroup:
    def __bool__(self) -> bool: ...
    @typing.overload
    def __getitem__(self, altloc: str) -> Atom: ...
    @typing.overload
    def __getitem__(self, index: int) -> Atom: ...
    def __iter__(self) -> typing.Iterator[Atom]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def name(self) -> str: ...

class AtomicRadiiSet:
    """
    Members:

      VanDerWaals

      Cctbx

      Refmac

      Constant
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Cctbx: gemmi.AtomicRadiiSet  # value = <AtomicRadiiSet.Cctbx: 1>
    Constant: gemmi.AtomicRadiiSet  # value = <AtomicRadiiSet.Constant: 3>
    Refmac: gemmi.AtomicRadiiSet  # value = <AtomicRadiiSet.Refmac: 2>
    VanDerWaals: gemmi.AtomicRadiiSet  # value = <AtomicRadiiSet.VanDerWaals: 0>

class AxisOrder:
    """
    Members:

      Unknown

      XYZ

      ZYX
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Unknown: gemmi.AxisOrder  # value = <AxisOrder.Unknown: 0>
    XYZ: gemmi.AxisOrder  # value = <AxisOrder.XYZ: 1>
    ZYX: gemmi.AxisOrder  # value = <AxisOrder.ZYX: 2>

class BasicRefinementInfo:
    def __init__(self) -> None: ...
    @property
    def completeness(self) -> float:
        """
        :type: float
        """
    @completeness.setter
    def completeness(self, arg0: float) -> None:
        pass
    @property
    def r_all(self) -> float:
        """
        :type: float
        """
    @r_all.setter
    def r_all(self, arg0: float) -> None:
        pass
    @property
    def r_free(self) -> float:
        """
        :type: float
        """
    @r_free.setter
    def r_free(self, arg0: float) -> None:
        pass
    @property
    def r_work(self) -> float:
        """
        :type: float
        """
    @r_work.setter
    def r_work(self, arg0: float) -> None:
        pass
    @property
    def reflection_count(self) -> int:
        """
        :type: int
        """
    @reflection_count.setter
    def reflection_count(self, arg0: int) -> None:
        pass
    @property
    def resolution_high(self) -> float:
        """
        :type: float
        """
    @resolution_high.setter
    def resolution_high(self, arg0: float) -> None:
        pass
    @property
    def resolution_low(self) -> float:
        """
        :type: float
        """
    @resolution_low.setter
    def resolution_low(self, arg0: float) -> None:
        pass
    @property
    def rfree_set_count(self) -> int:
        """
        :type: int
        """
    @rfree_set_count.setter
    def rfree_set_count(self, arg0: int) -> None:
        pass

class Binner:
    class Method:
        """
        Members:

          EqualCount

          Dstar

          Dstar2

          Dstar3
        """

        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        Dstar: gemmi.Binner.Method  # value = <Method.Dstar: 1>
        Dstar2: gemmi.Binner.Method  # value = <Method.Dstar2: 2>
        Dstar3: gemmi.Binner.Method  # value = <Method.Dstar3: 3>
        EqualCount: gemmi.Binner.Method  # value = <Method.EqualCount: 0>
    def __init__(self) -> None: ...
    def dmax_of_bin(self, arg0: int) -> float: ...
    def dmin_of_bin(self, arg0: int) -> float: ...
    def get_bin(self, arg0: list[int]) -> int: ...
    @typing.overload
    def get_bins(self, arg0: Mtz) -> numpy.ndarray[numpy.int32]: ...
    @typing.overload
    def get_bins(self, arg0: ReflnBlock) -> numpy.ndarray[numpy.int32]: ...
    @typing.overload
    def get_bins(self, arg0: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.int32]: ...
    def get_bins_from_1_d2(self, arg0: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.int32]: ...
    @typing.overload
    def setup(self, nbins: int, method: Binner.Method, hkl: numpy.ndarray[numpy.int32], cell: UnitCell) -> int: ...
    @typing.overload
    def setup(self, nbins: int, method: Binner.Method, mtz: Mtz, cell: UnitCell = None) -> int: ...
    @typing.overload
    def setup(self, nbins: int, method: Binner.Method, r: ReflnBlock, cell: UnitCell = None) -> int: ...
    def setup_from_1_d2(
        self,
        nbins: int,
        method: Binner.Method,
        inv_d2: numpy.ndarray[numpy.float64],
        cell: UnitCell,
    ) -> int: ...
    @property
    def cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @cell.setter
    def cell(self, arg0: UnitCell) -> None:
        pass
    @property
    def limits(self) -> list[float]:
        """
        :type: typing.List[float]
        """
    @property
    def max_1_d2(self) -> float:
        """
        :type: float
        """
    @property
    def min_1_d2(self) -> float:
        """
        :type: float
        """
    @property
    def size(self) -> int:
        """
        :type: int
        """

class Blob:
    @property
    def centroid(self) -> Position:
        """
        :type: Position
        """
    @property
    def peak_pos(self) -> Position:
        """
        :type: Position
        """
    @property
    def peak_value(self) -> float:
        """
        :type: float
        """
    @property
    def score(self) -> float:
        """
        :type: float
        """
    @property
    def volume(self) -> float:
        """
        :type: float
        """

class BondIndex:
    def __init__(self, arg0: Model) -> None: ...
    def add_link(self, arg0: Atom, arg1: Atom, arg2: bool) -> None: ...
    def add_monomer_bonds(self, arg0: MonLib) -> None: ...
    def are_linked(self, arg0: Atom, arg1: Atom, arg2: bool) -> bool: ...
    def graph_distance(self, a: Atom, b: Atom, same_index: bool, max_distance: int = 4) -> int: ...

class BondType:
    """
    Members:

      Unspec

      Single

      Double

      Triple

      Aromatic

      Deloc

      Metal
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Aromatic: gemmi.BondType  # value = <BondType.Aromatic: 4>
    Deloc: gemmi.BondType  # value = <BondType.Deloc: 5>
    Double: gemmi.BondType  # value = <BondType.Double: 2>
    Metal: gemmi.BondType  # value = <BondType.Metal: 6>
    Single: gemmi.BondType  # value = <BondType.Single: 1>
    Triple: gemmi.BondType  # value = <BondType.Triple: 3>
    Unspec: gemmi.BondType  # value = <BondType.Unspec: 0>

class C4322Coef:
    def calculate_density_iso(self, r2: float, B: float) -> float: ...
    def calculate_sf(self, stol2: float) -> float: ...
    def get_coefs(self) -> list[float]: ...
    def set_coefs(self, arg0: list[float]) -> None: ...
    @property
    def a(self) -> list[float]:
        """
        :type: typing.List[float]
        """
    @property
    def b(self) -> list[float]:
        """
        :type: typing.List[float]
        """

class CRA:
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def atom_matches(self, arg0: AtomAddress) -> bool: ...
    @property
    def atom(self) -> Atom:
        """
        :type: Atom
        """
    @property
    def chain(self) -> Chain:
        """
        :type: Chain
        """
    @property
    def residue(self) -> Residue:
        """
        :type: Residue
        """

class CalcFlag:
    """
    Members:

      NotSet

      Determined

      Calculated

      Dummy
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Calculated: gemmi.CalcFlag  # value = <CalcFlag.Calculated: 2>
    Determined: gemmi.CalcFlag  # value = <CalcFlag.Determined: 1>
    Dummy: gemmi.CalcFlag  # value = <CalcFlag.Dummy: 3>
    NotSet: gemmi.CalcFlag  # value = <CalcFlag.NotSet: 0>

class Ccp4Base:
    def axis_positions(self) -> list[int]: ...
    def get_extent(self) -> FractionalBox: ...
    def get_skew_transformation(self) -> Transform: ...
    def has_skew_transformation(self) -> bool: ...
    def header_float(self, arg0: int) -> float: ...
    def header_i32(self, arg0: int) -> int: ...
    def header_str(self, w: int, len: int = 80) -> str: ...
    def set_header_float(self, arg0: int, arg1: float) -> None: ...
    def set_header_i32(self, arg0: int, arg1: int) -> None: ...
    def set_header_str(self, arg0: int, arg1: str) -> None: ...

class Ccp4Map(Ccp4Base):
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def full_cell(self) -> bool: ...
    def set_extent(self, arg0: FractionalBox) -> None: ...
    def setup(self, default_value: float, mode: MapSetup = ...) -> None: ...
    def update_ccp4_header(self, mode: int = -1, update_stats: bool = True) -> None: ...
    def write_ccp4_map(self, filename: str) -> None: ...
    @property
    def grid(self) -> FloatGrid:
        """
        :type: FloatGrid
        """
    @grid.setter
    def grid(self, arg0: FloatGrid) -> None:
        pass

class Ccp4Mask(Ccp4Base):
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def full_cell(self) -> bool: ...
    def set_extent(self, arg0: FractionalBox) -> None: ...
    def setup(self, default_value: int, mode: MapSetup = ...) -> None: ...
    def update_ccp4_header(self, mode: int = -1, update_stats: bool = True) -> None: ...
    def write_ccp4_map(self, filename: str) -> None: ...
    @property
    def grid(self) -> Int8Grid:
        """
        :type: Int8Grid
        """
    @grid.setter
    def grid(self, arg0: Int8Grid) -> None:
        pass

class Chain:
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __delitem__(self, index: int) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list: ...
    @typing.overload
    def __getitem__(self, index: int) -> Residue: ...
    @typing.overload
    def __getitem__(self, pdb_seqid: str) -> ResidueGroup: ...
    def __init__(self, arg0: str) -> None: ...
    def __iter__(self) -> typing.Iterator[Residue]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def add_residue(self, residue: Residue, pos: int = -1) -> Residue: ...
    def append_residues(self, new_residues: list[Residue], min_sep: int = 0) -> None: ...
    def calculate_center_of_mass(self) -> Position: ...
    def calculate_mass(self) -> float: ...
    def clone(self) -> Chain: ...
    def count_atom_sites(self, sel: Selection = None) -> int: ...
    def count_occupancies(self, sel: Selection = None) -> float: ...
    def first_conformer(self) -> FirstConformerRes: ...
    def get_ligands(self) -> ResidueSpan: ...
    def get_polymer(self) -> ResidueSpan: ...
    def get_subchain(self, arg0: str) -> ResidueSpan: ...
    def get_waters(self) -> ResidueSpan: ...
    def next_residue(self, arg0: Residue) -> Residue: ...
    def previous_residue(self, arg0: Residue) -> Residue: ...
    def subchains(self) -> list[ResidueSpan]: ...
    def trim_to_alanine(self) -> None: ...
    def whole(self) -> ResidueSpan: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass

class ChemComp:
    class Aliasing:
        def name_from_alias(self, arg0: str) -> str: ...
        @property
        def group(self) -> ChemComp.Group:
            """
            :type: ChemComp.Group
            """

    class Atom:
        def is_hydrogen(self) -> bool: ...
        @property
        def charge(self) -> float:
            """
            :type: float
            """
        @property
        def chem_type(self) -> str:
            """
            :type: str
            """
        @property
        def el(self) -> Element:
            """
            :type: Element
            """
        @property
        def id(self) -> str:
            """
            :type: str
            """

    class Group:
        """
        Members:

          Peptide

          PPeptide

          MPeptide

          Dna

          Rna

          DnaRna

          Pyranose

          Ketopyranose

          Furanose

          NonPolymer

          Null
        """

        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        Dna: gemmi.ChemComp.Group  # value = <Group.Dna: 3>
        DnaRna: gemmi.ChemComp.Group  # value = <Group.DnaRna: 5>
        Furanose: gemmi.ChemComp.Group  # value = <Group.Furanose: 8>
        Ketopyranose: gemmi.ChemComp.Group  # value = <Group.Ketopyranose: 7>
        MPeptide: gemmi.ChemComp.Group  # value = <Group.MPeptide: 2>
        NonPolymer: gemmi.ChemComp.Group  # value = <Group.NonPolymer: 9>
        Null: gemmi.ChemComp.Group  # value = <Group.Null: 10>
        PPeptide: gemmi.ChemComp.Group  # value = <Group.PPeptide: 1>
        Peptide: gemmi.ChemComp.Group  # value = <Group.Peptide: 0>
        Pyranose: gemmi.ChemComp.Group  # value = <Group.Pyranose: 6>
        Rna: gemmi.ChemComp.Group  # value = <Group.Rna: 4>
    def find_atom(self, arg0: str) -> ChemComp.Atom: ...
    def get_atom(self, arg0: str) -> ChemComp.Atom: ...
    @staticmethod
    def group_str(arg0: ChemComp.Group) -> str: ...
    def remove_hydrogens(self) -> ChemComp: ...
    def set_group(self, arg0: str) -> None: ...
    @property
    def atoms(self) -> ChemCompAtoms:
        """
        :type: ChemCompAtoms
        """
    @property
    def group(self) -> ChemComp.Group:
        """
        :type: ChemComp.Group
        """
    @group.setter
    def group(self, arg0: ChemComp.Group) -> None:
        pass
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def rt(self) -> Restraints:
        """
        :type: Restraints
        """

class ChemCompAtoms:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> ChemComp.Atom:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> ChemCompAtoms: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: ChemCompAtoms) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator[ChemComp.Atom]: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: ChemComp.Atom) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: ChemCompAtoms) -> None: ...
    def append(self, x: ChemComp.Atom) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: ChemCompAtoms) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: ChemComp.Atom) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> ChemComp.Atom:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> ChemComp.Atom: ...

class ChemCompMap:
    def __bool__(self) -> bool:
        """
        Check whether the map is nonempty
        """
    @typing.overload
    def __contains__(self, arg0: object) -> bool: ...
    @typing.overload
    def __contains__(self, arg0: str) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> ChemComp: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator[ChemComp]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: str, arg1: ChemComp) -> None: ...
    def items(self) -> typing.ItemsView[str, ChemComp]: ...
    def keys(self) -> typing.KeysView[str]: ...
    def values(self) -> typing.ValuesView[ChemComp]: ...

class ChemLink:
    class Side:
        def __init__(self) -> None: ...
        def __repr__(self) -> str: ...
        @property
        def comp(self) -> str:
            """
            :type: str
            """
        @comp.setter
        def comp(self, arg0: str) -> None:
            pass
        @property
        def group(self) -> ChemComp.Group:
            """
            :type: ChemComp.Group
            """
        @group.setter
        def group(self, arg0: ChemComp.Group) -> None:
            pass
        @property
        def mod(self) -> str:
            """
            :type: str
            """
        @mod.setter
        def mod(self, arg0: str) -> None:
            pass
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def id(self) -> str:
        """
        :type: str
        """
    @id.setter
    def id(self, arg0: str) -> None:
        pass
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def rt(self) -> Restraints:
        """
        :type: Restraints
        """
    @rt.setter
    def rt(self, arg0: Restraints) -> None:
        pass
    @property
    def side1(self) -> ChemLink.Side:
        """
        :type: ChemLink.Side
        """
    @side1.setter
    def side1(self, arg0: ChemLink.Side) -> None:
        pass
    @property
    def side2(self) -> ChemLink.Side:
        """
        :type: ChemLink.Side
        """
    @side2.setter
    def side2(self, arg0: ChemLink.Side) -> None:
        pass

class ChemLinkMap:
    def __bool__(self) -> bool:
        """
        Check whether the map is nonempty
        """
    @typing.overload
    def __contains__(self, arg0: object) -> bool: ...
    @typing.overload
    def __contains__(self, arg0: str) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> ChemLink: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator[ChemLink]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: str, arg1: ChemLink) -> None: ...
    def items(self) -> typing.ItemsView[str, ChemLink]: ...
    def keys(self) -> typing.KeysView[str]: ...
    def values(self) -> typing.ValuesView[ChemLink]: ...

class ChemMod:
    class AtomMod:
        @property
        def charge(self) -> float:
            """
            :type: float
            """
        @charge.setter
        def charge(self, arg0: float) -> None:
            pass
        @property
        def chem_type(self) -> str:
            """
            :type: str
            """
        @chem_type.setter
        def chem_type(self, arg0: str) -> None:
            pass
        @property
        def el(self) -> Element:
            """
            :type: Element
            """
        @el.setter
        def el(self, arg0: Element) -> None:
            pass
        @property
        def func(self) -> int:
            """
            :type: int
            """
        @func.setter
        def func(self, arg0: int) -> None:
            pass
        @property
        def new_id(self) -> str:
            """
            :type: str
            """
        @new_id.setter
        def new_id(self, arg0: str) -> None:
            pass
        @property
        def old_id(self) -> str:
            """
            :type: str
            """
        @old_id.setter
        def old_id(self, arg0: str) -> None:
            pass
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def atom_mods(self) -> list[ChemMod.AtomMod]:
        """
        :type: typing.List[ChemMod.AtomMod]
        """
    @atom_mods.setter
    def atom_mods(self, arg0: list[ChemMod.AtomMod]) -> None:
        pass
    @property
    def comp_id(self) -> str:
        """
        :type: str
        """
    @comp_id.setter
    def comp_id(self, arg0: str) -> None:
        pass
    @property
    def group_id(self) -> str:
        """
        :type: str
        """
    @group_id.setter
    def group_id(self, arg0: str) -> None:
        pass
    @property
    def id(self) -> str:
        """
        :type: str
        """
    @id.setter
    def id(self, arg0: str) -> None:
        pass
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def rt(self) -> Restraints:
        """
        :type: Restraints
        """
    @rt.setter
    def rt(self, arg0: Restraints) -> None:
        pass

class ChemModMap:
    def __bool__(self) -> bool:
        """
        Check whether the map is nonempty
        """
    @typing.overload
    def __contains__(self, arg0: object) -> bool: ...
    @typing.overload
    def __contains__(self, arg0: str) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> ChemMod: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator[ChemMod]: ...
    def __len__(self) -> int: ...
    def __setitem__(self, arg0: str, arg1: ChemMod) -> None: ...
    def items(self) -> typing.ItemsView[str, ChemMod]: ...
    def keys(self) -> typing.KeysView[str]: ...
    def values(self) -> typing.ValuesView[ChemMod]: ...

class ChiralityType:
    """
    Members:

      Positive

      Negative

      Both
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Both: gemmi.ChiralityType  # value = <ChiralityType.Both: 2>
    Negative: gemmi.ChiralityType  # value = <ChiralityType.Negative: 1>
    Positive: gemmi.ChiralityType  # value = <ChiralityType.Positive: 0>

class CifToMtz:
    def __init__(self) -> None: ...
    def convert_block_to_mtz(self, arg0: ReflnBlock) -> Mtz: ...
    @property
    def history(self) -> list[str]:
        """
        :type: typing.List[str]
        """
    @history.setter
    def history(self, arg0: list[str]) -> None:
        pass
    @property
    def spec_lines(self) -> list[str]:
        """
        :type: typing.List[str]
        """
    @spec_lines.setter
    def spec_lines(self, arg0: list[str]) -> None:
        pass
    @property
    def title(self) -> str:
        """
        :type: str
        """
    @title.setter
    def title(self, arg0: str) -> None:
        pass

class CifWalk:
    def __init__(self, arg0: str) -> None: ...
    def __iter__(self) -> typing.Iterator[pathlib.Path]: ...

class ComplexAsuData:
    def __getitem__(self, index: int) -> ComplexHklValue: ...
    def __init__(
        self,
        cell: UnitCell,
        sg: SpaceGroup,
        miller_array: numpy.ndarray[numpy.int32],
        value_array: numpy.ndarray[numpy.complex64],
    ) -> None: ...
    def __iter__(self) -> typing.Iterator[ComplexHklValue]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def calculate_correlation(self, arg0: ComplexAsuData) -> ComplexCorrelation: ...
    def copy(self) -> ComplexAsuData: ...
    def count_equal_values(self, arg0: ComplexAsuData) -> int: ...
    def data_fits_into(self, size: list[int]) -> bool: ...
    def ensure_asu(self, tnt_asu: bool = False) -> None: ...
    def ensure_sorted(self) -> None: ...
    def get_f_phi_on_grid(
        self,
        size: list[int],
        half_l: bool = False,
        order: AxisOrder = ...,
    ) -> ReciprocalComplexGrid: ...
    def get_size_for_hkl(
        self,
        min_size: list[int] = [0, 0, 0],
        sample_rate: float = 0.0,
    ) -> list[int]: ...
    def make_1_d2_array(self) -> numpy.ndarray[numpy.float32]: ...
    def make_d_array(self) -> numpy.ndarray[numpy.float32]: ...
    def transform_f_phi_to_map(
        self,
        min_size: list[int] = [0, 0, 0],
        sample_rate: float = 0.0,
        exact_size: list[int] = [0, 0, 0],
        order: AxisOrder = ...,
    ) -> FloatGrid: ...
    @property
    def miller_array(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    @property
    def spacegroup(self) -> SpaceGroup:
        """
        :type: SpaceGroup
        """
    @spacegroup.setter
    def spacegroup(self, arg0: SpaceGroup) -> None:
        pass
    @property
    def unit_cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @unit_cell.setter
    def unit_cell(self, arg0: UnitCell) -> None:
        pass
    @property
    def value_array(self) -> numpy.ndarray[numpy.complex64]:
        """
        :type: numpy.ndarray[numpy.complex64]
        """

class ComplexCorrelation:
    def coefficient(self) -> complex: ...
    def mean_ratio(self) -> float: ...
    @property
    def n(self) -> int:
        """
        :type: int
        """

class GridMeta:
    def get_fractional(self, arg0: int, arg1: int, arg2: int) -> Fractional: ...
    def get_position(self, arg0: int, arg1: int, arg2: int) -> Position: ...
    @property
    def axis_order(self) -> AxisOrder:
        """
        :type: AxisOrder
        """
    @property
    def nu(self) -> int:
        """
        size in the first (fastest-changing) dim

        :type: int
        """
    @property
    def nv(self) -> int:
        """
        size in the second dimension

        :type: int
        """
    @property
    def nw(self) -> int:
        """
        size in the third (slowest-changing) dim

        :type: int
        """
    @property
    def point_count(self) -> int:
        """
        :type: int
        """
    @property
    def shape(self) -> tuple:
        """
        :type: tuple
        """
    @property
    def spacegroup(self) -> SpaceGroup:
        """
        :type: SpaceGroup
        """
    @spacegroup.setter
    def spacegroup(self, arg0: SpaceGroup) -> None:
        pass
    @property
    def unit_cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @unit_cell.setter
    def unit_cell(self, arg0: UnitCell) -> None:
        pass

class ComplexHklValue:
    def __repr__(self) -> str: ...
    @property
    def hkl(self) -> list[int]:
        """
        :type: typing.List[int]
        """
    @property
    def value(self) -> complex:
        """
        :type: complex
        """
    @value.setter
    def value(self, arg0: complex) -> None:
        pass

class Connection:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def asu(self) -> Asu:
        """
        :type: Asu
        """
    @asu.setter
    def asu(self, arg0: Asu) -> None:
        pass
    @property
    def link_id(self) -> str:
        """
        :type: str
        """
    @link_id.setter
    def link_id(self, arg0: str) -> None:
        pass
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def partner1(self) -> AtomAddress:
        """
        :type: AtomAddress
        """
    @partner1.setter
    def partner1(self, arg0: AtomAddress) -> None:
        pass
    @property
    def partner2(self) -> AtomAddress:
        """
        :type: AtomAddress
        """
    @partner2.setter
    def partner2(self, arg0: AtomAddress) -> None:
        pass
    @property
    def reported_distance(self) -> float:
        """
        :type: float
        """
    @reported_distance.setter
    def reported_distance(self, arg0: float) -> None:
        pass
    @property
    def type(self) -> ConnectionType:
        """
        :type: ConnectionType
        """
    @type.setter
    def type(self, arg0: ConnectionType) -> None:
        pass

class ConnectionList:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Connection:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> ConnectionList: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: ConnectionList) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator[Connection]: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Connection) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: ConnectionList) -> None: ...
    def append(self, x: Connection) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: ConnectionList) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Connection) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Connection:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Connection: ...

class ConnectionType:
    """
    Members:

      Covale

      Disulf

      Hydrog

      MetalC

      Unknown
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Covale: gemmi.ConnectionType  # value = <ConnectionType.Covale: 0>
    Disulf: gemmi.ConnectionType  # value = <ConnectionType.Disulf: 1>
    Hydrog: gemmi.ConnectionType  # value = <ConnectionType.Hydrog: 2>
    MetalC: gemmi.ConnectionType  # value = <ConnectionType.MetalC: 3>
    Unknown: gemmi.ConnectionType  # value = <ConnectionType.Unknown: 4>

class ContactSearch:
    class Ignore:
        """
        Members:

          Nothing

          SameResidue

          AdjacentResidues

          SameChain

          SameAsu
        """

        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        AdjacentResidues: gemmi.ContactSearch.Ignore  # value = <Ignore.AdjacentResidues: 2>
        Nothing: gemmi.ContactSearch.Ignore  # value = <Ignore.Nothing: 0>
        SameAsu: gemmi.ContactSearch.Ignore  # value = <Ignore.SameAsu: 4>
        SameChain: gemmi.ContactSearch.Ignore  # value = <Ignore.SameChain: 3>
        SameResidue: gemmi.ContactSearch.Ignore  # value = <Ignore.SameResidue: 1>

    class Result:
        @property
        def dist(self) -> float:
            """
            :type: float
            """
        @property
        def image_idx(self) -> int:
            """
            :type: int
            """
        @property
        def partner1(self) -> CRA:
            """
            :type: CRA
            """
        @property
        def partner2(self) -> CRA:
            """
            :type: CRA
            """
    def __init__(self, arg0: float) -> None: ...
    def find_contacts(self, arg0: NeighborSearch) -> list[ContactSearch.Result]: ...
    def get_radius(self, arg0: Element) -> float: ...
    def set_radius(self, arg0: Element, arg1: float) -> None: ...
    def setup_atomic_radii(self, arg0: float, arg1: float) -> None: ...
    @property
    def ignore(self) -> ContactSearch.Ignore:
        """
        :type: ContactSearch.Ignore
        """
    @ignore.setter
    def ignore(self, arg0: ContactSearch.Ignore) -> None:
        pass
    @property
    def min_occupancy(self) -> float:
        """
        :type: float
        """
    @min_occupancy.setter
    def min_occupancy(self, arg0: float) -> None:
        pass
    @property
    def search_radius(self) -> float:
        """
        :type: float
        """
    @search_radius.setter
    def search_radius(self, arg0: float) -> None:
        pass
    @property
    def special_pos_cutoff_sq(self) -> float:
        """
        :type: float
        """
    @special_pos_cutoff_sq.setter
    def special_pos_cutoff_sq(self, arg0: float) -> None:
        pass
    @property
    def twice(self) -> bool:
        """
        :type: bool
        """
    @twice.setter
    def twice(self, arg0: bool) -> None:
        pass

class CoorFileWalk:
    def __init__(self, arg0: str) -> None: ...
    def __iter__(self) -> typing.Iterator[pathlib.Path]: ...

class CoorFormat:
    """
    Members:

      Unknown

      Detect

      Pdb

      Mmcif

      Mmjson

      ChemComp
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    ChemComp: gemmi.CoorFormat  # value = <CoorFormat.ChemComp: 5>
    Detect: gemmi.CoorFormat  # value = <CoorFormat.Detect: 1>
    Mmcif: gemmi.CoorFormat  # value = <CoorFormat.Mmcif: 3>
    Mmjson: gemmi.CoorFormat  # value = <CoorFormat.Mmjson: 4>
    Pdb: gemmi.CoorFormat  # value = <CoorFormat.Pdb: 2>
    Unknown: gemmi.CoorFormat  # value = <CoorFormat.Unknown: 0>

class Correlation:
    def coefficient(self) -> float: ...
    def mean_ratio(self) -> float: ...
    @property
    def n(self) -> int:
        """
        :type: int
        """

class CraGenerator:
    def __iter__(self) -> typing.Iterator[]: ...

class CrystalInfo:
    def __init__(self) -> None: ...
    @property
    def description(self) -> str:
        """
        :type: str
        """
    @description.setter
    def description(self, arg0: str) -> None:
        pass
    @property
    def diffractions(self) -> list[DiffractionInfo]:
        """
        :type: typing.List[DiffractionInfo]
        """
    @diffractions.setter
    def diffractions(self, arg0: list[DiffractionInfo]) -> None:
        pass
    @property
    def id(self) -> str:
        """
        :type: str
        """
    @id.setter
    def id(self, arg0: str) -> None:
        pass
    @property
    def ph(self) -> float:
        """
        :type: float
        """
    @ph.setter
    def ph(self, arg0: float) -> None:
        pass
    @property
    def ph_range(self) -> str:
        """
        :type: str
        """
    @ph_range.setter
    def ph_range(self, arg0: str) -> None:
        pass

class CrystalSystem:
    """
    Members:

      Triclinic

      Monoclinic

      Orthorhombic

      Tetragonal

      Trigonal

      Hexagonal

      Cubic
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Cubic: gemmi.CrystalSystem  # value = <CrystalSystem.Cubic: 6>
    Hexagonal: gemmi.CrystalSystem  # value = <CrystalSystem.Hexagonal: 5>
    Monoclinic: gemmi.CrystalSystem  # value = <CrystalSystem.Monoclinic: 1>
    Orthorhombic: gemmi.CrystalSystem  # value = <CrystalSystem.Orthorhombic: 2>
    Tetragonal: gemmi.CrystalSystem  # value = <CrystalSystem.Tetragonal: 3>
    Triclinic: gemmi.CrystalSystem  # value = <CrystalSystem.Triclinic: 0>
    Trigonal: gemmi.CrystalSystem  # value = <CrystalSystem.Trigonal: 4>

class DataType:
    """
    Members:

      Unknown

      Unmerged

      Mean

      Anomalous
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Anomalous: gemmi.DataType  # value = <DataType.Anomalous: 3>
    Mean: gemmi.DataType  # value = <DataType.Mean: 2>
    Unknown: gemmi.DataType  # value = <DataType.Unknown: 0>
    Unmerged: gemmi.DataType  # value = <DataType.Unmerged: 1>

class DensityCalculatorE:
    def __init__(self) -> None: ...
    def add_atom_density_to_grid(self, arg0: Atom) -> None: ...
    def add_c_contribution_to_grid(self, arg0: Atom, arg1: float) -> None: ...
    def add_model_density_to_grid(self, arg0: Model) -> None: ...
    def estimate_radius(self, arg0: Atom) -> float: ...
    def initialize_grid(self) -> None: ...
    def mott_bethe_factor(self, arg0: list[int]) -> float: ...
    def put_model_density_on_grid(self, arg0: Model) -> None: ...
    def reciprocal_space_multiplier(self, arg0: float) -> float: ...
    def set_grid_cell_and_spacegroup(self, arg0: Structure) -> None: ...
    def set_refmac_compatible_blur(self, arg0: Model) -> None: ...
    @property
    def addends(self) -> Addends:
        """
        :type: Addends
        """
    @addends.setter
    def addends(self, arg0: Addends) -> None:
        pass
    @property
    def blur(self) -> float:
        """
        :type: float
        """
    @blur.setter
    def blur(self, arg0: float) -> None:
        pass
    @property
    def cutoff(self) -> float:
        """
        :type: float
        """
    @cutoff.setter
    def cutoff(self, arg0: float) -> None:
        pass
    @property
    def d_min(self) -> float:
        """
        :type: float
        """
    @d_min.setter
    def d_min(self, arg0: float) -> None:
        pass
    @property
    def grid(self) -> FloatGrid:
        """
        :type: FloatGrid
        """
    @property
    def rate(self) -> float:
        """
        :type: float
        """
    @rate.setter
    def rate(self, arg0: float) -> None:
        pass

class DensityCalculatorN:
    def __init__(self) -> None: ...
    def add_atom_density_to_grid(self, arg0: Atom) -> None: ...
    def add_c_contribution_to_grid(self, arg0: Atom, arg1: float) -> None: ...
    def add_model_density_to_grid(self, arg0: Model) -> None: ...
    def estimate_radius(self, arg0: Atom) -> float: ...
    def initialize_grid(self) -> None: ...
    def mott_bethe_factor(self, arg0: list[int]) -> float: ...
    def put_model_density_on_grid(self, arg0: Model) -> None: ...
    def reciprocal_space_multiplier(self, arg0: float) -> float: ...
    def set_grid_cell_and_spacegroup(self, arg0: Structure) -> None: ...
    def set_refmac_compatible_blur(self, arg0: Model) -> None: ...
    @property
    def addends(self) -> Addends:
        """
        :type: Addends
        """
    @addends.setter
    def addends(self, arg0: Addends) -> None:
        pass
    @property
    def blur(self) -> float:
        """
        :type: float
        """
    @blur.setter
    def blur(self, arg0: float) -> None:
        pass
    @property
    def cutoff(self) -> float:
        """
        :type: float
        """
    @cutoff.setter
    def cutoff(self, arg0: float) -> None:
        pass
    @property
    def d_min(self) -> float:
        """
        :type: float
        """
    @d_min.setter
    def d_min(self, arg0: float) -> None:
        pass
    @property
    def grid(self) -> FloatGrid:
        """
        :type: FloatGrid
        """
    @property
    def rate(self) -> float:
        """
        :type: float
        """
    @rate.setter
    def rate(self, arg0: float) -> None:
        pass

class DensityCalculatorX:
    def __init__(self) -> None: ...
    def add_atom_density_to_grid(self, arg0: Atom) -> None: ...
    def add_c_contribution_to_grid(self, arg0: Atom, arg1: float) -> None: ...
    def add_model_density_to_grid(self, arg0: Model) -> None: ...
    def estimate_radius(self, arg0: Atom) -> float: ...
    def initialize_grid(self) -> None: ...
    def mott_bethe_factor(self, arg0: list[int]) -> float: ...
    def put_model_density_on_grid(self, arg0: Model) -> None: ...
    def reciprocal_space_multiplier(self, arg0: float) -> float: ...
    def set_grid_cell_and_spacegroup(self, arg0: Structure) -> None: ...
    def set_refmac_compatible_blur(self, arg0: Model) -> None: ...
    @property
    def addends(self) -> Addends:
        """
        :type: Addends
        """
    @addends.setter
    def addends(self, arg0: Addends) -> None:
        pass
    @property
    def blur(self) -> float:
        """
        :type: float
        """
    @blur.setter
    def blur(self, arg0: float) -> None:
        pass
    @property
    def cutoff(self) -> float:
        """
        :type: float
        """
    @cutoff.setter
    def cutoff(self, arg0: float) -> None:
        pass
    @property
    def d_min(self) -> float:
        """
        :type: float
        """
    @d_min.setter
    def d_min(self, arg0: float) -> None:
        pass
    @property
    def grid(self) -> FloatGrid:
        """
        :type: FloatGrid
        """
    @property
    def rate(self) -> float:
        """
        :type: float
        """
    @rate.setter
    def rate(self, arg0: float) -> None:
        pass

class DiffractionInfo:
    def __init__(self) -> None: ...
    @property
    def beamline(self) -> str:
        """
        :type: str
        """
    @beamline.setter
    def beamline(self, arg0: str) -> None:
        pass
    @property
    def collection_date(self) -> str:
        """
        :type: str
        """
    @collection_date.setter
    def collection_date(self, arg0: str) -> None:
        pass
    @property
    def detector(self) -> str:
        """
        :type: str
        """
    @detector.setter
    def detector(self, arg0: str) -> None:
        pass
    @property
    def detector_make(self) -> str:
        """
        :type: str
        """
    @detector_make.setter
    def detector_make(self, arg0: str) -> None:
        pass
    @property
    def id(self) -> str:
        """
        :type: str
        """
    @id.setter
    def id(self, arg0: str) -> None:
        pass
    @property
    def mono_or_laue(self) -> str:
        """
        :type: str
        """
    @mono_or_laue.setter
    def mono_or_laue(self, arg0: str) -> None:
        pass
    @property
    def monochromator(self) -> str:
        """
        :type: str
        """
    @monochromator.setter
    def monochromator(self, arg0: str) -> None:
        pass
    @property
    def optics(self) -> str:
        """
        :type: str
        """
    @optics.setter
    def optics(self, arg0: str) -> None:
        pass
    @property
    def scattering_type(self) -> str:
        """
        :type: str
        """
    @scattering_type.setter
    def scattering_type(self, arg0: str) -> None:
        pass
    @property
    def source(self) -> str:
        """
        :type: str
        """
    @source.setter
    def source(self, arg0: str) -> None:
        pass
    @property
    def source_type(self) -> str:
        """
        :type: str
        """
    @source_type.setter
    def source_type(self, arg0: str) -> None:
        pass
    @property
    def synchrotron(self) -> str:
        """
        :type: str
        """
    @synchrotron.setter
    def synchrotron(self, arg0: str) -> None:
        pass
    @property
    def temperature(self) -> float:
        """
        :type: float
        """
    @temperature.setter
    def temperature(self, arg0: float) -> None:
        pass
    @property
    def wavelengths(self) -> str:
        """
        :type: str
        """
    @wavelengths.setter
    def wavelengths(self, arg0: str) -> None:
        pass

class Element:
    def __eq__(self, arg0: Element) -> bool: ...
    def __hash__(self) -> int: ...
    @typing.overload
    def __init__(self, arg0: int) -> None: ...
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def atomic_number(self) -> int:
        """
        :type: int
        """
    @property
    def c4322(self) -> C4322Coef:
        """
        :type: C4322Coef
        """
    @property
    def covalent_r(self) -> float:
        """
        :type: float
        """
    @property
    def is_hydrogen(self) -> bool:
        """
        :type: bool
        """
    @property
    def is_metal(self) -> bool:
        """
        :type: bool
        """
    @property
    def it92(self) -> IT92Coef:
        """
        :type: IT92Coef
        """
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def neutron92(self) -> Neutron92:
        """
        :type: Neutron92
        """
    @property
    def vdw_r(self) -> float:
        """
        :type: float
        """
    @property
    def weight(self) -> float:
        """
        :type: float
        """

class EnerLib:
    pass

class Entity:
    def __init__(self, arg0: str) -> None: ...
    def __repr__(self) -> str: ...
    @staticmethod
    def first_mon(arg0: str) -> str: ...
    @property
    def entity_type(self) -> EntityType:
        """
        :type: EntityType
        """
    @entity_type.setter
    def entity_type(self, arg0: EntityType) -> None:
        pass
    @property
    def full_sequence(self) -> list[str]:
        """
        :type: typing.List[str]
        """
    @full_sequence.setter
    def full_sequence(self, arg0: list[str]) -> None:
        pass
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def polymer_type(self) -> PolymerType:
        """
        :type: PolymerType
        """
    @polymer_type.setter
    def polymer_type(self, arg0: PolymerType) -> None:
        pass
    @property
    def sifts_unp_acc(self) -> list[str]:
        """
        :type: typing.List[str]
        """
    @sifts_unp_acc.setter
    def sifts_unp_acc(self, arg0: list[str]) -> None:
        pass
    @property
    def subchains(self) -> list[str]:
        """
        :type: typing.List[str]
        """
    @subchains.setter
    def subchains(self, arg0: list[str]) -> None:
        pass

class EntityList:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Entity:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> EntityList: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: EntityList) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator[Entity]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Entity) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: EntityList) -> None: ...
    def append(self, x: Entity) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: EntityList) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Entity) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Entity:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Entity: ...

class EntityType:
    """
    Members:

      Unknown

      Polymer

      NonPolymer

      Branched

      Water
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Branched: gemmi.EntityType  # value = <EntityType.Branched: 3>
    NonPolymer: gemmi.EntityType  # value = <EntityType.NonPolymer: 2>
    Polymer: gemmi.EntityType  # value = <EntityType.Polymer: 1>
    Unknown: gemmi.EntityType  # value = <EntityType.Unknown: 0>
    Water: gemmi.EntityType  # value = <EntityType.Water: 4>

class ExperimentInfo:
    def __init__(self) -> None: ...
    @property
    def b_wilson(self) -> float:
        """
        :type: float
        """
    @b_wilson.setter
    def b_wilson(self, arg0: float) -> None:
        pass
    @property
    def diffraction_ids(self) -> list[str]:
        """
        :type: typing.List[str]
        """
    @diffraction_ids.setter
    def diffraction_ids(self, arg0: list[str]) -> None:
        pass
    @property
    def method(self) -> str:
        """
        :type: str
        """
    @method.setter
    def method(self, arg0: str) -> None:
        pass
    @property
    def number_of_crystals(self) -> int:
        """
        :type: int
        """
    @number_of_crystals.setter
    def number_of_crystals(self, arg0: int) -> None:
        pass
    @property
    def reflections(self) -> ReflectionsInfo:
        """
        :type: ReflectionsInfo
        """
    @reflections.setter
    def reflections(self, arg0: ReflectionsInfo) -> None:
        pass
    @property
    def shells(self) -> list[ReflectionsInfo]:
        """
        :type: typing.List[ReflectionsInfo]
        """
    @shells.setter
    def shells(self, arg0: list[ReflectionsInfo]) -> None:
        pass
    @property
    def unique_reflections(self) -> int:
        """
        :type: int
        """
    @unique_reflections.setter
    def unique_reflections(self, arg0: int) -> None:
        pass

class Transform:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, mat33: Mat33, vec3: Vec3) -> None: ...
    def apply(self, arg0: Vec3) -> Vec3: ...
    def approx(self, other: Transform, epsilon: float) -> bool: ...
    def combine(self, arg0: Transform) -> Transform: ...
    def inverse(self) -> Transform: ...
    def is_identity(self) -> bool: ...
    @property
    def mat(self) -> Mat33:
        """
        :type: Mat33
        """
    @property
    def vec(self) -> Vec3:
        """
        :type: Vec3
        """

class FirstConformerAtoms:
    def __iter__(self) -> typing.Iterator[Atom]: ...

class FirstConformerRes:
    def __iter__(self) -> typing.Iterator[]: ...

class FirstConformerResSpan:
    def __iter__(self) -> typing.Iterator: ...

class FloatAsuData:
    def __getitem__(self, index: int) -> FloatHklValue: ...
    def __init__(
        self,
        cell: UnitCell,
        sg: SpaceGroup,
        miller_array: numpy.ndarray[numpy.int32],
        value_array: numpy.ndarray[numpy.float32],
    ) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def calculate_correlation(self, arg0: FloatAsuData) -> Correlation: ...
    def copy(self) -> FloatAsuData: ...
    def count_equal_values(self, arg0: FloatAsuData) -> int: ...
    def ensure_asu(self, tnt_asu: bool = False) -> None: ...
    def ensure_sorted(self) -> None: ...
    def make_1_d2_array(self) -> numpy.ndarray[numpy.float32]: ...
    def make_d_array(self) -> numpy.ndarray[numpy.float32]: ...
    @property
    def miller_array(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    @property
    def spacegroup(self) -> SpaceGroup:
        """
        :type: SpaceGroup
        """
    @spacegroup.setter
    def spacegroup(self, arg0: SpaceGroup) -> None:
        pass
    @property
    def unit_cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @unit_cell.setter
    def unit_cell(self, arg0: UnitCell) -> None:
        pass
    @property
    def value_array(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """

class FloatGridBase(GridMeta):
    class Point:
        def __repr__(self) -> str: ...
        @property
        def u(self) -> int:
            """
            :type: int
            """
        @property
        def v(self) -> int:
            """
            :type: int
            """
        @property
        def value(self) -> float:
            """
            :type: float
            """
        @value.setter
        def value(self, arg1: float) -> None:
            pass
        @property
        def w(self) -> int:
            """
            :type: int
            """
    def __iter__(self) -> typing.Iterator[float]: ...
    def calculate_correlation(self, arg0: FloatGridBase) -> Correlation: ...
    def fill(self, value: float) -> None: ...
    def get_nonzero_extent(self) -> FractionalBox: ...
    def index_to_point(self, arg0: int) -> FloatGridBase.Point: ...
    def point_to_index(self, arg0: FloatGridBase.Point) -> int: ...
    def sum(self) -> float: ...
    @property
    def array(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """

class FloatGrid(FloatGridBase, GridMeta):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(
        self,
        arg0: numpy.ndarray[numpy.float32],
        cell: UnitCell = None,
        spacegroup: SpaceGroup = None,
    ) -> None: ...
    @typing.overload
    def __init__(self, nx: int, ny: int, nz: int) -> None: ...
    def __repr__(self) -> str: ...
    def add_soft_edge_to_mask(self, arg0: float) -> None: ...
    def change_values(self, old_value: float, new_value: float) -> None: ...
    def clone(self) -> FloatGrid: ...
    def copy_metadata_from(self, arg0: GridMeta) -> None: ...
    def get_nearest_point(self, arg0: Position) -> FloatGridBase.Point: ...
    def get_point(self, arg0: int, arg1: int, arg2: int) -> FloatGridBase.Point: ...
    def get_subarray(self, start: list[int], shape: list[int]) -> numpy.ndarray[numpy.float32]: ...
    def get_value(self, arg0: int, arg1: int, arg2: int) -> float: ...
    @typing.overload
    def interpolate_value(self, arg0: Fractional) -> float: ...
    @typing.overload
    def interpolate_value(self, arg0: Position) -> float: ...
    def interpolate_values(self, arg0: numpy.ndarray[numpy.float32], arg1: Transform, order: int = 2) -> None: ...
    def mask_points_in_constant_radius(self, model: Model, radius: float, value: float) -> None: ...
    def masked_asu(self) -> MaskedFloatGrid: ...
    def normalize(self) -> None: ...
    def point_to_fractional(self, arg0: FloatGridBase.Point) -> Fractional: ...
    def point_to_position(self, arg0: FloatGridBase.Point) -> Position: ...
    def resample_to(self, dest: FloatGrid, order: int) -> None: ...
    def set_points_around(self, position: Position, radius: float, value: float, use_pbc: bool = True) -> None: ...
    def set_size(self, arg0: int, arg1: int, arg2: int) -> None: ...
    def set_size_from_spacing(self, spacing: float, rounding: GridSizeRounding) -> None: ...
    def set_subarray(self, arr: numpy.ndarray[numpy.float32], start: list[int]) -> None: ...
    def set_unit_cell(self, arg0: UnitCell) -> None: ...
    def set_value(self, arg0: int, arg1: int, arg2: int, arg3: float) -> None: ...
    def setup_from(self, st: Structure, spacing: float) -> None: ...
    def symmetrize_abs_max(self) -> None: ...
    def symmetrize_max(self) -> None: ...
    def symmetrize_min(self) -> None: ...
    def symmetrize_sum(self) -> None: ...
    @typing.overload
    def tricubic_interpolation(self, arg0: Fractional) -> float: ...
    @typing.overload
    def tricubic_interpolation(self, arg0: Position) -> float: ...
    def tricubic_interpolation_der(self, arg0: Fractional) -> list[float]: ...
    @property
    def spacing(self) -> tuple:
        """
        :type: tuple
        """

class FloatHklValue:
    def __repr__(self) -> str: ...
    @property
    def hkl(self) -> list[int]:
        """
        :type: typing.List[int]
        """
    @property
    def value(self) -> float:
        """
        :type: float
        """
    @value.setter
    def value(self, arg0: float) -> None:
        pass

class Vec3:
    def __add__(self, arg0: Vec3) -> Vec3: ...
    def __getitem__(self, arg0: int) -> float: ...
    def __iadd__(self, arg0: Vec3) -> Vec3: ...
    def __imul__(self, arg0: float) -> Vec3: ...
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None: ...
    def __isub__(self, arg0: Vec3) -> Vec3: ...
    def __itruediv__(self, arg0: float) -> Vec3: ...
    def __mul__(self, arg0: float) -> Vec3: ...
    def __neg__(self) -> Vec3: ...
    def __repr__(self) -> str: ...
    def __rmul__(self, arg0: float) -> Vec3: ...
    def __setitem__(self, arg0: int, arg1: float) -> None: ...
    def __sub__(self, arg0: Vec3) -> Vec3: ...
    def __truediv__(self, arg0: float) -> Vec3: ...
    def approx(self, other: Vec3, epsilon: float) -> bool: ...
    def cross(self, arg0: Vec3) -> Vec3: ...
    def dot(self, arg0: Vec3) -> float: ...
    def fromlist(self, arg0: list[float]) -> None: ...
    def length(self) -> float: ...
    def normalized(self) -> Vec3: ...
    def tolist(self) -> list[float]: ...
    @property
    def x(self) -> float:
        """
        :type: float
        """
    @x.setter
    def x(self, arg0: float) -> None:
        pass
    @property
    def y(self) -> float:
        """
        :type: float
        """
    @y.setter
    def y(self, arg0: float) -> None:
        pass
    @property
    def z(self) -> float:
        """
        :type: float
        """
    @z.setter
    def z(self, arg0: float) -> None:
        pass

class FractionalBox:
    def __init__(self) -> None: ...
    def add_margin(self, arg0: float) -> None: ...
    def extend(self, arg0: Fractional) -> None: ...
    def get_size(self) -> Fractional: ...
    @property
    def maximum(self) -> Fractional:
        """
        :type: Fractional
        """
    @maximum.setter
    def maximum(self, arg0: Fractional) -> None:
        pass
    @property
    def minimum(self) -> Fractional:
        """
        :type: Fractional
        """
    @minimum.setter
    def minimum(self, arg0: Fractional) -> None:
        pass

class GeomTarget:
    def am_for_coo(self) -> tuple: ...
    @property
    def am(self) -> list[float]:
        """
        :type: typing.List[float]
        """
    @property
    def target(self) -> float:
        """
        :type: float
        """
    @property
    def vn(self) -> list[float]:
        """
        :type: typing.List[float]
        """

class Geometry:
    class Angle:
        class Value:
            def __init__(self, arg0: float, arg1: float) -> None: ...
            @property
            def sigma(self) -> float:
                """
                :type: float
                """
            @sigma.setter
            def sigma(self, arg0: float) -> None:
                pass
            @property
            def value(self) -> float:
                """
                :type: float
                """
            @value.setter
            def value(self, arg0: float) -> None:
                pass

        class Values:
            def __bool__(self) -> bool:
                """
                Check whether the list is nonempty
                """
            @typing.overload
            def __delitem__(self, arg0: int) -> None:
                """
                Delete the list elements at index ``i``

                Delete list elements using a slice object
                """
            @typing.overload
            def __delitem__(self, arg0: slice) -> None: ...
            @typing.overload
            def __getitem__(self, arg0: int) -> Geometry.Angle.Value:
                """
                Retrieve list elements using a slice object
                """
            @typing.overload
            def __getitem__(self, s: slice) -> Geometry.Angle.Values: ...
            @typing.overload
            def __init__(self) -> None:
                """
                Copy constructor
                """
            @typing.overload
            def __init__(self, arg0: Geometry.Angle.Values) -> None: ...
            @typing.overload
            def __init__(self, arg0: typing.Iterable) -> None: ...
            def __iter__(self) -> typing.Iterator: ...
            def __len__(self) -> int: ...
            @typing.overload
            def __setitem__(self, arg0: int, arg1: Geometry.Angle.Value) -> None:
                """
                Assign list elements using a slice object
                """
            @typing.overload
            def __setitem__(self, arg0: slice, arg1: Geometry.Angle.Values) -> None: ...
            def append(self, x: Geometry.Angle.Value) -> None:
                """
                Add an item to the end of the list
                """
            def clear(self) -> None:
                """
                Clear the contents
                """
            @typing.overload
            def extend(self, L: Geometry.Angle.Values) -> None:
                """
                Extend the list by appending all the items in the given list

                Extend the list by appending all the items in the given list
                """
            @typing.overload
            def extend(self, L: typing.Iterable) -> None: ...
            def insert(self, i: int, x: Geometry.Angle.Value) -> None:
                """
                Insert an item at a given position.
                """
            @typing.overload
            def pop(self) -> Geometry.Angle.Value:
                """
                Remove and return the last item

                Remove and return the item at index ``i``
                """
            @typing.overload
            def pop(self, i: int) -> Geometry.Angle.Value: ...

        def __init__(self, arg0: Atom, arg1: Atom, arg2: Atom) -> None: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @atoms.setter
        def atoms(self, arg0: list[Atom]) -> None:
            pass
        @property
        def values(self) -> list[Geometry.Angle.Value]:
            """
            :type: typing.List[Geometry.Angle.Value]
            """
        @values.setter
        def values(self, arg0: list[Geometry.Angle.Value]) -> None:
            pass

    class Angles:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Geometry.Angle:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.Angles: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.Angles) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Geometry.Angle) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.Angles) -> None: ...
        def append(self, x: Geometry.Angle) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Geometry.Angles) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Geometry.Angle) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Geometry.Angle:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Geometry.Angle: ...

    class Bond:
        class Value:
            def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float) -> None: ...
            @property
            def sigma(self) -> float:
                """
                :type: float
                """
            @sigma.setter
            def sigma(self, arg0: float) -> None:
                pass
            @property
            def sigma_nucleus(self) -> float:
                """
                :type: float
                """
            @sigma_nucleus.setter
            def sigma_nucleus(self, arg0: float) -> None:
                pass
            @property
            def value(self) -> float:
                """
                :type: float
                """
            @value.setter
            def value(self, arg0: float) -> None:
                pass
            @property
            def value_nucleus(self) -> float:
                """
                :type: float
                """
            @value_nucleus.setter
            def value_nucleus(self, arg0: float) -> None:
                pass

        class Values:
            def __bool__(self) -> bool:
                """
                Check whether the list is nonempty
                """
            @typing.overload
            def __delitem__(self, arg0: int) -> None:
                """
                Delete the list elements at index ``i``

                Delete list elements using a slice object
                """
            @typing.overload
            def __delitem__(self, arg0: slice) -> None: ...
            @typing.overload
            def __getitem__(self, arg0: int) -> Geometry.Bond.Value:
                """
                Retrieve list elements using a slice object
                """
            @typing.overload
            def __getitem__(self, s: slice) -> Geometry.Bond.Values: ...
            @typing.overload
            def __init__(self) -> None:
                """
                Copy constructor
                """
            @typing.overload
            def __init__(self, arg0: Geometry.Bond.Values) -> None: ...
            @typing.overload
            def __init__(self, arg0: typing.Iterable) -> None: ...
            def __iter__(self) -> typing.Iterator: ...
            def __len__(self) -> int: ...
            @typing.overload
            def __setitem__(self, arg0: int, arg1: Geometry.Bond.Value) -> None:
                """
                Assign list elements using a slice object
                """
            @typing.overload
            def __setitem__(self, arg0: slice, arg1: Geometry.Bond.Values) -> None: ...
            def append(self, x: Geometry.Bond.Value) -> None:
                """
                Add an item to the end of the list
                """
            def clear(self) -> None:
                """
                Clear the contents
                """
            @typing.overload
            def extend(self, L: Geometry.Bond.Values) -> None:
                """
                Extend the list by appending all the items in the given list

                Extend the list by appending all the items in the given list
                """
            @typing.overload
            def extend(self, L: typing.Iterable) -> None: ...
            def insert(self, i: int, x: Geometry.Bond.Value) -> None:
                """
                Insert an item at a given position.
                """
            @typing.overload
            def pop(self) -> Geometry.Bond.Value:
                """
                Remove and return the last item

                Remove and return the item at index ``i``
                """
            @typing.overload
            def pop(self, i: int) -> Geometry.Bond.Value: ...

        def __init__(self, arg0: Atom, arg1: Atom) -> None: ...
        def set_image(self, arg0: NearestImage) -> None: ...
        @property
        def alpha(self) -> float:
            """
            :type: float
            """
        @alpha.setter
        def alpha(self, arg0: float) -> None:
            pass
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @atoms.setter
        def atoms(self, arg0: list[Atom]) -> None:
            pass
        @property
        def pbc_shift(self) -> list[int]:
            """
            :type: typing.List[int]
            """
        @pbc_shift.setter
        def pbc_shift(self, arg0: list[int]) -> None:
            pass
        @property
        def sym_idx(self) -> int:
            """
            :type: int
            """
        @sym_idx.setter
        def sym_idx(self, arg0: int) -> None:
            pass
        @property
        def type(self) -> int:
            """
            :type: int
            """
        @type.setter
        def type(self, arg0: int) -> None:
            pass
        @property
        def values(self) -> list[Geometry.Bond.Value]:
            """
            :type: typing.List[Geometry.Bond.Value]
            """
        @values.setter
        def values(self, arg0: list[Geometry.Bond.Value]) -> None:
            pass

    class Bonds:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Geometry.Bond:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.Bonds: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.Bonds) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Geometry.Bond) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.Bonds) -> None: ...
        def append(self, x: Geometry.Bond) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Geometry.Bonds) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Geometry.Bond) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Geometry.Bond:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Geometry.Bond: ...

    class Chirality:
        def __init__(self, arg0: Atom, arg1: Atom, arg2: Atom, arg3: Atom) -> None: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @atoms.setter
        def atoms(self, arg0: list[Atom]) -> None:
            pass
        @property
        def sigma(self) -> float:
            """
            :type: float
            """
        @sigma.setter
        def sigma(self, arg0: float) -> None:
            pass
        @property
        def sign(self) -> ChiralityType:
            """
            :type: ChiralityType
            """
        @sign.setter
        def sign(self, arg0: ChiralityType) -> None:
            pass
        @property
        def value(self) -> float:
            """
            :type: float
            """
        @value.setter
        def value(self, arg0: float) -> None:
            pass

    class Chiralitys:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Geometry.Chirality:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.Chiralitys: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.Chiralitys) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Geometry.Chirality) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.Chiralitys) -> None: ...
        def append(self, x: Geometry.Chirality) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Geometry.Chiralitys) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Geometry.Chirality) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Geometry.Chirality:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Geometry.Chirality: ...

    class Harmonic:
        def __init__(self, arg0: Atom) -> None: ...
        @property
        def atom(self) -> Atom:
            """
            :type: Atom
            """
        @atom.setter
        def atom(self, arg0: Atom) -> None:
            pass
        @property
        def sigma(self) -> float:
            """
            :type: float
            """
        @sigma.setter
        def sigma(self, arg0: float) -> None:
            pass

    class Harmonics:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Geometry.Harmonic:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.Harmonics: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.Harmonics) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Geometry.Harmonic) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.Harmonics) -> None: ...
        def append(self, x: Geometry.Harmonic) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Geometry.Harmonics) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Geometry.Harmonic) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Geometry.Harmonic:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Geometry.Harmonic: ...

    class Interval:
        def __init__(self, arg0: Atom, arg1: Atom) -> None: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @atoms.setter
        def atoms(self, arg0: list[Atom]) -> None:
            pass
        @property
        def dmax(self) -> float:
            """
            :type: float
            """
        @dmax.setter
        def dmax(self, arg0: float) -> None:
            pass
        @property
        def dmin(self) -> float:
            """
            :type: float
            """
        @dmin.setter
        def dmin(self, arg0: float) -> None:
            pass
        @property
        def smax(self) -> float:
            """
            :type: float
            """
        @smax.setter
        def smax(self, arg0: float) -> None:
            pass
        @property
        def smin(self) -> float:
            """
            :type: float
            """
        @smin.setter
        def smin(self, arg0: float) -> None:
            pass

    class Intervals:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Geometry.Interval:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.Intervals: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.Intervals) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Geometry.Interval) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.Intervals) -> None: ...
        def append(self, x: Geometry.Interval) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Geometry.Intervals) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Geometry.Interval) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Geometry.Interval:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Geometry.Interval: ...

    class Plane:
        def __init__(self, arg0: list[Atom]) -> None: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @atoms.setter
        def atoms(self, arg0: list[Atom]) -> None:
            pass
        @property
        def label(self) -> str:
            """
            :type: str
            """
        @label.setter
        def label(self, arg0: str) -> None:
            pass
        @property
        def sigma(self) -> float:
            """
            :type: float
            """
        @sigma.setter
        def sigma(self, arg0: float) -> None:
            pass

    class Planes:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Geometry.Plane:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.Planes: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.Planes) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Geometry.Plane) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.Planes) -> None: ...
        def append(self, x: Geometry.Plane) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Geometry.Planes) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Geometry.Plane) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Geometry.Plane:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Geometry.Plane: ...

    class Reporting:
        def get_angle_outliers(self, min_z: float) -> dict: ...
        def get_bond_outliers(self, use_nucleus: bool, min_z: float) -> dict: ...
        def get_chiral_outliers(self, min_z: float) -> dict: ...
        def get_plane_outliers(self, min_z: float) -> dict: ...
        def get_stacking_angle_outliers(self, min_z: float) -> dict: ...
        def get_stacking_dist_outliers(self, min_z: float) -> dict: ...
        def get_summary_table(self, arg0: bool) -> dict: ...
        def get_torsion_outliers(self, min_z: float) -> dict: ...
        def get_vdw_outliers(self, min_z: float) -> dict: ...
        @property
        def angles(self) -> list[tuple[Geometry.Angle, Geometry.Angle.Value, float]]:
            """
            :type: typing.List[typing.Tuple[Geometry.Angle, Geometry.Angle.Value, float]]
            """
        @property
        def bonds(self) -> list[tuple[Geometry.Bond, Geometry.Bind.Value, float]]:
            """
            :type: typing.List[typing.Tuple[Geometry.Bond, Geometry.Bind.Value, float]]
            """
        @property
        def chirs(self) -> list[tuple[Geometry.Chirality, float, float]]:
            """
            :type: typing.List[typing.Tuple[Geometry.Chirality, float, float]]
            """
        @property
        def planes(self) -> list[tuple[Geometry.Plane, float]]:
            """
            :type: typing.List[typing.Tuple[Geometry.Plane, float]]
            """
        @property
        def stackings(self) -> list[tuple[Geometry.Stacking, float, float, float]]:
            """
            :type: typing.List[typing.Tuple[Geometry.Stacking, float, float, float]]
            """
        @property
        def torsions(self) -> list[tuple[Geometry.Torsion, Geometry.Torsion.Value, float]]:
            """
            :type: typing.List[typing.Tuple[Geometry.Torsion, Geometry.Torsion.Value, float]]
            """
        @property
        def vdws(self) -> list[tuple[Geometry.Vdw]]:
            """
            :type: typing.List[typing.Tuple[Geometry.Vdw]]
            """

    class ReportingAngles:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        def __contains__(self, x: tuple[Geometry.Angle, Geometry.Angle.Value, float]) -> bool:
            """
            Return true the container contains ``x``
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        def __eq__(self, arg0: Geometry.ReportingAngles) -> bool: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> tuple[Geometry.Angle, Geometry.Angle.Value, float]:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.ReportingAngles: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.ReportingAngles) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        def __ne__(self, arg0: Geometry.ReportingAngles) -> bool: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: tuple[Geometry.Angle, Geometry.Angle.Value, float]) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.ReportingAngles) -> None: ...
        def append(self, x: tuple[Geometry.Angle, Geometry.Angle.Value, float]) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        def count(self, x: tuple[Geometry.Angle, Geometry.Angle.Value, float]) -> int:
            """
            Return the number of times ``x`` appears in the list
            """
        @typing.overload
        def extend(self, L: Geometry.ReportingAngles) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: tuple[Geometry.Angle, Geometry.Angle.Value, float]) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> tuple[Geometry.Angle, Geometry.Angle.Value, float]:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> tuple[Geometry.Angle, Geometry.Angle.Value, float]: ...
        def remove(self, x: tuple[Geometry.Angle, Geometry.Angle.Value, float]) -> None:
            """
            Remove the first item from the list whose value is x. It is an error if there is no such item.
            """
        __hash__ = None

    class ReportingBonds:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        def __contains__(self, x: tuple[Geometry.Bond, Geometry.Bond.Value, float]) -> bool:
            """
            Return true the container contains ``x``
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        def __eq__(self, arg0: Geometry.ReportingBonds) -> bool: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> tuple[Geometry.Bond, Geometry.Bond.Value, float]:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.ReportingBonds: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.ReportingBonds) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        def __ne__(self, arg0: Geometry.ReportingBonds) -> bool: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: tuple[Geometry.Bond, Geometry.Bond.Value, float]) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.ReportingBonds) -> None: ...
        def append(self, x: tuple[Geometry.Bond, Geometry.Bond.Value, float]) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        def count(self, x: tuple[Geometry.Bond, Geometry.Bond.Value, float]) -> int:
            """
            Return the number of times ``x`` appears in the list
            """
        @typing.overload
        def extend(self, L: Geometry.ReportingBonds) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: tuple[Geometry.Bond, Geometry.Bond.Value, float]) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> tuple[Geometry.Bond, Geometry.Bond.Value, float]:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> tuple[Geometry.Bond, Geometry.Bond.Value, float]: ...
        def remove(self, x: tuple[Geometry.Bond, Geometry.Bond.Value, float]) -> None:
            """
            Remove the first item from the list whose value is x. It is an error if there is no such item.
            """
        __hash__ = None

    class ReportingChirals:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        def __contains__(self, x: tuple[Geometry.Chirality, float, float]) -> bool:
            """
            Return true the container contains ``x``
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        def __eq__(self, arg0: Geometry.ReportingChirals) -> bool: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> tuple[Geometry.Chirality, float, float]:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.ReportingChirals: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.ReportingChirals) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        def __ne__(self, arg0: Geometry.ReportingChirals) -> bool: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: tuple[Geometry.Chirality, float, float]) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.ReportingChirals) -> None: ...
        def append(self, x: tuple[Geometry.Chirality, float, float]) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        def count(self, x: tuple[Geometry.Chirality, float, float]) -> int:
            """
            Return the number of times ``x`` appears in the list
            """
        @typing.overload
        def extend(self, L: Geometry.ReportingChirals) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: tuple[Geometry.Chirality, float, float]) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> tuple[Geometry.Chirality, float, float]:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> tuple[Geometry.Chirality, float, float]: ...
        def remove(self, x: tuple[Geometry.Chirality, float, float]) -> None:
            """
            Remove the first item from the list whose value is x. It is an error if there is no such item.
            """
        __hash__ = None

    class ReportingPlanes:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        def __contains__(self, x: tuple[Geometry.Plane, list[float]]) -> bool:
            """
            Return true the container contains ``x``
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        def __eq__(self, arg0: Geometry.ReportingPlanes) -> bool: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> tuple[Geometry.Plane, list[float]]:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.ReportingPlanes: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.ReportingPlanes) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        def __ne__(self, arg0: Geometry.ReportingPlanes) -> bool: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: tuple[Geometry.Plane, list[float]]) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.ReportingPlanes) -> None: ...
        def append(self, x: tuple[Geometry.Plane, list[float]]) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        def count(self, x: tuple[Geometry.Plane, list[float]]) -> int:
            """
            Return the number of times ``x`` appears in the list
            """
        @typing.overload
        def extend(self, L: Geometry.ReportingPlanes) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: tuple[Geometry.Plane, list[float]]) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> tuple[Geometry.Plane, list[float]]:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> tuple[Geometry.Plane, list[float]]: ...
        def remove(self, x: tuple[Geometry.Plane, list[float]]) -> None:
            """
            Remove the first item from the list whose value is x. It is an error if there is no such item.
            """
        __hash__ = None

    class ReportingStackings:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        def __contains__(self, x: tuple[Geometry.Stacking, float, float, float]) -> bool:
            """
            Return true the container contains ``x``
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        def __eq__(self, arg0: Geometry.ReportingStackings) -> bool: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> tuple[Geometry.Stacking, float, float, float]:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.ReportingStackings: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.ReportingStackings) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        def __ne__(self, arg0: Geometry.ReportingStackings) -> bool: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: tuple[Geometry.Stacking, float, float, float]) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.ReportingStackings) -> None: ...
        def append(self, x: tuple[Geometry.Stacking, float, float, float]) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        def count(self, x: tuple[Geometry.Stacking, float, float, float]) -> int:
            """
            Return the number of times ``x`` appears in the list
            """
        @typing.overload
        def extend(self, L: Geometry.ReportingStackings) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: tuple[Geometry.Stacking, float, float, float]) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> tuple[Geometry.Stacking, float, float, float]:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> tuple[Geometry.Stacking, float, float, float]: ...
        def remove(self, x: tuple[Geometry.Stacking, float, float, float]) -> None:
            """
            Remove the first item from the list whose value is x. It is an error if there is no such item.
            """
        __hash__ = None

    class ReportingTorsions:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        def __contains__(self, x: tuple[Geometry.Torsion, Geometry.Torsion.Value, float]) -> bool:
            """
            Return true the container contains ``x``
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        def __eq__(self, arg0: Geometry.ReportingTorsions) -> bool: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> tuple[Geometry.Torsion, Geometry.Torsion.Value, float]:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.ReportingTorsions: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.ReportingTorsions) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        def __ne__(self, arg0: Geometry.ReportingTorsions) -> bool: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: tuple[Geometry.Torsion, Geometry.Torsion.Value, float]) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.ReportingTorsions) -> None: ...
        def append(self, x: tuple[Geometry.Torsion, Geometry.Torsion.Value, float]) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        def count(self, x: tuple[Geometry.Torsion, Geometry.Torsion.Value, float]) -> int:
            """
            Return the number of times ``x`` appears in the list
            """
        @typing.overload
        def extend(self, L: Geometry.ReportingTorsions) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: tuple[Geometry.Torsion, Geometry.Torsion.Value, float]) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> tuple[Geometry.Torsion, Geometry.Torsion.Value, float]:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> tuple[Geometry.Torsion, Geometry.Torsion.Value, float]: ...
        def remove(self, x: tuple[Geometry.Torsion, Geometry.Torsion.Value, float]) -> None:
            """
            Remove the first item from the list whose value is x. It is an error if there is no such item.
            """
        __hash__ = None

    class ReportingVdws:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        def __contains__(self, x: tuple[Geometry.Vdw, float]) -> bool:
            """
            Return true the container contains ``x``
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        def __eq__(self, arg0: Geometry.ReportingVdws) -> bool: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> tuple[Geometry.Vdw, float]:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.ReportingVdws: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.ReportingVdws) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        def __ne__(self, arg0: Geometry.ReportingVdws) -> bool: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: tuple[Geometry.Vdw, float]) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.ReportingVdws) -> None: ...
        def append(self, x: tuple[Geometry.Vdw, float]) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        def count(self, x: tuple[Geometry.Vdw, float]) -> int:
            """
            Return the number of times ``x`` appears in the list
            """
        @typing.overload
        def extend(self, L: Geometry.ReportingVdws) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: tuple[Geometry.Vdw, float]) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> tuple[Geometry.Vdw, float]:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> tuple[Geometry.Vdw, float]: ...
        def remove(self, x: tuple[Geometry.Vdw, float]) -> None:
            """
            Remove the first item from the list whose value is x. It is an error if there is no such item.
            """
        __hash__ = None

    class Special:
        def __init__(self, arg0: Atom) -> None: ...
        @property
        def atom(self) -> Atom:
            """
            :type: Atom
            """
        @atom.setter
        def atom(self, arg0: Atom) -> None:
            pass
        @property
        def mat_u(self) -> Mat33:
            """
            :type: Mat33
            """
        @mat_u.setter
        def mat_u(self, arg0: Mat33) -> None:
            pass
        @property
        def sigma_t(self) -> float:
            """
            :type: float
            """
        @sigma_t.setter
        def sigma_t(self, arg0: float) -> None:
            pass
        @property
        def sigma_u(self) -> float:
            """
            :type: float
            """
        @sigma_u.setter
        def sigma_u(self, arg0: float) -> None:
            pass
        @property
        def trans_t(self) -> Transform:
            """
            :type: Transform
            """
        @trans_t.setter
        def trans_t(self, arg0: Transform) -> None:
            pass
        @property
        def u_val_incl(self) -> bool:
            """
            :type: bool
            """
        @u_val_incl.setter
        def u_val_incl(self, arg0: bool) -> None:
            pass

    class Specials:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Geometry.Special:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.Specials: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.Specials) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Geometry.Special) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.Specials) -> None: ...
        def append(self, x: Geometry.Special) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Geometry.Specials) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Geometry.Special) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Geometry.Special:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Geometry.Special: ...

    class Stacking:
        def __init__(self, arg0: list[Atom], arg1: list[Atom]) -> None: ...
        @property
        def angle(self) -> float:
            """
            :type: float
            """
        @angle.setter
        def angle(self, arg0: float) -> None:
            pass
        @property
        def dist(self) -> float:
            """
            :type: float
            """
        @dist.setter
        def dist(self, arg0: float) -> None:
            pass
        @property
        def planes(self) -> list[list[Atom]]:
            """
            :type: typing.List[typing.List[Atom]]
            """
        @planes.setter
        def planes(self, arg0: list[list[Atom]]) -> None:
            pass
        @property
        def sd_angle(self) -> float:
            """
            :type: float
            """
        @sd_angle.setter
        def sd_angle(self, arg0: float) -> None:
            pass
        @property
        def sd_dist(self) -> float:
            """
            :type: float
            """
        @sd_dist.setter
        def sd_dist(self, arg0: float) -> None:
            pass

    class Stackings:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Geometry.Stacking:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.Stackings: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.Stackings) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Geometry.Stacking) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.Stackings) -> None: ...
        def append(self, x: Geometry.Stacking) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Geometry.Stackings) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Geometry.Stacking) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Geometry.Stacking:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Geometry.Stacking: ...

    class Torsion:
        class Value:
            def __init__(self, arg0: float, arg1: float, arg2: int) -> None: ...
            @property
            def label(self) -> str:
                """
                :type: str
                """
            @label.setter
            def label(self, arg0: str) -> None:
                pass
            @property
            def period(self) -> int:
                """
                :type: int
                """
            @period.setter
            def period(self, arg0: int) -> None:
                pass
            @property
            def sigma(self) -> float:
                """
                :type: float
                """
            @sigma.setter
            def sigma(self, arg0: float) -> None:
                pass
            @property
            def value(self) -> float:
                """
                :type: float
                """
            @value.setter
            def value(self, arg0: float) -> None:
                pass

        class Values:
            def __bool__(self) -> bool:
                """
                Check whether the list is nonempty
                """
            @typing.overload
            def __delitem__(self, arg0: int) -> None:
                """
                Delete the list elements at index ``i``

                Delete list elements using a slice object
                """
            @typing.overload
            def __delitem__(self, arg0: slice) -> None: ...
            @typing.overload
            def __getitem__(self, arg0: int) -> Geometry.Torsion.Value:
                """
                Retrieve list elements using a slice object
                """
            @typing.overload
            def __getitem__(self, s: slice) -> Geometry.Torsion.Values: ...
            @typing.overload
            def __init__(self) -> None:
                """
                Copy constructor
                """
            @typing.overload
            def __init__(self, arg0: Geometry.Torsion.Values) -> None: ...
            @typing.overload
            def __init__(self, arg0: typing.Iterable) -> None: ...
            def __iter__(self) -> typing.Iterator: ...
            def __len__(self) -> int: ...
            @typing.overload
            def __setitem__(self, arg0: int, arg1: Geometry.Torsion.Value) -> None:
                """
                Assign list elements using a slice object
                """
            @typing.overload
            def __setitem__(self, arg0: slice, arg1: Geometry.Torsion.Values) -> None: ...
            def append(self, x: Geometry.Torsion.Value) -> None:
                """
                Add an item to the end of the list
                """
            def clear(self) -> None:
                """
                Clear the contents
                """
            @typing.overload
            def extend(self, L: Geometry.Torsion.Values) -> None:
                """
                Extend the list by appending all the items in the given list

                Extend the list by appending all the items in the given list
                """
            @typing.overload
            def extend(self, L: typing.Iterable) -> None: ...
            def insert(self, i: int, x: Geometry.Torsion.Value) -> None:
                """
                Insert an item at a given position.
                """
            @typing.overload
            def pop(self) -> Geometry.Torsion.Value:
                """
                Remove and return the last item

                Remove and return the item at index ``i``
                """
            @typing.overload
            def pop(self, i: int) -> Geometry.Torsion.Value: ...

        def __init__(self, arg0: Atom, arg1: Atom, arg2: Atom, arg3: Atom) -> None: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @atoms.setter
        def atoms(self, arg0: list[Atom]) -> None:
            pass
        @property
        def values(self) -> list[Geometry.Torsion.Value]:
            """
            :type: typing.List[Geometry.Torsion.Value]
            """
        @values.setter
        def values(self, arg0: list[Geometry.Torsion.Value]) -> None:
            pass

    class Torsions:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Geometry.Torsion:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.Torsions: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.Torsions) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Geometry.Torsion) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.Torsions) -> None: ...
        def append(self, x: Geometry.Torsion) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Geometry.Torsions) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Geometry.Torsion) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Geometry.Torsion:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Geometry.Torsion: ...

    class Vdw:
        def __init__(self, arg0: Atom, arg1: Atom) -> None: ...
        def set_image(self, arg0: NearestImage) -> None: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @atoms.setter
        def atoms(self, arg0: list[Atom]) -> None:
            pass
        @property
        def pbc_shift(self) -> list[int]:
            """
            :type: typing.List[int]
            """
        @pbc_shift.setter
        def pbc_shift(self, arg0: list[int]) -> None:
            pass
        @property
        def sigma(self) -> float:
            """
            :type: float
            """
        @sigma.setter
        def sigma(self, arg0: float) -> None:
            pass
        @property
        def sym_idx(self) -> int:
            """
            :type: int
            """
        @sym_idx.setter
        def sym_idx(self, arg0: int) -> None:
            pass
        @property
        def type(self) -> int:
            """
            :type: int
            """
        @type.setter
        def type(self, arg0: int) -> None:
            pass
        @property
        def value(self) -> float:
            """
            :type: float
            """
        @value.setter
        def value(self, arg0: float) -> None:
            pass

    class Vdws:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Geometry.Vdw:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Geometry.Vdws: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Geometry.Vdws) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Geometry.Vdw) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Geometry.Vdws) -> None: ...
        def append(self, x: Geometry.Vdw) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Geometry.Vdws) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Geometry.Vdw) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Geometry.Vdw:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Geometry.Vdw: ...

    def __init__(self, st: Structure, ener_lib: EnerLib = None) -> None: ...
    def calc(
        self,
        use_nucleus: bool,
        check_only: bool,
        wbond: float = 1,
        wangle: float = 1,
        wtors: float = 1,
        wchir: float = 1,
        wplane: float = 1,
        wstack: float = 1,
        wvdw: float = 1,
    ) -> float: ...
    def calc_adp_restraint(self, arg0: bool, arg1: float) -> float: ...
    def clear_target(self) -> None: ...
    def finalize_restraints(self) -> None: ...
    def load_topo(self, arg0: Topo) -> None: ...
    def setup_nonbonded(self) -> None: ...
    def setup_target(self, arg0: bool, arg1: int) -> None: ...
    @property
    def adpr_d_power(self) -> float:
        """
        :type: float
        """
    @adpr_d_power.setter
    def adpr_d_power(self, arg0: float) -> None:
        pass
    @property
    def adpr_exp_fac(self) -> float:
        """
        :type: float
        """
    @adpr_exp_fac.setter
    def adpr_exp_fac(self, arg0: float) -> None:
        pass
    @property
    def adpr_max_dist(self) -> float:
        """
        :type: float
        """
    @adpr_max_dist.setter
    def adpr_max_dist(self, arg0: float) -> None:
        pass
    @property
    def angles(self) -> Geometry.Angles:
        """
        :type: Geometry.Angles
        """
    @property
    def bonds(self) -> Geometry.Bonds:
        """
        :type: Geometry.Bonds
        """
    @property
    def chirs(self) -> Geometry.Chiralitys:
        """
        :type: Geometry.Chiralitys
        """
    @property
    def dinc_dummy(self) -> float:
        """
        :type: float
        """
    @dinc_dummy.setter
    def dinc_dummy(self, arg0: float) -> None:
        pass
    @property
    def dinc_torsion_all(self) -> float:
        """
        :type: float
        """
    @dinc_torsion_all.setter
    def dinc_torsion_all(self, arg0: float) -> None:
        pass
    @property
    def dinc_torsion_c(self) -> float:
        """
        :type: float
        """
    @dinc_torsion_c.setter
    def dinc_torsion_c(self, arg0: float) -> None:
        pass
    @property
    def dinc_torsion_n(self) -> float:
        """
        :type: float
        """
    @dinc_torsion_n.setter
    def dinc_torsion_n(self, arg0: float) -> None:
        pass
    @property
    def dinc_torsion_o(self) -> float:
        """
        :type: float
        """
    @dinc_torsion_o.setter
    def dinc_torsion_o(self, arg0: float) -> None:
        pass
    @property
    def harmonics(self) -> Geometry.Harmonics:
        """
        :type: Geometry.Harmonics
        """
    @property
    def hbond_dinc_ad(self) -> float:
        """
        :type: float
        """
    @hbond_dinc_ad.setter
    def hbond_dinc_ad(self, arg0: float) -> None:
        pass
    @property
    def hbond_dinc_ah(self) -> float:
        """
        :type: float
        """
    @hbond_dinc_ah.setter
    def hbond_dinc_ah(self, arg0: float) -> None:
        pass
    @property
    def intervals(self) -> Geometry.Intervals:
        """
        :type: Geometry.Intervals
        """
    @property
    def planes(self) -> Geometry.Planes:
        """
        :type: Geometry.Planes
        """
    @property
    def reporting(self) -> Geometry.Reporting:
        """
        :type: Geometry.Reporting
        """
    @property
    def ridge_dmax(self) -> float:
        """
        :type: float
        """
    @ridge_dmax.setter
    def ridge_dmax(self, arg0: float) -> None:
        pass
    @property
    def ridge_sigma(self) -> float:
        """
        :type: float
        """
    @ridge_sigma.setter
    def ridge_sigma(self, arg0: float) -> None:
        pass
    @property
    def ridge_symm(self) -> bool:
        """
        :type: bool
        """
    @ridge_symm.setter
    def ridge_symm(self, arg0: bool) -> None:
        pass
    @property
    def specials(self) -> Geometry.Specials:
        """
        :type: Geometry.Specials
        """
    @property
    def stackings(self) -> Geometry.Stackings:
        """
        :type: Geometry.Stackings
        """
    @property
    def target(self) -> GeomTarget:
        """
        :type: GeomTarget
        """
    @property
    def torsions(self) -> Geometry.Torsions:
        """
        :type: Geometry.Torsions
        """
    @property
    def vdw_sdi_dummy(self) -> float:
        """
        :type: float
        """
    @vdw_sdi_dummy.setter
    def vdw_sdi_dummy(self, arg0: float) -> None:
        pass
    @property
    def vdw_sdi_hbond(self) -> float:
        """
        :type: float
        """
    @vdw_sdi_hbond.setter
    def vdw_sdi_hbond(self, arg0: float) -> None:
        pass
    @property
    def vdw_sdi_metal(self) -> float:
        """
        :type: float
        """
    @vdw_sdi_metal.setter
    def vdw_sdi_metal(self, arg0: float) -> None:
        pass
    @property
    def vdw_sdi_torsion(self) -> float:
        """
        :type: float
        """
    @vdw_sdi_torsion.setter
    def vdw_sdi_torsion(self, arg0: float) -> None:
        pass
    @property
    def vdw_sdi_vdw(self) -> float:
        """
        :type: float
        """
    @vdw_sdi_vdw.setter
    def vdw_sdi_vdw(self, arg0: float) -> None:
        pass
    @property
    def vdws(self) -> Geometry.Vdws:
        """
        :type: Geometry.Vdws
        """

class ComplexGridBase(GridMeta):
    class Point:
        def __repr__(self) -> str: ...
        @property
        def u(self) -> int:
            """
            :type: int
            """
        @property
        def v(self) -> int:
            """
            :type: int
            """
        @property
        def value(self) -> complex:
            """
            :type: complex
            """
        @value.setter
        def value(self, arg1: complex) -> None:
            pass
        @property
        def w(self) -> int:
            """
            :type: int
            """
    def __iter__(self) -> typing.Iterator: ...
    def fill(self, value: complex) -> None: ...
    def index_to_point(self, arg0: int) -> ComplexGridBase.Point: ...
    def point_to_index(self, arg0: ComplexGridBase.Point) -> int: ...
    def sum(self) -> complex: ...
    @property
    def array(self) -> numpy.ndarray[numpy.complex64]:
        """
        :type: numpy.ndarray[numpy.complex64]
        """

class GridSizeRounding:
    """
    Members:

      Nearest

      Up

      Down
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Down: gemmi.GridSizeRounding  # value = <GridSizeRounding.Down: 2>
    Nearest: gemmi.GridSizeRounding  # value = <GridSizeRounding.Nearest: 0>
    Up: gemmi.GridSizeRounding  # value = <GridSizeRounding.Up: 1>

class GroupOps:
    def __deepcopy__(self, memo: dict) -> GroupOps: ...
    def __eq__(self, arg0: GroupOps) -> bool: ...
    def __init__(self, arg0: list[Op]) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def add_inversion(self) -> bool: ...
    def add_missing_elements(self) -> None: ...
    def centric_flag_array(self, arg0: numpy.ndarray[numpy.int32]) -> numpy.ndarray[bool]: ...
    def change_basis_backward(self, cob: Op) -> None:
        """
        Applies inverse of the change-of-basis operator (in place).
        """
    def change_basis_forward(self, cob: Op) -> None:
        """
        Applies the change-of-basis operator (in place).
        """
    def derive_symmorphic(self) -> GroupOps: ...
    def epsilon_factor(self, arg0: list[int]) -> int: ...
    def epsilon_factor_array(self, arg0: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.int32]: ...
    def epsilon_factor_without_centering(self, arg0: list[int]) -> int: ...
    def epsilon_factor_without_centering_array(
        self,
        arg0: numpy.ndarray[numpy.int32],
    ) -> numpy.ndarray[numpy.int32]: ...
    def find_centering(self) -> str: ...
    def find_grid_factors(self) -> list[int]:
        """
        Minimal multiplicity for real-space grid (e.g. 1,1,6 for P61).
        """
    def has_same_centring(self, arg0: GroupOps) -> bool: ...
    def has_same_rotations(self, arg0: GroupOps) -> bool: ...
    def is_centrosymmetric(self) -> bool: ...
    def is_reflection_centric(self, arg0: list[int]) -> bool: ...
    def is_systematically_absent(self, arg0: list[int]) -> bool: ...
    def systematic_absences(self, arg0: numpy.ndarray[numpy.int32]) -> numpy.ndarray[bool]: ...
    @property
    def cen_ops(self) -> list[list[int]]:
        """
        Centering vectors.

        :type: typing.List[typing.List[int]]
        """
    @cen_ops.setter
    def cen_ops(self, arg0: list[list[int]]) -> None:
        """
        Centering vectors.
        """
    @property
    def sym_ops(self) -> list[Op]:
        """
        Symmetry operations (to be combined with centering vectors).

        :type: typing.List[Op]
        """
    @sym_ops.setter
    def sym_ops(self, arg0: list[Op]) -> None:
        """
        Symmetry operations (to be combined with centering vectors).
        """
    __hash__ = None

class GruberVector:
    @typing.overload
    def __init__(self, arg0: list[float]) -> None: ...
    @typing.overload
    def __init__(self, cell: UnitCell, centring: str, track_change_of_basis: bool = False) -> None: ...
    @typing.overload
    def __init__(self, cell: UnitCell, sg: SpaceGroup, track_change_of_basis: bool = False) -> None: ...
    def __repr__(self) -> str: ...
    def buerger_reduce(self) -> int: ...
    def cell_parameters(self) -> tuple: ...
    def get_cell(self) -> UnitCell: ...
    def is_buerger(self, epsilon: float = 1e-09) -> bool: ...
    def is_niggli(self, epsilon: float = 1e-09) -> bool: ...
    def is_normalized(self) -> bool: ...
    def niggli_reduce(self, epsilon: float = 1e-09, iteration_limit: int = 100) -> int: ...
    def niggli_step(self, epsilon: float) -> bool: ...
    def normalize(self, epsilon: float = 1e-09) -> None: ...
    def selling(self) -> SellingVector: ...
    @property
    def change_of_basis(self) -> Op:
        """
        :type: Op
        """
    @property
    def parameters(self) -> tuple:
        """
        :type: tuple
        """

class Helix:
    class HelixClass:
        """
        Members:

          UnknownHelix

          RAlpha

          ROmega

          RPi

          RGamma

          R310

          LAlpha

          LOmega

          LGamma

          Helix27

          HelixPolyProlineNone
        """

        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        Helix27: gemmi.Helix.HelixClass  # value = <HelixClass.Helix27: 9>
        HelixPolyProlineNone: gemmi.Helix.HelixClass  # value = <HelixClass.HelixPolyProlineNone: 10>
        LAlpha: gemmi.Helix.HelixClass  # value = <HelixClass.LAlpha: 6>
        LGamma: gemmi.Helix.HelixClass  # value = <HelixClass.LGamma: 8>
        LOmega: gemmi.Helix.HelixClass  # value = <HelixClass.LOmega: 7>
        R310: gemmi.Helix.HelixClass  # value = <HelixClass.R310: 5>
        RAlpha: gemmi.Helix.HelixClass  # value = <HelixClass.RAlpha: 1>
        RGamma: gemmi.Helix.HelixClass  # value = <HelixClass.RGamma: 4>
        ROmega: gemmi.Helix.HelixClass  # value = <HelixClass.ROmega: 2>
        RPi: gemmi.Helix.HelixClass  # value = <HelixClass.RPi: 3>
        UnknownHelix: gemmi.Helix.HelixClass  # value = <HelixClass.UnknownHelix: 0>
    def __init__(self) -> None: ...
    @property
    def end(self) -> AtomAddress:
        """
        :type: AtomAddress
        """
    @end.setter
    def end(self, arg0: AtomAddress) -> None:
        pass
    @property
    def length(self) -> int:
        """
        :type: int
        """
    @length.setter
    def length(self, arg0: int) -> None:
        pass
    @property
    def pdb_helix_class(self) -> Helix.HelixClass:
        """
        :type: Helix.HelixClass
        """
    @pdb_helix_class.setter
    def pdb_helix_class(self, arg0: Helix.HelixClass) -> None:
        pass
    @property
    def start(self) -> AtomAddress:
        """
        :type: AtomAddress
        """
    @start.setter
    def start(self, arg0: AtomAddress) -> None:
        pass

class HelixList:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Helix:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> HelixList: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: HelixList) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Helix) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: HelixList) -> None: ...
    def append(self, x: Helix) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: HelixList) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Helix) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Helix:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Helix: ...

class HklMatch:
    def __init__(self, hkl: numpy.ndarray[numpy.int32], ref: numpy.ndarray[numpy.int32]) -> None: ...
    def aligned(self, arg0: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]: ...
    @property
    def pos(self) -> list[int]:
        """
        :type: typing.List[int]
        """

class HowToNameCopiedChain:
    """
    Members:

      Short

      AddNumber

      Dup
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    AddNumber: gemmi.HowToNameCopiedChain  # value = <HowToNameCopiedChain.AddNumber: 1>
    Dup: gemmi.HowToNameCopiedChain  # value = <HowToNameCopiedChain.Dup: 2>
    Short: gemmi.HowToNameCopiedChain  # value = <HowToNameCopiedChain.Short: 0>

class HydrogenChange:
    """
    Members:

      NoChange

      Shift

      Remove

      ReAdd

      ReAddButWater
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    NoChange: gemmi.HydrogenChange  # value = <HydrogenChange.NoChange: 0>
    ReAdd: gemmi.HydrogenChange  # value = <HydrogenChange.ReAdd: 3>
    ReAddButWater: gemmi.HydrogenChange  # value = <HydrogenChange.ReAddButWater: 4>
    Remove: gemmi.HydrogenChange  # value = <HydrogenChange.Remove: 2>
    Shift: gemmi.HydrogenChange  # value = <HydrogenChange.Shift: 1>

class IT92Coef:
    def calculate_density_iso(self, r2: numpy.ndarray[numpy.float64], B: float) -> object: ...
    def calculate_sf(self, stol2: numpy.ndarray[numpy.float64]) -> object: ...
    def get_coefs(self) -> list[float]: ...
    def set_coefs(self, arg0: list[float]) -> None: ...
    @property
    def a(self) -> list[float]:
        """
        :type: typing.List[float]
        """
    @property
    def b(self) -> list[float]:
        """
        :type: typing.List[float]
        """
    @property
    def c(self) -> float:
        """
        :type: float
        """

class InfoMap:
    def __bool__(self) -> bool:
        """
        Check whether the map is nonempty
        """
    @typing.overload
    def __contains__(self, arg0: object) -> bool: ...
    @typing.overload
    def __contains__(self, arg0: str) -> bool: ...
    def __delitem__(self, arg0: str) -> None: ...
    def __getitem__(self, arg0: str) -> str: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this map.
        """
    def __setitem__(self, arg0: str, arg1: str) -> None: ...
    def items(self) -> typing.ItemsView[str, str]: ...
    def keys(self) -> typing.KeysView[str]: ...
    def values(self) -> typing.ValuesView[str]: ...

class Int8GridBase(GridMeta):
    class Point:
        def __repr__(self) -> str: ...
        @property
        def u(self) -> int:
            """
            :type: int
            """
        @property
        def v(self) -> int:
            """
            :type: int
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        @value.setter
        def value(self, arg1: int) -> None:
            pass
        @property
        def w(self) -> int:
            """
            :type: int
            """
    def __iter__(self) -> typing.Iterator: ...
    def fill(self, value: int) -> None: ...
    def get_nonzero_extent(self) -> FractionalBox: ...
    def index_to_point(self, arg0: int) -> Int8GridBase.Point: ...
    def point_to_index(self, arg0: Int8GridBase.Point) -> int: ...
    def sum(self) -> int: ...
    @property
    def array(self) -> numpy.ndarray[numpy.int8]:
        """
        :type: numpy.ndarray[numpy.int8]
        """

class Int8Grid(Int8GridBase, GridMeta):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(
        self,
        arg0: numpy.ndarray[numpy.int8],
        cell: UnitCell = None,
        spacegroup: SpaceGroup = None,
    ) -> None: ...
    @typing.overload
    def __init__(self, nx: int, ny: int, nz: int) -> None: ...
    def __repr__(self) -> str: ...
    def change_values(self, old_value: int, new_value: int) -> None: ...
    def clone(self) -> Int8Grid: ...
    def copy_metadata_from(self, arg0: GridMeta) -> None: ...
    def get_nearest_point(self, arg0: Position) -> Int8GridBase.Point: ...
    def get_point(self, arg0: int, arg1: int, arg2: int) -> Int8GridBase.Point: ...
    def get_subarray(self, start: list[int], shape: list[int]) -> numpy.ndarray[numpy.int8]: ...
    def get_value(self, arg0: int, arg1: int, arg2: int) -> int: ...
    def mask_points_in_constant_radius(self, model: Model, radius: float, value: int) -> None: ...
    def masked_asu(self) -> MaskedInt8Grid: ...
    def point_to_fractional(self, arg0: Int8GridBase.Point) -> Fractional: ...
    def point_to_position(self, arg0: Int8GridBase.Point) -> Position: ...
    def resample_to(self, dest: Int8Grid, order: int) -> None: ...
    def set_points_around(self, position: Position, radius: float, value: int, use_pbc: bool = True) -> None: ...
    def set_size(self, arg0: int, arg1: int, arg2: int) -> None: ...
    def set_size_from_spacing(self, spacing: float, rounding: GridSizeRounding) -> None: ...
    def set_subarray(self, arr: numpy.ndarray[numpy.int8], start: list[int]) -> None: ...
    def set_unit_cell(self, arg0: UnitCell) -> None: ...
    def set_value(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    def setup_from(self, st: Structure, spacing: float) -> None: ...
    def symmetrize_abs_max(self) -> None: ...
    def symmetrize_max(self) -> None: ...
    def symmetrize_min(self) -> None: ...
    def symmetrize_sum(self) -> None: ...
    @property
    def spacing(self) -> tuple:
        """
        :type: tuple
        """

class IntAsuData:
    def __getitem__(self, index: int) -> IntHklValue: ...
    def __init__(
        self,
        cell: UnitCell,
        sg: SpaceGroup,
        miller_array: numpy.ndarray[numpy.int32],
        value_array: numpy.ndarray[numpy.int32],
    ) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def copy(self) -> IntAsuData: ...
    def count_equal_values(self, arg0: IntAsuData) -> int: ...
    def ensure_asu(self, tnt_asu: bool = False) -> None: ...
    def ensure_sorted(self) -> None: ...
    def make_1_d2_array(self) -> numpy.ndarray[numpy.float32]: ...
    def make_d_array(self) -> numpy.ndarray[numpy.float32]: ...
    @property
    def miller_array(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    @property
    def spacegroup(self) -> SpaceGroup:
        """
        :type: SpaceGroup
        """
    @spacegroup.setter
    def spacegroup(self, arg0: SpaceGroup) -> None:
        pass
    @property
    def unit_cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @unit_cell.setter
    def unit_cell(self, arg0: UnitCell) -> None:
        pass
    @property
    def value_array(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """

class IntHklValue:
    def __repr__(self) -> str: ...
    @property
    def hkl(self) -> list[int]:
        """
        :type: typing.List[int]
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    @value.setter
    def value(self, arg0: int) -> None:
        pass

class Intensities:
    def __init__(self) -> None: ...
    def merge_in_place(self, itype: DataType) -> None: ...
    def read_mtz(self, mtz: Mtz, type: DataType) -> None: ...
    def remove_systematic_absences(self) -> None: ...
    def resolution_range(self) -> list[float]: ...
    def set_data(
        self,
        cell: UnitCell,
        sg: SpaceGroup,
        miller_array: numpy.ndarray[numpy.int32],
        value_array: numpy.ndarray[numpy.float64],
        sigma_array: numpy.ndarray[numpy.float64],
    ) -> None: ...
    @property
    def isign_array(self) -> numpy.ndarray[numpy.int16]:
        """
        :type: numpy.ndarray[numpy.int16]
        """
    @property
    def miller_array(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    @property
    def nobs_array(self) -> numpy.ndarray[numpy.int16]:
        """
        :type: numpy.ndarray[numpy.int16]
        """
    @property
    def sigma_array(self) -> numpy.ndarray[numpy.float64]:
        """
        :type: numpy.ndarray[numpy.float64]
        """
    @property
    def spacegroup(self) -> SpaceGroup:
        """
        :type: SpaceGroup
        """
    @spacegroup.setter
    def spacegroup(self, arg0: SpaceGroup) -> None:
        pass
    @property
    def type(self) -> DataType:
        """
        :type: DataType
        """
    @type.setter
    def type(self, arg0: DataType) -> None:
        pass
    @property
    def unit_cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @unit_cell.setter
    def unit_cell(self, arg0: UnitCell) -> None:
        pass
    @property
    def value_array(self) -> numpy.ndarray[numpy.float64]:
        """
        :type: numpy.ndarray[numpy.float64]
        """

class LLX:
    def __init__(
        self,
        cell: UnitCell,
        sg: SpaceGroup,
        atoms: list[Atom],
        mott_bethe: bool,
        refine_xyz: bool,
        adp_mode: int,
        refine_h: bool,
    ) -> None: ...
    def calc_grad(self, arg0: FloatGrid, arg1: float) -> list[float]: ...
    def fisher_diag_from_table(self) -> list[float]: ...
    def fisher_for_coo(self) -> tuple: ...
    def make_fisher_table_diag_fast(self, arg0: float, arg1: float, arg2: TableS3) -> None: ...
    def set_ncs(self, arg0: list[Transform]) -> None: ...
    @property
    def aa(self) -> list[list[float]]:
        """
        :type: typing.List[typing.List[float]]
        """
    @property
    def bb(self) -> list[list[float]]:
        """
        :type: typing.List[typing.List[float]]
        """
    @property
    def pp1(self) -> list[list[float]]:
        """
        :type: typing.List[typing.List[float]]
        """
    @property
    def table_bs(self) -> list[float]:
        """
        :type: typing.List[float]
        """

class LinkHunt:
    class Match:
        @property
        def bond_length(self) -> float:
            """
            :type: float
            """
        @property
        def chem_link(self) -> ChemLink:
            """
            :type: ChemLink
            """
        @property
        def chem_link_count(self) -> int:
            """
            :type: int
            """
        @property
        def conn(self) -> Connection:
            """
            :type: Connection
            """
        @property
        def cra1(self) -> CRA:
            """
            :type: CRA
            """
        @property
        def cra2(self) -> CRA:
            """
            :type: CRA
            """
        @property
        def same_image(self) -> bool:
            """
            :type: bool
            """
    def __init__(self) -> None: ...
    def find_possible_links(
        self,
        st: Structure,
        bond_margin: float,
        radius_margin: float,
        ignore: ContactSearch.Ignore = ...,
    ) -> list[LinkHunt.Match]: ...
    def index_chem_links(self, monlib: MonLib, use_alias: bool = True) -> None: ...

class MapSetup:
    """
    Members:

      Full

      NoSymmetry

      ReorderOnly
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Full: gemmi.MapSetup  # value = <MapSetup.Full: 0>
    NoSymmetry: gemmi.MapSetup  # value = <MapSetup.NoSymmetry: 1>
    ReorderOnly: gemmi.MapSetup  # value = <MapSetup.ReorderOnly: 2>

class MaskedFloatGrid:
    def __iter__(self) -> typing.Iterator: ...
    @property
    def grid(self) -> FloatGrid:
        """
        :type: FloatGrid
        """
    @property
    def mask_array(self) -> numpy.ndarray[numpy.int8]:
        """
        :type: numpy.ndarray[numpy.int8]
        """

class MaskedInt8Grid:
    def __iter__(self) -> typing.Iterator: ...
    @property
    def grid(self) -> Int8Grid:
        """
        :type: Int8Grid
        """
    @property
    def mask_array(self) -> numpy.ndarray[numpy.int8]:
        """
        :type: numpy.ndarray[numpy.int8]
        """

class Mat33:
    def __add__(self, arg0: Mat33) -> Mat33: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: list[list[float]]) -> None: ...
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Mat33) -> Mat33: ...
    def approx(self, other: Mat33, epsilon: float) -> bool: ...
    def column_copy(self, arg0: int) -> Vec3: ...
    def determinant(self) -> float: ...
    def fromlist(self, arg0: list[list[float]]) -> None: ...
    def inverse(self) -> Mat33: ...
    def is_identity(self) -> bool: ...
    def left_multiply(self, arg0: Vec3) -> Vec3: ...
    @typing.overload
    def multiply(self, arg0: Mat33) -> Mat33: ...
    @typing.overload
    def multiply(self, arg0: Vec3) -> Vec3: ...
    def multiply_by_diagonal(self, arg0: Vec3) -> Mat33: ...
    def row_copy(self, arg0: int) -> Vec3: ...
    def tolist(self) -> list[list[float]]: ...
    def trace(self) -> float: ...
    def transpose(self) -> Mat33: ...

class Metadata:
    @property
    def authors(self) -> list[str]:
        """
        :type: typing.List[str]
        """
    @authors.setter
    def authors(self, arg0: list[str]) -> None:
        pass
    @property
    def refinement(self) -> list[RefinementInfo]:
        """
        :type: typing.List[RefinementInfo]
        """
    @refinement.setter
    def refinement(self, arg0: list[RefinementInfo]) -> None:
        pass
    @property
    def software(self) -> list[SoftwareItem]:
        """
        :type: typing.List[SoftwareItem]
        """
    @software.setter
    def software(self, arg0: list[SoftwareItem]) -> None:
        pass

class MmcifOutputGroups:
    def __init__(self, all: bool, **kwargs) -> None: ...
    @property
    def assembly(self) -> bool:
        """
        :type: bool
        """
    @assembly.setter
    def assembly(self, arg1: bool) -> None:
        pass
    @property
    def atom_type(self) -> bool:
        """
        :type: bool
        """
    @atom_type.setter
    def atom_type(self, arg1: bool) -> None:
        pass
    @property
    def atoms(self) -> bool:
        """
        :type: bool
        """
    @atoms.setter
    def atoms(self, arg1: bool) -> None:
        pass
    @property
    def author(self) -> bool:
        """
        :type: bool
        """
    @author.setter
    def author(self, arg1: bool) -> None:
        pass
    @property
    def block_name(self) -> bool:
        """
        :type: bool
        """
    @block_name.setter
    def block_name(self, arg1: bool) -> None:
        pass
    @property
    def cell(self) -> bool:
        """
        :type: bool
        """
    @cell.setter
    def cell(self, arg1: bool) -> None:
        pass
    @property
    def chem_comp(self) -> bool:
        """
        :type: bool
        """
    @chem_comp.setter
    def chem_comp(self, arg1: bool) -> None:
        pass
    @property
    def cis(self) -> bool:
        """
        :type: bool
        """
    @cis.setter
    def cis(self, arg1: bool) -> None:
        pass
    @property
    def conn(self) -> bool:
        """
        :type: bool
        """
    @conn.setter
    def conn(self, arg1: bool) -> None:
        pass
    @property
    def database_status(self) -> bool:
        """
        :type: bool
        """
    @database_status.setter
    def database_status(self, arg1: bool) -> None:
        pass
    @property
    def diffrn(self) -> bool:
        """
        :type: bool
        """
    @diffrn.setter
    def diffrn(self, arg1: bool) -> None:
        pass
    @property
    def entity(self) -> bool:
        """
        :type: bool
        """
    @entity.setter
    def entity(self, arg1: bool) -> None:
        pass
    @property
    def entity_poly(self) -> bool:
        """
        :type: bool
        """
    @entity_poly.setter
    def entity_poly(self, arg1: bool) -> None:
        pass
    @property
    def entity_poly_seq(self) -> bool:
        """
        :type: bool
        """
    @entity_poly_seq.setter
    def entity_poly_seq(self, arg1: bool) -> None:
        pass
    @property
    def entry(self) -> bool:
        """
        :type: bool
        """
    @entry.setter
    def entry(self, arg1: bool) -> None:
        pass
    @property
    def exptl(self) -> bool:
        """
        :type: bool
        """
    @exptl.setter
    def exptl(self, arg1: bool) -> None:
        pass
    @property
    def group_pdb(self) -> bool:
        """
        :type: bool
        """
    @group_pdb.setter
    def group_pdb(self, arg1: bool) -> None:
        pass
    @property
    def ncs(self) -> bool:
        """
        :type: bool
        """
    @ncs.setter
    def ncs(self, arg1: bool) -> None:
        pass
    @property
    def origx(self) -> bool:
        """
        :type: bool
        """
    @origx.setter
    def origx(self, arg1: bool) -> None:
        pass
    @property
    def refine(self) -> bool:
        """
        :type: bool
        """
    @refine.setter
    def refine(self, arg1: bool) -> None:
        pass
    @property
    def reflns(self) -> bool:
        """
        :type: bool
        """
    @reflns.setter
    def reflns(self, arg1: bool) -> None:
        pass
    @property
    def scale(self) -> bool:
        """
        :type: bool
        """
    @scale.setter
    def scale(self, arg1: bool) -> None:
        pass
    @property
    def software(self) -> bool:
        """
        :type: bool
        """
    @software.setter
    def software(self, arg1: bool) -> None:
        pass
    @property
    def struct_asym(self) -> bool:
        """
        :type: bool
        """
    @struct_asym.setter
    def struct_asym(self, arg1: bool) -> None:
        pass
    @property
    def struct_biol(self) -> bool:
        """
        :type: bool
        """
    @struct_biol.setter
    def struct_biol(self, arg1: bool) -> None:
        pass
    @property
    def struct_conf(self) -> bool:
        """
        :type: bool
        """
    @struct_conf.setter
    def struct_conf(self, arg1: bool) -> None:
        pass
    @property
    def struct_ref(self) -> bool:
        """
        :type: bool
        """
    @struct_ref.setter
    def struct_ref(self, arg1: bool) -> None:
        pass
    @property
    def struct_sheet(self) -> bool:
        """
        :type: bool
        """
    @struct_sheet.setter
    def struct_sheet(self, arg1: bool) -> None:
        pass
    @property
    def symmetry(self) -> bool:
        """
        :type: bool
        """
    @symmetry.setter
    def symmetry(self, arg1: bool) -> None:
        pass
    @property
    def title_keywords(self) -> bool:
        """
        :type: bool
        """
    @title_keywords.setter
    def title_keywords(self, arg1: bool) -> None:
        pass
    @property
    def tls(self) -> bool:
        """
        :type: bool
        """
    @tls.setter
    def tls(self, arg1: bool) -> None:
        pass

class Model:
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __delitem__(self, index: int) -> None: ...
    @typing.overload
    def __delitem__(self, name: str) -> None: ...
    @typing.overload
    def __getitem__(self, index: int) -> Chain: ...
    @typing.overload
    def __getitem__(self, name: str) -> Chain: ...
    def __init__(self, arg0: str) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    @typing.overload
    def add_chain(self, chain: Chain, pos: int = -1, unique_name: bool = False) -> Chain: ...
    @typing.overload
    def add_chain(self, name: str) -> Chain: ...
    def all(self) -> CraGenerator: ...
    def calculate_center_of_mass(self) -> Position: ...
    def calculate_mass(self) -> float: ...
    def clone(self) -> Model: ...
    def count_atom_sites(self, sel: Selection = None) -> int: ...
    def count_hydrogen_sites(self) -> int: ...
    def count_occupancies(self, sel: Selection = None) -> float: ...
    def find_chain(self, name: str) -> Chain: ...
    def find_cra(self, arg0: AtomAddress, ignore_segment: bool = False) -> CRA: ...
    def find_last_chain(self, name: str) -> Chain: ...
    def find_residue_group(self, chain: str, seqid: SeqId) -> ResidueGroup: ...
    def get_all_residue_names(self) -> list[str]: ...
    def get_subchain(self, name: str) -> ResidueSpan: ...
    def has_hydrogen(self) -> bool: ...
    def remove_alternative_conformations(self) -> None: ...
    def remove_chain(self, name: str) -> None: ...
    def remove_hydrogens(self) -> None: ...
    def remove_ligands_and_waters(self) -> None: ...
    def remove_waters(self) -> None: ...
    def sole_residue(self, chain: str, seqid: SeqId) -> Residue: ...
    def split_chains_by_segments(self, arg0: HowToNameCopiedChain) -> None: ...
    def subchains(self) -> list[ResidueSpan]: ...
    def transform_pos_and_adp(self, tr: Transform) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass

class MonLib:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def add_monomer_if_present(self, arg0: cif.Block) -> None: ...
    def find_ideal_distance(self, arg0: CRA, arg1: CRA) -> float: ...
    def get_link(self, link_id: str) -> ChemLink: ...
    def get_mod(self, name: str) -> ChemMod: ...
    def match_link(
        self,
        res1: Residue,
        atom1: str,
        alt1: str,
        res2: Residue,
        atom2: str,
        alt2: str,
        min_bond_sq: float = 0.0,
    ) -> tuple[ChemLink, bool, ChemComp.Aliasing, ChemComp.Aliasing]: ...
    def path(self, code: str = "") -> str: ...
    def read_monomer_cif(self, arg0: str) -> None: ...
    def read_monomer_doc(self, arg0: cif.Document) -> None: ...
    def read_monomer_lib(self, arg0: str, arg1: list[str]) -> bool: ...
    def test_link(self, link: ChemLink, res1: str, atom1: str, res2: str, atom2: str) -> tuple: ...
    @property
    def ener_lib(self) -> EnerLib:
        """
        :type: EnerLib
        """
    @property
    def links(self) -> ChemLinkMap:
        """
        :type: ChemLinkMap
        """
    @property
    def modifications(self) -> ChemModMap:
        """
        :type: ChemModMap
        """
    @property
    def monomer_dir(self) -> str:
        """
        :type: str
        """
    @property
    def monomers(self) -> ChemCompMap:
        """
        :type: ChemCompMap
        """

class Mtz:
    class Batch:
        def __init__(self) -> None: ...
        @property
        def axes(self) -> list[str]:
            """
            :type: typing.List[str]
            """
        @property
        def dataset_id(self) -> int:
            """
            :type: int
            """
        @property
        def floats(self) -> list[float]:
            """
            :type: typing.List[float]
            """
        @property
        def ints(self) -> list[int]:
            """
            :type: typing.List[int]
            """
        @property
        def number(self) -> int:
            """
            :type: int
            """
        @number.setter
        def number(self, arg0: int) -> None:
            pass
        @property
        def title(self) -> str:
            """
            :type: str
            """
        @title.setter
        def title(self, arg0: str) -> None:
            pass

    class Column:
        def __getitem__(self, index: int) -> float: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        def __repr__(self) -> str: ...
        def is_integer(self) -> bool: ...
        @property
        def array(self) -> numpy.ndarray[numpy.float32]:
            """
            :type: numpy.ndarray[numpy.float32]
            """
        @property
        def dataset(self) -> Mtz.Dataset:
            """
            :type: Mtz.Dataset
            """
        @property
        def dataset_id(self) -> int:
            """
            :type: int
            """
        @dataset_id.setter
        def dataset_id(self, arg0: int) -> None:
            pass
        @property
        def idx(self) -> int:
            """
            :type: int
            """
        @idx.setter
        def idx(self, arg0: int) -> None:
            pass
        @property
        def label(self) -> str:
            """
            :type: str
            """
        @label.setter
        def label(self, arg0: str) -> None:
            pass
        @property
        def max_value(self) -> float:
            """
            :type: float
            """
        @max_value.setter
        def max_value(self, arg0: float) -> None:
            pass
        @property
        def min_value(self) -> float:
            """
            :type: float
            """
        @min_value.setter
        def min_value(self, arg0: float) -> None:
            pass
        @property
        def source(self) -> str:
            """
            :type: str
            """
        @source.setter
        def source(self, arg0: str) -> None:
            pass
        @property
        def type(self) -> str:
            """
            :type: str
            """
        @type.setter
        def type(self, arg0: str) -> None:
            pass

    class Dataset:
        def __repr__(self) -> str: ...
        @property
        def cell(self) -> UnitCell:
            """
            :type: UnitCell
            """
        @cell.setter
        def cell(self, arg0: UnitCell) -> None:
            pass
        @property
        def crystal_name(self) -> str:
            """
            :type: str
            """
        @crystal_name.setter
        def crystal_name(self, arg0: str) -> None:
            pass
        @property
        def dataset_name(self) -> str:
            """
            :type: str
            """
        @dataset_name.setter
        def dataset_name(self, arg0: str) -> None:
            pass
        @property
        def id(self) -> int:
            """
            :type: int
            """
        @id.setter
        def id(self, arg0: int) -> None:
            pass
        @property
        def project_name(self) -> str:
            """
            :type: str
            """
        @project_name.setter
        def project_name(self, arg0: str) -> None:
            pass
        @property
        def wavelength(self) -> float:
            """
            :type: float
            """
        @wavelength.setter
        def wavelength(self, arg0: float) -> None:
            pass
    def __init__(self, with_base: bool = False) -> None: ...
    def __repr__(self) -> str: ...
    def add_column(
        self,
        label: str,
        type: str,
        dataset_id: int = -1,
        pos: int = -1,
        expand_data: bool = True,
    ) -> Mtz.Column: ...
    def add_dataset(self, name: str) -> Mtz.Dataset: ...
    def column_labels(self) -> list[str]: ...
    def column_with_label(self, label: str, dataset: Mtz.Dataset = None) -> Mtz.Column: ...
    def columns_with_type(self, type: str) -> list[Mtz.Column]: ...
    def copy_column(self, dest_idx: int, src_col: Mtz.Column, trailing_cols: list[str] = []) -> Mtz.Column: ...
    def count(self, label: str) -> int: ...
    def data_fits_into(self, size: list[int]) -> bool: ...
    def dataset(self, id: int) -> Mtz.Dataset: ...
    def ensure_asu(self, tnt_asu: bool = False) -> None: ...
    def get_cell(self, dataset: int = -1) -> UnitCell: ...
    def get_f_phi(self, f: str, phi: str, as_is: bool = False) -> ComplexAsuData: ...
    def get_f_phi_on_grid(
        self,
        f: str,
        phi: str,
        size: list[int],
        half_l: bool = False,
        order: AxisOrder = ...,
    ) -> ReciprocalComplexGrid: ...
    def get_float(self, col: str, as_is: bool = False) -> FloatAsuData: ...
    def get_int(self, col: str, as_is: bool = False) -> IntAsuData: ...
    def get_size_for_hkl(
        self,
        min_size: list[int] = [0, 0, 0],
        sample_rate: float = 0.0,
    ) -> list[int]: ...
    def get_value_on_grid(
        self,
        label: str,
        size: list[int],
        half_l: bool = False,
        order: AxisOrder = ...,
    ) -> ReciprocalFloatGrid: ...
    def get_value_sigma(self, f: str, sigma: str, as_is: bool = False) -> ValueSigmaAsuData: ...
    def make_1_d2_array(self, dataset: int = -1) -> numpy.ndarray[numpy.float32]: ...
    def make_d_array(self, dataset: int = -1) -> numpy.ndarray[numpy.float32]: ...
    def make_miller_array(self) -> numpy.ndarray[numpy.int32]: ...
    def reindex(self, op: Op) -> str: ...
    def remove_column(self, index: int) -> None: ...
    def replace_column(
        self,
        dest_idx: int,
        src_col: Mtz.Column,
        trailing_cols: list[str] = [],
    ) -> Mtz.Column: ...
    def resolution_high(self) -> float: ...
    def resolution_low(self) -> float: ...
    def rfree_column(self) -> Mtz.Column: ...
    def set_cell_for_all(self, arg0: UnitCell) -> None: ...
    @typing.overload
    def set_data(self, array: numpy.ndarray[numpy.float32]) -> None: ...
    @typing.overload
    def set_data(self, asu_data: ComplexAsuData) -> None: ...
    @typing.overload
    def set_data(self, asu_data: FloatAsuData) -> None: ...
    def sort(self, use_first: int = 3) -> bool: ...
    def switch_to_asu_hkl(self) -> bool: ...
    def switch_to_original_hkl(self) -> bool: ...
    def transform_f_phi_to_map(
        self,
        f: str,
        phi: str,
        min_size: list[int] = [0, 0, 0],
        exact_size: list[int] = [0, 0, 0],
        sample_rate: float = 0.0,
        order: AxisOrder = ...,
    ) -> FloatGrid: ...
    def update_reso(self) -> None: ...
    def write_to_file(self, path: str) -> None: ...
    @property
    def appended_text(self) -> str:
        """
        :type: str
        """
    @appended_text.setter
    def appended_text(self, arg0: str) -> None:
        pass
    @property
    def array(self) -> numpy.ndarray[numpy.float32]:
        """
        :type: numpy.ndarray[numpy.float32]
        """
    @property
    def batches(self) -> MtzBatches:
        """
        :type: MtzBatches
        """
    @batches.setter
    def batches(self, arg0: MtzBatches) -> None:
        pass
    @property
    def cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @cell.setter
    def cell(self, arg0: UnitCell) -> None:
        pass
    @property
    def columns(self) -> MtzColumns:
        """
        :type: MtzColumns
        """
    @columns.setter
    def columns(self, arg0: MtzColumns) -> None:
        pass
    @property
    def datasets(self) -> MtzDatasets:
        """
        :type: MtzDatasets
        """
    @datasets.setter
    def datasets(self, arg0: MtzDatasets) -> None:
        pass
    @property
    def history(self) -> list[str]:
        """
        :type: typing.List[str]
        """
    @history.setter
    def history(self, arg0: list[str]) -> None:
        pass
    @property
    def max_1_d2(self) -> float:
        """
        :type: float
        """
    @max_1_d2.setter
    def max_1_d2(self, arg0: float) -> None:
        pass
    @property
    def min_1_d2(self) -> float:
        """
        :type: float
        """
    @min_1_d2.setter
    def min_1_d2(self, arg0: float) -> None:
        pass
    @property
    def nreflections(self) -> int:
        """
        :type: int
        """
    @nreflections.setter
    def nreflections(self, arg0: int) -> None:
        pass
    @property
    def nsymop(self) -> int:
        """
        :type: int
        """
    @property
    def sort_order(self) -> list[int]:
        """
        :type: typing.List[int]
        """
    @sort_order.setter
    def sort_order(self, arg0: list[int]) -> None:
        pass
    @property
    def spacegroup(self) -> SpaceGroup:
        """
        :type: SpaceGroup
        """
    @spacegroup.setter
    def spacegroup(self, arg0: SpaceGroup) -> None:
        pass
    @property
    def spacegroup_name(self) -> str:
        """
        :type: str
        """
    @property
    def spacegroup_number(self) -> int:
        """
        :type: int
        """
    @property
    def title(self) -> str:
        """
        :type: str
        """
    @title.setter
    def title(self, arg0: str) -> None:
        pass
    @property
    def valm(self) -> float:
        """
        :type: float
        """
    @valm.setter
    def valm(self, arg0: float) -> None:
        pass

class MtzBatches:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Mtz.Batch:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> MtzBatches: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: MtzBatches) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator[Mtz.Batch]: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Mtz.Batch) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: MtzBatches) -> None: ...
    def append(self, x: Mtz.Batch) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: MtzBatches) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Mtz.Batch) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Mtz.Batch:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Mtz.Batch: ...

class MtzColumns:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Mtz.Column:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> MtzColumns: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: MtzColumns) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator[Mtz.Column]: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Mtz.Column) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: MtzColumns) -> None: ...
    def append(self, x: Mtz.Column) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: MtzColumns) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Mtz.Column) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Mtz.Column:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Mtz.Column: ...

class MtzDatasets:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Mtz.Dataset:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> MtzDatasets: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: MtzDatasets) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator[Mtz.Dataset]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Mtz.Dataset) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: MtzDatasets) -> None: ...
    def append(self, x: Mtz.Dataset) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: MtzDatasets) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Mtz.Dataset) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Mtz.Dataset:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Mtz.Dataset: ...

class NcsOp:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, tr: Transform, id: str = "", given: bool = False) -> None: ...
    def __repr__(self) -> str: ...
    def apply(self, arg0: Position) -> Position: ...
    @property
    def given(self) -> bool:
        """
        :type: bool
        """
    @given.setter
    def given(self, arg0: bool) -> None:
        pass
    @property
    def id(self) -> str:
        """
        :type: str
        """
    @id.setter
    def id(self, arg0: str) -> None:
        pass
    @property
    def tr(self) -> Transform:
        """
        :type: Transform
        """

class NcsOpList:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> NcsOp:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> NcsOpList: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: NcsOpList) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator[NcsOp]: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: NcsOp) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: NcsOpList) -> None: ...
    def append(self, x: NcsOp) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: NcsOpList) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: NcsOp) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> NcsOp:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> NcsOp: ...

class NearestImage:
    def __repr__(self) -> str: ...
    def dist(self) -> float: ...
    def symmetry_code(self, underscore: bool = True) -> str: ...
    @property
    def pbc_shift(self) -> tuple:
        """
        :type: tuple
        """
    @property
    def sym_idx(self) -> int:
        """
        :type: int
        """

class NeighborSearch:
    class Mark:
        def __repr__(self) -> str: ...
        def pos(self) -> Position: ...
        def to_cra(self, arg0: Model) -> CRA: ...
        def to_site(self, arg0: SmallStructure) -> SmallStructure.Site: ...
        @property
        def altloc(self) -> str:
            """
            :type: str
            """
        @property
        def atom_idx(self) -> int:
            """
            :type: int
            """
        @property
        def chain_idx(self) -> int:
            """
            :type: int
            """
        @property
        def element(self) -> Element:
            """
            :type: Element
            """
        @property
        def image_idx(self) -> int:
            """
            :type: int
            """
        @property
        def residue_idx(self) -> int:
            """
            :type: int
            """
        @property
        def x(self) -> float:
            """
            :type: float
            """
        @property
        def y(self) -> float:
            """
            :type: float
            """
        @property
        def z(self) -> float:
            """
            :type: float
            """
    @typing.overload
    def __init__(self, model: Model, cell: UnitCell, max_radius: float) -> None: ...
    @typing.overload
    def __init__(self, small_structure: SmallStructure, max_radius: float) -> None: ...
    @typing.overload
    def __init__(self, st: Structure, max_radius: float, model_index: int = 0) -> None: ...
    def __repr__(self) -> str: ...
    def add_atom(self, atom: Atom, n_ch: int, n_res: int, n_atom: int) -> None:
        """
        Lower-level alternative to populate()
        """
    def add_chain(self, chain: Chain, include_h: bool = True) -> None: ...
    def dist(self, arg0: Position, arg1: Position) -> float: ...
    def find_atoms(self, pos: Position, alt: str = "\x00", radius: float = 0) -> VectorMarkPtr: ...
    def find_nearest_atom(self, arg0: Position) -> NeighborSearch.Mark: ...
    def find_neighbors(self, atom: Atom, min_dist: float = 0, max_dist: float = 0) -> VectorMarkPtr: ...
    def find_site_neighbors(
        self,
        atom: SmallStructure.Site,
        min_dist: float = 0,
        max_dist: float = 0,
    ) -> VectorMarkPtr: ...
    def get_image_transformation(self, arg0: int) -> FTransform: ...
    def populate(self, include_h: bool = True) -> NeighborSearch:
        """
        Usually run after constructing NeighborSearch.
        """
    @property
    def grid_cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @property
    def radius_specified(self) -> float:
        """
        :type: float
        """

class Neutron92:
    def calculate_density_iso(self, r2: float, B: float) -> float: ...
    def calculate_sf(self, stol2: float) -> float: ...
    def get_coefs(self) -> list[float]: ...

class Op:
    def __copy__(self) -> Op: ...
    def __deepcopy__(self, memo: dict) -> Op: ...
    @typing.overload
    def __eq__(self, arg0: Op) -> bool: ...
    @typing.overload
    def __eq__(self, arg0: str) -> bool: ...
    def __hash__(self) -> int: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    @typing.overload
    def __mul__(self, arg0: Op) -> Op: ...
    @typing.overload
    def __mul__(self, arg0: str) -> Op: ...
    def __repr__(self) -> str: ...
    def __rmul__(self, arg0: str) -> Op: ...
    def apply_to_hkl(self, hkl: list[int]) -> list[int]: ...
    def apply_to_xyz(self, xyz: list[float]) -> list[float]: ...
    def combine(self, b: Op) -> Op:
        """
        Combine two symmetry operations.
        """
    def det_rot(self) -> int:
        """
        Determinant of the 3x3 matrix.
        """
    def float_seitz(self) -> list[list[float]]:
        """
        Returns Seitz matrix (floats)
        """
    def inverse(self) -> Op:
        """
        Returns inverted operator.
        """
    def phase_shift(self, hkl: list[int]) -> float: ...
    def rot_type(self) -> int: ...
    def seitz(self) -> list:
        """
        Returns Seitz matrix (fractions)
        """
    def translated(self, a: list[int]) -> Op:
        """
        Adds a to tran
        """
    def transposed_rot(self) -> list[list[int]]: ...
    def triplet(self, style: str = "x") -> str: ...
    def wrap(self) -> Op:
        """
        Wrap the translation part to [0,1)
        """
    @property
    def rot(self) -> list[list[int]]:
        """
        3x3 integer matrix.

        :type: typing.List[typing.List[int]]
        """
    @rot.setter
    def rot(self, arg0: list[list[int]]) -> None:
        """
        3x3 integer matrix.
        """
    @property
    def tran(self) -> list[int]:
        """
        :type: typing.List[int]
        """
    @tran.setter
    def tran(self, arg0: list[int]) -> None:
        pass
    DEN = 24

class PolymerType:
    """
    Members:

      PeptideL

      PeptideD

      Dna

      Rna

      DnaRnaHybrid

      SaccharideD

      SaccharideL

      Pna

      CyclicPseudoPeptide

      Other

      Unknown
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    CyclicPseudoPeptide: gemmi.PolymerType  # value = <PolymerType.CyclicPseudoPeptide: 9>
    Dna: gemmi.PolymerType  # value = <PolymerType.Dna: 3>
    DnaRnaHybrid: gemmi.PolymerType  # value = <PolymerType.DnaRnaHybrid: 5>
    Other: gemmi.PolymerType  # value = <PolymerType.Other: 10>
    PeptideD: gemmi.PolymerType  # value = <PolymerType.PeptideD: 2>
    PeptideL: gemmi.PolymerType  # value = <PolymerType.PeptideL: 1>
    Pna: gemmi.PolymerType  # value = <PolymerType.Pna: 8>
    Rna: gemmi.PolymerType  # value = <PolymerType.Rna: 4>
    SaccharideD: gemmi.PolymerType  # value = <PolymerType.SaccharideD: 6>
    SaccharideL: gemmi.PolymerType  # value = <PolymerType.SaccharideL: 7>
    Unknown: gemmi.PolymerType  # value = <PolymerType.Unknown: 0>

class Position(Vec3):
    def __add__(self, arg0: Position) -> Position: ...
    def __iadd__(self, arg0: Position) -> Position: ...
    def __imul__(self, arg0: float) -> Position: ...
    @typing.overload
    def __init__(self, arg0: Vec3) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None: ...
    def __isub__(self, arg0: Position) -> Position: ...
    def __itruediv__(self, arg0: float) -> Position: ...
    def __mul__(self, arg0: float) -> Position: ...
    def __neg__(self) -> Position: ...
    def __repr__(self) -> str: ...
    def __rmul__(self, arg0: float) -> Position: ...
    def __sub__(self, arg0: Position) -> Position: ...
    def __truediv__(self, arg0: float) -> Position: ...
    def dist(self, arg0: Position) -> float: ...

class PositionBox:
    def __init__(self) -> None: ...
    def add_margin(self, arg0: float) -> None: ...
    def extend(self, arg0: Position) -> None: ...
    def get_size(self) -> Position: ...
    @property
    def maximum(self) -> Position:
        """
        :type: Position
        """
    @maximum.setter
    def maximum(self, arg0: Position) -> None:
        pass
    @property
    def minimum(self) -> Position:
        """
        :type: Position
        """
    @minimum.setter
    def minimum(self, arg0: Position) -> None:
        pass

class RKind:
    """
    Members:

      Bond

      Angle

      Torsion

      Chirality

      Plane
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Angle: gemmi.RKind  # value = <RKind.Angle: 1>
    Bond: gemmi.RKind  # value = <RKind.Bond: 0>
    Chirality: gemmi.RKind  # value = <RKind.Chirality: 3>
    Plane: gemmi.RKind  # value = <RKind.Plane: 4>
    Torsion: gemmi.RKind  # value = <RKind.Torsion: 2>

class ReciprocalAsu:
    def __init__(self, arg0: SpaceGroup, tnt: bool = False) -> None: ...
    def condition_str(self) -> str: ...
    def is_in(self, hkl: list[int]) -> bool: ...
    def to_asu(self, hkl: list[int], group_ops: GroupOps) -> tuple[list[int], int]: ...

class ReciprocalComplexGrid(ComplexGridBase, GridMeta):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(
        self,
        arg0: numpy.ndarray[numpy.complex64],
        cell: UnitCell = None,
        spacegroup: SpaceGroup = None,
    ) -> None: ...
    @typing.overload
    def __init__(self, nx: int, ny: int, nz: int) -> None: ...
    def __repr__(self) -> str: ...
    def calculate_1_d2(self, arg0: ComplexGridBase.Point) -> float: ...
    def calculate_d(self, arg0: ComplexGridBase.Point) -> float: ...
    def get_value(self, arg0: int, arg1: int, arg2: int) -> complex: ...
    def get_value_by_hkl(
        self,
        hkl: numpy.ndarray[numpy.int32],
        unblur: float = 0,
        mott_bethe: bool = False,
        mott_bethe_000: complex = 0,
    ) -> numpy.ndarray[numpy.complex64]: ...
    def get_value_or_zero(self, arg0: int, arg1: int, arg2: int) -> complex: ...
    def prepare_asu_data(
        self,
        dmin: float = 0.0,
        unblur: float = 0.0,
        with_000: bool = False,
        with_sys_abs: bool = False,
        mott_bethe: bool = False,
    ) -> ComplexAsuData: ...
    def set_value(self, arg0: int, arg1: int, arg2: int, arg3: complex) -> None: ...
    def to_hkl(self, arg0: ComplexGridBase.Point) -> list[int]: ...
    @property
    def half_l(self) -> bool:
        """
        :type: bool
        """

class ReciprocalFloatGrid(FloatGridBase, GridMeta):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(
        self,
        arg0: numpy.ndarray[numpy.float32],
        cell: UnitCell = None,
        spacegroup: SpaceGroup = None,
    ) -> None: ...
    @typing.overload
    def __init__(self, nx: int, ny: int, nz: int) -> None: ...
    def __repr__(self) -> str: ...
    def calculate_1_d2(self, arg0: FloatGridBase.Point) -> float: ...
    def calculate_d(self, arg0: FloatGridBase.Point) -> float: ...
    def get_value(self, arg0: int, arg1: int, arg2: int) -> float: ...
    def get_value_by_hkl(
        self,
        hkl: numpy.ndarray[numpy.int32],
        unblur: float = 0,
        mott_bethe: bool = False,
        mott_bethe_000: float = 0,
    ) -> numpy.ndarray[numpy.float32]: ...
    def get_value_or_zero(self, arg0: int, arg1: int, arg2: int) -> float: ...
    def prepare_asu_data(
        self,
        dmin: float = 0.0,
        unblur: float = 0.0,
        with_000: bool = False,
        with_sys_abs: bool = False,
        mott_bethe: bool = False,
    ) -> FloatAsuData: ...
    def set_value(self, arg0: int, arg1: int, arg2: int, arg3: float) -> None: ...
    def to_hkl(self, arg0: FloatGridBase.Point) -> list[int]: ...
    @property
    def half_l(self) -> bool:
        """
        :type: bool
        """

class ReciprocalInt8Grid(Int8GridBase, GridMeta):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(
        self,
        arg0: numpy.ndarray[numpy.int8],
        cell: UnitCell = None,
        spacegroup: SpaceGroup = None,
    ) -> None: ...
    @typing.overload
    def __init__(self, nx: int, ny: int, nz: int) -> None: ...
    def __repr__(self) -> str: ...
    def calculate_1_d2(self, arg0: Int8GridBase.Point) -> float: ...
    def calculate_d(self, arg0: Int8GridBase.Point) -> float: ...
    def get_value(self, arg0: int, arg1: int, arg2: int) -> int: ...
    def get_value_by_hkl(
        self,
        hkl: numpy.ndarray[numpy.int32],
        unblur: float = 0,
        mott_bethe: bool = False,
        mott_bethe_000: int = 0,
    ) -> numpy.ndarray[numpy.int32]: ...
    def get_value_or_zero(self, arg0: int, arg1: int, arg2: int) -> int: ...
    def prepare_asu_data(
        self,
        dmin: float = 0.0,
        unblur: float = 0.0,
        with_000: bool = False,
        with_sys_abs: bool = False,
        mott_bethe: bool = False,
    ) -> IntAsuData: ...
    def set_value(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    def to_hkl(self, arg0: Int8GridBase.Point) -> list[int]: ...
    @property
    def half_l(self) -> bool:
        """
        :type: bool
        """

class RefinementInfo(BasicRefinementInfo):
    class Restr:
        def __init__(self, arg0: str) -> None: ...
        @property
        def count(self) -> int:
            """
            :type: int
            """
        @count.setter
        def count(self, arg0: int) -> None:
            pass
        @property
        def dev_ideal(self) -> float:
            """
            :type: float
            """
        @dev_ideal.setter
        def dev_ideal(self, arg0: float) -> None:
            pass
        @property
        def function(self) -> str:
            """
            :type: str
            """
        @function.setter
        def function(self, arg0: str) -> None:
            pass
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @name.setter
        def name(self, arg0: str) -> None:
            pass
        @property
        def weight(self) -> float:
            """
            :type: float
            """
        @weight.setter
        def weight(self, arg0: float) -> None:
            pass
    def __init__(self) -> None: ...
    @property
    def aniso_b(self) -> Mat33:
        """
        :type: Mat33
        """
    @aniso_b.setter
    def aniso_b(self, arg0: Mat33) -> None:
        pass
    @property
    def bin_count(self) -> int:
        """
        :type: int
        """
    @bin_count.setter
    def bin_count(self, arg0: int) -> None:
        pass
    @property
    def bins(self) -> list[BasicRefinementInfo]:
        """
        :type: typing.List[BasicRefinementInfo]
        """
    @bins.setter
    def bins(self, arg0: list[BasicRefinementInfo]) -> None:
        pass
    @property
    def cc_fo_fc(self) -> float:
        """
        :type: float
        """
    @cc_fo_fc.setter
    def cc_fo_fc(self, arg0: float) -> None:
        pass
    @property
    def cc_fo_fc_free(self) -> float:
        """
        :type: float
        """
    @cc_fo_fc_free.setter
    def cc_fo_fc_free(self, arg0: float) -> None:
        pass
    @property
    def cross_validation_method(self) -> str:
        """
        :type: str
        """
    @cross_validation_method.setter
    def cross_validation_method(self, arg0: str) -> None:
        pass
    @property
    def dpi_blow_r(self) -> float:
        """
        :type: float
        """
    @dpi_blow_r.setter
    def dpi_blow_r(self, arg0: float) -> None:
        pass
    @property
    def dpi_blow_rfree(self) -> float:
        """
        :type: float
        """
    @dpi_blow_rfree.setter
    def dpi_blow_rfree(self, arg0: float) -> None:
        pass
    @property
    def dpi_cruickshank_r(self) -> float:
        """
        :type: float
        """
    @dpi_cruickshank_r.setter
    def dpi_cruickshank_r(self, arg0: float) -> None:
        pass
    @property
    def dpi_cruickshank_rfree(self) -> float:
        """
        :type: float
        """
    @dpi_cruickshank_rfree.setter
    def dpi_cruickshank_rfree(self, arg0: float) -> None:
        pass
    @property
    def id(self) -> str:
        """
        :type: str
        """
    @id.setter
    def id(self, arg0: str) -> None:
        pass
    @property
    def luzzati_error(self) -> float:
        """
        :type: float
        """
    @luzzati_error.setter
    def luzzati_error(self, arg0: float) -> None:
        pass
    @property
    def mean_b(self) -> float:
        """
        :type: float
        """
    @mean_b.setter
    def mean_b(self, arg0: float) -> None:
        pass
    @property
    def remarks(self) -> str:
        """
        :type: str
        """
    @remarks.setter
    def remarks(self, arg0: str) -> None:
        pass
    @property
    def restr_stats(self) -> list[RefinementInfo.Restr]:
        """
        :type: typing.List[RefinementInfo.Restr]
        """
    @restr_stats.setter
    def restr_stats(self, arg0: list[RefinementInfo.Restr]) -> None:
        pass
    @property
    def rfree_selection_method(self) -> str:
        """
        :type: str
        """
    @rfree_selection_method.setter
    def rfree_selection_method(self, arg0: str) -> None:
        pass
    @property
    def tls_groups(self) -> list[TlsGroup]:
        """
        :type: typing.List[TlsGroup]
        """
    @tls_groups.setter
    def tls_groups(self, arg0: list[TlsGroup]) -> None:
        pass

class ReflectionsInfo:
    def __init__(self) -> None: ...
    @property
    def completeness(self) -> float:
        """
        :type: float
        """
    @completeness.setter
    def completeness(self, arg0: float) -> None:
        pass
    @property
    def mean_I_over_sigma(self) -> float:
        """
        :type: float
        """
    @mean_I_over_sigma.setter
    def mean_I_over_sigma(self, arg0: float) -> None:
        pass
    @property
    def r_merge(self) -> float:
        """
        :type: float
        """
    @r_merge.setter
    def r_merge(self, arg0: float) -> None:
        pass
    @property
    def r_sym(self) -> float:
        """
        :type: float
        """
    @r_sym.setter
    def r_sym(self, arg0: float) -> None:
        pass
    @property
    def redundancy(self) -> float:
        """
        :type: float
        """
    @redundancy.setter
    def redundancy(self, arg0: float) -> None:
        pass
    @property
    def resolution_high(self) -> float:
        """
        :type: float
        """
    @resolution_high.setter
    def resolution_high(self, arg0: float) -> None:
        pass
    @property
    def resolution_low(self) -> float:
        """
        :type: float
        """
    @resolution_low.setter
    def resolution_low(self, arg0: float) -> None:
        pass

class ReflnBlock:
    def __bool__(self) -> bool: ...
    def __repr__(self) -> str: ...
    def column_labels(self) -> list[str]: ...
    def data_fits_into(self, size: list[int]) -> bool: ...
    def get_f_phi(self, f: str, phi: str, as_is: bool = False) -> ComplexAsuData: ...
    def get_f_phi_on_grid(
        self,
        f: str,
        phi: str,
        size: list[int],
        half_l: bool = False,
        order: AxisOrder = ...,
    ) -> ReciprocalComplexGrid: ...
    def get_float(self, col: str, as_is: bool = False) -> FloatAsuData: ...
    def get_int(self, col: str, as_is: bool = False) -> IntAsuData: ...
    def get_size_for_hkl(
        self,
        min_size: list[int] = [0, 0, 0],
        sample_rate: float = 0.0,
    ) -> list[int]: ...
    def get_value_on_grid(
        self,
        column: str,
        size: list[int],
        half_l: bool = False,
        order: AxisOrder = ...,
    ) -> ReciprocalFloatGrid: ...
    def get_value_sigma(self, f: str, sigma: str, as_is: bool = False) -> ValueSigmaAsuData: ...
    def is_unmerged(self) -> bool: ...
    def make_1_d2_array(self) -> numpy.ndarray[numpy.float64]: ...
    def make_d_array(self) -> numpy.ndarray[numpy.float64]: ...
    @typing.overload
    def make_float_array(self, tag: str, null: float = ...) -> numpy.ndarray[numpy.float64]: ...
    @typing.overload
    def make_float_array(self, tag: str, null: float = ...) -> list[float]: ...
    def make_int_array(self, tag: str, null: int) -> numpy.ndarray[numpy.int32]: ...
    def make_miller_array(self) -> numpy.ndarray[numpy.int32]: ...
    def transform_f_phi_to_map(
        self,
        f: str,
        phi: str,
        min_size: list[int] = [0, 0, 0],
        exact_size: list[int] = [0, 0, 0],
        sample_rate: float = 0.0,
        order: AxisOrder = ...,
    ) -> FloatGrid: ...
    def use_unmerged(self, arg0: bool) -> None: ...
    @property
    def block(self) -> cif.Block:
        """
        :type: cif.Block
        """
    @property
    def cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @property
    def entry_id(self) -> str:
        """
        :type: str
        """
    @property
    def spacegroup(self) -> SpaceGroup:
        """
        :type: SpaceGroup
        """
    @property
    def wavelength(self) -> float:
        """
        :type: float
        """

class ReflnBlocks:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __getitem__(self, arg0: int) -> ReflnBlock: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator[ReflnBlock]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """

class ResidueId:
    def __eq__(self, arg0: ResidueId) -> bool: ...
    def __getstate__(self) -> tuple: ...
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    def __str__(self) -> str: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def segment(self) -> str:
        """
        :type: str
        """
    @segment.setter
    def segment(self, arg0: str) -> None:
        pass
    @property
    def seqid(self) -> SeqId:
        """
        :type: SeqId
        """
    @seqid.setter
    def seqid(self, arg0: SeqId) -> None:
        pass
    __hash__ = None

class ResidueSpan:
    def __bool__(self) -> bool: ...
    def __delitem__(self, index: int) -> None: ...
    @typing.overload
    def __getitem__(self, index: int) -> Residue: ...
    @typing.overload
    def __getitem__(self, pdb_seqid: str) -> ResidueGroup: ...
    def __iter__(self) -> typing.Iterator[Residue]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def add_residue(self, residue: Residue, pos: int = -1) -> Residue: ...
    def auth_seq_id_to_label(self, arg0: SeqId) -> int | None: ...
    def check_polymer_type(self) -> PolymerType: ...
    def first_conformer(self) -> FirstConformerResSpan: ...
    def label_seq_id_to_auth(self, arg0: int | None) -> SeqId: ...
    def length(self) -> int: ...
    def make_one_letter_sequence(self) -> str: ...
    def residue_groups(self) -> ResidueSpanGroups: ...
    def subchain_id(self) -> str: ...
    def transform_pos_and_adp(self, arg0: Transform) -> None: ...

class Residue(ResidueId):
    def __contains__(self, arg0: str) -> bool: ...
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __delitem__(self, index: int) -> None: ...
    @typing.overload
    def __getitem__(self, index: int) -> Atom: ...
    @typing.overload
    def __getitem__(self, name: str) -> AtomGroup: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator[Atom]: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def add_atom(self, atom: Atom, pos: int = -1) -> Atom: ...
    def clone(self) -> Residue: ...
    @staticmethod
    def find_atom(self, name: str, altloc: str, el: gemmi.Element = None) -> gemmi.Atom: ...
    def first_conformer(self) -> FirstConformerAtoms: ...
    def get_ca(self) -> Atom: ...
    def get_p(self) -> Atom: ...
    def is_water(self) -> bool: ...
    @staticmethod
    def remove_atom(self, name: str, altloc: str, el: gemmi.Element = None) -> None: ...
    def remove_hydrogens(self) -> None: ...
    def sole_atom(self, arg0: str) -> Atom: ...
    def trim_to_alanine(self) -> bool: ...
    @property
    def entity_id(self) -> str:
        """
        :type: str
        """
    @property
    def entity_type(self) -> EntityType:
        """
        :type: EntityType
        """
    @entity_type.setter
    def entity_type(self, arg0: EntityType) -> None:
        pass
    @property
    def flag(self) -> str:
        """
        :type: str
        """
    @flag.setter
    def flag(self, arg0: str) -> None:
        pass
    @property
    def het_flag(self) -> str:
        """
        :type: str
        """
    @het_flag.setter
    def het_flag(self, arg0: str) -> None:
        pass
    @property
    def label_seq(self) -> int | None:
        """
        :type: typing.Optional[int]
        """
    @label_seq.setter
    def label_seq(self, arg0: int | None) -> None:
        pass
    @property
    def sifts_unp(self) -> tuple:
        """
        :type: tuple
        """
    @property
    def subchain(self) -> str:
        """
        :type: str
        """
    @subchain.setter
    def subchain(self, arg0: str) -> None:
        pass

class ResidueInfo:
    def fasta_code(self) -> str: ...
    def found(self) -> bool: ...
    def is_amino_acid(self) -> bool: ...
    def is_nucleic_acid(self) -> bool: ...
    def is_standard(self) -> bool: ...
    def is_water(self) -> bool: ...
    @property
    def hydrogen_count(self) -> int:
        """
        :type: int
        """
    @property
    def kind(self) -> ResidueInfoKind:
        """
        :type: ResidueInfoKind
        """
    @property
    def one_letter_code(self) -> str:
        """
        :type: str
        """
    @property
    def weight(self) -> float:
        """
        :type: float
        """

class ResidueInfoKind:
    """
    Members:

      UNKNOWN

      AA

      AAD

      PAA

      MAA

      RNA

      DNA

      BUF

      HOH

      PYR

      KET

      ELS
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    AA: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.AA: 1>
    AAD: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.AAD: 2>
    BUF: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.BUF: 7>
    DNA: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.DNA: 6>
    ELS: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.ELS: 11>
    HOH: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.HOH: 8>
    KET: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.KET: 10>
    MAA: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.MAA: 4>
    PAA: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.PAA: 3>
    PYR: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.PYR: 9>
    RNA: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.RNA: 5>
    UNKNOWN: gemmi.ResidueInfoKind  # value = <ResidueInfoKind.UNKNOWN: 0>

class ResidueGroup(ResidueSpan):
    def __delitem__(self, name: str) -> None: ...
    @typing.overload
    def __getitem__(self, index: int) -> Residue: ...
    @typing.overload
    def __getitem__(self, name: str) -> Residue: ...
    def __repr__(self) -> str: ...

class ResidueSpanGroups:
    def __iter__(self) -> typing.Iterator[]: ...

class Restraints:
    class Angle:
        def __init__(self) -> None: ...
        def __repr__(self) -> str: ...
        @property
        def esd(self) -> float:
            """
            :type: float
            """
        @esd.setter
        def esd(self, arg0: float) -> None:
            pass
        @property
        def id1(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id1.setter
        def id1(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def id2(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id2.setter
        def id2(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def id3(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id3.setter
        def id3(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def value(self) -> float:
            """
            :type: float
            """
        @value.setter
        def value(self, arg0: float) -> None:
            pass

    class AtomId:
        @typing.overload
        def __init__(self, arg0: int, arg1: str) -> None: ...
        @typing.overload
        def __init__(self, arg0: str) -> None: ...
        def __repr__(self) -> str: ...
        def get_from(self, res1: Residue, res2: Residue, altloc1: str, altloc2: str) -> Atom: ...
        @property
        def atom(self) -> str:
            """
            :type: str
            """
        @atom.setter
        def atom(self, arg0: str) -> None:
            pass
        @property
        def comp(self) -> int:
            """
            :type: int
            """
        @comp.setter
        def comp(self, arg0: int) -> None:
            pass

    class Bond:
        def __init__(self) -> None: ...
        def __repr__(self) -> str: ...
        def lexicographic_str(self) -> str: ...
        @property
        def aromatic(self) -> bool:
            """
            :type: bool
            """
        @aromatic.setter
        def aromatic(self, arg0: bool) -> None:
            pass
        @property
        def esd(self) -> float:
            """
            :type: float
            """
        @esd.setter
        def esd(self, arg0: float) -> None:
            pass
        @property
        def esd_nucleus(self) -> float:
            """
            :type: float
            """
        @esd_nucleus.setter
        def esd_nucleus(self, arg0: float) -> None:
            pass
        @property
        def id1(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id1.setter
        def id1(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def id2(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id2.setter
        def id2(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def type(self) -> BondType:
            """
            :type: BondType
            """
        @type.setter
        def type(self, arg0: BondType) -> None:
            pass
        @property
        def value(self) -> float:
            """
            :type: float
            """
        @value.setter
        def value(self, arg0: float) -> None:
            pass
        @property
        def value_nucleus(self) -> float:
            """
            :type: float
            """
        @value_nucleus.setter
        def value_nucleus(self, arg0: float) -> None:
            pass

    class Chirality:
        def __init__(self) -> None: ...
        def __repr__(self) -> str: ...
        def is_wrong(self, arg0: float) -> bool: ...
        @property
        def id1(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id1.setter
        def id1(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def id2(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id2.setter
        def id2(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def id3(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id3.setter
        def id3(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def id_ctr(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id_ctr.setter
        def id_ctr(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def sign(self) -> ChiralityType:
            """
            :type: ChiralityType
            """
        @sign.setter
        def sign(self, arg0: ChiralityType) -> None:
            pass

    class DistanceOf:
        """
        Members:

          ElectronCloud

          Nucleus
        """

        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        ElectronCloud: gemmi.Restraints.DistanceOf  # value = <DistanceOf.ElectronCloud: 0>
        Nucleus: gemmi.Restraints.DistanceOf  # value = <DistanceOf.Nucleus: 1>

    class Plane:
        def __init__(self) -> None: ...
        def __repr__(self) -> str: ...
        @property
        def esd(self) -> float:
            """
            :type: float
            """
        @esd.setter
        def esd(self, arg0: float) -> None:
            pass
        @property
        def ids(self) -> list[Restraints.AtomId]:
            """
            :type: typing.List[Restraints.AtomId]
            """
        @ids.setter
        def ids(self, arg0: list[Restraints.AtomId]) -> None:
            pass
        @property
        def label(self) -> str:
            """
            :type: str
            """
        @label.setter
        def label(self, arg0: str) -> None:
            pass

    class Torsion:
        def __init__(self) -> None: ...
        def __repr__(self) -> str: ...
        @property
        def esd(self) -> float:
            """
            :type: float
            """
        @esd.setter
        def esd(self, arg0: float) -> None:
            pass
        @property
        def id1(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id1.setter
        def id1(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def id2(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id2.setter
        def id2(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def id3(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id3.setter
        def id3(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def id4(self) -> Restraints.AtomId:
            """
            :type: Restraints.AtomId
            """
        @id4.setter
        def id4(self, arg0: Restraints.AtomId) -> None:
            pass
        @property
        def label(self) -> str:
            """
            :type: str
            """
        @label.setter
        def label(self, arg0: str) -> None:
            pass
        @property
        def period(self) -> int:
            """
            :type: int
            """
        @period.setter
        def period(self, arg0: int) -> None:
            pass
        @property
        def value(self) -> float:
            """
            :type: float
            """
        @value.setter
        def value(self, arg0: float) -> None:
            pass
    def __init__(self) -> None: ...
    def chiral_abs_volume(self, arg0: Restraints.Chirality) -> float: ...
    def empty(self) -> bool: ...
    def find_shortest_path(
        self,
        arg0: Restraints.AtomId,
        arg1: Restraints.AtomId,
        arg2: list[Restraints.AtomId],
    ) -> list[Restraints.AtomId]: ...
    @typing.overload
    def get_bond(self, arg0: Restraints.AtomId, arg1: Restraints.AtomId) -> Restraints.Bond: ...
    @typing.overload
    def get_bond(self, arg0: str, arg1: str) -> Restraints.Bond: ...
    @property
    def angles(self) -> RestraintsAngles:
        """
        :type: RestraintsAngles
        """
    @angles.setter
    def angles(self, arg0: RestraintsAngles) -> None:
        pass
    @property
    def bonds(self) -> RestraintsBonds:
        """
        :type: RestraintsBonds
        """
    @bonds.setter
    def bonds(self, arg0: RestraintsBonds) -> None:
        pass
    @property
    def chirs(self) -> RestraintsChirs:
        """
        :type: RestraintsChirs
        """
    @chirs.setter
    def chirs(self, arg0: RestraintsChirs) -> None:
        pass
    @property
    def planes(self) -> RestraintsPlanes:
        """
        :type: RestraintsPlanes
        """
    @planes.setter
    def planes(self, arg0: RestraintsPlanes) -> None:
        pass
    @property
    def torsions(self) -> RestraintsTorsions:
        """
        :type: RestraintsTorsions
        """
    @torsions.setter
    def torsions(self, arg0: RestraintsTorsions) -> None:
        pass

class RestraintsAngles:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Restraints.Angle:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> RestraintsAngles: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: RestraintsAngles) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Restraints.Angle) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: RestraintsAngles) -> None: ...
    def append(self, x: Restraints.Angle) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: RestraintsAngles) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Restraints.Angle) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Restraints.Angle:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Restraints.Angle: ...

class RestraintsBonds:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Restraints.Bond:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> RestraintsBonds: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: RestraintsBonds) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Restraints.Bond) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: RestraintsBonds) -> None: ...
    def append(self, x: Restraints.Bond) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: RestraintsBonds) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Restraints.Bond) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Restraints.Bond:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Restraints.Bond: ...

class RestraintsChirs:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Restraints.Chirality:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> RestraintsChirs: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: RestraintsChirs) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Restraints.Chirality) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: RestraintsChirs) -> None: ...
    def append(self, x: Restraints.Chirality) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: RestraintsChirs) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Restraints.Chirality) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Restraints.Chirality:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Restraints.Chirality: ...

class RestraintsPlanes:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Restraints.Plane:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> RestraintsPlanes: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: RestraintsPlanes) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Restraints.Plane) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: RestraintsPlanes) -> None: ...
    def append(self, x: Restraints.Plane) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: RestraintsPlanes) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Restraints.Plane) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Restraints.Plane:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Restraints.Plane: ...

class RestraintsTorsions:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Restraints.Torsion:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> RestraintsTorsions: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: RestraintsTorsions) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Restraints.Torsion) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: RestraintsTorsions) -> None: ...
    def append(self, x: Restraints.Torsion) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: RestraintsTorsions) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Restraints.Torsion) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Restraints.Torsion:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Restraints.Torsion: ...

class SMat33d:
    def __add__(self, arg0: SMat33d) -> SMat33d: ...
    def __init__(self, u11: float, u22: float, u33: float, u12: float, u13: float, u23: float) -> None: ...
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: SMat33d) -> SMat33d: ...
    def added_kI(self, arg0: float) -> SMat33d: ...
    def as_mat33(self) -> Mat33: ...
    def calculate_eigenvalues(self) -> list[float]: ...
    def determinant(self) -> float: ...
    def elements_pdb(self) -> list[float]: ...
    def elements_voigt(self) -> list[float]: ...
    def inverse(self) -> SMat33d: ...
    def multiply(self, arg0: Vec3) -> Vec3: ...
    def nonzero(self) -> bool: ...
    @typing.overload
    def r_u_r(self, arg0: Vec3) -> float: ...
    @typing.overload
    def r_u_r(self, arg0: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float64]: ...
    def scaled(self, arg0: float) -> SMat33d: ...
    def trace(self) -> float: ...
    def transformed_by(self, arg0: Mat33) -> SMat33d: ...
    @property
    def u11(self) -> float:
        """
        :type: float
        """
    @u11.setter
    def u11(self, arg0: float) -> None:
        pass
    @property
    def u12(self) -> float:
        """
        :type: float
        """
    @u12.setter
    def u12(self, arg0: float) -> None:
        pass
    @property
    def u13(self) -> float:
        """
        :type: float
        """
    @u13.setter
    def u13(self, arg0: float) -> None:
        pass
    @property
    def u22(self) -> float:
        """
        :type: float
        """
    @u22.setter
    def u22(self, arg0: float) -> None:
        pass
    @property
    def u23(self) -> float:
        """
        :type: float
        """
    @u23.setter
    def u23(self, arg0: float) -> None:
        pass
    @property
    def u33(self) -> float:
        """
        :type: float
        """
    @u33.setter
    def u33(self, arg0: float) -> None:
        pass

class SMat33f:
    def __add__(self, arg0: SMat33f) -> SMat33f: ...
    def __init__(self, u11: float, u22: float, u33: float, u12: float, u13: float, u23: float) -> None: ...
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: SMat33f) -> SMat33f: ...
    def added_kI(self, arg0: float) -> SMat33f: ...
    def as_mat33(self) -> Mat33: ...
    def calculate_eigenvalues(self) -> list[float]: ...
    def determinant(self) -> float: ...
    def elements_pdb(self) -> list[float]: ...
    def elements_voigt(self) -> list[float]: ...
    def inverse(self) -> SMat33f: ...
    def multiply(self, arg0: Vec3) -> Vec3: ...
    def nonzero(self) -> bool: ...
    @typing.overload
    def r_u_r(self, arg0: Vec3) -> float: ...
    @typing.overload
    def r_u_r(self, arg0: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float32]: ...
    def scaled(self, arg0: float) -> SMat33f: ...
    def trace(self) -> float: ...
    def transformed_by(self, arg0: Mat33) -> SMat33f: ...
    @property
    def u11(self) -> float:
        """
        :type: float
        """
    @u11.setter
    def u11(self, arg0: float) -> None:
        pass
    @property
    def u12(self) -> float:
        """
        :type: float
        """
    @u12.setter
    def u12(self, arg0: float) -> None:
        pass
    @property
    def u13(self) -> float:
        """
        :type: float
        """
    @u13.setter
    def u13(self, arg0: float) -> None:
        pass
    @property
    def u22(self) -> float:
        """
        :type: float
        """
    @u22.setter
    def u22(self, arg0: float) -> None:
        pass
    @property
    def u23(self) -> float:
        """
        :type: float
        """
    @u23.setter
    def u23(self, arg0: float) -> None:
        pass
    @property
    def u33(self) -> float:
        """
        :type: float
        """
    @u33.setter
    def u33(self, arg0: float) -> None:
        pass

class Scaling:
    def __init__(self, arg0: UnitCell, arg1: SpaceGroup) -> None: ...
    def fit_isotropic_b_approximately(self) -> None: ...
    def fit_parameters(self) -> None: ...
    @typing.overload
    def get_overall_scale_factor(self, arg0: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float64]: ...
    @typing.overload
    def get_overall_scale_factor(self, hkl: list[int]) -> float: ...
    def get_solvent_scale(self, stol2: numpy.ndarray[numpy.float64]) -> object: ...
    @staticmethod
    def prepare_points(
        self,
        calc: gemmi.ComplexAsuData,
        obs: gemmi.ValueSigmaAsuData,
        mask: gemmi.ComplexAsuData = None,
    ) -> None: ...
    @staticmethod
    def scale_data(self, asu_data: gemmi.ComplexAsuData, mask_data: gemmi.ComplexAsuData = None) -> None: ...
    def scale_value(self, hkl: list[int], f_value: complex, mask_value: complex) -> complex: ...
    @property
    def b_overall(self) -> SMat33d:
        """
        :type: SMat33d
        """
    @b_overall.setter
    def b_overall(self, arg1: SMat33d) -> None:
        pass
    @property
    def b_sol(self) -> float:
        """
        :type: float
        """
    @b_sol.setter
    def b_sol(self, arg0: float) -> None:
        pass
    @property
    def cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @cell.setter
    def cell(self, arg0: UnitCell) -> None:
        pass
    @property
    def crystal_system(self) -> CrystalSystem:
        """
        :type: CrystalSystem
        """
    @crystal_system.setter
    def crystal_system(self, arg0: CrystalSystem) -> None:
        pass
    @property
    def k_overall(self) -> float:
        """
        :type: float
        """
    @k_overall.setter
    def k_overall(self, arg0: float) -> None:
        pass
    @property
    def k_sol(self) -> float:
        """
        :type: float
        """
    @k_sol.setter
    def k_sol(self, arg0: float) -> None:
        pass
    @property
    def use_solvent(self) -> bool:
        """
        :type: bool
        """
    @use_solvent.setter
    def use_solvent(self, arg0: bool) -> None:
        pass

class Selection:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    def __repr__(self) -> str: ...
    def atoms(self, arg0: Residue) -> SelectionAtomsProxy: ...
    def chains(self, arg0: Model) -> SelectionChainsProxy: ...
    def copy_model_selection(self, arg0: Model) -> Model: ...
    def copy_structure_selection(self, arg0: Structure) -> Structure: ...
    def first(self, arg0: Structure) -> tuple[Model, CRA]: ...
    def first_in_model(self, arg0: Model) -> CRA: ...
    def models(self, arg0: Structure) -> SelectionModelsProxy: ...
    @typing.overload
    def remove_not_selected(self, arg0: Model) -> None: ...
    @typing.overload
    def remove_not_selected(self, arg0: Structure) -> None: ...
    @typing.overload
    def remove_selected(self, arg0: Model) -> None: ...
    @typing.overload
    def remove_selected(self, arg0: Structure) -> None: ...
    def residues(self, arg0: Chain) -> SelectionResiduesProxy: ...
    def set_atom_flags(self, arg0: str) -> Selection: ...
    def set_residue_flags(self, arg0: str) -> Selection: ...
    def str(self) -> str: ...

class SelectionAtomsProxy:
    def __iter__(self) -> typing.Iterator[]: ...

class SelectionChainsProxy:
    def __iter__(self) -> typing.Iterator: ...

class SelectionModelsProxy:
    def __iter__(self) -> typing.Iterator: ...

class SelectionResiduesProxy:
    def __iter__(self) -> typing.Iterator: ...

class SellingVector:
    @typing.overload
    def __init__(self, arg0: UnitCell, arg1: SpaceGroup) -> None: ...
    @typing.overload
    def __init__(self, arg0: list[float]) -> None: ...
    def __repr__(self) -> str: ...
    def cell_parameters(self) -> tuple: ...
    def get_cell(self) -> UnitCell: ...
    def gruber(self) -> GruberVector: ...
    def is_reduced(self, epsilon: float = 1e-09) -> bool: ...
    def reduce(self, epsilon: float = 1e-09, iteration_limit: int = 100) -> int: ...
    def reduce_step(self, epsilon: float = 1e-09) -> bool: ...
    def sort(self, epsilon: float = 1e-09) -> None: ...
    def sum_b_squared(self) -> float: ...
    @property
    def parameters(self) -> tuple:
        """
        :type: tuple
        """

class SeqId:
    def __eq__(self, arg0: SeqId) -> bool: ...
    def __getstate__(self) -> tuple: ...
    @typing.overload
    def __init__(self, arg0: int, arg1: str) -> None: ...
    @typing.overload
    def __init__(self, arg0: str) -> None: ...
    def __lt__(self, arg0: SeqId) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    def __str__(self) -> str: ...
    @property
    def icode(self) -> str:
        """
        :type: str
        """
    @icode.setter
    def icode(self, arg0: str) -> None:
        pass
    @property
    def num(self) -> int | None:
        """
        :type: typing.Optional[int]
        """
    @num.setter
    def num(self, arg0: int | None) -> None:
        pass
    __hash__ = None

class Sheet:
    class Strand:
        def __init__(self) -> None: ...
        @property
        def end(self) -> AtomAddress:
            """
            :type: AtomAddress
            """
        @end.setter
        def end(self, arg0: AtomAddress) -> None:
            pass
        @property
        def hbond_atom1(self) -> AtomAddress:
            """
            :type: AtomAddress
            """
        @hbond_atom1.setter
        def hbond_atom1(self, arg0: AtomAddress) -> None:
            pass
        @property
        def hbond_atom2(self) -> AtomAddress:
            """
            :type: AtomAddress
            """
        @hbond_atom2.setter
        def hbond_atom2(self, arg0: AtomAddress) -> None:
            pass
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @name.setter
        def name(self, arg0: str) -> None:
            pass
        @property
        def sense(self) -> int:
            """
            :type: int
            """
        @sense.setter
        def sense(self, arg0: int) -> None:
            pass
        @property
        def start(self) -> AtomAddress:
            """
            :type: AtomAddress
            """
        @start.setter
        def start(self, arg0: AtomAddress) -> None:
            pass

    class StrandList:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> Sheet.Strand:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> Sheet.StrandList: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: Sheet.StrandList) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: Sheet.Strand) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: Sheet.StrandList) -> None: ...
        def append(self, x: Sheet.Strand) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: Sheet.StrandList) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: Sheet.Strand) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> Sheet.Strand:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> Sheet.Strand: ...

    def __init__(self, arg0: str) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def strands(self) -> Sheet.StrandList:
        """
        :type: Sheet.StrandList
        """
    @strands.setter
    def strands(self, arg0: Sheet.StrandList) -> None:
        pass

class SheetList:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Sheet:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> SheetList: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: SheetList) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Sheet) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: SheetList) -> None: ...
    def append(self, x: Sheet) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: SheetList) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Sheet) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Sheet:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Sheet: ...

class SmallStructure:
    class AtomType:
        def __repr__(self) -> str: ...
        @property
        def dispersion_imag(self) -> float:
            """
            :type: float
            """
        @dispersion_imag.setter
        def dispersion_imag(self, arg0: float) -> None:
            pass
        @property
        def dispersion_real(self) -> float:
            """
            :type: float
            """
        @dispersion_real.setter
        def dispersion_real(self, arg0: float) -> None:
            pass
        @property
        def element(self) -> Element:
            """
            :type: Element
            """
        @property
        def symbol(self) -> str:
            """
            :type: str
            """

    class Site:
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, arg0: Atom, arg1: UnitCell) -> None: ...
        def __repr__(self) -> str: ...
        def orth(self, arg0: UnitCell) -> Position: ...
        @property
        def aniso(self) -> SMat33d:
            """
            :type: SMat33d
            """
        @aniso.setter
        def aniso(self, arg0: SMat33d) -> None:
            pass
        @property
        def charge(self) -> int:
            """
            :type: int
            """
        @charge.setter
        def charge(self, arg0: int) -> None:
            pass
        @property
        def disorder_group(self) -> int:
            """
            :type: int
            """
        @disorder_group.setter
        def disorder_group(self, arg0: int) -> None:
            pass
        @property
        def element(self) -> Element:
            """
            :type: Element
            """
        @element.setter
        def element(self, arg0: Element) -> None:
            pass
        @property
        def fract(self) -> Fractional:
            """
            :type: Fractional
            """
        @fract.setter
        def fract(self, arg0: Fractional) -> None:
            pass
        @property
        def label(self) -> str:
            """
            :type: str
            """
        @label.setter
        def label(self, arg0: str) -> None:
            pass
        @property
        def occ(self) -> float:
            """
            :type: float
            """
        @occ.setter
        def occ(self, arg0: float) -> None:
            pass
        @property
        def type_symbol(self) -> str:
            """
            :type: str
            """
        @type_symbol.setter
        def type_symbol(self, arg0: str) -> None:
            pass
        @property
        def u_iso(self) -> float:
            """
            :type: float
            """
        @u_iso.setter
        def u_iso(self, arg0: float) -> None:
            pass

    class SiteList:
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``

            Delete list elements using a slice object
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None: ...
        @typing.overload
        def __getitem__(self, arg0: int) -> SmallStructure.Site:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> SmallStructure.SiteList: ...
        @typing.overload
        def __init__(self) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: SmallStructure.SiteList) -> None: ...
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: SmallStructure.Site) -> None:
            """
            Assign list elements using a slice object
            """
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: SmallStructure.SiteList) -> None: ...
        def append(self, x: SmallStructure.Site) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: SmallStructure.SiteList) -> None:
            """
            Extend the list by appending all the items in the given list

            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None: ...
        def insert(self, i: int, x: SmallStructure.Site) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> SmallStructure.Site:
            """
            Remove and return the last item

            Remove and return the item at index ``i``
            """
        @typing.overload
        def pop(self, i: int) -> SmallStructure.Site: ...

    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def add_site(self, arg0: SmallStructure.Site) -> None: ...
    def change_occupancies_to_crystallographic(self, max_dist: float = 0.4) -> None: ...
    def find_spacegroup(self) -> SpaceGroup: ...
    def get_all_unit_cell_sites(self) -> SmallStructure.SiteList: ...
    def get_atom_type(self, arg0: str) -> SmallStructure.AtomType: ...
    def make_cif_block(self) -> cif.Block: ...
    def remove_hydrogens(self) -> None: ...
    def setup_cell_images(self) -> None: ...
    @property
    def atom_types(self) -> list[SmallStructure.AtomType]:
        """
        :type: typing.List[SmallStructure.AtomType]
        """
    @property
    def cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @cell.setter
    def cell(self, arg0: UnitCell) -> None:
        pass
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def sites(self) -> SmallStructure.SiteList:
        """
        :type: SmallStructure.SiteList
        """
    @property
    def spacegroup_hm(self) -> str:
        """
        :type: str
        """
    @spacegroup_hm.setter
    def spacegroup_hm(self, arg0: str) -> None:
        pass
    @property
    def wavelength(self) -> float:
        """
        :type: float
        """
    @wavelength.setter
    def wavelength(self, arg0: float) -> None:
        pass

class SoftwareItem:
    class Classification:
        """
        Members:

          DataCollection

          DataExtraction

          DataProcessing

          DataReduction

          DataScaling

          ModelBuilding

          Phasing

          Refinement

          Unspecified
        """

        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        DataCollection: gemmi.SoftwareItem.Classification  # value = <Classification.DataCollection: 0>
        DataExtraction: gemmi.SoftwareItem.Classification  # value = <Classification.DataExtraction: 1>
        DataProcessing: gemmi.SoftwareItem.Classification  # value = <Classification.DataProcessing: 2>
        DataReduction: gemmi.SoftwareItem.Classification  # value = <Classification.DataReduction: 3>
        DataScaling: gemmi.SoftwareItem.Classification  # value = <Classification.DataScaling: 4>
        ModelBuilding: gemmi.SoftwareItem.Classification  # value = <Classification.ModelBuilding: 5>
        Phasing: gemmi.SoftwareItem.Classification  # value = <Classification.Phasing: 6>
        Refinement: gemmi.SoftwareItem.Classification  # value = <Classification.Refinement: 7>
        Unspecified: gemmi.SoftwareItem.Classification  # value = <Classification.Unspecified: 8>
    def __init__(self) -> None: ...
    @property
    def classification(self) -> SoftwareItem.Classification:
        """
        :type: SoftwareItem.Classification
        """
    @classification.setter
    def classification(self, arg0: SoftwareItem.Classification) -> None:
        pass
    @property
    def date(self) -> str:
        """
        :type: str
        """
    @date.setter
    def date(self, arg0: str) -> None:
        pass
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def pdbx_ordinal(self) -> int:
        """
        :type: int
        """
    @pdbx_ordinal.setter
    def pdbx_ordinal(self, arg0: int) -> None:
        pass
    @property
    def version(self) -> str:
        """
        :type: str
        """
    @version.setter
    def version(self, arg0: str) -> None:
        pass

class SolventMasker:
    def __init__(self, choice: AtomicRadiiSet, constant_r: float = 0.0) -> None: ...
    def put_mask_on_float_grid(self, arg0: FloatGrid, arg1: Model) -> None: ...
    def put_mask_on_int8_grid(self, arg0: Int8Grid, arg1: Model) -> None: ...
    def set_radii(self, choice: AtomicRadiiSet, constant_r: float = 0.0) -> None: ...
    def set_to_zero(self, arg0: FloatGrid, arg1: Model) -> None: ...
    @property
    def atomic_radii_set(self) -> AtomicRadiiSet:
        """
        :type: AtomicRadiiSet
        """
    @atomic_radii_set.setter
    def atomic_radii_set(self, arg0: AtomicRadiiSet) -> None:
        pass
    @property
    def constant_r(self) -> float:
        """
        :type: float
        """
    @constant_r.setter
    def constant_r(self, arg0: float) -> None:
        pass
    @property
    def island_min_volume(self) -> float:
        """
        :type: float
        """
    @island_min_volume.setter
    def island_min_volume(self, arg0: float) -> None:
        pass
    @property
    def rprobe(self) -> float:
        """
        :type: float
        """
    @rprobe.setter
    def rprobe(self, arg0: float) -> None:
        pass
    @property
    def rshrink(self) -> float:
        """
        :type: float
        """
    @rshrink.setter
    def rshrink(self, arg0: float) -> None:
        pass

class SpaceGroup:
    def __getstate__(self) -> str: ...
    @typing.overload
    def __init__(self, ccp4: int) -> None: ...
    @typing.overload
    def __init__(self, hm: str) -> None: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, arg0: str) -> None: ...
    def centred_to_primitive(self) -> Op: ...
    def centring_type(self) -> str: ...
    def change_of_hand_op(self) -> Op: ...
    def crystal_system(self) -> CrystalSystem: ...
    def crystal_system_str(self) -> str:
        """
        Returns lower-case name of the crystal system.
        """
    def is_centrosymmetric(self) -> bool: ...
    def is_enantiomorphic(self) -> bool: ...
    def is_reference_setting(self) -> bool: ...
    def is_sohncke(self) -> bool: ...
    def is_symmorphic(self) -> bool: ...
    def laue_str(self) -> str:
        """
        Returns name of the Laue class (for centrosymmetric groups the same as point_group_hm).
        """
    def operations(self) -> GroupOps:
        """
        Group of operations
        """
    def point_group_hm(self) -> str:
        """
        Returns H-M name of the point group.
        """
    def short_name(self) -> str:
        """
        H-M name w/o spaces and with 1's removed in '1 ... 1'.
        """
    def switch_to_asu(self, miller_array: numpy.ndarray[numpy.int32]) -> None: ...
    def xhm(self) -> str:
        """
        extended Hermann-Mauguin name
        """
    @property
    def basisop(self) -> Op:
        """
        :type: Op
        """
    @property
    def ccp4(self) -> int:
        """
        ccp4 number

        :type: int
        """
    @property
    def ext(self) -> str:
        """
        :type: str
        """
    @property
    def hall(self) -> str:
        """
        Hall symbol

        :type: str
        """
    @property
    def hm(self) -> str:
        """
        Hermann-Mauguin name

        :type: str
        """
    @property
    def number(self) -> int:
        """
        number 1-230.

        :type: int
        """
    @property
    def qualifier(self) -> str:
        """
        e.g. 'cab'

        :type: str
        """

class Structure:
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __delitem__(self, index: int) -> None: ...
    @typing.overload
    def __delitem__(self, name: str) -> None: ...
    @typing.overload
    def __getitem__(self, index: int) -> Model: ...
    @typing.overload
    def __getitem__(self, name: str) -> Model: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __setitem__(self, arg0: int, arg1: Model) -> None: ...
    def add_entity_types(self, overwrite: bool = False) -> None: ...
    def add_model(self, model: Model, pos: int = -1) -> Model: ...
    def assign_cis_flags(self) -> None: ...
    def assign_label_seq_id(self, force: bool = False) -> None: ...
    def assign_serial_numbers(self) -> None: ...
    def assign_subchains(self, force: bool = False, fail_if_unknown: bool = True) -> None: ...
    def calculate_box(self, margin: float = 0.0) -> PositionBox: ...
    def calculate_fractional_box(self, margin: float = 0.0) -> FractionalBox: ...
    def clone(self) -> Structure: ...
    def collapse_hd_mixture(self) -> None: ...
    def deduplicate_entities(self) -> None: ...
    def ensure_entities(self) -> None: ...
    def expand_hd_mixture(self) -> None: ...
    def expand_ncs(self, how: HowToNameCopiedChain) -> None: ...
    def find_connection(self, partner1: AtomAddress, partner2: AtomAddress) -> Connection: ...
    def find_connection_by_cra(self, arg0: CRA, arg1: CRA) -> Connection: ...
    def find_or_add_model(self, name: str) -> Model: ...
    def find_spacegroup(self) -> SpaceGroup: ...
    def get_entity(self, subchain: str) -> Entity: ...
    def get_entity_of(self, subchain: ResidueSpan) -> Entity: ...
    def make_minimal_pdb(self) -> str: ...
    def make_mmcif_block(self, groups: MmcifOutputGroups = ...) -> cif.Block: ...
    def make_mmcif_document(self, groups: MmcifOutputGroups = ...) -> cif.Document: ...
    def make_mmcif_headers(self) -> cif.Block: ...
    def make_pdb_headers(self) -> str: ...
    def merge_chain_parts(self, min_sep: int = 0) -> None: ...
    def remove_alternative_conformations(self) -> None: ...
    def remove_empty_chains(self) -> None: ...
    def remove_hydrogens(self) -> None: ...
    def remove_ligands_and_waters(self) -> None: ...
    def remove_waters(self) -> None: ...
    def renumber_models(self) -> None: ...
    def setup_cell_images(self) -> None: ...
    def setup_entities(self) -> None: ...
    def shorten_chain_names(self) -> None: ...
    def transform_to_assembly(self, assembly_name: str, how: HowToNameCopiedChain) -> None: ...
    def update_mmcif_block(self, block: cif.Block, groups: MmcifOutputGroups = ...) -> None: ...
    def write_minimal_pdb(self, path: str) -> None: ...
    def write_pdb(
        self,
        path: str,
        seqres_records: bool = True,
        ssbond_records: bool = True,
        link_records: bool = True,
        cispep_records: bool = True,
        ter_records: bool = True,
        numbered_ter: bool = True,
        ter_ignores_type: bool = False,
        use_linkr: bool = False,
    ) -> None: ...
    @property
    def assemblies(self) -> AssemblyList:
        """
        :type: AssemblyList
        """
    @assemblies.setter
    def assemblies(self, arg0: AssemblyList) -> None:
        pass
    @property
    def cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @cell.setter
    def cell(self, arg0: UnitCell) -> None:
        pass
    @property
    def connections(self) -> ConnectionList:
        """
        :type: ConnectionList
        """
    @connections.setter
    def connections(self, arg0: ConnectionList) -> None:
        pass
    @property
    def entities(self) -> EntityList:
        """
        :type: EntityList
        """
    @entities.setter
    def entities(self, arg0: EntityList) -> None:
        pass
    @property
    def has_d_fraction(self) -> bool:
        """
        :type: bool
        """
    @has_d_fraction.setter
    def has_d_fraction(self, arg0: bool) -> None:
        pass
    @property
    def helices(self) -> HelixList:
        """
        :type: HelixList
        """
    @helices.setter
    def helices(self, arg0: HelixList) -> None:
        pass
    @property
    def info(self) -> InfoMap:
        """
        :type: InfoMap
        """
    @info.setter
    def info(self, arg0: InfoMap) -> None:
        pass
    @property
    def input_format(self) -> CoorFormat:
        """
        :type: CoorFormat
        """
    @input_format.setter
    def input_format(self, arg0: CoorFormat) -> None:
        pass
    @property
    def meta(self) -> Metadata:
        """
        :type: Metadata
        """
    @meta.setter
    def meta(self, arg0: Metadata) -> None:
        pass
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    @property
    def ncs(self) -> NcsOpList:
        """
        :type: NcsOpList
        """
    @ncs.setter
    def ncs(self, arg0: NcsOpList) -> None:
        pass
    @property
    def raw_remarks(self) -> list[str]:
        """
        :type: typing.List[str]
        """
    @raw_remarks.setter
    def raw_remarks(self, arg0: list[str]) -> None:
        pass
    @property
    def resolution(self) -> float:
        """
        :type: float
        """
    @resolution.setter
    def resolution(self, arg0: float) -> None:
        pass
    @property
    def sheets(self) -> SheetList:
        """
        :type: SheetList
        """
    @sheets.setter
    def sheets(self, arg0: SheetList) -> None:
        pass
    @property
    def spacegroup_hm(self) -> str:
        """
        :type: str
        """
    @spacegroup_hm.setter
    def spacegroup_hm(self, arg0: str) -> None:
        pass

class StructureFactorCalculatorE:
    def __init__(self, arg0: UnitCell) -> None: ...
    def calculate_sf_from_model(self, arg0: Model, arg1: list[int]) -> complex: ...
    def calculate_sf_from_small_structure(self, arg0: SmallStructure, arg1: list[int]) -> complex: ...
    @property
    def addends(self) -> Addends:
        """
        :type: Addends
        """
    @addends.setter
    def addends(self, arg0: Addends) -> None:
        pass

class StructureFactorCalculatorN:
    def __init__(self, arg0: UnitCell) -> None: ...
    def calculate_sf_from_model(self, arg0: Model, arg1: list[int]) -> complex: ...
    def calculate_sf_from_small_structure(self, arg0: SmallStructure, arg1: list[int]) -> complex: ...
    @property
    def addends(self) -> Addends:
        """
        :type: Addends
        """
    @addends.setter
    def addends(self, arg0: Addends) -> None:
        pass

class StructureFactorCalculatorX:
    def __init__(self, arg0: UnitCell) -> None: ...
    def calculate_mb_z(self, model: Model, hkl: list[int], only_h: bool = False) -> complex: ...
    def calculate_sf_from_model(self, arg0: Model, arg1: list[int]) -> complex: ...
    def calculate_sf_from_small_structure(self, arg0: SmallStructure, arg1: list[int]) -> complex: ...
    def mott_bethe_factor(self) -> float: ...
    @property
    def addends(self) -> Addends:
        """
        :type: Addends
        """
    @addends.setter
    def addends(self, arg0: Addends) -> None:
        pass

class SupResult:
    @property
    def center1(self) -> Position:
        """
        :type: Position
        """
    @property
    def center2(self) -> Position:
        """
        :type: Position
        """
    @property
    def count(self) -> int:
        """
        :type: int
        """
    @property
    def rmsd(self) -> float:
        """
        :type: float
        """
    @property
    def transform(self) -> Transform:
        """
        :type: Transform
        """

class SupSelect:
    """
    Members:

      CaP

      MainChain

      All
    """

    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    All: gemmi.SupSelect  # value = <SupSelect.All: 2>
    CaP: gemmi.SupSelect  # value = <SupSelect.CaP: 0>
    MainChain: gemmi.SupSelect  # value = <SupSelect.MainChain: 1>

class TableS3:
    def __init__(self, d_min: float, d_max: float) -> None: ...
    def get_value(self, arg0: float) -> float: ...
    def make_table(self, arg0: list[float], arg1: list[float]) -> None: ...
    @property
    def s3_values(self) -> list[float]:
        """
        :type: typing.List[float]
        """
    @property
    def y_values(self) -> list[float]:
        """
        :type: typing.List[float]
        """

class TlsGroup:
    class Selection:
        def __init__(self) -> None: ...
        @property
        def chain(self) -> str:
            """
            :type: str
            """
        @chain.setter
        def chain(self, arg0: str) -> None:
            pass
        @property
        def details(self) -> str:
            """
            :type: str
            """
        @details.setter
        def details(self, arg0: str) -> None:
            pass
        @property
        def res_begin(self) -> SeqId:
            """
            :type: SeqId
            """
        @res_begin.setter
        def res_begin(self, arg0: SeqId) -> None:
            pass
        @property
        def res_end(self) -> SeqId:
            """
            :type: SeqId
            """
        @res_end.setter
        def res_end(self, arg0: SeqId) -> None:
            pass
    def __init__(self) -> None: ...
    @property
    def L(self) -> Mat33:
        """
        :type: Mat33
        """
    @L.setter
    def L(self, arg0: Mat33) -> None:
        pass
    @property
    def S(self) -> Mat33:
        """
        :type: Mat33
        """
    @S.setter
    def S(self, arg0: Mat33) -> None:
        pass
    @property
    def T(self) -> Mat33:
        """
        :type: Mat33
        """
    @T.setter
    def T(self, arg0: Mat33) -> None:
        pass
    @property
    def id(self) -> str:
        """
        :type: str
        """
    @id.setter
    def id(self, arg0: str) -> None:
        pass
    @property
    def origin(self) -> Position:
        """
        :type: Position
        """
    @origin.setter
    def origin(self, arg0: Position) -> None:
        pass
    @property
    def selections(self) -> list[TlsGroup.Selection]:
        """
        :type: typing.List[TlsGroup.Selection]
        """
    @selections.setter
    def selections(self, arg0: list[TlsGroup.Selection]) -> None:
        pass

class Topo:
    class Angle:
        def calculate(self) -> float: ...
        def calculate_z(self) -> float: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @property
        def restr(self) -> Restraints.Angle:
            """
            :type: Restraints.Angle
            """

    class Bond:
        def calculate(self) -> float: ...
        def calculate_z(self) -> float: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @property
        def restr(self) -> Restraints.Bond:
            """
            :type: Restraints.Bond
            """

    class ChainInfo:
        @property
        def chain_ref(self) -> Chain:
            """
            :type: Chain
            """
        @property
        def entity_id(self) -> str:
            """
            :type: str
            """
        @property
        def polymer(self) -> bool:
            """
            :type: bool
            """
        @property
        def polymer_type(self) -> PolymerType:
            """
            :type: PolymerType
            """
        @property
        def res_infos(self) -> list[Topo.ResInfo]:
            """
            :type: typing.List[Topo.ResInfo]
            """
        @property
        def subchain_name(self) -> str:
            """
            :type: str
            """

    class Chirality:
        def calculate(self) -> float: ...
        def calculate_z(self, ideal_abs_vol: float, esd: float) -> float: ...
        def check(self) -> bool: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @property
        def restr(self) -> Restraints.Chirality:
            """
            :type: Restraints.Chirality
            """

    class FinalChemComp:
        @property
        def altloc(self) -> str:
            """
            :type: str
            """
        @property
        def cc(self) -> ChemComp:
            """
            :type: ChemComp
            """

    class Link:
        @property
        def alt1(self) -> str:
            """
            :type: str
            """
        @property
        def alt2(self) -> str:
            """
            :type: str
            """
        @property
        def link_id(self) -> str:
            """
            :type: str
            """
        @property
        def res1(self) -> Residue:
            """
            :type: Residue
            """
        @property
        def res2(self) -> Residue:
            """
            :type: Residue
            """

    class Mod:
        @property
        def alias(self) -> ChemComp.Group:
            """
            :type: ChemComp.Group
            """
        @property
        def altloc(self) -> str:
            """
            :type: str
            """
        @property
        def id(self) -> str:
            """
            :type: str
            """

    class Plane:
        def has(self, arg0: Atom) -> bool: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @property
        def restr(self) -> Restraints.Plane:
            """
            :type: Restraints.Plane
            """

    class ResInfo:
        def get_final_chemcomp(self, arg0: str) -> ChemComp: ...
        @property
        def chemcomps(self) -> list[Topo.FinalChemComp]:
            """
            :type: typing.List[Topo.FinalChemComp]
            """
        @property
        def mods(self) -> list[Topo.Mod]:
            """
            :type: typing.List[Topo.Mod]
            """
        @property
        def monomer_rules(self) -> list[Topo.Rule]:
            """
            :type: typing.List[Topo.Rule]
            """
        @property
        def prev(self) -> list[Topo.Link]:
            """
            :type: typing.List[Topo.Link]
            """
        @property
        def res(self) -> Residue:
            """
            :type: Residue
            """

    class Rule:
        @property
        def index(self) -> int:
            """
            :type: int
            """
        @property
        def rkind(self) -> RKind:
            """
            :type: RKind
            """

    class Torsion:
        def calculate(self) -> float: ...
        def calculate_z(self) -> float: ...
        @property
        def atoms(self) -> list[Atom]:
            """
            :type: typing.List[Atom]
            """
        @property
        def restr(self) -> Restraints.Torsion:
            """
            :type: Restraints.Torsion
            """
    def __init__(self) -> None: ...
    def adjust_hydrogen_distances(self, of: Restraints.DistanceOf, default_scale: float = 1.0) -> None: ...
    def first_bond_in_link(self, arg0: Topo.Link) -> Topo.Bond: ...
    def ideal_chiral_abs_volume_sigma(self, arg0: Topo.Chirality) -> tuple[float, float]: ...
    def links_to_previous(self, arg0: Residue) -> TopoLinks: ...
    @property
    def angles(self) -> TopoAngles:
        """
        :type: TopoAngles
        """
    @property
    def bonds(self) -> TopoBonds:
        """
        :type: TopoBonds
        """
    @property
    def chain_infos(self) -> TopoChainInfos:
        """
        :type: TopoChainInfos
        """
    @property
    def chirs(self) -> TopoChirs:
        """
        :type: TopoChirs
        """
    @property
    def extras(self) -> TopoLinks:
        """
        :type: TopoLinks
        """
    @property
    def planes(self) -> TopoPlanes:
        """
        :type: TopoPlanes
        """
    @property
    def torsions(self) -> TopoTorsions:
        """
        :type: TopoTorsions
        """

class TopoAngles:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Topo.Angle:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> TopoAngles: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TopoAngles) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Topo.Angle) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TopoAngles) -> None: ...
    def append(self, x: Topo.Angle) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: TopoAngles) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Topo.Angle) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Topo.Angle:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Topo.Angle: ...

class TopoBonds:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Topo.Bond:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> TopoBonds: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TopoBonds) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Topo.Bond) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TopoBonds) -> None: ...
    def append(self, x: Topo.Bond) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: TopoBonds) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Topo.Bond) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Topo.Bond:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Topo.Bond: ...

class TopoChainInfos:
    def __getitem__(self, arg0: int) -> Topo.ChainInfo: ...
    def __len__(self) -> int: ...

class TopoChirs:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Topo.Chirality:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> TopoChirs: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TopoChirs) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Topo.Chirality) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TopoChirs) -> None: ...
    def append(self, x: Topo.Chirality) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: TopoChirs) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Topo.Chirality) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Topo.Chirality:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Topo.Chirality: ...

class TopoFinalChemComps:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Topo.FinalChemComp:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> TopoFinalChemComps: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TopoFinalChemComps) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Topo.FinalChemComp) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TopoFinalChemComps) -> None: ...
    def append(self, x: Topo.FinalChemComp) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: TopoFinalChemComps) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Topo.FinalChemComp) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Topo.FinalChemComp:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Topo.FinalChemComp: ...

class TopoLinks:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Topo.Link:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> TopoLinks: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TopoLinks) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Topo.Link) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TopoLinks) -> None: ...
    def append(self, x: Topo.Link) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: TopoLinks) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Topo.Link) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Topo.Link:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Topo.Link: ...

class TopoMods:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: Topo.Mod) -> bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: TopoMods) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Topo.Mod:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> TopoMods: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TopoMods) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: TopoMods) -> bool: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Topo.Mod) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TopoMods) -> None: ...
    def append(self, x: Topo.Mod) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: Topo.Mod) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: TopoMods) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Topo.Mod) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Topo.Mod:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Topo.Mod: ...
    def remove(self, x: Topo.Mod) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None

class TopoPlanes:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Topo.Plane:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> TopoPlanes: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TopoPlanes) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Topo.Plane) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TopoPlanes) -> None: ...
    def append(self, x: Topo.Plane) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: TopoPlanes) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Topo.Plane) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Topo.Plane:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Topo.Plane: ...

class TopoResInfos:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Topo.ResInfo:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> TopoResInfos: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TopoResInfos) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Topo.ResInfo) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TopoResInfos) -> None: ...
    def append(self, x: Topo.ResInfo) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: TopoResInfos) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Topo.ResInfo) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Topo.ResInfo:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Topo.ResInfo: ...

class TopoRules:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Topo.Rule:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> TopoRules: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TopoRules) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Topo.Rule) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TopoRules) -> None: ...
    def append(self, x: Topo.Rule) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: TopoRules) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Topo.Rule) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Topo.Rule:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Topo.Rule: ...

class TopoTorsions:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> Topo.Torsion:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> TopoTorsions: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: TopoTorsions) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    @typing.overload
    def __setitem__(self, arg0: int, arg1: Topo.Torsion) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: TopoTorsions) -> None: ...
    def append(self, x: Topo.Torsion) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    @typing.overload
    def extend(self, L: TopoTorsions) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: Topo.Torsion) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> Topo.Torsion:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> Topo.Torsion: ...

class FTransform(Transform):
    def apply(self, arg0: Fractional) -> Fractional: ...

class UnitCell:
    def __eq__(self, arg0: UnitCell) -> bool: ...
    def __getstate__(self) -> tuple: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a: float, b: float, c: float, alpha: float, beta: float, gamma: float) -> None: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    def approx(self, other: UnitCell, epsilon: float) -> bool: ...
    def calculate_1_d2(self, hkl: list[int]) -> float: ...
    def calculate_1_d2_array(self, arg0: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float64]: ...
    def calculate_d(self, hkl: list[int]) -> float: ...
    def calculate_d_array(self, arg0: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float64]: ...
    def calculate_u_eq(self, arg0: SMat33d) -> float: ...
    def changed_basis_backward(self, op: Op, set_images: bool) -> UnitCell: ...
    def changed_basis_forward(self, op: Op, set_images: bool) -> UnitCell: ...
    def find_nearest_image(self, ref: Position, pos: Position, asu: Asu = ...) -> NearestImage: ...
    @typing.overload
    def find_nearest_pbc_image(self, fref: Fractional, fpos: Fractional, image_idx: int) -> NearestImage: ...
    @typing.overload
    def find_nearest_pbc_image(self, ref: Position, pos: Position, image_idx: int) -> NearestImage: ...
    def find_nearest_pbc_position(
        self,
        ref: Position,
        pos: Position,
        image_idx: int,
        inverse: bool = False,
    ) -> Position: ...
    def fractionalize(self, arg0: Position) -> Fractional: ...
    def get_hkl_limits(self, dmin: float) -> list[int]: ...
    def is_compatible_with_spacegroup(self, sg: SpaceGroup, eps: float = 0.001) -> bool: ...
    def is_crystal(self) -> bool: ...
    def is_similar(self, other: UnitCell, rel: float, deg: float) -> bool: ...
    @typing.overload
    def is_special_position(self, fpos: Fractional, max_dist: float) -> int: ...
    @typing.overload
    def is_special_position(self, pos: Position, max_dist: float = 0.8) -> int: ...
    def metric_tensor(self) -> SMat33d: ...
    def op_as_transform(self, arg0: Op) -> Transform: ...
    def orthogonalize(self, arg0: Fractional) -> Position: ...
    def orthogonalize_box(self, arg0: FractionalBox) -> PositionBox: ...
    def primitive_orth_matrix(self, centring_type: str) -> Mat33: ...
    def reciprocal(self) -> UnitCell: ...
    def reciprocal_metric_tensor(self) -> SMat33d: ...
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> None: ...
    def volume_per_image(self) -> float: ...
    @property
    def a(self) -> float:
        """
        :type: float
        """
    @property
    def alpha(self) -> float:
        """
        :type: float
        """
    @property
    def b(self) -> float:
        """
        :type: float
        """
    @property
    def beta(self) -> float:
        """
        :type: float
        """
    @property
    def c(self) -> float:
        """
        :type: float
        """
    @property
    def frac(self) -> Transform:
        """
        :type: Transform
        """
    @property
    def fractionalization_matrix(self) -> Mat33:
        """
        :type: Mat33
        """
    @property
    def gamma(self) -> float:
        """
        :type: float
        """
    @property
    def images(self) -> list[FTransform]:
        """
        :type: typing.List[FTransform]
        """
    @property
    def orth(self) -> Transform:
        """
        :type: Transform
        """
    @property
    def orthogonalization_matrix(self) -> Mat33:
        """
        :type: Mat33
        """
    @property
    def parameters(self) -> tuple:
        """
        :type: tuple
        """
    @property
    def volume(self) -> float:
        """
        :type: float
        """
    __hash__ = None

class ValueSigma:
    def __repr__(self) -> str: ...
    @property
    def sigma(self) -> float:
        """
        :type: float
        """
    @sigma.setter
    def sigma(self, arg0: float) -> None:
        pass
    @property
    def value(self) -> float:
        """
        :type: float
        """
    @value.setter
    def value(self, arg0: float) -> None:
        pass

class ValueSigmaAsuData:
    def __getitem__(self, index: int) -> ValueSigmaHklValue: ...
    def __init__(
        self,
        cell: UnitCell,
        sg: SpaceGroup,
        miller_array: numpy.ndarray[numpy.int32],
        value_array: numpy.ndarray[ValueSigma],
    ) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def copy(self) -> ValueSigmaAsuData: ...
    def count_equal_values(self, arg0: ValueSigmaAsuData) -> int: ...
    def ensure_asu(self, tnt_asu: bool = False) -> None: ...
    def ensure_sorted(self) -> None: ...
    def make_1_d2_array(self) -> numpy.ndarray[numpy.float32]: ...
    def make_d_array(self) -> numpy.ndarray[numpy.float32]: ...
    @property
    def miller_array(self) -> numpy.ndarray[numpy.int32]:
        """
        :type: numpy.ndarray[numpy.int32]
        """
    @property
    def spacegroup(self) -> SpaceGroup:
        """
        :type: SpaceGroup
        """
    @spacegroup.setter
    def spacegroup(self, arg0: SpaceGroup) -> None:
        pass
    @property
    def unit_cell(self) -> UnitCell:
        """
        :type: UnitCell
        """
    @unit_cell.setter
    def unit_cell(self, arg0: UnitCell) -> None:
        pass
    @property
    def value_array(self) -> numpy.ndarray[ValueSigma]:
        """
        :type: numpy.ndarray[ValueSigma]
        """

class ValueSigmaHklValue:
    def __repr__(self) -> str: ...
    @property
    def hkl(self) -> list[int]:
        """
        :type: typing.List[int]
        """
    @property
    def value(self) -> ValueSigma:
        """
        :type: ValueSigma
        """
    @value.setter
    def value(self, arg0: ValueSigma) -> None:
        pass

class Fractional(Vec3):
    def __add__(self, arg0: Fractional) -> Fractional: ...
    def __getitem__(self, arg0: int) -> float: ...
    @typing.overload
    def __init__(self, arg0: Vec3) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: float) -> None: ...
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Fractional) -> Fractional: ...
    def wrap_to_unit(self) -> Fractional: ...
    def wrap_to_zero(self) -> Fractional: ...

class VectorMarkPtr:
    def __bool__(self) -> bool:
        """
        Check whether the list is nonempty
        """
    def __contains__(self, x: NeighborSearch.Mark) -> bool:
        """
        Return true the container contains ``x``
        """
    @typing.overload
    def __delitem__(self, arg0: int) -> None:
        """
        Delete the list elements at index ``i``

        Delete list elements using a slice object
        """
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __eq__(self, arg0: VectorMarkPtr) -> bool: ...
    @typing.overload
    def __getitem__(self, arg0: int) -> NeighborSearch.Mark:
        """
        Retrieve list elements using a slice object
        """
    @typing.overload
    def __getitem__(self, s: slice) -> VectorMarkPtr: ...
    @typing.overload
    def __init__(self) -> None:
        """
        Copy constructor
        """
    @typing.overload
    def __init__(self, arg0: VectorMarkPtr) -> None: ...
    @typing.overload
    def __init__(self, arg0: typing.Iterable) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __ne__(self, arg0: VectorMarkPtr) -> bool: ...
    def __repr__(self) -> str:
        """
        Return the canonical string representation of this list.
        """
    @typing.overload
    def __setitem__(self, arg0: int, arg1: NeighborSearch.Mark) -> None:
        """
        Assign list elements using a slice object
        """
    @typing.overload
    def __setitem__(self, arg0: slice, arg1: VectorMarkPtr) -> None: ...
    def append(self, x: NeighborSearch.Mark) -> None:
        """
        Add an item to the end of the list
        """
    def clear(self) -> None:
        """
        Clear the contents
        """
    def count(self, x: NeighborSearch.Mark) -> int:
        """
        Return the number of times ``x`` appears in the list
        """
    @typing.overload
    def extend(self, L: VectorMarkPtr) -> None:
        """
        Extend the list by appending all the items in the given list

        Extend the list by appending all the items in the given list
        """
    @typing.overload
    def extend(self, L: typing.Iterable) -> None: ...
    def insert(self, i: int, x: NeighborSearch.Mark) -> None:
        """
        Insert an item at a given position.
        """
    @typing.overload
    def pop(self) -> NeighborSearch.Mark:
        """
        Remove and return the last item

        Remove and return the item at index ``i``
        """
    @typing.overload
    def pop(self, i: int) -> NeighborSearch.Mark: ...
    def remove(self, x: NeighborSearch.Mark) -> None:
        """
        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """
    __hash__ = None

def IT92_normalize() -> None:
    pass

def add_automatic_links(arg0: Model, arg1: Structure, arg2: MonLib) -> None:
    pass

def add_chemcomp_to_block(arg0: ChemComp, arg1: cif.Block) -> None:
    pass

def align_sequence_to_polymer(
    full_seq: list[str],
    polymer: ResidueSpan,
    polymer_type: PolymerType,
    scoring: AlignmentScoring = ...,
) -> AlignmentResult:
    pass

def align_string_sequences(
    query: list[str],
    target: list[str],
    free_gapo: list[bool],
    scoring: AlignmentScoring = ...,
) -> AlignmentResult:
    pass

def as_refln_blocks(arg0: cif.Document) -> ReflnBlocks:
    pass

def bessel_i1_over_i0(arg0: numpy.ndarray[numpy.float64]) -> object:
    pass

def bincorr(
    nbins: numpy.ndarray[numpy.int32],
    obs: numpy.ndarray[numpy.float64],
    calc: numpy.ndarray[numpy.float64],
) -> list[Correlation]:
    pass

def binmean(nbins: numpy.ndarray[numpy.int32], values: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
    pass

def binrfactor(
    nbins: numpy.ndarray[numpy.int32],
    obs: numpy.ndarray[numpy.float64],
    calc: numpy.ndarray[numpy.float64],
    riso: bool = False,
) -> numpy.ndarray[numpy.float64]:
    pass

def calculate_angle(arg0: Position, arg1: Position, arg2: Position) -> float:
    """
    Input: three points. Output: angle in radians.
    """

def calculate_b_est(arg0: Atom) -> float:
    pass

def calculate_current_rmsd(
    fixed: ResidueSpan,
    movable: ResidueSpan,
    ptype: PolymerType,
    sel: SupSelect,
    altloc: str = "\x00",
) -> SupResult:
    pass

def calculate_dihedral(arg0: Position, arg1: Position, arg2: Position, arg3: Position) -> float:
    """
    Input: four points. Output: dihedral angle in radians.
    """

def calculate_omega(residue: Residue, next_residue: Residue) -> float:
    pass

def calculate_phi_psi(prev_residue: Residue, residue: Residue, next_residue: Residue) -> list[float]:
    pass

def calculate_sequence_weight(sequence: list[str], unknown: float = 0.0) -> float:
    pass

def calculate_superposition(
    fixed: ResidueSpan,
    movable: ResidueSpan,
    ptype: PolymerType,
    sel: SupSelect,
    trim_cycles: int = 0,
    trim_cutoff: float = 2.0,
    altloc: str = "\x00",
) -> SupResult:
    pass

def calculate_superpositions_in_moving_window(
    fixed: ResidueSpan,
    movable: ResidueSpan,
    ptype: PolymerType,
    radius: float = 10.0,
) -> list[SupResult]:
    pass

@typing.overload
def check_data_type_under_symmetry(arg0: Mtz) -> DataType:
    pass

@typing.overload
def check_data_type_under_symmetry(arg0: ReflnBlock) -> DataType:
    pass

def combine_correlations(arg0: list[Correlation]) -> Correlation:
    pass

def count_reflections(
    cell: UnitCell,
    spacegroup: SpaceGroup,
    dmin: float,
    dmax: float = 0.0,
    unique: bool = True,
) -> int:
    pass

def cromer_liberman(z: int, energy: float) -> tuple[float, float]:
    pass

def estimate_uncompressed_size(path: str) -> int:
    """
    Returns uncompressed size of a .gz file (not always reliable)
    """

def expand_if_pdb_code(code: str, filetype: str = "M") -> str:
    pass

def expand_pdb_code_to_path(arg0: str, arg1: str) -> str:
    pass

def expand_protein_one_letter(arg0: str) -> str:
    pass

def expand_protein_one_letter_string(arg0: str) -> list[str]:
    pass

def find_asu_brick(arg0: SpaceGroup) -> AsuBrick:
    pass

def find_best_plane(atoms: list[Atom]) -> list[float]:
    pass

def find_blobs_by_flood_fill(
    grid: FloatGrid,
    cutoff: float,
    min_volume: float = 10.0,
    min_score: float = 15.0,
    min_peak: float = 0.0,
    negate: bool = False,
) -> list[Blob]:
    pass

def find_lattice_2fold_ops(reduced_cell: UnitCell, max_obliq: float) -> list[tuple[Op, float]]:
    pass

def find_lattice_symmetry(cell: UnitCell, centring: str, max_obliq: float) -> GroupOps:
    pass

def find_lattice_symmetry_r(arg0: UnitCell, arg1: float) -> GroupOps:
    pass

def find_spacegroup_by_name(hm: str, alpha: float = 0.0, gamma: float = 0.0) -> SpaceGroup:
    """
    Returns space-group with given name.
    """

def find_spacegroup_by_number(ccp4: int) -> SpaceGroup:
    """
    Returns space-group of given number.
    """

def find_spacegroup_by_ops(group_ops: GroupOps) -> SpaceGroup:
    """
    Returns space-group with identical operations.
    """

def find_tabulated_residue(name: str) -> ResidueInfo:
    """
    Find chemical component information in the internal table.
    """

def find_twin_laws(cell: UnitCell, sg: SpaceGroup, max_obliq: float, all_ops: bool) -> list[Op]:
    pass

def flood_fill_above(grid: FloatGrid, seeds: list[Position], threshold: float, negate: bool = False) -> Int8Grid:
    pass

def generators_from_hall(hall: str) -> GroupOps:
    """
    Parse Hall notation.
    """

def get_distance_from_plane(pos: Position, coeff: list[float]) -> float:
    pass

def get_spacegroup_reference_setting(number: int) -> SpaceGroup:
    pass

def hkl_cif_as_refln_block(block: cif.Block) -> ReflnBlock:
    pass

def interpolate_grid(dest: FloatGrid, src: FloatGrid, tr: Transform, order: int = 2) -> None:
    pass

def interpolate_grid_of_aligned_model2(
    dest: FloatGrid,
    src: FloatGrid,
    tr: Transform,
    dest_model: Model,
    radius: float,
    order: int = 2,
) -> None:
    pass

def is_pdb_code(arg0: str) -> bool:
    pass

def log_bessel_i0(arg0: numpy.ndarray[numpy.float64]) -> object:
    pass

def log_cosh(arg0: numpy.ndarray[numpy.float64]) -> object:
    pass

def make_address(arg0: Chain, arg1: Residue, arg2: Atom) -> AtomAddress:
    pass

def make_assembly(arg0: Assembly, arg1: Model, arg2: HowToNameCopiedChain) -> Model:
    pass

def make_chemcomp_from_block(arg0: cif.Block) -> ChemComp:
    pass

def make_miller_array(
    cell: UnitCell,
    spacegroup: SpaceGroup,
    dmin: float,
    dmax: float = 0.0,
    unique: bool = True,
) -> numpy.ndarray[numpy.int32]:
    pass

def make_small_structure_from_block(block: cif.Block) -> SmallStructure:
    """
    Takes CIF block and returns SmallStructure.
    """

def make_structure_from_block(block: cif.Block) -> Structure:
    """
    Takes mmCIF block and returns Structure.
    """

def make_structure_from_chemcomp_block(block: cif.Block) -> Structure:
    """
    CIF block from CCD or monomer library -> single-residue Structure.
    """

def make_triplet_part(xyz: list[int], w: int, style: str = "x") -> str:
    """
    Make one of the three parts of a triplet.
    """

def merge_atoms_in_expanded_model(model: Model, cell: UnitCell, max_dist: float = 0.2) -> None:
    pass

def mott_bethe_const() -> float:
    pass

def mx_to_sx_structure(st: Structure, n: int = 0) -> SmallStructure:
    pass

@typing.overload
def one_letter_code(arg0: ResidueSpan) -> str:
    pass

@typing.overload
def one_letter_code(arg0: list[str]) -> str:
    pass

def parse_triplet(triplet: str) -> Op:
    """
    Parse coordinate triplet into gemmi.Op.
    """

def parse_triplet_part(s: str) -> list[int]:
    """
    Parse one of the three parts of a triplet.
    """

def precondition_eigen_coo(
    arg0: numpy.ndarray[numpy.float64],
    arg1: numpy.ndarray[numpy.int32],
    arg2: numpy.ndarray[numpy.int32],
    arg3: int,
    arg4: float,
) -> tuple:
    pass

def prepare_blosum62_scoring() -> AlignmentScoring:
    pass

def prepare_refmac_crd(arg0: Structure, arg1: Topo, arg2: MonLib, arg3: HydrogenChange) -> cif.Document:
    pass

def prepare_topology(
    st: Structure,
    monlib: MonLib,
    model_index: int = 0,
    h_change: HydrogenChange = ...,
    reorder: bool = False,
    warnings: object = None,
    ignore_unknown_links: bool = False,
) -> Topo:
    pass

def read_ccp4_map(path: str, setup: bool = False) -> Ccp4Map:
    """
    Reads a CCP4 file, mode 2 (floating-point data).
    """

def read_ccp4_mask(path: str, setup: bool = False) -> Ccp4Mask:
    """
    Reads a CCP4 file, mode 0 (int8_t data, usually 0/1 masks).
    """

def read_monomer_lib(
    monomer_dir: str,
    resnames: list[str],
    libin: str = "",
    ignore_missing: bool = False,
) -> MonLib:
    pass

def read_mtz_file(path: str) -> Mtz:
    pass

def read_pdb(filename: str, max_line_length: int = 0, split_chain_on_ter: bool = False) -> Structure:
    pass

def read_pdb_string(s: str, max_line_length: int = 0, split_chain_on_ter: bool = False) -> Structure:
    """
    Reads a string as PDB file.
    """

def read_small_structure(path: str) -> SmallStructure:
    """
    Reads a small molecule CIF file.
    """

def read_structure(
    path: str,
    merge_chain_parts: bool = True,
    format: CoorFormat = ...,
    save_doc: cif.Document = None,
) -> Structure:
    """
    Reads a coordinate file into Structure.
    """

def seitz_to_op(arg0: list[list[float]]) -> Op:
    pass

def setup_for_crd(arg0: Structure) -> None:
    pass

def spacegroup_table() -> typing.Iterator:
    pass

def spacegroup_table_itb() -> typing.Iterator:
    pass

def superpose_positions(
    pos1: list[Position],
    pos2: list[Position],
    weight: list[float] = [],
) -> SupResult:
    pass

def symops_from_hall(hall: str) -> GroupOps:
    """
    Parse Hall notation.
    """

def transform_f_phi_grid_to_map(grid: ReciprocalComplexGrid) -> FloatGrid:
    pass

def transform_map_to_f_phi(map: FloatGrid, half_l: bool = False, use_scale: bool = True) -> ReciprocalComplexGrid:
    pass

__version__ = "0.6.0"
hc = ...
