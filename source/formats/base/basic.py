from ast import literal_eval
import numpy as np
from struct import Struct
from generated.array import Array
from generated.io import MAX_LEN


def class_from_struct(struct, from_value_func):
    # declare these in the local scope for faster name resolutions
    base_value = from_value_func(0)
    pack = struct.pack
    unpack = struct.unpack
    size = struct.size
    # these functions are used for efficient read/write of arrays
    empty = np.empty
    dtype = np.dtype(struct.format)

    class ConstructedClass:

        np_dtype = dtype

        def __new__(cls, context=None, arg=0, template=None):
            return base_value

        from_value = staticmethod(from_value_func)

        @staticmethod
        def from_stream(stream, context=None, arg=0, template=None):
            return unpack(stream.read(size))[0]

        @staticmethod
        def to_stream(instance, stream, context=None, arg=0, template=None):
            stream.write(pack(instance))

        @staticmethod
        def get_size(instance, context, arg=0, template=None):
            return size

        @staticmethod
        def create_array(shape, default=None, context=None, arg=0, template=None):
            if default:
                return np.full(shape, default, dtype)
            else:
                return np.zeros(shape, dtype)

        @staticmethod
        def read_array(stream, shape, context=None, arg=0, template=None):
            array = empty(shape, dtype)
            stream.readinto(array)
            return array

        @staticmethod
        def write_array(instance, stream):
            # check that it is a numpy array
            if not isinstance(instance, np.ndarray):
                instance = np.array(instance, dtype)
            # cast if wrong incoming dtype
            elif instance.dtype != dtype:
                instance = instance.astype(dtype)
            stream.write(instance.tobytes())

        @staticmethod
        def functions_for_stream(stream):
            # declare these in the local scope for faster name resolutions
            read = stream.read
            write = stream.write
            readinto = stream.readinto

            def read_value():
                return unpack(read(size))[0]

            def write_value(instance):
                write(pack(instance))

            def read_values(shape):
                array = empty(shape, dtype)
                # noinspection PyTypeChecker
                readinto(array)
                return array

            def write_values(instance):
                # check that it is a numpy array
                if not isinstance(instance, np.ndarray):
                    instance = np.array(instance, dtype)
                # cast if wrong incoming dtype
                elif instance.dtype != dtype:
                    instance = instance.astype(dtype)
                write(instance.tobytes())

            return read_value, write_value, read_values, write_values

        @staticmethod
        def from_xml(target, elem, prop, arg=0, template=None):
            return literal_eval(elem.attrib[prop])

        @staticmethod
        def _from_xml_array(instance, elem):
            return np.fromstring(elem.text, dtype=dtype, sep=" ")

        @staticmethod
        def to_xml(elem, prop, instance, arg, template, debug):
            elem.attrib[prop] = str(instance)

        @staticmethod
        def _to_xml_array(instance, elem, debug):
            elem.text = " ".join([str(member) for member in instance.flat])

        @staticmethod
        def fmt_member(member, indent=0):
            lines = str(member).split("\n")
            lines_new = [lines[0], ] + ["\t" * indent + line for line in lines[1:]]
            return "\n".join(lines_new)

        @classmethod
        def validate_instance(cls, instance, context=None, arg=0, template=None):
            assert(instance == cls.from_value(instance))

        @classmethod
        def validate_array(cls, instance, context=None, arg=0, template=None, shape=()):
            assert instance.shape == shape
            assert instance.dtype.char == dtype.char

    return ConstructedClass


Byte = class_from_struct(Struct("<b"), lambda value: (int(value) + 128) % 256 - 128)
Ubyte = class_from_struct(Struct("<B"), lambda value: int(value) % 256)
Uint64 = class_from_struct(Struct("<Q"), lambda value: int(value) % 18446744073709551616)
Uint = class_from_struct(Struct("<I"), lambda value: int(value) % 4294967296)
Ushort = class_from_struct(Struct("<H"), lambda value: int(value) % 65536)
Int = class_from_struct(Struct("<i"), lambda value: (int(value) + 2147483648) % 4294967296 - 2147483648)
Int64 = class_from_struct(Struct("<q"), lambda value: (int(value) + 9223372036854775808) % 18446744073709551616 - 9223372036854775808)
Short = class_from_struct(Struct("<h"), lambda value: (int(value) + 32768) % 65536 - 32768)
Char = Byte
Float = class_from_struct(Struct("<f"), float)
Double = class_from_struct(Struct("<d"), float)
Hfloat = class_from_struct(Struct("<e"), float)


# @staticmethod
def r_zstr(rfunc):
    i = 0
    val = b''
    char = b''
    while char != b'\x00':
        i += 1
        if i > MAX_LEN:
            raise ValueError(f'string too long')
        val += char
        char = rfunc(1)
        if not char:
            raise ValueError('Reached end of file before end of zstring')
    return val.decode(errors="surrogateescape")


# @staticmethod
def w_zstr(wfunc, val):
    wfunc(val.encode(errors="surrogateescape"))
    wfunc(b'\x00')


class ZString:

    def __new__(cls, context=None, arg=0, template=None):
        return ''

    @staticmethod
    def from_stream(stream, context=None, arg=0, template=None):
        return r_zstr(stream.read)

    @staticmethod
    def to_stream(instance, stream, context=None, arg=0, template=None):
        w_zstr(stream.write, instance)

    @staticmethod
    def from_value(value, context=None, arg=0, template=None):
        return str(value)

    @classmethod
    def functions_for_stream(cls, stream):
        # declare these in the local scope for faster name resolutions
        read = stream.read
        write = stream.write

        def read_zstring():
            return r_zstr(read)

        def write_zstring(instance):
            w_zstr(write, instance)

        def read_zstrings(shape):
            # pass empty context
            return Array.from_stream(stream, None, 0, None, shape, cls)

        def write_zstrings(instance):
            # pass empty context
            return Array.to_stream(instance, stream, None, 0, None, dtype=cls)

        return read_zstring, write_zstring, read_zstrings, write_zstrings

    @staticmethod
    def from_xml(target, elem, prop, arg=0, template=None):
        return elem[prop]

    @staticmethod
    def to_xml(elem, prop, instance, arg, template, debug):
        elem.attrib[prop] = instance

    @staticmethod
    def fmt_member(member, indent=0):
        lines = str(member).split("\n")
        lines_new = [lines[0], ] + ["\t" * indent + line for line in lines[1:]]
        return "\n".join(lines_new)

    @classmethod
    def validate_instance(instance, context=None, arg=0, template=None):
        assert(isinstance(instance, str))
        assert(len(instance.encode(errors="surrogateescape")) <= MAX_LEN)

    @staticmethod
    def get_size(instance, context, arg=0, template=None):
        return len(instance.encode(errors="surrogateescape")) + 1
