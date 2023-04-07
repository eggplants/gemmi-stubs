"""CIF file format"""
from __future__ import annotations
import gemmi.cif
import typing

__all__ = [
    "Block",
    "Column",
    "Document",
    "Item",
    "Loop",
    "Style",
    "Table",
    "as_int",
    "as_number",
    "as_string",
    "is_null",
    "quote",
    "quote_list",
    "read",
    "read_file",
    "read_mmjson",
    "read_string"
]


class Block():
    def __getitem__(self, index: int) -> Item: ...
    def __init__(self, arg0: str) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __repr__(self) -> str: ...
    def add_item(self, item: Item, pos: int = -1) -> Item: ...
    def as_string(self, style: Style = Style.Simple) -> str: 
        """
        Returns a string in CIF format.
        """
    @typing.overload
    def find(self, prefix: str, tags: typing.List[str]) -> Table: ...
    @typing.overload
    def find(self, tags: typing.List[str]) -> Table: ...
    def find_frame(self, name: str) -> Block: ...
    def find_loop(self, tag: str) -> Column: ...
    def find_loop_item(self, tag: str) -> Item: ...
    def find_mmcif_category(self, category: str) -> Table: 
        """
        Returns Table with all items in the category.
        """
    def find_or_add(self, prefix: str, tags: typing.List[str]) -> Table: ...
    def find_pair(self, tag: str) -> object: ...
    def find_pair_item(self, tag: str) -> Item: ...
    def find_value(self, tag: str) -> str: ...
    def find_values(self, tag: str) -> Column: ...
    def get_index(self, tag: str) -> int: ...
    def get_mmcif_category(self, name: str, raw: bool = False) -> dict: ...
    def get_mmcif_category_names(self) -> typing.List[str]: 
        """
        For mmCIF files only. Returns list of all category prefixes (_x.)
        """
    def init_loop(self, prefix: str, tags: typing.List[str]) -> Loop: ...
    def init_mmcif_loop(self, cat: str, tags: typing.List[str]) -> Loop: ...
    def item_as_table(self, arg0: Item) -> Table: ...
    def move_item(self, old_pos: int, new_pos: int) -> None: ...
    def set_mmcif_category(self, name: str, data: dict, raw: bool = False) -> None: ...
    def set_pair(self, tag: str, value: str) -> None: ...
    def set_pairs(self, prefix: str, data: dict, raw: bool = False) -> None: ...
    def write_file(self, filename: str, style: Style = Style.Simple) -> None: 
        """
        Write data to a CIF file.
        """
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        pass
    pass
class Column():
    def __bool__(self) -> bool: ...
    def __getitem__(self, arg0: int) -> str: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __setitem__(self, arg0: int, arg1: str) -> None: ...
    def get_loop(self) -> Loop: ...
    def str(self, index: int) -> str: ...
    @property
    def tag(self) -> str:
        """
        :type: str
        """
    @tag.setter
    def tag(self, arg1: str) -> None:
        pass
    pass
class Document():
    def __contains__(self, name: str) -> bool: ...
    def __delitem__(self, index: int) -> None: ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> list: ...
    @typing.overload
    def __getitem__(self, index: int) -> Block: ...
    @typing.overload
    def __getitem__(self, name: str) -> Block: ...
    def __init__(self) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def add_copied_block(self, block: Block, pos: int = -1) -> Block: ...
    def add_new_block(self, name: str, pos: int = -1) -> Block: ...
    def as_json(self, mmjson: bool = False, lowercase_names: bool = True) -> str: 
        """
        Returns JSON representation in a string.
        """
    def as_string(self, style: Style = Style.Simple) -> str: 
        """
        Returns a string in CIF format.
        """
    def check_for_duplicates(self) -> None: ...
    def check_for_missing_values(self) -> None: ...
    def clear(self) -> None: ...
    def find_block(self, name: str) -> Block: ...
    def parse_file(self, arg0: str) -> None: ...
    def parse_string(self, arg0: str) -> None: ...
    def sole_block(self) -> Block: 
        """
        Returns the only block if there is exactly one
        """
    def write_file(self, filename: str, style: Style = Style.Simple) -> None: 
        """
        Write data to a CIF file.
        """
    @property
    def source(self) -> str:
        """
        :type: str
        """
    @source.setter
    def source(self, arg0: str) -> None:
        pass
    pass
class Item():
    def erase(self) -> None: ...
    @property
    def frame(self) -> Block:
        """
        :type: Block
        """
    @property
    def line_number(self) -> int:
        """
        :type: int
        """
    @property
    def loop(self) -> Loop:
        """
        :type: Loop
        """
    @property
    def pair(self) -> object:
        """
        :type: object
        """
    pass
class Loop():
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def add_row(self, new_values: typing.List[str], pos: int = -1) -> None: ...
    def length(self) -> int: 
        """
        Returns number of rows
        """
    def set_all_values(self, columns: typing.List[typing.List[str]]) -> None: ...
    def val(self, row: int, col: int) -> str: ...
    def width(self) -> int: 
        """
        Returns number of columns
        """
    @property
    def tags(self) -> typing.List[str]:
        """
        :type: typing.List[str]
        """
    @property
    def values(self) -> typing.List[str]:
        """
        :type: typing.List[str]
        """
    pass
class Style():
    """
    Members:

      Simple

      NoBlankLines

      PreferPairs

      Pdbx

      Indent35

      Aligned
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
    Aligned: gemmi.cif.Style # value = <Style.Aligned: 5>
    Indent35: gemmi.cif.Style # value = <Style.Indent35: 4>
    NoBlankLines: gemmi.cif.Style # value = <Style.NoBlankLines: 1>
    Pdbx: gemmi.cif.Style # value = <Style.Pdbx: 3>
    PreferPairs: gemmi.cif.Style # value = <Style.PreferPairs: 2>
    Simple: gemmi.cif.Style # value = <Style.Simple: 0>
    __members__: dict # value = {'Simple': <Style.Simple: 0>, 'NoBlankLines': <Style.NoBlankLines: 1>, 'PreferPairs': <Style.PreferPairs: 2>, 'Pdbx': <Style.Pdbx: 3>, 'Indent35': <Style.Indent35: 4>, 'Aligned': <Style.Aligned: 5>}
    pass
class Table():
    class Row():
        @typing.overload
        def __getitem__(self, arg0: int) -> str: ...
        @typing.overload
        def __getitem__(self, arg0: str) -> str: ...
        def __iter__(self) -> typing.Iterator: ...
        def __len__(self) -> int: ...
        def __repr__(self) -> str: ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: str) -> None: ...
        @typing.overload
        def __setitem__(self, arg0: str, arg1: str) -> None: ...
        def get(self, index: int) -> str: ...
        def has(self, index: int) -> bool: ...
        def str(self, arg0: int) -> str: ...
        @property
        def row_index(self) -> int:
            """
            :type: int
            """
        pass
    def __bool__(self) -> bool: ...
    @typing.overload
    def __delitem__(self, arg0: int) -> None: ...
    @typing.overload
    def __delitem__(self, arg0: slice) -> None: ...
    def __getitem__(self, arg0: int) -> Table.Row: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def append_row(self, new_values: typing.List[str]) -> None: ...
    def column(self, n: int) -> Column: ...
    def erase(self) -> None: ...
    def find_column(self, tag: str) -> Column: ...
    def find_row(self, arg0: str) -> Table.Row: ...
    def get_prefix(self) -> str: ...
    def has_column(self, arg0: int) -> bool: ...
    def move_row(self, old_pos: int, new_pos: int) -> None: ...
    def remove_row(self, row_index: int) -> None: ...
    def width(self) -> int: ...
    @property
    def loop(self) -> Loop:
        """
        :type: Loop
        """
    @property
    def prefix_length(self) -> int:
        """
        :type: int
        """
    @property
    def tags(self) -> Table.Row:
        """
        :type: Table.Row
        """
    pass
@typing.overload
def as_int(value: str) -> int:
    """
    Returns int number from string value.

    Returns int number from string value or the second arg if null.
    """
@typing.overload
def as_int(value: str, default: int) -> int:
    pass
def as_number(value: str, default: float = nan) -> float:
    """
    Returns float number from string
    """
def as_string(value: str) -> str:
    """
    Get string content (no quotes) from raw string.
    """
def is_null(value: str) -> bool:
    pass
def quote(string: str) -> str:
    pass
def quote_list(arg0: list) -> typing.List[str]:
    pass
def read(filename: str) -> Document:
    """
    Reads normal or gzipped CIF file.
    """
def read_file(filename: str) -> Document:
    """
    Reads a CIF file copying data into Document.
    """
def read_mmjson(filename: str) -> Document:
    """
    Reads normal or gzipped mmJSON file.
    """
def read_string(data: str) -> Document:
    """
    Reads a string as a CIF file.
    """
