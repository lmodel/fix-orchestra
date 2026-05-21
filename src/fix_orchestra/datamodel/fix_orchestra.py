# Auto generated from fix_orchestra.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-21T18:02:06
# Schema: fix_orchestra
#
# id: https://w3id.org/lmodel/fix-orchestra
# description: LinkML schema generated from the FIX Orchestra v1.1-RC2 XSD artifacts (repository.xsd, repositorytypes.xsd, interfaces.xsd).
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDate, XSDDateTime

metamodel_version = "1.11.0"
version = "1.1-rc2"

# Namespaces
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
DCMITYPE = CurieNamespace('dcmitype', 'http://purl.org/dc/dcmitype/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
FIX_ORCHESTRA = CurieNamespace('fix_orchestra', 'https://w3id.org/lmodel/fix-orchestra/')
FIXI = CurieNamespace('fixi', 'http://fixprotocol.io/2024/orchestra/interfaces/')
FIXR = CurieNamespace('fixr', 'http://fixprotocol.io/2024/orchestra/repository/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XML = CurieNamespace('xml', 'http://www.w3.org/XML/1998/namespace#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = FIX_ORCHESTRA


# Types
class ComponentName(String):
    type_class_uri = FIXR["ComponentName_t"]
    type_class_curie = "fixr:ComponentName_t"
    type_name = "ComponentName"
    type_model_uri = FIX_ORCHESTRA.ComponentName


class DatatypeStandard(String):
    """ Extensible datatype standards | Union of: fixr:datatypeStandard_enum, xs:string """
    type_class_uri = FIXR["datatypeStandard_t"]
    type_class_curie = "fixr:datatypeStandard_t"
    type_name = "DatatypeStandard"
    type_model_uri = FIX_ORCHESTRA.DatatypeStandard


class EP(Integer):
    type_class_uri = FIXR["EP_t"]
    type_class_curie = "fixr:EP_t"
    type_name = "EP"
    type_model_uri = FIX_ORCHESTRA.EP


class ExpressionType(String):
    """ Expressed in a Domain Specific Language """
    type_class_uri = FIXR["expressionType"]
    type_class_curie = "fixr:expressionType"
    type_name = "ExpressionType"
    type_model_uri = FIX_ORCHESTRA.ExpressionType


class Id(Integer):
    type_class_uri = FIXR["id_t"]
    type_class_curie = "fixr:id_t"
    type_name = "Id"
    type_model_uri = FIX_ORCHESTRA.Id


class Language(String):
    type_class_uri = FIXR["language_t"]
    type_class_curie = "fixr:language_t"
    type_name = "Language"
    type_model_uri = FIX_ORCHESTRA.Language


class Mime(String):
    """ Multipurpose Internet Mail Extensions (MIME) media type """
    type_class_uri = FIXR["mime_t"]
    type_class_curie = "fixr:mime_t"
    type_name = "Mime"
    type_model_uri = FIX_ORCHESTRA.Mime


class MsgType(String):
    type_class_uri = FIXR["MsgType_t"]
    type_class_curie = "fixr:MsgType_t"
    type_name = "MsgType"
    type_model_uri = FIX_ORCHESTRA.MsgType


class Name(String):
    """ Names are from 1-64 characters. The XML processor will remove line feeds, carriage returns, tabs, leading and trailing spaces, and multiple spaces. Single internal spaces are allowed by the schema but may be restricted by an external style. """
    type_class_uri = FIXR["Name_t"]
    type_class_curie = "fixr:Name_t"
    type_name = "Name"
    type_model_uri = FIX_ORCHESTRA.Name


class Purpose(String):
    """ Extensible annotation purposes | Union of: fixr:purpose_enum, xs:string """
    type_class_uri = FIXR["purpose_t"]
    type_class_curie = "fixr:purpose_t"
    type_name = "Purpose"
    type_model_uri = FIX_ORCHESTRA.Purpose


class UnboundedIntType(String):
    """ Union of: xs:nonNegativeInteger, fixr:unbounded """
    type_class_uri = FIXR["unboundedIntType"]
    type_class_curie = "fixr:unboundedIntType"
    type_name = "UnboundedIntType"
    type_model_uri = FIX_ORCHESTRA.UnboundedIntType


class Version(String):
    type_class_uri = FIXR["Version_t"]
    type_class_curie = "fixr:Version_t"
    type_name = "Version"
    type_model_uri = FIX_ORCHESTRA.Version


class ProtocolName(String):
    """ Protocol names are not constrained to FIX protocols | Union of: fixi:protocolEnum_t, xs:token """
    type_class_uri = FIXI["protocolName_t"]
    type_class_curie = "fixi:protocolName_t"
    type_name = "ProtocolName"
    type_model_uri = FIX_ORCHESTRA.ProtocolName


class InterfacePurpose(String):
    """ Extensible annotation purposes | Union of: fixi:purpose_enum, xs:token """
    type_class_uri = FIXI["purpose_t"]
    type_class_curie = "fixi:purpose_t"
    type_name = "InterfacePurpose"
    type_model_uri = FIX_ORCHESTRA.InterfacePurpose


class TransportUse(String):
    """ Extensible transport use | Union of: fixi:transportUse_enum, xs:token """
    type_class_uri = FIXI["transportUse_t"]
    type_class_curie = "fixi:transportUse_t"
    type_name = "TransportUse"
    type_model_uri = FIX_ORCHESTRA.TransportUse


class FIXInt(Integer):
    """ FIX int base datatype. Sequence of digits without commas or decimals and optional sign character (ASCII characters "-" and "0" - "9" ). The sign character utilizes one byte (i.e. positive int is "99999" while negative int is "-99999"). Note that int values may contain leading zeros (e.g. "00023" = "23"). """
    type_class_uri = FIXR["int"]
    type_class_curie = "fixr:int"
    type_name = "FIXInt"
    type_model_uri = FIX_ORCHESTRA.FIXInt


class FIXLength(Integer):
    """ FIX Length datatype (extends int). int field representing the length in bytes. Value must be positive. """
    type_class_uri = FIXR["Length"]
    type_class_curie = "fixr:Length"
    type_name = "FIXLength"
    type_model_uri = FIX_ORCHESTRA.FIXLength


class FIXTagNum(Integer):
    """ FIX TagNum datatype (extends int). int field representing a field's tag number when using FIX "Tag=Value" syntax. Value must be positive and may not contain leading zeros. """
    type_class_uri = FIXR["TagNum"]
    type_class_curie = "fixr:TagNum"
    type_name = "FIXTagNum"
    type_model_uri = FIX_ORCHESTRA.FIXTagNum


class FIXSeqNum(Integer):
    """ FIX SeqNum datatype (extends int). int field representing a message sequence number. Value must be positive. """
    type_class_uri = FIXR["SeqNum"]
    type_class_curie = "fixr:SeqNum"
    type_name = "FIXSeqNum"
    type_model_uri = FIX_ORCHESTRA.FIXSeqNum


class FIXNumInGroup(String):
    """ FIX NumInGroup datatype (extends int). int field representing the number of entries in a repeating group. Value must be positive. """
    type_class_uri = FIXR["NumInGroup"]
    type_class_curie = "fixr:NumInGroup"
    type_name = "FIXNumInGroup"
    type_model_uri = FIX_ORCHESTRA.FIXNumInGroup


class FIXDayOfMonth(Integer):
    """ FIX DayOfMonth datatype (extends int). int field representing a day during a particular month (values 1 to 31). """
    type_class_uri = FIXR["DayOfMonth"]
    type_class_curie = "fixr:DayOfMonth"
    type_name = "FIXDayOfMonth"
    type_model_uri = FIX_ORCHESTRA.FIXDayOfMonth


class FIXFloat(Float):
    """ FIX float base datatype. Sequence of digits with optional decimal point and sign character (ASCII characters "-", "0" - "9" and "."); the absence of the decimal point within the string will be interpreted as the float representation of an integer value. All float fields must accommodate up to fifteen significant digits. The number of decimal places used should be a factor of business/market needs and mutual agreement between counterparties. Note that float values may contain leading zeros (e.g. "00023.23" = "23.23") and may contain or omit trailing zeros after the decimal point (e.g. "23.0" = "23.0000" = "23" = "23."). Note that fields which are derived from float may contain negative values unless explicitly specified otherwise. """
    type_class_uri = FIXR["float"]
    type_class_curie = "fixr:float"
    type_name = "FIXFloat"
    type_model_uri = FIX_ORCHESTRA.FIXFloat


class FIXQty(Float):
    """ FIX Qty datatype (extends float). float field capable of storing either a whole number (no decimal places) of "shares" (securities denominated in whole units) or a decimal value containing decimal places for non-share quantity asset classes (securities denominated in fractional units). """
    type_class_uri = FIXR["Qty"]
    type_class_curie = "fixr:Qty"
    type_name = "FIXQty"
    type_model_uri = FIX_ORCHESTRA.FIXQty


class FIXPrice(Float):
    """ FIX Price datatype (extends float). float field representing a price. Note the number of decimal places may vary. For certain asset classes prices may be negative values. For example, prices for options strategies can be negative under certain market conditions. Refer to Volume 7: FIX Usage by Product for asset classes that support negative price values. """
    type_class_uri = FIXR["Price"]
    type_class_curie = "fixr:Price"
    type_name = "FIXPrice"
    type_model_uri = FIX_ORCHESTRA.FIXPrice


class FIXPriceOffset(Float):
    """ FIX PriceOffset datatype (extends float). float field representing a price offset, which can be mathematically added to a "Price". Note the number of decimal places may vary and some fields such as LastForwardPoints may be negative. """
    type_class_uri = FIXR["PriceOffset"]
    type_class_curie = "fixr:PriceOffset"
    type_name = "FIXPriceOffset"
    type_model_uri = FIX_ORCHESTRA.FIXPriceOffset


class FIXAmt(Float):
    """ FIX Amt datatype (extends float). float field typically representing a Price times a Qty """
    type_class_uri = FIXR["Amt"]
    type_class_curie = "fixr:Amt"
    type_name = "FIXAmt"
    type_model_uri = FIX_ORCHESTRA.FIXAmt


class FIXPercentage(Float):
    """ FIX Percentage datatype (extends float). float field representing a percentage (e.g. 0.05 represents 5% and 0.9525 represents 95.25%). Note the number of decimal places may vary. """
    type_class_uri = FIXR["Percentage"]
    type_class_curie = "fixr:Percentage"
    type_name = "FIXPercentage"
    type_model_uri = FIX_ORCHESTRA.FIXPercentage


class FIXChar(String):
    """ FIX char base datatype. Single character value, can include any alphanumeric character or punctuation except the delimiter. All char fields are case sensitive (i.e. m != M). """
    type_class_uri = FIXR["char"]
    type_class_curie = "fixr:char"
    type_name = "FIXChar"
    type_model_uri = FIX_ORCHESTRA.FIXChar


class FIXBoolean(String):
    """ FIX Boolean datatype (extends char). char field containing one of two values: """
    type_class_uri = FIXR["Boolean"]
    type_class_curie = "fixr:Boolean"
    type_name = "FIXBoolean"
    type_model_uri = FIX_ORCHESTRA.FIXBoolean


class FIXString(String):
    """ FIX String base datatype. Alpha-numeric free format strings, can include any character or punctuation except the delimiter. All String fields are case sensitive (i.e. morstatt != Morstatt). """
    type_class_uri = FIXR["String"]
    type_class_curie = "fixr:String"
    type_name = "FIXString"
    type_model_uri = FIX_ORCHESTRA.FIXString


class FIXMultipleCharValue(String):
    """ FIX MultipleCharValue datatype (extends String). string field containing one or more space delimited single character values (e.g. |18=2 A F| ). """
    type_class_uri = FIXR["MultipleCharValue"]
    type_class_curie = "fixr:MultipleCharValue"
    type_name = "FIXMultipleCharValue"
    type_model_uri = FIX_ORCHESTRA.FIXMultipleCharValue


class FIXMultipleStringValue(String):
    """ FIX MultipleStringValue datatype (extends String). string field containing one or more space delimited multiple character values (e.g. |277=AV AN A| ). """
    type_class_uri = FIXR["MultipleStringValue"]
    type_class_curie = "fixr:MultipleStringValue"
    type_name = "FIXMultipleStringValue"
    type_model_uri = FIX_ORCHESTRA.FIXMultipleStringValue


class FIXCountry(String):
    """ FIX Country datatype (extends String). string field representing a country using ISO 3166 Country code (2 character) values (see Appendix 6-B). """
    type_class_uri = FIXR["Country"]
    type_class_curie = "fixr:Country"
    type_name = "FIXCountry"
    type_model_uri = FIX_ORCHESTRA.FIXCountry


class FIXCurrency(String):
    """ FIX Currency datatype (extends String). string field representing a currency type using ISO 4217 Currency code (3 character) values (see Appendix 6-A). """
    type_class_uri = FIXR["Currency"]
    type_class_curie = "fixr:Currency"
    type_name = "FIXCurrency"
    type_model_uri = FIX_ORCHESTRA.FIXCurrency


class FIXExchange(String):
    """ FIX Exchange datatype (extends String). string field representing a market or exchange using ISO 10383 Market Identifier Code (MIC) values (see"Appendix 6-C). """
    type_class_uri = FIXR["Exchange"]
    type_class_curie = "fixr:Exchange"
    type_name = "FIXExchange"
    type_model_uri = FIX_ORCHESTRA.FIXExchange


class FIXMonthYear(String):
    """ FIX MonthYear datatype (extends String). string field representing month of a year. An optional day of the month can be appended or an optional week code. """
    type_class_uri = FIXR["MonthYear"]
    type_class_curie = "fixr:MonthYear"
    type_name = "FIXMonthYear"
    type_model_uri = FIX_ORCHESTRA.FIXMonthYear


class FIXUTCTimestamp(Datetime):
    """ FIX UTCTimestamp datatype (extends String). string field representing time/date combination represented in UTC (Universal Time Coordinated, also known as "GMT") in either YYYYMMDD-HH:MM:SS (whole seconds) or YYYYMMDD-HH:MM:SS.sss* format, colons, dash, and period required. """
    type_class_uri = FIXR["UTCTimestamp"]
    type_class_curie = "fixr:UTCTimestamp"
    type_name = "FIXUTCTimestamp"
    type_model_uri = FIX_ORCHESTRA.FIXUTCTimestamp


class FIXUTCTimeOnly(String):
    """ FIX UTCTimeOnly datatype (extends String). string field representing time-only represented in UTC (Universal Time Coordinated, also known as "GMT") in either HH:MM:SS (whole seconds) or HH:MM:SS.sss* (milliseconds) format, colons, and period required. This special-purpose field is paired with UTCDateOnly to form a proper UTCTimestamp for bandwidth-sensitive messages. """
    type_class_uri = FIXR["UTCTimeOnly"]
    type_class_curie = "fixr:UTCTimeOnly"
    type_name = "FIXUTCTimeOnly"
    type_model_uri = FIX_ORCHESTRA.FIXUTCTimeOnly


class FIXUTCDateOnly(Date):
    """ FIX UTCDateOnly datatype (extends String). string field representing Date represented in UTC (Universal Time Coordinated, also known as "GMT") in YYYYMMDD format. This special-purpose field is paired with UTCTimeOnly to form a proper UTCTimestamp for bandwidth-sensitive messages. """
    type_class_uri = FIXR["UTCDateOnly"]
    type_class_curie = "fixr:UTCDateOnly"
    type_name = "FIXUTCDateOnly"
    type_model_uri = FIX_ORCHESTRA.FIXUTCDateOnly


class FIXLocalMktDate(Date):
    """ FIX LocalMktDate datatype (extends String). string field representing a Date of Local Market (as opposed to UTC) in YYYYMMDD format. This is the "normal" date field used by the FIX Protocol. """
    type_class_uri = FIXR["LocalMktDate"]
    type_class_curie = "fixr:LocalMktDate"
    type_name = "FIXLocalMktDate"
    type_model_uri = FIX_ORCHESTRA.FIXLocalMktDate


class FIXTZTimeOnly(String):
    """ FIX TZTimeOnly datatype (extends String). string field representing the time represented based on ISO 8601. This is the time with a UTC offset to allow identification of local time and timezone of that time. """
    type_class_uri = FIXR["TZTimeOnly"]
    type_class_curie = "fixr:TZTimeOnly"
    type_name = "FIXTZTimeOnly"
    type_model_uri = FIX_ORCHESTRA.FIXTZTimeOnly


class FIXTZTimestamp(Datetime):
    """ FIX TZTimestamp datatype (extends String). string field representing a time/date combination representing local time with an offset to UTC to allow identification of local time and timezone offset of that time. The representation is based on ISO 8601. """
    type_class_uri = FIXR["TZTimestamp"]
    type_class_curie = "fixr:TZTimestamp"
    type_name = "FIXTZTimestamp"
    type_model_uri = FIX_ORCHESTRA.FIXTZTimestamp


class FIXData(String):
    """ FIX data base datatype. string field containing opaque or non-ASCII data with no format or content restrictions. Data fields are always immediately preceded by a length field. The length field should specify the number of bytes of the value of the data field (up to but not including the terminating SOH). The number of bytes does not equal the number of characters when multibyte character sets are used. Caution: The value of these fields may contain the delimiter (SOH) character. Note that the value specified for these fields must be followed by the delimiter (SOH) character as all tag-value fields are terminated with an SOH. """
    type_class_uri = FIXR["data"]
    type_class_curie = "fixr:data"
    type_name = "FIXData"
    type_model_uri = FIX_ORCHESTRA.FIXData


class FIXPattern(String):
    """ FIX Pattern base datatype. Used to build on and provide some restrictions on what is allowed as valid values in fields that uses a base FIX data type and a pattern data type. The universe of allowable valid values for the field would then be the union of the base set of valid values and what is defined by the pattern data type. The pattern data type used by the field will retain its base FIX data type (e.g. String, int, char). """
    type_class_uri = FIXR["Pattern"]
    type_class_curie = "fixr:Pattern"
    type_name = "FIXPattern"
    type_model_uri = FIX_ORCHESTRA.FIXPattern


class FIXTenor(String):
    """ FIX Tenor datatype (extends Pattern). used to allow the expression of FX standard tenors in addition to the base valid enumerations defined for the field that uses this pattern data type. This pattern data type is defined as follows: """
    type_class_uri = FIXR["Tenor"]
    type_class_curie = "fixr:Tenor"
    type_name = "FIXTenor"
    type_model_uri = FIX_ORCHESTRA.FIXTenor


class FIXReserved100Plus(Integer):
    """ FIX Reserved100Plus datatype (extends Pattern). Values "100" and above are reserved for bilaterally agreed upon user defined enumerations. """
    type_class_uri = FIXR["Reserved100Plus"]
    type_class_curie = "fixr:Reserved100Plus"
    type_name = "FIXReserved100Plus"
    type_model_uri = FIX_ORCHESTRA.FIXReserved100Plus


class FIXReserved1000Plus(Integer):
    """ FIX Reserved1000Plus datatype (extends Pattern). Values "1000" and above are reserved for bilaterally agreed upon user defined enumerations. """
    type_class_uri = FIXR["Reserved1000Plus"]
    type_class_curie = "fixr:Reserved1000Plus"
    type_name = "FIXReserved1000Plus"
    type_model_uri = FIX_ORCHESTRA.FIXReserved1000Plus


class FIXReserved4000Plus(Integer):
    """ FIX Reserved4000Plus datatype (extends Pattern). Values "4000" and above are reserved for bilaterally agreed upon user defined enumerations. """
    type_class_uri = FIXR["Reserved4000Plus"]
    type_class_curie = "fixr:Reserved4000Plus"
    type_name = "FIXReserved4000Plus"
    type_model_uri = FIX_ORCHESTRA.FIXReserved4000Plus


class FIXXMLData(String):
    """ FIX XMLData datatype (extends String). Contains an XML document raw data with no format or content restrictions. XMLData fields are always immediately preceded by a length field. The length field should specify the number of bytes of the value of the data field (up to but not including the terminating SOH). """
    type_class_uri = FIXR["XMLData"]
    type_class_curie = "fixr:XMLData"
    type_name = "FIXXMLData"
    type_model_uri = FIX_ORCHESTRA.FIXXMLData


class FIXLanguage(String):
    """ FIX Language datatype (extends String). Identifier for a national language - uses ISO 639-1 standard """
    type_class_uri = FIXR["Language"]
    type_class_curie = "fixr:Language"
    type_name = "FIXLanguage"
    type_model_uri = FIX_ORCHESTRA.FIXLanguage


class FIXLocalMktTime(String):
    """ FIX LocalMktTime datatype (extends String). string field representing the time local to a particular market center. Used where offset to UTC varies throughout the year and the defining market center is identified in a corresponding field. """
    type_class_uri = FIXR["LocalMktTime"]
    type_class_curie = "fixr:LocalMktTime"
    type_name = "FIXLocalMktTime"
    type_model_uri = FIX_ORCHESTRA.FIXLocalMktTime


class FIXXID(String):
    """ FIX XID datatype (extends String). The purpose of the XID datatype is to define a unique identifier that is global to a FIX message. An identifier defined using this datatype uniquely identifies its containing element, whatever its type and name is. The constraint added by this datatype is that the values of all the fields that have an XID datatype in a FIX message must be unique. """
    type_class_uri = FIXR["XID"]
    type_class_curie = "fixr:XID"
    type_name = "FIXXID"
    type_model_uri = FIX_ORCHESTRA.FIXXID


class FIXXIDREF(String):
    """ FIX XIDREF datatype (extends String). The XIDREF datatype defines a reference to an identifier defined by the XID datatype. """
    type_class_uri = FIXR["XIDREF"]
    type_class_curie = "fixr:XIDREF"
    type_name = "FIXXIDREF"
    type_model_uri = FIX_ORCHESTRA.FIXXIDREF


class DcmitypeDCMIType(String):
    """ Union of:  """
    type_class_uri = DCMITYPE["DCMIType"]
    type_class_curie = "dcmitype:DCMIType"
    type_name = "DcmitypeDCMIType"
    type_model_uri = FIX_ORCHESTRA.DcmitypeDCMIType


class XmlLangType(String):
    """ Anonymous simpleType for xml:lang (from xml.xsd). """
    type_class_uri = XML["lang_t"]
    type_class_curie = "xml:lang_t"
    type_name = "XmlLangType"
    type_model_uri = FIX_ORCHESTRA.XmlLangType


# Class references



@dataclass(repr=False)
class EntityAttribGrp(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["entityAttribGrp"]
    class_class_curie: ClassVar[str] = "fixr:entityAttribGrp"
    class_name: ClassVar[str] = "EntityAttribGrp"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.EntityAttribGrp

    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FieldAttribGrp(YAMLRoot):
    """
    Attributes of a field that be overridden by a rule
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["fieldAttribGrp"]
    class_class_curie: ClassVar[str] = "fixr:fieldAttribGrp"
    class_name: ClassVar[str] = "FieldAttribGrp"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.FieldAttribGrp

    min_inclusive: Optional[str] = None
    max_inclusive: Optional[str] = None
    impl_length: Optional[int] = None
    impl_min_length: Optional[int] = None
    impl_max_length: Optional[int] = None
    presence: Optional[Union[str, "Presence"]] = 'optional'
    value: Optional[str] = None
    rendering: Optional[str] = None
    encoding: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.min_inclusive is not None and not isinstance(self.min_inclusive, str):
            self.min_inclusive = str(self.min_inclusive)

        if self.max_inclusive is not None and not isinstance(self.max_inclusive, str):
            self.max_inclusive = str(self.max_inclusive)

        if self.impl_length is not None and not isinstance(self.impl_length, int):
            self.impl_length = int(self.impl_length)

        if self.impl_min_length is not None and not isinstance(self.impl_min_length, int):
            self.impl_min_length = int(self.impl_min_length)

        if self.impl_max_length is not None and not isinstance(self.impl_max_length, int):
            self.impl_max_length = int(self.impl_max_length)

        if self.presence is not None and not isinstance(self.presence, Presence):
            self.presence = Presence(self.presence)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.rendering is not None and not isinstance(self.rendering, str):
            self.rendering = str(self.rendering)

        if self.encoding is not None and not isinstance(self.encoding, str):
            self.encoding = str(self.encoding)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OidGrp(YAMLRoot):
    """
    The identifiers of a message element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["oidGrp"]
    class_class_curie: ClassVar[str] = "fixr:oidGrp"
    class_name: ClassVar[str] = "OidGrp"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OidGrp

    id: Union[int, Id] = None
    name: Union[str, Name] = None
    abbr_name: Optional[Union[str, Name]] = None
    scenario_id: Optional[Union[int, Id]] = 1
    scenario: Optional[Union[str, Name]] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.abbr_name is not None and not isinstance(self.abbr_name, Name):
            self.abbr_name = Name(self.abbr_name)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RefidGrp(YAMLRoot):
    """
    A reference to a message element by its key identifiers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["refidGrp"]
    class_class_curie: ClassVar[str] = "fixr:refidGrp"
    class_name: ClassVar[str] = "RefidGrp"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.RefidGrp

    id: Union[int, Id] = None
    scenario_id: Optional[Union[int, Id]] = 1
    name: Optional[Union[str, Name]] = None
    scenario: Optional[Union[str, Name]] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.name is not None and not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScenarioRefGrp(YAMLRoot):
    """
    A reference to a scenario by its key identifiers. There are no defaults as scenario references are optional.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["scenarioRefGrp"]
    class_class_curie: ClassVar[str] = "fixr:scenarioRefGrp"
    class_name: ClassVar[str] = "ScenarioRefGrp"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ScenarioRefGrp

    scenario_ref_id: Optional[Union[int, Id]] = None
    scenario_ref: Optional[Union[str, Name]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.scenario_ref_id is not None and not isinstance(self.scenario_ref_id, Id):
            self.scenario_ref_id = Id(self.scenario_ref_id)

        if self.scenario_ref is not None and not isinstance(self.scenario_ref, Name):
            self.scenario_ref = Name(self.scenario_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActionType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["actionType"]
    class_class_curie: ClassVar[str] = "fixr:actionType"
    class_name: ClassVar[str] = "ActionType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ActionType

    field: Optional[Union[Union[dict, "FieldType"], list[Union[dict, "FieldType"]]]] = empty_list()
    field_ref: Optional[Union[Union[dict, "FieldRefType"], list[Union[dict, "FieldRefType"]]]] = empty_list()
    component: Optional[Union[Union[dict, "ComponentType"], list[Union[dict, "ComponentType"]]]] = empty_list()
    component_ref: Optional[Union[Union[dict, "ComponentRefType"], list[Union[dict, "ComponentRefType"]]]] = empty_list()
    group_ref: Optional[Union[Union[dict, "GroupRefType"], list[Union[dict, "GroupRefType"]]]] = empty_list()
    message_ref: Optional[Union[Union[dict, "MessageRefType"], list[Union[dict, "MessageRefType"]]]] = empty_list()
    trigger: Optional[Union[Union[dict, "TriggerType"], list[Union[dict, "TriggerType"]]]] = empty_list()
    timer_schedule: Optional[Union[Union[dict, "TimerSchedule"], list[Union[dict, "TimerSchedule"]]]] = empty_list()
    group: Optional[Union[Union[dict, "GroupType"], list[Union[dict, "GroupType"]]]] = empty_list()
    assign: Optional[Union[Union[str, ExpressionType], list[Union[str, ExpressionType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="field", slot_type=FieldType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="field_ref", slot_type=FieldRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="component", slot_type=ComponentType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="component_ref", slot_type=ComponentRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="group_ref", slot_type=GroupRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="message_ref", slot_type=MessageRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="trigger", slot_type=TriggerType, key_name="state_machine", keyed=False)

        self._normalize_inlined_as_list(slot_name="timer_schedule", slot_type=TimerSchedule, key_name="operation", keyed=False)

        self._normalize_inlined_as_list(slot_name="group", slot_type=GroupType, key_name="id", keyed=False)

        if not isinstance(self.assign, list):
            self.assign = [self.assign] if self.assign is not None else []
        self.assign = [v if isinstance(v, ExpressionType) else ExpressionType(v) for v in self.assign]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActorType(YAMLRoot):
    """
    Represents a class of participants
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["actorType"]
    class_class_curie: ClassVar[str] = "fixr:actorType"
    class_name: ClassVar[str] = "ActorType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ActorType

    name: Union[str, Name] = None
    field: Optional[Union[Union[dict, "FieldType"], list[Union[dict, "FieldType"]]]] = empty_list()
    field_ref: Optional[Union[Union[dict, "FieldRefType"], list[Union[dict, "FieldRefType"]]]] = empty_list()
    component: Optional[Union[Union[dict, "ComponentType"], list[Union[dict, "ComponentType"]]]] = empty_list()
    component_ref: Optional[Union[Union[dict, "ComponentRefType"], list[Union[dict, "ComponentRefType"]]]] = empty_list()
    group_ref: Optional[Union[Union[dict, "GroupRefType"], list[Union[dict, "GroupRefType"]]]] = empty_list()
    states: Optional[Union[Union[dict, "StateMachineType"], list[Union[dict, "StateMachineType"]]]] = empty_list()
    timer: Optional[Union[Union[dict, "TimerType"], list[Union[dict, "TimerType"]]]] = empty_list()
    group: Optional[Union[Union[dict, "GroupType"], list[Union[dict, "GroupType"]]]] = empty_list()
    annotation: Optional[Union[dict, "Annotation"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        self._normalize_inlined_as_list(slot_name="field", slot_type=FieldType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="field_ref", slot_type=FieldRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="component", slot_type=ComponentType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="component_ref", slot_type=ComponentRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="group_ref", slot_type=GroupRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="states", slot_type=StateMachineType, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="timer", slot_type=TimerType, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="group", slot_type=GroupType, key_name="id", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Annotation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["annotation"]
    class_class_curie: ClassVar[str] = "fixr:annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Annotation

    documentation: Optional[Union[Union[dict, "Documentation"], list[Union[dict, "Documentation"]]]] = empty_list()
    appinfo: Optional[Union[Union[dict, "Appinfo"], list[Union[dict, "Appinfo"]]]] = empty_list()
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.documentation, list):
            self.documentation = [self.documentation] if self.documentation is not None else []
        self.documentation = [v if isinstance(v, Documentation) else Documentation(**as_dict(v)) for v in self.documentation]

        if not isinstance(self.appinfo, list):
            self.appinfo = [self.appinfo] if self.appinfo is not None else []
        self.appinfo = [v if isinstance(v, Appinfo) else Appinfo(**as_dict(v)) for v in self.appinfo]

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Appinfo(YAMLRoot):
    """
    Usage specific annotation, optionally with link to an external reference or standard
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["appinfo"]
    class_class_curie: ClassVar[str] = "fixr:appinfo"
    class_name: ClassVar[str] = "Appinfo"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Appinfo

    spec_url: Optional[Union[str, URI]] = None
    value: Optional[str] = None
    content: Optional[Union[str, list[str]]] = empty_list()
    extra_attributes: Optional[Union[str, list[str]]] = empty_list()
    lang_id: Optional[Union[str, Language]] = None
    purpose: Optional[Union[str, Purpose]] = None
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.spec_url is not None and not isinstance(self.spec_url, URI):
            self.spec_url = URI(self.spec_url)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, str) else str(v) for v in self.content]

        if not isinstance(self.extra_attributes, list):
            self.extra_attributes = [self.extra_attributes] if self.extra_attributes is not None else []
        self.extra_attributes = [v if isinstance(v, str) else str(v) for v in self.extra_attributes]

        if self.lang_id is not None and not isinstance(self.lang_id, Language):
            self.lang_id = Language(self.lang_id)

        if self.purpose is not None and not isinstance(self.purpose, Purpose):
            self.purpose = Purpose(self.purpose)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BlockAssignmentType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["blockAssignmentType"]
    class_class_curie: ClassVar[str] = "fixr:blockAssignmentType"
    class_name: ClassVar[str] = "BlockAssignmentType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.BlockAssignmentType

    component_ref: Optional[Union[Union[dict, "ComponentRefType"], list[Union[dict, "ComponentRefType"]]]] = empty_list()
    group_ref: Optional[Union[Union[dict, "GroupRefType"], list[Union[dict, "GroupRefType"]]]] = empty_list()
    field_ref: Optional[Union[Union[dict, "FieldRefType"], list[Union[dict, "FieldRefType"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="component_ref", slot_type=ComponentRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="group_ref", slot_type=GroupRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="field_ref", slot_type=FieldRefType, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CategoryType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["categoryType"]
    class_class_curie: ClassVar[str] = "fixr:categoryType"
    class_name: ClassVar[str] = "CategoryType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.CategoryType

    name: Union[str, Name] = None
    fixml_file_name: Optional[Union[str, Name]] = None
    component_type: Optional[Union[str, "CatComponentType"]] = None
    include_file: Optional[Union[str, "CatIncludeFile"]] = None
    annotation: Optional[Union[dict, Annotation]] = None
    section: Optional[Union[str, Name]] = None
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.fixml_file_name is not None and not isinstance(self.fixml_file_name, Name):
            self.fixml_file_name = Name(self.fixml_file_name)

        if self.component_type is not None and not isinstance(self.component_type, CatComponentType):
            self.component_type = CatComponentType(self.component_type)

        if self.include_file is not None and not isinstance(self.include_file, CatIncludeFile):
            self.include_file = CatIncludeFile(self.include_file)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.section is not None and not isinstance(self.section, Name):
            self.section = Name(self.section)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeSetType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["codeSetType"]
    class_class_curie: ClassVar[str] = "fixr:codeSetType"
    class_name: ClassVar[str] = "CodeSetType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.CodeSetType

    type: Union[str, Name] = None
    id: Union[int, Id] = None
    name: Union[str, Name] = None
    code: Optional[Union[Union[dict, "CodeType"], list[Union[dict, "CodeType"]]]] = empty_list()
    default: Optional[str] = None
    spec_url: Optional[Union[str, URI]] = None
    union_data_type: Optional[Union[str, "UnionDataType"]] = None
    annotation: Optional[Union[dict, Annotation]] = None
    abbr_name: Optional[Union[str, Name]] = None
    scenario_id: Optional[Union[int, Id]] = 1
    scenario: Optional[Union[str, Name]] = "base"
    scenario_ref_id: Optional[Union[int, Id]] = None
    scenario_ref: Optional[Union[str, Name]] = None
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, Name):
            self.type = Name(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        self._normalize_inlined_as_list(slot_name="code", slot_type=CodeType, key_name="value", keyed=False)

        if self.default is not None and not isinstance(self.default, str):
            self.default = str(self.default)

        if self.spec_url is not None and not isinstance(self.spec_url, URI):
            self.spec_url = URI(self.spec_url)

        if self.union_data_type is not None and not isinstance(self.union_data_type, UnionDataType):
            self.union_data_type = UnionDataType(self.union_data_type)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.abbr_name is not None and not isinstance(self.abbr_name, Name):
            self.abbr_name = Name(self.abbr_name)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        if self.scenario_ref_id is not None and not isinstance(self.scenario_ref_id, Id):
            self.scenario_ref_id = Id(self.scenario_ref_id)

        if self.scenario_ref is not None and not isinstance(self.scenario_ref, Name):
            self.scenario_ref = Name(self.scenario_ref)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["codeType"]
    class_class_curie: ClassVar[str] = "fixr:codeType"
    class_name: ClassVar[str] = "CodeType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.CodeType

    value: str = None
    id: Union[int, Id] = None
    name: Union[str, Name] = None
    sort: Optional[int] = None
    annotation: Optional[Union[dict, Annotation]] = None
    group: Optional[str] = None
    abbr_name: Optional[Union[str, Name]] = None
    scenario_id: Optional[Union[int, Id]] = 1
    scenario: Optional[Union[str, Name]] = "base"
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.sort is not None and not isinstance(self.sort, int):
            self.sort = int(self.sort)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.group is not None and not isinstance(self.group, str):
            self.group = str(self.group)

        if self.abbr_name is not None and not isinstance(self.abbr_name, Name):
            self.abbr_name = Name(self.abbr_name)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComponentRefType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["componentRefType"]
    class_class_curie: ClassVar[str] = "fixr:componentRefType"
    class_name: ClassVar[str] = "ComponentRefType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ComponentRefType

    id: Union[int, Id] = None
    block_assignment: Optional[Union[Union[dict, BlockAssignmentType], list[Union[dict, BlockAssignmentType]]]] = empty_list()
    presence: Optional[Union[str, "Presence"]] = 'optional'
    rule: Optional[Union[Union[dict, "ComponentRuleType"], list[Union[dict, "ComponentRuleType"]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    instance_name: Optional[Union[str, ComponentName]] = None
    scenario_id: Optional[Union[int, Id]] = 1
    name: Optional[Union[str, Name]] = None
    scenario: Optional[Union[str, Name]] = "base"
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if not isinstance(self.block_assignment, list):
            self.block_assignment = [self.block_assignment] if self.block_assignment is not None else []
        self.block_assignment = [v if isinstance(v, BlockAssignmentType) else BlockAssignmentType(**as_dict(v)) for v in self.block_assignment]

        if self.presence is not None and not isinstance(self.presence, Presence):
            self.presence = Presence(self.presence)

        self._normalize_inlined_as_list(slot_name="rule", slot_type=ComponentRuleType, key_name="when", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.instance_name is not None and not isinstance(self.instance_name, ComponentName):
            self.instance_name = ComponentName(self.instance_name)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.name is not None and not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComponentRuleType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["componentRuleType"]
    class_class_curie: ClassVar[str] = "fixr:componentRuleType"
    class_name: ClassVar[str] = "ComponentRuleType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ComponentRuleType

    when: Union[str, ExpressionType] = None
    presence: Optional[Union[str, "Presence"]] = 'optional'
    name: Optional[Union[str, Name]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.when):
            self.MissingRequiredField("when")
        if not isinstance(self.when, ExpressionType):
            self.when = ExpressionType(self.when)

        if self.presence is not None and not isinstance(self.presence, Presence):
            self.presence = Presence(self.presence)

        if self.name is not None and not isinstance(self.name, Name):
            self.name = Name(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComponentType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["componentType"]
    class_class_curie: ClassVar[str] = "fixr:componentType"
    class_name: ClassVar[str] = "ComponentType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ComponentType

    id: Union[int, Id] = None
    name: Union[str, Name] = None
    component_ref: Optional[Union[Union[dict, ComponentRefType], list[Union[dict, ComponentRefType]]]] = empty_list()
    group_ref: Optional[Union[Union[dict, "GroupRefType"], list[Union[dict, "GroupRefType"]]]] = empty_list()
    field_ref: Optional[Union[Union[dict, "FieldRefType"], list[Union[dict, "FieldRefType"]]]] = empty_list()
    rendering: Optional[str] = None
    which: Optional[Union[str, "MemberType"]] = None
    annotation: Optional[Union[dict, Annotation]] = None
    category: Optional[Union[str, Name]] = None
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None
    abbr_name: Optional[Union[str, Name]] = None
    scenario_id: Optional[Union[int, Id]] = 1
    scenario: Optional[Union[str, Name]] = "base"
    scenario_ref_id: Optional[Union[int, Id]] = None
    scenario_ref: Optional[Union[str, Name]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        self._normalize_inlined_as_list(slot_name="component_ref", slot_type=ComponentRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="group_ref", slot_type=GroupRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="field_ref", slot_type=FieldRefType, key_name="id", keyed=False)

        if self.rendering is not None and not isinstance(self.rendering, str):
            self.rendering = str(self.rendering)

        if self.which is not None and not isinstance(self.which, MemberType):
            self.which = MemberType(self.which)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.category is not None and not isinstance(self.category, Name):
            self.category = Name(self.category)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        if self.abbr_name is not None and not isinstance(self.abbr_name, Name):
            self.abbr_name = Name(self.abbr_name)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        if self.scenario_ref_id is not None and not isinstance(self.scenario_ref_id, Id):
            self.scenario_ref_id = Id(self.scenario_ref_id)

        if self.scenario_ref is not None and not isinstance(self.scenario_ref, Name):
            self.scenario_ref = Name(self.scenario_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["conceptType"]
    class_class_curie: ClassVar[str] = "fixr:conceptType"
    class_name: ClassVar[str] = "ConceptType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ConceptType

    name: Union[str, Name] = None
    component_ref: Optional[Union[Union[dict, ComponentRefType], list[Union[dict, ComponentRefType]]]] = empty_list()
    group_ref: Optional[Union[Union[dict, "GroupRefType"], list[Union[dict, "GroupRefType"]]]] = empty_list()
    field_ref: Optional[Union[Union[dict, "FieldRefType"], list[Union[dict, "FieldRefType"]]]] = empty_list()
    message_ref: Optional[Union[Union[dict, "MessageRefType"], list[Union[dict, "MessageRefType"]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        self._normalize_inlined_as_list(slot_name="component_ref", slot_type=ComponentRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="group_ref", slot_type=GroupRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="field_ref", slot_type=FieldRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="message_ref", slot_type=MessageRefType, key_name="id", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Documentation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["documentation"]
    class_class_curie: ClassVar[str] = "fixr:documentation"
    class_name: ClassVar[str] = "Documentation"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Documentation

    value: Optional[str] = None
    content: Optional[Union[str, list[str]]] = empty_list()
    lang_id: Optional[Union[str, Language]] = None
    purpose: Optional[Union[str, Purpose]] = None
    content_type: Optional[Union[str, Mime]] = "text/plain"
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, str) else str(v) for v in self.content]

        if self.lang_id is not None and not isinstance(self.lang_id, Language):
            self.lang_id = Language(self.lang_id)

        if self.purpose is not None and not isinstance(self.purpose, Purpose):
            self.purpose = Purpose(self.purpose)

        if self.content_type is not None and not isinstance(self.content_type, Mime):
            self.content_type = Mime(self.content_type)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FieldRefType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["fieldRefType"]
    class_class_curie: ClassVar[str] = "fixr:fieldRefType"
    class_name: ClassVar[str] = "FieldRefType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.FieldRefType

    id: Union[int, Id] = None
    length_id: Optional[Union[int, Id]] = None
    non_encoded_field_id: Optional[Union[int, Id]] = None
    rule: Optional[Union[Union[dict, "FieldRuleType"], list[Union[dict, "FieldRuleType"]]]] = empty_list()
    assign: Optional[Union[str, ExpressionType]] = None
    annotation: Optional[Union[dict, Annotation]] = None
    instance_name: Optional[Union[str, Name]] = None
    scenario_id: Optional[Union[int, Id]] = 1
    name: Optional[Union[str, Name]] = None
    scenario: Optional[Union[str, Name]] = "base"
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None
    min_inclusive: Optional[str] = None
    max_inclusive: Optional[str] = None
    impl_length: Optional[int] = None
    impl_min_length: Optional[int] = None
    impl_max_length: Optional[int] = None
    presence: Optional[Union[str, "Presence"]] = 'optional'
    value: Optional[str] = None
    rendering: Optional[str] = None
    encoding: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self.length_id is not None and not isinstance(self.length_id, Id):
            self.length_id = Id(self.length_id)

        if self.non_encoded_field_id is not None and not isinstance(self.non_encoded_field_id, Id):
            self.non_encoded_field_id = Id(self.non_encoded_field_id)

        self._normalize_inlined_as_list(slot_name="rule", slot_type=FieldRuleType, key_name="when", keyed=False)

        if self.assign is not None and not isinstance(self.assign, ExpressionType):
            self.assign = ExpressionType(self.assign)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.instance_name is not None and not isinstance(self.instance_name, Name):
            self.instance_name = Name(self.instance_name)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.name is not None and not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        if self.min_inclusive is not None and not isinstance(self.min_inclusive, str):
            self.min_inclusive = str(self.min_inclusive)

        if self.max_inclusive is not None and not isinstance(self.max_inclusive, str):
            self.max_inclusive = str(self.max_inclusive)

        if self.impl_length is not None and not isinstance(self.impl_length, int):
            self.impl_length = int(self.impl_length)

        if self.impl_min_length is not None and not isinstance(self.impl_min_length, int):
            self.impl_min_length = int(self.impl_min_length)

        if self.impl_max_length is not None and not isinstance(self.impl_max_length, int):
            self.impl_max_length = int(self.impl_max_length)

        if self.presence is not None and not isinstance(self.presence, Presence):
            self.presence = Presence(self.presence)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.rendering is not None and not isinstance(self.rendering, str):
            self.rendering = str(self.rendering)

        if self.encoding is not None and not isinstance(self.encoding, str):
            self.encoding = str(self.encoding)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UniqueInline(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["UniqueInline"]
    class_class_curie: ClassVar[str] = "fix_orchestra:UniqueInline"
    class_name: ClassVar[str] = "UniqueInline"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.UniqueInline

    field_ref: Optional[Union[Union[dict, FieldRefType], list[Union[dict, FieldRefType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="field_ref", slot_type=FieldRefType, key_name="id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FieldRuleType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["fieldRuleType"]
    class_class_curie: ClassVar[str] = "fixr:fieldRuleType"
    class_name: ClassVar[str] = "FieldRuleType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.FieldRuleType

    when: Union[str, ExpressionType] = None
    unique: Optional[Union[dict, UniqueInline]] = None
    assign: Optional[Union[Union[str, ExpressionType], list[Union[str, ExpressionType]]]] = empty_list()
    name: Optional[Union[str, Name]] = None
    type: Optional[Union[str, Name]] = None
    min_inclusive: Optional[str] = None
    max_inclusive: Optional[str] = None
    impl_length: Optional[int] = None
    impl_min_length: Optional[int] = None
    impl_max_length: Optional[int] = None
    presence: Optional[Union[str, "Presence"]] = 'optional'
    value: Optional[str] = None
    rendering: Optional[str] = None
    encoding: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.when):
            self.MissingRequiredField("when")
        if not isinstance(self.when, ExpressionType):
            self.when = ExpressionType(self.when)

        if self.unique is not None and not isinstance(self.unique, UniqueInline):
            self.unique = UniqueInline(**as_dict(self.unique))

        if not isinstance(self.assign, list):
            self.assign = [self.assign] if self.assign is not None else []
        self.assign = [v if isinstance(v, ExpressionType) else ExpressionType(v) for v in self.assign]

        if self.name is not None and not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.type is not None and not isinstance(self.type, Name):
            self.type = Name(self.type)

        if self.min_inclusive is not None and not isinstance(self.min_inclusive, str):
            self.min_inclusive = str(self.min_inclusive)

        if self.max_inclusive is not None and not isinstance(self.max_inclusive, str):
            self.max_inclusive = str(self.max_inclusive)

        if self.impl_length is not None and not isinstance(self.impl_length, int):
            self.impl_length = int(self.impl_length)

        if self.impl_min_length is not None and not isinstance(self.impl_min_length, int):
            self.impl_min_length = int(self.impl_min_length)

        if self.impl_max_length is not None and not isinstance(self.impl_max_length, int):
            self.impl_max_length = int(self.impl_max_length)

        if self.presence is not None and not isinstance(self.presence, Presence):
            self.presence = Presence(self.presence)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.rendering is not None and not isinstance(self.rendering, str):
            self.rendering = str(self.rendering)

        if self.encoding is not None and not isinstance(self.encoding, str):
            self.encoding = str(self.encoding)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FieldType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["fieldType"]
    class_class_curie: ClassVar[str] = "fixr:fieldType"
    class_name: ClassVar[str] = "FieldType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.FieldType

    id: Union[int, Id] = None
    name: Union[str, Name] = None
    length_id: Optional[Union[int, Id]] = None
    non_encoded_field_id: Optional[Union[int, Id]] = None
    discriminator_id: Optional[Union[int, Id]] = None
    base_category: Optional[Union[str, Name]] = None
    base_category_abbr_name: Optional[Union[str, Name]] = None
    union_data_type: Optional[Union[str, "UnionDataType"]] = None
    rule: Optional[Union[Union[dict, FieldRuleType], list[Union[dict, FieldRuleType]]]] = empty_list()
    assign: Optional[Union[str, ExpressionType]] = None
    annotation: Optional[Union[dict, Annotation]] = None
    type: Optional[Union[str, Name]] = None
    code_set: Optional[Union[str, Name]] = None
    abbr_name: Optional[Union[str, Name]] = None
    scenario_id: Optional[Union[int, Id]] = 1
    scenario: Optional[Union[str, Name]] = "base"
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None
    min_inclusive: Optional[str] = None
    max_inclusive: Optional[str] = None
    impl_length: Optional[int] = None
    impl_min_length: Optional[int] = None
    impl_max_length: Optional[int] = None
    presence: Optional[Union[str, "Presence"]] = 'optional'
    value: Optional[str] = None
    rendering: Optional[str] = None
    encoding: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.length_id is not None and not isinstance(self.length_id, Id):
            self.length_id = Id(self.length_id)

        if self.non_encoded_field_id is not None and not isinstance(self.non_encoded_field_id, Id):
            self.non_encoded_field_id = Id(self.non_encoded_field_id)

        if self.discriminator_id is not None and not isinstance(self.discriminator_id, Id):
            self.discriminator_id = Id(self.discriminator_id)

        if self.base_category is not None and not isinstance(self.base_category, Name):
            self.base_category = Name(self.base_category)

        if self.base_category_abbr_name is not None and not isinstance(self.base_category_abbr_name, Name):
            self.base_category_abbr_name = Name(self.base_category_abbr_name)

        if self.union_data_type is not None and not isinstance(self.union_data_type, UnionDataType):
            self.union_data_type = UnionDataType(self.union_data_type)

        self._normalize_inlined_as_list(slot_name="rule", slot_type=FieldRuleType, key_name="when", keyed=False)

        if self.assign is not None and not isinstance(self.assign, ExpressionType):
            self.assign = ExpressionType(self.assign)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.type is not None and not isinstance(self.type, Name):
            self.type = Name(self.type)

        if self.code_set is not None and not isinstance(self.code_set, Name):
            self.code_set = Name(self.code_set)

        if self.abbr_name is not None and not isinstance(self.abbr_name, Name):
            self.abbr_name = Name(self.abbr_name)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        if self.min_inclusive is not None and not isinstance(self.min_inclusive, str):
            self.min_inclusive = str(self.min_inclusive)

        if self.max_inclusive is not None and not isinstance(self.max_inclusive, str):
            self.max_inclusive = str(self.max_inclusive)

        if self.impl_length is not None and not isinstance(self.impl_length, int):
            self.impl_length = int(self.impl_length)

        if self.impl_min_length is not None and not isinstance(self.impl_min_length, int):
            self.impl_min_length = int(self.impl_min_length)

        if self.impl_max_length is not None and not isinstance(self.impl_max_length, int):
            self.impl_max_length = int(self.impl_max_length)

        if self.presence is not None and not isinstance(self.presence, Presence):
            self.presence = Presence(self.presence)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.rendering is not None and not isinstance(self.rendering, str):
            self.rendering = str(self.rendering)

        if self.encoding is not None and not isinstance(self.encoding, str):
            self.encoding = str(self.encoding)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FlowType(YAMLRoot):
    """
    A stream of messages in one direction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["flowType"]
    class_class_curie: ClassVar[str] = "fixr:flowType"
    class_name: ClassVar[str] = "FlowType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.FlowType

    source: str = None
    destination: str = None
    name: Union[str, Name] = None
    annotation: Optional[Union[dict, Annotation]] = None
    reliability: Optional[Union[str, "Reliability"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.destination):
            self.MissingRequiredField("destination")
        if not isinstance(self.destination, str):
            self.destination = str(self.destination)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.reliability is not None and not isinstance(self.reliability, Reliability):
            self.reliability = Reliability(self.reliability)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GroupRefType(ComponentRefType):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["groupRefType"]
    class_class_curie: ClassVar[str] = "fixr:groupRefType"
    class_name: ClassVar[str] = "GroupRefType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.GroupRefType

    id: Union[int, Id] = None
    impl_min_occurs: Optional[int] = None
    impl_max_occurs: Optional[Union[str, UnboundedIntType]] = "unbounded"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.impl_min_occurs is not None and not isinstance(self.impl_min_occurs, int):
            self.impl_min_occurs = int(self.impl_min_occurs)

        if self.impl_max_occurs is not None and not isinstance(self.impl_max_occurs, UnboundedIntType):
            self.impl_max_occurs = UnboundedIntType(self.impl_max_occurs)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GroupType(YAMLRoot):
    """
    A repeating group. Logically, groupType is a subclass of componentType, but to make numInGroup first in the
    sequence, it cannot be an extension.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["groupType"]
    class_class_curie: ClassVar[str] = "fixr:groupType"
    class_name: ClassVar[str] = "GroupType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.GroupType

    id: Union[int, Id] = None
    name: Union[str, Name] = None
    num_in_group: Optional[Union[dict, FieldRefType]] = None
    component_ref: Optional[Union[Union[dict, ComponentRefType], list[Union[dict, ComponentRefType]]]] = empty_list()
    group_ref: Optional[Union[Union[dict, GroupRefType], list[Union[dict, GroupRefType]]]] = empty_list()
    field_ref: Optional[Union[Union[dict, FieldRefType], list[Union[dict, FieldRefType]]]] = empty_list()
    rendering: Optional[str] = None
    impl_min_occurs: Optional[int] = None
    impl_max_occurs: Optional[Union[str, UnboundedIntType]] = "unbounded"
    which: Optional[Union[str, "MemberType"]] = None
    annotation: Optional[Union[dict, Annotation]] = None
    category: Optional[Union[str, Name]] = None
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None
    abbr_name: Optional[Union[str, Name]] = None
    scenario_id: Optional[Union[int, Id]] = 1
    scenario: Optional[Union[str, Name]] = "base"
    scenario_ref_id: Optional[Union[int, Id]] = None
    scenario_ref: Optional[Union[str, Name]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.num_in_group is not None and not isinstance(self.num_in_group, FieldRefType):
            self.num_in_group = FieldRefType(**as_dict(self.num_in_group))

        self._normalize_inlined_as_list(slot_name="component_ref", slot_type=ComponentRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="group_ref", slot_type=GroupRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="field_ref", slot_type=FieldRefType, key_name="id", keyed=False)

        if self.rendering is not None and not isinstance(self.rendering, str):
            self.rendering = str(self.rendering)

        if self.impl_min_occurs is not None and not isinstance(self.impl_min_occurs, int):
            self.impl_min_occurs = int(self.impl_min_occurs)

        if self.impl_max_occurs is not None and not isinstance(self.impl_max_occurs, UnboundedIntType):
            self.impl_max_occurs = UnboundedIntType(self.impl_max_occurs)

        if self.which is not None and not isinstance(self.which, MemberType):
            self.which = MemberType(self.which)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.category is not None and not isinstance(self.category, Name):
            self.category = Name(self.category)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        if self.abbr_name is not None and not isinstance(self.abbr_name, Name):
            self.abbr_name = Name(self.abbr_name)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        if self.scenario_ref_id is not None and not isinstance(self.scenario_ref_id, Id):
            self.scenario_ref_id = Id(self.scenario_ref_id)

        if self.scenario_ref is not None and not isinstance(self.scenario_ref, Name):
            self.scenario_ref = Name(self.scenario_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentifiersType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["identifiersType"]
    class_class_curie: ClassVar[str] = "fixr:identifiersType"
    class_name: ClassVar[str] = "IdentifiersType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.IdentifiersType

    correlate: Optional[Union[Union[dict, "IdentifierType"], list[Union[dict, "IdentifierType"]]]] = empty_list()
    assign: Optional[Union[Union[dict, "IdentifierType"], list[Union[dict, "IdentifierType"]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.correlate, list):
            self.correlate = [self.correlate] if self.correlate is not None else []
        self.correlate = [v if isinstance(v, IdentifierType) else IdentifierType(**as_dict(v)) for v in self.correlate]

        if not isinstance(self.assign, list):
            self.assign = [self.assign] if self.assign is not None else []
        self.assign = [v if isinstance(v, IdentifierType) else IdentifierType(**as_dict(v)) for v in self.assign]

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentifierType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["identifierType"]
    class_class_curie: ClassVar[str] = "fixi:identifierType"
    class_name: ClassVar[str] = "IdentifierType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.IdentifierType

    value: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExtensionInline(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["ExtensionInline"]
    class_class_curie: ClassVar[str] = "fix_orchestra:ExtensionInline"
    class_name: ClassVar[str] = "ExtensionInline"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ExtensionInline

    content: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, str) else str(v) for v in self.content]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MappedDatatype(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["mappedDatatype"]
    class_class_curie: ClassVar[str] = "fixr:mappedDatatype"
    class_name: ClassVar[str] = "MappedDatatype"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.MappedDatatype

    standard: Union[str, DatatypeStandard] = None
    extension: Optional[Union[dict, ExtensionInline]] = None
    builtin: Optional[Union[bool, Bool]] = None
    pattern: Optional[str] = None
    element: Optional[str] = None
    size: Optional[int] = None
    parameter: Optional[str] = None
    min_inclusive: Optional[str] = None
    max_inclusive: Optional[str] = None
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.standard):
            self.MissingRequiredField("standard")
        if not isinstance(self.standard, DatatypeStandard):
            self.standard = DatatypeStandard(self.standard)

        if self.extension is not None and not isinstance(self.extension, ExtensionInline):
            self.extension = ExtensionInline(**as_dict(self.extension))

        if self.builtin is not None and not isinstance(self.builtin, Bool):
            self.builtin = Bool(self.builtin)

        if self.pattern is not None and not isinstance(self.pattern, str):
            self.pattern = str(self.pattern)

        if self.element is not None and not isinstance(self.element, str):
            self.element = str(self.element)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        if self.parameter is not None and not isinstance(self.parameter, str):
            self.parameter = str(self.parameter)

        if self.min_inclusive is not None and not isinstance(self.min_inclusive, str):
            self.min_inclusive = str(self.min_inclusive)

        if self.max_inclusive is not None and not isinstance(self.max_inclusive, str):
            self.max_inclusive = str(self.max_inclusive)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MessageRefType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["messageRefType"]
    class_class_curie: ClassVar[str] = "fixr:messageRefType"
    class_name: ClassVar[str] = "MessageRefType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.MessageRefType

    id: Union[int, Id] = None
    identifiers: Optional[Union[dict, IdentifiersType]] = None
    msg_type: Optional[Union[str, MsgType]] = None
    impl_min_occurs: Optional[int] = 1
    impl_max_occurs: Optional[Union[str, UnboundedIntType]] = "unbounded"
    scenario_id: Optional[Union[int, Id]] = 1
    name: Optional[Union[str, Name]] = None
    scenario: Optional[Union[str, Name]] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self.identifiers is not None and not isinstance(self.identifiers, IdentifiersType):
            self.identifiers = IdentifiersType(**as_dict(self.identifiers))

        if self.msg_type is not None and not isinstance(self.msg_type, MsgType):
            self.msg_type = MsgType(self.msg_type)

        if self.impl_min_occurs is not None and not isinstance(self.impl_min_occurs, int):
            self.impl_min_occurs = int(self.impl_min_occurs)

        if self.impl_max_occurs is not None and not isinstance(self.impl_max_occurs, UnboundedIntType):
            self.impl_max_occurs = UnboundedIntType(self.impl_max_occurs)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.name is not None and not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StructureInline(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["StructureInline"]
    class_class_curie: ClassVar[str] = "fix_orchestra:StructureInline"
    class_name: ClassVar[str] = "StructureInline"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.StructureInline

    component_ref: Optional[Union[Union[dict, ComponentRefType], list[Union[dict, ComponentRefType]]]] = empty_list()
    group_ref: Optional[Union[Union[dict, GroupRefType], list[Union[dict, GroupRefType]]]] = empty_list()
    field_ref: Optional[Union[Union[dict, FieldRefType], list[Union[dict, FieldRefType]]]] = empty_list()
    which: Optional[Union[str, "MemberType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="component_ref", slot_type=ComponentRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="group_ref", slot_type=GroupRefType, key_name="id", keyed=False)

        self._normalize_inlined_as_list(slot_name="field_ref", slot_type=FieldRefType, key_name="id", keyed=False)

        if self.which is not None and not isinstance(self.which, MemberType):
            self.which = MemberType(self.which)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResponsesInline(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["ResponsesInline"]
    class_class_curie: ClassVar[str] = "fix_orchestra:ResponsesInline"
    class_name: ClassVar[str] = "ResponsesInline"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ResponsesInline

    response: Union[Union[dict, "ResponseType"], list[Union[dict, "ResponseType"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.response):
            self.MissingRequiredField("response")
        if not isinstance(self.response, list):
            self.response = [self.response] if self.response is not None else []
        self.response = [v if isinstance(v, ResponseType) else ResponseType(**as_dict(v)) for v in self.response]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MessageType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["messageType"]
    class_class_curie: ClassVar[str] = "fixr:messageType"
    class_name: ClassVar[str] = "MessageType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.MessageType

    id: Union[int, Id] = None
    name: Union[str, Name] = None
    structure: Optional[Union[dict, StructureInline]] = None
    when: Optional[Union[str, ExpressionType]] = None
    responses: Optional[Union[dict, ResponsesInline]] = None
    msg_type: Optional[Union[str, MsgType]] = None
    rendering: Optional[str] = None
    annotation: Optional[Union[dict, Annotation]] = None
    category: Optional[Union[str, Name]] = None
    flow: Optional[Union[str, Name]] = None
    abbr_name: Optional[Union[str, Name]] = None
    scenario_id: Optional[Union[int, Id]] = 1
    scenario: Optional[Union[str, Name]] = "base"
    scenario_ref_id: Optional[Union[int, Id]] = None
    scenario_ref: Optional[Union[str, Name]] = None
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.structure is not None and not isinstance(self.structure, StructureInline):
            self.structure = StructureInline(**as_dict(self.structure))

        if self.when is not None and not isinstance(self.when, ExpressionType):
            self.when = ExpressionType(self.when)

        if self.responses is not None and not isinstance(self.responses, ResponsesInline):
            self.responses = ResponsesInline(**as_dict(self.responses))

        if self.msg_type is not None and not isinstance(self.msg_type, MsgType):
            self.msg_type = MsgType(self.msg_type)

        if self.rendering is not None and not isinstance(self.rendering, str):
            self.rendering = str(self.rendering)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.category is not None and not isinstance(self.category, Name):
            self.category = Name(self.category)

        if self.flow is not None and not isinstance(self.flow, Name):
            self.flow = Name(self.flow)

        if self.abbr_name is not None and not isinstance(self.abbr_name, Name):
            self.abbr_name = Name(self.abbr_name)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        if self.scenario_ref_id is not None and not isinstance(self.scenario_ref_id, Id):
            self.scenario_ref_id = Id(self.scenario_ref_id)

        if self.scenario_ref is not None and not isinstance(self.scenario_ref, Name):
            self.scenario_ref = Name(self.scenario_ref)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResponseType(ActionType):
    """
    Any number of action behaviors can be triggered by the same 'when' condition
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["responseType"]
    class_class_curie: ClassVar[str] = "fixr:responseType"
    class_name: ClassVar[str] = "ResponseType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ResponseType

    when: Optional[Union[str, ExpressionType]] = None
    sync: Optional[Union[str, "Synchronization"]] = None
    annotation: Optional[Union[dict, Annotation]] = None
    name: Optional[Union[str, Name]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.when is not None and not isinstance(self.when, ExpressionType):
            self.when = ExpressionType(self.when)

        if self.sync is not None and not isinstance(self.sync, Synchronization):
            self.sync = Synchronization(self.sync)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.name is not None and not isinstance(self.name, Name):
            self.name = Name(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScenarioType(YAMLRoot):
    """
    The use case of an element, distinguished by workflow, asset class, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["scenarioType"]
    class_class_curie: ClassVar[str] = "fixr:scenarioType"
    class_name: ClassVar[str] = "ScenarioType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ScenarioType

    annotation: Optional[Union[dict, Annotation]] = None
    id: Optional[Union[int, Id]] = 1
    name: Optional[Union[str, Name]] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.id is not None and not isinstance(self.id, Id):
            self.id = Id(self.id)

        if self.name is not None and not isinstance(self.name, Name):
            self.name = Name(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SectionType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["sectionType"]
    class_class_curie: ClassVar[str] = "fixr:sectionType"
    class_name: ClassVar[str] = "SectionType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.SectionType

    name: Union[str, Name] = None
    display_order: Optional[int] = None
    fixml_file_name: Optional[Union[str, Name]] = None
    annotation: Optional[Union[dict, Annotation]] = None
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.display_order is not None and not isinstance(self.display_order, int):
            self.display_order = int(self.display_order)

        if self.fixml_file_name is not None and not isinstance(self.fixml_file_name, Name):
            self.fixml_file_name = Name(self.fixml_file_name)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StateMachineType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["stateMachineType"]
    class_class_curie: ClassVar[str] = "fixr:stateMachineType"
    class_name: ClassVar[str] = "StateMachineType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.StateMachineType

    initial: Union[dict, "StateType"] = None
    state: Union[Union[dict, "StateType"], list[Union[dict, "StateType"]]] = None
    name: Union[str, Name] = None
    annotation: Optional[Union[dict, Annotation]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.initial):
            self.MissingRequiredField("initial")
        if not isinstance(self.initial, StateType):
            self.initial = StateType(**as_dict(self.initial))

        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        self._normalize_inlined_as_list(slot_name="state", slot_type=StateType, key_name="name", keyed=False)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StateType(YAMLRoot):
    """
    A state of a state machine. If it has no transitions, then it is a final state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["stateType"]
    class_class_curie: ClassVar[str] = "fixr:stateType"
    class_name: ClassVar[str] = "StateType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.StateType

    name: Union[str, Name] = None
    transition: Optional[Union[Union[dict, "TransitionType"], list[Union[dict, "TransitionType"]]]] = empty_list()
    onentry: Optional[Union[dict, ActionType]] = None
    activity: Optional[Union[dict, ActionType]] = None
    onexit: Optional[Union[dict, ActionType]] = None
    annotation: Optional[Union[dict, Annotation]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        self._normalize_inlined_as_list(slot_name="transition", slot_type=TransitionType, key_name="target", keyed=False)

        if self.onentry is not None and not isinstance(self.onentry, ActionType):
            self.onentry = ActionType(**as_dict(self.onentry))

        if self.activity is not None and not isinstance(self.activity, ActionType):
            self.activity = ActionType(**as_dict(self.activity))

        if self.onexit is not None and not isinstance(self.onexit, ActionType):
            self.onexit = ActionType(**as_dict(self.onexit))

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimerSchedule(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["timerSchedule"]
    class_class_curie: ClassVar[str] = "fixr:timerSchedule"
    class_name: ClassVar[str] = "TimerSchedule"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.TimerSchedule

    activity: Union[dict, ActionType] = None
    operation: Union[str, "TimerOperation"] = None
    actor: Union[str, Name] = None
    name: Union[str, Name] = None
    interval: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.activity):
            self.MissingRequiredField("activity")
        if not isinstance(self.activity, ActionType):
            self.activity = ActionType(**as_dict(self.activity))

        if self._is_empty(self.operation):
            self.MissingRequiredField("operation")
        if not isinstance(self.operation, TimerOperation):
            self.operation = TimerOperation(self.operation)

        if self._is_empty(self.actor):
            self.MissingRequiredField("actor")
        if not isinstance(self.actor, Name):
            self.actor = Name(self.actor)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.interval is not None and not isinstance(self.interval, str):
            self.interval = str(self.interval)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimerType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["timerType"]
    class_class_curie: ClassVar[str] = "fixr:timerType"
    class_name: ClassVar[str] = "TimerType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.TimerType

    name: Union[str, Name] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TransitionType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["transitionType"]
    class_class_curie: ClassVar[str] = "fixr:transitionType"
    class_name: ClassVar[str] = "TransitionType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.TransitionType

    target: str = None
    name: Union[str, Name] = None
    when: Optional[Union[str, ExpressionType]] = None
    annotation: Optional[Union[dict, Annotation]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, str):
            self.target = str(self.target)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        if self.when is not None and not isinstance(self.when, ExpressionType):
            self.when = ExpressionType(self.when)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TriggerType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["triggerType"]
    class_class_curie: ClassVar[str] = "fixr:triggerType"
    class_name: ClassVar[str] = "TriggerType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.TriggerType

    state_machine: str = None
    actor: Union[str, Name] = None
    name: Union[str, Name] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state_machine):
            self.MissingRequiredField("state_machine")
        if not isinstance(self.state_machine, str):
            self.state_machine = str(self.state_machine)

        if self._is_empty(self.actor):
            self.MissingRequiredField("actor")
        if not isinstance(self.actor, Name):
            self.actor = Name(self.actor)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterfaceAnnotation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["annotation"]
    class_class_curie: ClassVar[str] = "fixi:annotation"
    class_name: ClassVar[str] = "InterfaceAnnotation"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.InterfaceAnnotation

    documentation: Optional[Union[Union[dict, "InterfaceDocumentation"], list[Union[dict, "InterfaceDocumentation"]]]] = empty_list()
    appinfo: Optional[Union[Union[dict, "InterfaceAppinfo"], list[Union[dict, "InterfaceAppinfo"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.documentation, list):
            self.documentation = [self.documentation] if self.documentation is not None else []
        self.documentation = [v if isinstance(v, InterfaceDocumentation) else InterfaceDocumentation(**as_dict(v)) for v in self.documentation]

        if not isinstance(self.appinfo, list):
            self.appinfo = [self.appinfo] if self.appinfo is not None else []
        self.appinfo = [v if isinstance(v, InterfaceAppinfo) else InterfaceAppinfo(**as_dict(v)) for v in self.appinfo]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterfaceAppinfo(YAMLRoot):
    """
    Usage specific annotation, optionally with link to an external reference or standard
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["appinfo"]
    class_class_curie: ClassVar[str] = "fixi:appinfo"
    class_name: ClassVar[str] = "InterfaceAppinfo"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.InterfaceAppinfo

    spec_url: Optional[Union[str, URI]] = None
    value: Optional[str] = None
    content: Optional[Union[str, list[str]]] = empty_list()
    extra_attributes: Optional[Union[str, list[str]]] = empty_list()
    lang_id: Optional[str] = None
    purpose: Optional[Union[str, InterfacePurpose]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.spec_url is not None and not isinstance(self.spec_url, URI):
            self.spec_url = URI(self.spec_url)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, str) else str(v) for v in self.content]

        if not isinstance(self.extra_attributes, list):
            self.extra_attributes = [self.extra_attributes] if self.extra_attributes is not None else []
        self.extra_attributes = [v if isinstance(v, str) else str(v) for v in self.extra_attributes]

        if self.lang_id is not None and not isinstance(self.lang_id, str):
            self.lang_id = str(self.lang_id)

        if self.purpose is not None and not isinstance(self.purpose, InterfacePurpose):
            self.purpose = InterfacePurpose(self.purpose)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BaseInterfaceType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["baseInterfaceType"]
    class_class_curie: ClassVar[str] = "fixi:baseInterfaceType"
    class_name: ClassVar[str] = "BaseInterfaceType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.BaseInterfaceType

    name: str = None
    service: Optional[Union[Union[dict, "ServiceType"], list[Union[dict, "ServiceType"]]]] = empty_list()
    user_interface: Optional[Union[Union[dict, "UserInterfaceType"], list[Union[dict, "UserInterfaceType"]]]] = empty_list()
    session_protocol: Optional[Union[Union[dict, "SessionProtocolType"], list[Union[dict, "SessionProtocolType"]]]] = empty_list()
    protocol: Optional[Union[Union[dict, "ProtocolType"], list[Union[dict, "ProtocolType"]]]] = empty_list()
    transport: Optional[Union[Union[dict, "TransportProtocolType"], list[Union[dict, "TransportProtocolType"]]]] = empty_list()
    extra_attributes: Optional[Union[str, list[str]]] = empty_list()
    encoding: Optional[Union[Union[dict, "EncodingType"], list[Union[dict, "EncodingType"]]]] = empty_list()
    annotation: Optional[Union[dict, InterfaceAnnotation]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.service, list):
            self.service = [self.service] if self.service is not None else []
        self.service = [v if isinstance(v, ServiceType) else ServiceType(**as_dict(v)) for v in self.service]

        if not isinstance(self.user_interface, list):
            self.user_interface = [self.user_interface] if self.user_interface is not None else []
        self.user_interface = [v if isinstance(v, UserInterfaceType) else UserInterfaceType(**as_dict(v)) for v in self.user_interface]

        if not isinstance(self.session_protocol, list):
            self.session_protocol = [self.session_protocol] if self.session_protocol is not None else []
        self.session_protocol = [v if isinstance(v, SessionProtocolType) else SessionProtocolType(**as_dict(v)) for v in self.session_protocol]

        if not isinstance(self.protocol, list):
            self.protocol = [self.protocol] if self.protocol is not None else []
        self.protocol = [v if isinstance(v, ProtocolType) else ProtocolType(**as_dict(v)) for v in self.protocol]

        if not isinstance(self.transport, list):
            self.transport = [self.transport] if self.transport is not None else []
        self.transport = [v if isinstance(v, TransportProtocolType) else TransportProtocolType(**as_dict(v)) for v in self.transport]

        if not isinstance(self.extra_attributes, list):
            self.extra_attributes = [self.extra_attributes] if self.extra_attributes is not None else []
        self.extra_attributes = [v if isinstance(v, str) else str(v) for v in self.extra_attributes]

        if not isinstance(self.encoding, list):
            self.encoding = [self.encoding] if self.encoding is not None else []
        self.encoding = [v if isinstance(v, EncodingType) else EncodingType(**as_dict(v)) for v in self.encoding]

        if self.annotation is not None and not isinstance(self.annotation, InterfaceAnnotation):
            self.annotation = InterfaceAnnotation(**as_dict(self.annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterfaceDocumentation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["documentation"]
    class_class_curie: ClassVar[str] = "fixi:documentation"
    class_name: ClassVar[str] = "InterfaceDocumentation"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.InterfaceDocumentation

    value: Optional[str] = None
    content: Optional[Union[str, list[str]]] = empty_list()
    lang_id: Optional[str] = None
    purpose: Optional[Union[str, InterfacePurpose]] = None
    content_type: Optional[str] = "text/plain"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, str) else str(v) for v in self.content]

        if self.lang_id is not None and not isinstance(self.lang_id, str):
            self.lang_id = str(self.lang_id)

        if self.purpose is not None and not isinstance(self.purpose, InterfacePurpose):
            self.purpose = InterfacePurpose(self.purpose)

        if self.content_type is not None and not isinstance(self.content_type, str):
            self.content_type = str(self.content_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SessionsInline(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["SessionsInline"]
    class_class_curie: ClassVar[str] = "fix_orchestra:SessionsInline"
    class_name: ClassVar[str] = "SessionsInline"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.SessionsInline

    session: Union[Union[dict, "SessionType"], list[Union[dict, "SessionType"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.session):
            self.MissingRequiredField("session")
        self._normalize_inlined_as_list(slot_name="session", slot_type=SessionType, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InterfaceType(BaseInterfaceType):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["interfaceType"]
    class_class_curie: ClassVar[str] = "fixi:interfaceType"
    class_name: ClassVar[str] = "InterfaceType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.InterfaceType

    name: str = None
    sessions: Optional[Union[dict, SessionsInline]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sessions is not None and not isinstance(self.sessions, SessionsInline):
            self.sessions = SessionsInline(**as_dict(self.sessions))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProtocolType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["protocolType"]
    class_class_curie: ClassVar[str] = "fixi:protocolType"
    class_name: ClassVar[str] = "ProtocolType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ProtocolType

    activation_time: Optional[Union[str, XSDDateTime]] = None
    deactivation_time: Optional[Union[str, XSDDateTime]] = None
    layer: Optional[Union[str, "Layer"]] = None
    orchestration: Optional[Union[str, URI]] = None
    extra_attributes: Optional[Union[str, list[str]]] = empty_list()
    annotation: Optional[Union[dict, InterfaceAnnotation]] = None
    name: Optional[Union[str, ProtocolName]] = None
    version: Optional[str] = None
    deprecated: Optional[Union[str, XSDDateTime]] = None
    reliability: Optional[Union[str, "InterfaceReliability"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.activation_time is not None and not isinstance(self.activation_time, XSDDateTime):
            self.activation_time = XSDDateTime(self.activation_time)

        if self.deactivation_time is not None and not isinstance(self.deactivation_time, XSDDateTime):
            self.deactivation_time = XSDDateTime(self.deactivation_time)

        if self.layer is not None and not isinstance(self.layer, Layer):
            self.layer = Layer(self.layer)

        if self.orchestration is not None and not isinstance(self.orchestration, URI):
            self.orchestration = URI(self.orchestration)

        if not isinstance(self.extra_attributes, list):
            self.extra_attributes = [self.extra_attributes] if self.extra_attributes is not None else []
        self.extra_attributes = [v if isinstance(v, str) else str(v) for v in self.extra_attributes]

        if self.annotation is not None and not isinstance(self.annotation, InterfaceAnnotation):
            self.annotation = InterfaceAnnotation(**as_dict(self.annotation))

        if self.name is not None and not isinstance(self.name, ProtocolName):
            self.name = ProtocolName(self.name)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.deprecated is not None and not isinstance(self.deprecated, XSDDateTime):
            self.deprecated = XSDDateTime(self.deprecated)

        if self.reliability is not None and not isinstance(self.reliability, InterfaceReliability):
            self.reliability = InterfaceReliability(self.reliability)

        super().__post_init__(**kwargs)


class EncodingType(ProtocolType):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["encodingType"]
    class_class_curie: ClassVar[str] = "fixi:encodingType"
    class_name: ClassVar[str] = "EncodingType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.EncodingType


class ServiceType(ProtocolType):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["serviceType"]
    class_class_curie: ClassVar[str] = "fixi:serviceType"
    class_name: ClassVar[str] = "ServiceType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.ServiceType


class SessionProtocolType(ProtocolType):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["sessionProtocolType"]
    class_class_curie: ClassVar[str] = "fixi:sessionProtocolType"
    class_name: ClassVar[str] = "SessionProtocolType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.SessionProtocolType


@dataclass(repr=False)
class SessionType(BaseInterfaceType):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["sessionType"]
    class_class_curie: ClassVar[str] = "fixi:sessionType"
    class_name: ClassVar[str] = "SessionType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.SessionType

    name: str = None
    role: Optional[Union[str, "Role"]] = None
    security_keys: Optional[str] = None
    activation_time: Optional[Union[str, XSDDateTime]] = None
    deactivation_time: Optional[Union[str, XSDDateTime]] = None
    identifier: Optional[Union[Union[dict, IdentifierType], list[Union[dict, IdentifierType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.role is not None and not isinstance(self.role, Role):
            self.role = Role(self.role)

        if self.security_keys is not None and not isinstance(self.security_keys, str):
            self.security_keys = str(self.security_keys)

        if self.activation_time is not None and not isinstance(self.activation_time, XSDDateTime):
            self.activation_time = XSDDateTime(self.activation_time)

        if self.deactivation_time is not None and not isinstance(self.deactivation_time, XSDDateTime):
            self.deactivation_time = XSDDateTime(self.deactivation_time)

        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier] if self.identifier is not None else []
        self.identifier = [v if isinstance(v, IdentifierType) else IdentifierType(**as_dict(v)) for v in self.identifier]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TransportProtocolType(ProtocolType):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["transportProtocolType"]
    class_class_curie: ClassVar[str] = "fixi:transportProtocolType"
    class_name: ClassVar[str] = "TransportProtocolType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.TransportProtocolType

    address: Optional[str] = None
    message_cast: Optional[Union[str, "MessageCast"]] = 'unicast'
    use: Optional[Union[str, TransportUse]] = None
    extra_attributes: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.message_cast is not None and not isinstance(self.message_cast, MessageCast):
            self.message_cast = MessageCast(self.message_cast)

        if self.use is not None and not isinstance(self.use, TransportUse):
            self.use = TransportUse(self.use)

        if not isinstance(self.extra_attributes, list):
            self.extra_attributes = [self.extra_attributes] if self.extra_attributes is not None else []
        self.extra_attributes = [v if isinstance(v, str) else str(v) for v in self.extra_attributes]

        super().__post_init__(**kwargs)


class UserInterfaceType(ProtocolType):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["userInterfaceType"]
    class_class_curie: ClassVar[str] = "fixi:userInterfaceType"
    class_name: ClassVar[str] = "UserInterfaceType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.UserInterfaceType


@dataclass(repr=False)
class Datatype(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["datatype"]
    class_class_curie: ClassVar[str] = "fixr:datatype"
    class_name: ClassVar[str] = "Datatype"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Datatype

    name: Union[str, Name] = None
    mapped_datatype: Optional[Union[Union[dict, MappedDatatype], list[Union[dict, MappedDatatype]]]] = empty_list()
    scenario_id: Optional[Union[int, Id]] = 1
    base_type: Optional[Union[str, Name]] = None
    annotation: Optional[Union[dict, Annotation]] = None
    scenario: Optional[Union[str, Name]] = "base"
    added: Optional[Union[str, Version]] = None
    added_ep: Optional[Union[int, EP]] = None
    change_type: Optional[Union[str, "ChangeType"]] = None
    deprecated_ep: Optional[Union[int, EP]] = None
    issue: Optional[str] = None
    last_modified: Optional[Union[str, Version]] = None
    replaced: Optional[Union[str, Version]] = None
    replaced_ep: Optional[Union[int, EP]] = None
    replaced_by_field: Optional[Union[int, Id]] = None
    supported: Optional[Union[str, "SupportType"]] = 'supported'
    updated: Optional[Union[str, Version]] = None
    updated_ep: Optional[Union[int, EP]] = None
    deprecated: Optional[Union[str, Version]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, Name):
            self.name = Name(self.name)

        self._normalize_inlined_as_list(slot_name="mapped_datatype", slot_type=MappedDatatype, key_name="standard", keyed=False)

        if self.scenario_id is not None and not isinstance(self.scenario_id, Id):
            self.scenario_id = Id(self.scenario_id)

        if self.base_type is not None and not isinstance(self.base_type, Name):
            self.base_type = Name(self.base_type)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.scenario is not None and not isinstance(self.scenario, Name):
            self.scenario = Name(self.scenario)

        if self.added is not None and not isinstance(self.added, Version):
            self.added = Version(self.added)

        if self.added_ep is not None and not isinstance(self.added_ep, EP):
            self.added_ep = EP(self.added_ep)

        if self.change_type is not None and not isinstance(self.change_type, ChangeType):
            self.change_type = ChangeType(self.change_type)

        if self.deprecated_ep is not None and not isinstance(self.deprecated_ep, EP):
            self.deprecated_ep = EP(self.deprecated_ep)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        if self.last_modified is not None and not isinstance(self.last_modified, Version):
            self.last_modified = Version(self.last_modified)

        if self.replaced is not None and not isinstance(self.replaced, Version):
            self.replaced = Version(self.replaced)

        if self.replaced_ep is not None and not isinstance(self.replaced_ep, EP):
            self.replaced_ep = EP(self.replaced_ep)

        if self.replaced_by_field is not None and not isinstance(self.replaced_by_field, Id):
            self.replaced_by_field = Id(self.replaced_by_field)

        if self.supported is not None and not isinstance(self.supported, SupportType):
            self.supported = SupportType(self.supported)

        if self.updated is not None and not isinstance(self.updated, Version):
            self.updated = Version(self.updated)

        if self.updated_ep is not None and not isinstance(self.updated_ep, EP):
            self.updated_ep = EP(self.updated_ep)

        if self.deprecated is not None and not isinstance(self.deprecated, Version):
            self.deprecated = Version(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Actors(YAMLRoot):
    """
    Participants and the message flows between them
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["actors"]
    class_class_curie: ClassVar[str] = "fixr:actors"
    class_name: ClassVar[str] = "Actors"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Actors

    actor: Optional[Union[Union[dict, ActorType], list[Union[dict, ActorType]]]] = empty_list()
    flow: Optional[Union[Union[dict, FlowType], list[Union[dict, FlowType]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="actor", slot_type=ActorType, key_name="name", keyed=False)

        self._normalize_inlined_as_list(slot_name="flow", slot_type=FlowType, key_name="source", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Categories(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["categories"]
    class_class_curie: ClassVar[str] = "fixr:categories"
    class_name: ClassVar[str] = "Categories"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Categories

    category: Optional[Union[Union[dict, CategoryType], list[Union[dict, CategoryType]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="category", slot_type=CategoryType, key_name="name", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeSets(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["codeSets"]
    class_class_curie: ClassVar[str] = "fixr:codeSets"
    class_name: ClassVar[str] = "CodeSets"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.CodeSets

    code_set: Optional[Union[Union[dict, CodeSetType], list[Union[dict, CodeSetType]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="code_set", slot_type=CodeSetType, key_name="type", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Components(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["components"]
    class_class_curie: ClassVar[str] = "fixr:components"
    class_name: ClassVar[str] = "Components"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Components

    component: Optional[Union[Union[dict, ComponentType], list[Union[dict, ComponentType]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="component", slot_type=ComponentType, key_name="id", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concepts(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["concepts"]
    class_class_curie: ClassVar[str] = "fixr:concepts"
    class_name: ClassVar[str] = "Concepts"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Concepts

    concept: Optional[Union[Union[dict, ConceptType], list[Union[dict, ConceptType]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="concept", slot_type=ConceptType, key_name="name", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Datatypes(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["datatypes"]
    class_class_curie: ClassVar[str] = "fixr:datatypes"
    class_name: ClassVar[str] = "Datatypes"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Datatypes

    datatype: Optional[Union[Union[dict, Datatype], list[Union[dict, Datatype]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="datatype", slot_type=Datatype, key_name="name", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Fields(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["fields"]
    class_class_curie: ClassVar[str] = "fixr:fields"
    class_name: ClassVar[str] = "Fields"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Fields

    field: Optional[Union[Union[dict, FieldType], list[Union[dict, FieldType]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="field", slot_type=FieldType, key_name="id", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Groups(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["groups"]
    class_class_curie: ClassVar[str] = "fixr:groups"
    class_name: ClassVar[str] = "Groups"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Groups

    group: Optional[Union[Union[dict, GroupType], list[Union[dict, GroupType]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="group", slot_type=GroupType, key_name="id", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Messages(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["messages"]
    class_class_curie: ClassVar[str] = "fixr:messages"
    class_name: ClassVar[str] = "Messages"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Messages

    message: Optional[Union[Union[dict, MessageType], list[Union[dict, MessageType]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="message", slot_type=MessageType, key_name="id", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Repository(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["repository"]
    class_class_curie: ClassVar[str] = "fixr:repository"
    class_name: ClassVar[str] = "Repository"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Repository

    metadata: Union[dict, "DctermsElementOrRefinementContainer"] = None
    datatypes: Union[dict, Datatypes] = None
    fields: Union[dict, Fields] = None
    messages: Union[dict, Messages] = None
    name: str = None
    version: Union[str, Version] = None
    categories: Optional[Union[dict, Categories]] = None
    sections: Optional[Union[dict, "Sections"]] = None
    code_sets: Optional[Union[dict, CodeSets]] = None
    actors: Optional[Union[dict, Actors]] = None
    components: Optional[Union[dict, Components]] = None
    groups: Optional[Union[dict, Groups]] = None
    concepts: Optional[Union[dict, Concepts]] = None
    scenarios: Optional[Union[dict, "Scenarios"]] = None
    guid: Optional[str] = None
    spec_url: Optional[Union[str, URI]] = None
    namespace: Optional[Union[str, URI]] = None
    expression_language: Optional[str] = "Score"
    annotation: Optional[Union[dict, Annotation]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, DctermsElementOrRefinementContainer):
            self.metadata = DctermsElementOrRefinementContainer(**as_dict(self.metadata))

        if self._is_empty(self.datatypes):
            self.MissingRequiredField("datatypes")
        if not isinstance(self.datatypes, Datatypes):
            self.datatypes = Datatypes(**as_dict(self.datatypes))

        if self._is_empty(self.fields):
            self.MissingRequiredField("fields")
        if not isinstance(self.fields, Fields):
            self.fields = Fields(**as_dict(self.fields))

        if self._is_empty(self.messages):
            self.MissingRequiredField("messages")
        if not isinstance(self.messages, Messages):
            self.messages = Messages(**as_dict(self.messages))

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, Version):
            self.version = Version(self.version)

        if self.categories is not None and not isinstance(self.categories, Categories):
            self.categories = Categories(**as_dict(self.categories))

        if self.sections is not None and not isinstance(self.sections, Sections):
            self.sections = Sections(**as_dict(self.sections))

        if self.code_sets is not None and not isinstance(self.code_sets, CodeSets):
            self.code_sets = CodeSets(**as_dict(self.code_sets))

        if self.actors is not None and not isinstance(self.actors, Actors):
            self.actors = Actors(**as_dict(self.actors))

        if self.components is not None and not isinstance(self.components, Components):
            self.components = Components(**as_dict(self.components))

        if self.groups is not None and not isinstance(self.groups, Groups):
            self.groups = Groups(**as_dict(self.groups))

        if self.concepts is not None and not isinstance(self.concepts, Concepts):
            self.concepts = Concepts(**as_dict(self.concepts))

        if self.scenarios is not None and not isinstance(self.scenarios, Scenarios):
            self.scenarios = Scenarios(**as_dict(self.scenarios))

        if self.guid is not None and not isinstance(self.guid, str):
            self.guid = str(self.guid)

        if self.spec_url is not None and not isinstance(self.spec_url, URI):
            self.spec_url = URI(self.spec_url)

        if self.namespace is not None and not isinstance(self.namespace, URI):
            self.namespace = URI(self.namespace)

        if self.expression_language is not None and not isinstance(self.expression_language, str):
            self.expression_language = str(self.expression_language)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Scenarios(YAMLRoot):
    """
    The default scenario is id='1' name='base'.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["scenarios"]
    class_class_curie: ClassVar[str] = "fixr:scenarios"
    class_name: ClassVar[str] = "Scenarios"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Scenarios

    scenario: Optional[Union[Union[dict, ScenarioType], list[Union[dict, ScenarioType]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.scenario, list):
            self.scenario = [self.scenario] if self.scenario is not None else []
        self.scenario = [v if isinstance(v, ScenarioType) else ScenarioType(**as_dict(v)) for v in self.scenario]

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sections(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXR["sections"]
    class_class_curie: ClassVar[str] = "fixr:sections"
    class_name: ClassVar[str] = "Sections"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Sections

    section: Optional[Union[Union[dict, SectionType], list[Union[dict, SectionType]]]] = empty_list()
    annotation: Optional[Union[dict, Annotation]] = None
    base: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="section", slot_type=SectionType, key_name="name", keyed=False)

        if self.annotation is not None and not isinstance(self.annotation, Annotation):
            self.annotation = Annotation(**as_dict(self.annotation))

        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Interfaces(YAMLRoot):
    """
    This represents the current state of service and session configurations. Changes to configuration can represented
    with patch operations. See IETF RFC 5261
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIXI["interfaces"]
    class_class_curie: ClassVar[str] = "fixi:interfaces"
    class_name: ClassVar[str] = "Interfaces"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.Interfaces

    metadata: Union[dict, "DctermsElementOrRefinementContainer"] = None
    interface: Optional[Union[Union[dict, InterfaceType], list[Union[dict, InterfaceType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.metadata):
            self.MissingRequiredField("metadata")
        if not isinstance(self.metadata, DctermsElementOrRefinementContainer):
            self.metadata = DctermsElementOrRefinementContainer(**as_dict(self.metadata))

        self._normalize_inlined_as_list(slot_name="interface", slot_type=InterfaceType, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DcSimpleLiteral(YAMLRoot):
    """
    This is the default type for all of the DC elements. It permits text content only with optional xml:lang
    attribute. Text is allowed because mixed="true", but sub-elements are disallowed because minOccurs="0" and
    maxOccurs="0" are on the xs:any tag. This complexType allows for restriction or extension permitting child
    elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["SimpleLiteral"]
    class_class_curie: ClassVar[str] = "dc:SimpleLiteral"
    class_name: ClassVar[str] = "DcSimpleLiteral"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcSimpleLiteral

    value: Optional[str] = None
    content: Optional[Union[str, list[str]]] = empty_list()
    lang: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if not isinstance(self.content, list):
            self.content = [self.content] if self.content is not None else []
        self.content = [v if isinstance(v, str) else str(v) for v in self.content]

        if self.lang is not None and not isinstance(self.lang, str):
            self.lang = str(self.lang)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DcElementContainer(YAMLRoot):
    """
    This complexType is included as a convenience for schema authors who need to define a root or container element
    for all of the DC elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["elementContainer"]
    class_class_curie: ClassVar[str] = "dc:elementContainer"
    class_name: ClassVar[str] = "DcElementContainer"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcElementContainer

    title: Optional[str] = None
    creator: Optional[str] = None
    subject: Optional[str] = None
    description: Optional[str] = None
    publisher: Optional[str] = None
    contributor: Optional[str] = None
    date: Optional[str] = None
    format: Optional[str] = None
    source: Optional[str] = None
    language: Optional[str] = None
    relation: Optional[str] = None
    coverage: Optional[str] = None
    rights: Optional[str] = None
    alternative: Optional[str] = None
    table_of_contents: Optional[str] = None
    abstract: Optional[str] = None
    created: Optional[str] = None
    valid: Optional[str] = None
    available: Optional[str] = None
    issued: Optional[str] = None
    modified: Optional[str] = None
    date_accepted: Optional[str] = None
    date_copyrighted: Optional[str] = None
    date_submitted: Optional[str] = None
    extent: Optional[str] = None
    medium: Optional[str] = None
    is_version_of: Optional[str] = None
    has_version: Optional[str] = None
    is_replaced_by: Optional[str] = None
    replaces: Optional[str] = None
    is_required_by: Optional[str] = None
    requires: Optional[str] = None
    is_part_of: Optional[str] = None
    has_part: Optional[str] = None
    is_referenced_by: Optional[str] = None
    references: Optional[str] = None
    is_format_of: Optional[str] = None
    has_format: Optional[str] = None
    conforms_to: Optional[str] = None
    spatial: Optional[str] = None
    temporal: Optional[str] = None
    audience: Optional[str] = None
    accrual_method: Optional[str] = None
    accrual_periodicity: Optional[str] = None
    accrual_policy: Optional[str] = None
    instructional_method: Optional[str] = None
    provenance: Optional[str] = None
    rights_holder: Optional[str] = None
    mediator: Optional[str] = None
    education_level: Optional[str] = None
    access_rights: Optional[str] = None
    license: Optional[str] = None
    bibliographic_citation: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.creator is not None and not isinstance(self.creator, str):
            self.creator = str(self.creator)

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.contributor is not None and not isinstance(self.contributor, str):
            self.contributor = str(self.contributor)

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.relation is not None and not isinstance(self.relation, str):
            self.relation = str(self.relation)

        if self.coverage is not None and not isinstance(self.coverage, str):
            self.coverage = str(self.coverage)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.alternative is not None and not isinstance(self.alternative, str):
            self.alternative = str(self.alternative)

        if self.table_of_contents is not None and not isinstance(self.table_of_contents, str):
            self.table_of_contents = str(self.table_of_contents)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.created is not None and not isinstance(self.created, str):
            self.created = str(self.created)

        if self.valid is not None and not isinstance(self.valid, str):
            self.valid = str(self.valid)

        if self.available is not None and not isinstance(self.available, str):
            self.available = str(self.available)

        if self.issued is not None and not isinstance(self.issued, str):
            self.issued = str(self.issued)

        if self.modified is not None and not isinstance(self.modified, str):
            self.modified = str(self.modified)

        if self.date_accepted is not None and not isinstance(self.date_accepted, str):
            self.date_accepted = str(self.date_accepted)

        if self.date_copyrighted is not None and not isinstance(self.date_copyrighted, str):
            self.date_copyrighted = str(self.date_copyrighted)

        if self.date_submitted is not None and not isinstance(self.date_submitted, str):
            self.date_submitted = str(self.date_submitted)

        if self.extent is not None and not isinstance(self.extent, str):
            self.extent = str(self.extent)

        if self.medium is not None and not isinstance(self.medium, str):
            self.medium = str(self.medium)

        if self.is_version_of is not None and not isinstance(self.is_version_of, str):
            self.is_version_of = str(self.is_version_of)

        if self.has_version is not None and not isinstance(self.has_version, str):
            self.has_version = str(self.has_version)

        if self.is_replaced_by is not None and not isinstance(self.is_replaced_by, str):
            self.is_replaced_by = str(self.is_replaced_by)

        if self.replaces is not None and not isinstance(self.replaces, str):
            self.replaces = str(self.replaces)

        if self.is_required_by is not None and not isinstance(self.is_required_by, str):
            self.is_required_by = str(self.is_required_by)

        if self.requires is not None and not isinstance(self.requires, str):
            self.requires = str(self.requires)

        if self.is_part_of is not None and not isinstance(self.is_part_of, str):
            self.is_part_of = str(self.is_part_of)

        if self.has_part is not None and not isinstance(self.has_part, str):
            self.has_part = str(self.has_part)

        if self.is_referenced_by is not None and not isinstance(self.is_referenced_by, str):
            self.is_referenced_by = str(self.is_referenced_by)

        if self.references is not None and not isinstance(self.references, str):
            self.references = str(self.references)

        if self.is_format_of is not None and not isinstance(self.is_format_of, str):
            self.is_format_of = str(self.is_format_of)

        if self.has_format is not None and not isinstance(self.has_format, str):
            self.has_format = str(self.has_format)

        if self.conforms_to is not None and not isinstance(self.conforms_to, str):
            self.conforms_to = str(self.conforms_to)

        if self.spatial is not None and not isinstance(self.spatial, str):
            self.spatial = str(self.spatial)

        if self.temporal is not None and not isinstance(self.temporal, str):
            self.temporal = str(self.temporal)

        if self.audience is not None and not isinstance(self.audience, str):
            self.audience = str(self.audience)

        if self.accrual_method is not None and not isinstance(self.accrual_method, str):
            self.accrual_method = str(self.accrual_method)

        if self.accrual_periodicity is not None and not isinstance(self.accrual_periodicity, str):
            self.accrual_periodicity = str(self.accrual_periodicity)

        if self.accrual_policy is not None and not isinstance(self.accrual_policy, str):
            self.accrual_policy = str(self.accrual_policy)

        if self.instructional_method is not None and not isinstance(self.instructional_method, str):
            self.instructional_method = str(self.instructional_method)

        if self.provenance is not None and not isinstance(self.provenance, str):
            self.provenance = str(self.provenance)

        if self.rights_holder is not None and not isinstance(self.rights_holder, str):
            self.rights_holder = str(self.rights_holder)

        if self.mediator is not None and not isinstance(self.mediator, str):
            self.mediator = str(self.mediator)

        if self.education_level is not None and not isinstance(self.education_level, str):
            self.education_level = str(self.education_level)

        if self.access_rights is not None and not isinstance(self.access_rights, str):
            self.access_rights = str(self.access_rights)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.bibliographic_citation is not None and not isinstance(self.bibliographic_citation, str):
            self.bibliographic_citation = str(self.bibliographic_citation)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)


class DcAny(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["any"]
    class_class_curie: ClassVar[str] = "dc:any"
    class_name: ClassVar[str] = "DcAny"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcAny


class DcTitle(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["title"]
    class_class_curie: ClassVar[str] = "dc:title"
    class_name: ClassVar[str] = "DcTitle"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcTitle


class DcCreator(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["creator"]
    class_class_curie: ClassVar[str] = "dc:creator"
    class_name: ClassVar[str] = "DcCreator"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcCreator


class DcSubject(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["subject"]
    class_class_curie: ClassVar[str] = "dc:subject"
    class_name: ClassVar[str] = "DcSubject"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcSubject


class DcDescription(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["description"]
    class_class_curie: ClassVar[str] = "dc:description"
    class_name: ClassVar[str] = "DcDescription"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcDescription


class DcPublisher(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["publisher"]
    class_class_curie: ClassVar[str] = "dc:publisher"
    class_name: ClassVar[str] = "DcPublisher"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcPublisher


class DcContributor(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["contributor"]
    class_class_curie: ClassVar[str] = "dc:contributor"
    class_name: ClassVar[str] = "DcContributor"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcContributor


class DcDate(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["date"]
    class_class_curie: ClassVar[str] = "dc:date"
    class_name: ClassVar[str] = "DcDate"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcDate


class DcType(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["type"]
    class_class_curie: ClassVar[str] = "dc:type"
    class_name: ClassVar[str] = "DcType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcType


class DcFormat(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["format"]
    class_class_curie: ClassVar[str] = "dc:format"
    class_name: ClassVar[str] = "DcFormat"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcFormat


class DcIdentifier(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["identifier"]
    class_class_curie: ClassVar[str] = "dc:identifier"
    class_name: ClassVar[str] = "DcIdentifier"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcIdentifier


class DcSource(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["source"]
    class_class_curie: ClassVar[str] = "dc:source"
    class_name: ClassVar[str] = "DcSource"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcSource


class DcLanguage(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["language"]
    class_class_curie: ClassVar[str] = "dc:language"
    class_name: ClassVar[str] = "DcLanguage"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcLanguage


class DcRelation(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["relation"]
    class_class_curie: ClassVar[str] = "dc:relation"
    class_name: ClassVar[str] = "DcRelation"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcRelation


class DcCoverage(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["coverage"]
    class_class_curie: ClassVar[str] = "dc:coverage"
    class_name: ClassVar[str] = "DcCoverage"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcCoverage


class DcRights(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["rights"]
    class_class_curie: ClassVar[str] = "dc:rights"
    class_name: ClassVar[str] = "DcRights"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcRights


class DcElementsGroup(YAMLRoot):
    """
    This group is included as a convenience for schema authors who need to refer to all the elements in the
    http://purl.org/dc/elements/1.1/ namespace.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DC["elementsGroup"]
    class_class_curie: ClassVar[str] = "dc:elementsGroup"
    class_name: ClassVar[str] = "DcElementsGroup"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DcElementsGroup


class DctermsLCSH(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["LCSH"]
    class_class_curie: ClassVar[str] = "dct:LCSH"
    class_name: ClassVar[str] = "DctermsLCSH"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsLCSH


class DctermsMESH(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["MESH"]
    class_class_curie: ClassVar[str] = "dct:MESH"
    class_name: ClassVar[str] = "DctermsMESH"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsMESH


class DctermsDDC(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["DDC"]
    class_class_curie: ClassVar[str] = "dct:DDC"
    class_name: ClassVar[str] = "DctermsDDC"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsDDC


class DctermsLCC(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["LCC"]
    class_class_curie: ClassVar[str] = "dct:LCC"
    class_name: ClassVar[str] = "DctermsLCC"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsLCC


class DctermsUDC(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["UDC"]
    class_class_curie: ClassVar[str] = "dct:UDC"
    class_name: ClassVar[str] = "DctermsUDC"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsUDC


class DctermsPeriod(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Period"]
    class_class_curie: ClassVar[str] = "dct:Period"
    class_name: ClassVar[str] = "DctermsPeriod"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsPeriod


class DctermsW3CDTF(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["W3CDTF"]
    class_class_curie: ClassVar[str] = "dct:W3CDTF"
    class_name: ClassVar[str] = "DctermsW3CDTF"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsW3CDTF


class DctermsDCMIType(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["DCMIType"]
    class_class_curie: ClassVar[str] = "dct:DCMIType"
    class_name: ClassVar[str] = "DctermsDCMIType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsDCMIType


class DctermsIMT(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["IMT"]
    class_class_curie: ClassVar[str] = "dct:IMT"
    class_name: ClassVar[str] = "DctermsIMT"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsIMT


class DctermsURI(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["URI"]
    class_class_curie: ClassVar[str] = "dct:URI"
    class_name: ClassVar[str] = "DctermsURI"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsURI


class DctermsISO6392(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["ISO639-2"]
    class_class_curie: ClassVar[str] = "dct:ISO639-2"
    class_name: ClassVar[str] = "DctermsISO6392"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsISO6392


class DctermsISO6393(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["ISO639-3"]
    class_class_curie: ClassVar[str] = "dct:ISO639-3"
    class_name: ClassVar[str] = "DctermsISO6393"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsISO6393


class DctermsRFC1766(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["RFC1766"]
    class_class_curie: ClassVar[str] = "dct:RFC1766"
    class_name: ClassVar[str] = "DctermsRFC1766"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsRFC1766


class DctermsRFC3066(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["RFC3066"]
    class_class_curie: ClassVar[str] = "dct:RFC3066"
    class_name: ClassVar[str] = "DctermsRFC3066"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsRFC3066


class DctermsRFC4646(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["RFC4646"]
    class_class_curie: ClassVar[str] = "dct:RFC4646"
    class_name: ClassVar[str] = "DctermsRFC4646"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsRFC4646


class DctermsPoint(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Point"]
    class_class_curie: ClassVar[str] = "dct:Point"
    class_name: ClassVar[str] = "DctermsPoint"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsPoint


class DctermsISO3166(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["ISO3166"]
    class_class_curie: ClassVar[str] = "dct:ISO3166"
    class_name: ClassVar[str] = "DctermsISO3166"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsISO3166


class DctermsBox(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["Box"]
    class_class_curie: ClassVar[str] = "dct:Box"
    class_name: ClassVar[str] = "DctermsBox"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsBox


class DctermsTGN(DcSimpleLiteral):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["TGN"]
    class_class_curie: ClassVar[str] = "dct:TGN"
    class_name: ClassVar[str] = "DctermsTGN"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsTGN


@dataclass(repr=False)
class DctermsElementOrRefinementContainer(YAMLRoot):
    """
    This is included as a convenience for schema authors who need to define a root or container element for all of the
    DC elements and element refinements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["elementOrRefinementContainer"]
    class_class_curie: ClassVar[str] = "dct:elementOrRefinementContainer"
    class_name: ClassVar[str] = "DctermsElementOrRefinementContainer"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsElementOrRefinementContainer

    title: Optional[str] = None
    creator: Optional[str] = None
    subject: Optional[str] = None
    description: Optional[str] = None
    publisher: Optional[str] = None
    contributor: Optional[str] = None
    date: Optional[str] = None
    format: Optional[str] = None
    source: Optional[str] = None
    language: Optional[str] = None
    relation: Optional[str] = None
    coverage: Optional[str] = None
    rights: Optional[str] = None
    alternative: Optional[str] = None
    table_of_contents: Optional[str] = None
    abstract: Optional[str] = None
    created: Optional[str] = None
    valid: Optional[str] = None
    available: Optional[str] = None
    issued: Optional[str] = None
    modified: Optional[str] = None
    date_accepted: Optional[str] = None
    date_copyrighted: Optional[str] = None
    date_submitted: Optional[str] = None
    extent: Optional[str] = None
    medium: Optional[str] = None
    is_version_of: Optional[str] = None
    has_version: Optional[str] = None
    is_replaced_by: Optional[str] = None
    replaces: Optional[str] = None
    is_required_by: Optional[str] = None
    requires: Optional[str] = None
    is_part_of: Optional[str] = None
    has_part: Optional[str] = None
    is_referenced_by: Optional[str] = None
    references: Optional[str] = None
    is_format_of: Optional[str] = None
    has_format: Optional[str] = None
    conforms_to: Optional[str] = None
    spatial: Optional[str] = None
    temporal: Optional[str] = None
    audience: Optional[str] = None
    accrual_method: Optional[str] = None
    accrual_periodicity: Optional[str] = None
    accrual_policy: Optional[str] = None
    instructional_method: Optional[str] = None
    provenance: Optional[str] = None
    rights_holder: Optional[str] = None
    mediator: Optional[str] = None
    education_level: Optional[str] = None
    access_rights: Optional[str] = None
    license: Optional[str] = None
    bibliographic_citation: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.creator is not None and not isinstance(self.creator, str):
            self.creator = str(self.creator)

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.contributor is not None and not isinstance(self.contributor, str):
            self.contributor = str(self.contributor)

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.relation is not None and not isinstance(self.relation, str):
            self.relation = str(self.relation)

        if self.coverage is not None and not isinstance(self.coverage, str):
            self.coverage = str(self.coverage)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.alternative is not None and not isinstance(self.alternative, str):
            self.alternative = str(self.alternative)

        if self.table_of_contents is not None and not isinstance(self.table_of_contents, str):
            self.table_of_contents = str(self.table_of_contents)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.created is not None and not isinstance(self.created, str):
            self.created = str(self.created)

        if self.valid is not None and not isinstance(self.valid, str):
            self.valid = str(self.valid)

        if self.available is not None and not isinstance(self.available, str):
            self.available = str(self.available)

        if self.issued is not None and not isinstance(self.issued, str):
            self.issued = str(self.issued)

        if self.modified is not None and not isinstance(self.modified, str):
            self.modified = str(self.modified)

        if self.date_accepted is not None and not isinstance(self.date_accepted, str):
            self.date_accepted = str(self.date_accepted)

        if self.date_copyrighted is not None and not isinstance(self.date_copyrighted, str):
            self.date_copyrighted = str(self.date_copyrighted)

        if self.date_submitted is not None and not isinstance(self.date_submitted, str):
            self.date_submitted = str(self.date_submitted)

        if self.extent is not None and not isinstance(self.extent, str):
            self.extent = str(self.extent)

        if self.medium is not None and not isinstance(self.medium, str):
            self.medium = str(self.medium)

        if self.is_version_of is not None and not isinstance(self.is_version_of, str):
            self.is_version_of = str(self.is_version_of)

        if self.has_version is not None and not isinstance(self.has_version, str):
            self.has_version = str(self.has_version)

        if self.is_replaced_by is not None and not isinstance(self.is_replaced_by, str):
            self.is_replaced_by = str(self.is_replaced_by)

        if self.replaces is not None and not isinstance(self.replaces, str):
            self.replaces = str(self.replaces)

        if self.is_required_by is not None and not isinstance(self.is_required_by, str):
            self.is_required_by = str(self.is_required_by)

        if self.requires is not None and not isinstance(self.requires, str):
            self.requires = str(self.requires)

        if self.is_part_of is not None and not isinstance(self.is_part_of, str):
            self.is_part_of = str(self.is_part_of)

        if self.has_part is not None and not isinstance(self.has_part, str):
            self.has_part = str(self.has_part)

        if self.is_referenced_by is not None and not isinstance(self.is_referenced_by, str):
            self.is_referenced_by = str(self.is_referenced_by)

        if self.references is not None and not isinstance(self.references, str):
            self.references = str(self.references)

        if self.is_format_of is not None and not isinstance(self.is_format_of, str):
            self.is_format_of = str(self.is_format_of)

        if self.has_format is not None and not isinstance(self.has_format, str):
            self.has_format = str(self.has_format)

        if self.conforms_to is not None and not isinstance(self.conforms_to, str):
            self.conforms_to = str(self.conforms_to)

        if self.spatial is not None and not isinstance(self.spatial, str):
            self.spatial = str(self.spatial)

        if self.temporal is not None and not isinstance(self.temporal, str):
            self.temporal = str(self.temporal)

        if self.audience is not None and not isinstance(self.audience, str):
            self.audience = str(self.audience)

        if self.accrual_method is not None and not isinstance(self.accrual_method, str):
            self.accrual_method = str(self.accrual_method)

        if self.accrual_periodicity is not None and not isinstance(self.accrual_periodicity, str):
            self.accrual_periodicity = str(self.accrual_periodicity)

        if self.accrual_policy is not None and not isinstance(self.accrual_policy, str):
            self.accrual_policy = str(self.accrual_policy)

        if self.instructional_method is not None and not isinstance(self.instructional_method, str):
            self.instructional_method = str(self.instructional_method)

        if self.provenance is not None and not isinstance(self.provenance, str):
            self.provenance = str(self.provenance)

        if self.rights_holder is not None and not isinstance(self.rights_holder, str):
            self.rights_holder = str(self.rights_holder)

        if self.mediator is not None and not isinstance(self.mediator, str):
            self.mediator = str(self.mediator)

        if self.education_level is not None and not isinstance(self.education_level, str):
            self.education_level = str(self.education_level)

        if self.access_rights is not None and not isinstance(self.access_rights, str):
            self.access_rights = str(self.access_rights)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.bibliographic_citation is not None and not isinstance(self.bibliographic_citation, str):
            self.bibliographic_citation = str(self.bibliographic_citation)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)


class DctermsTitle(DcTitle):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["title"]
    class_class_curie: ClassVar[str] = "dct:title"
    class_name: ClassVar[str] = "DctermsTitle"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsTitle


class DctermsCreator(DcCreator):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["creator"]
    class_class_curie: ClassVar[str] = "dct:creator"
    class_name: ClassVar[str] = "DctermsCreator"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsCreator


class DctermsSubject(DcSubject):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["subject"]
    class_class_curie: ClassVar[str] = "dct:subject"
    class_name: ClassVar[str] = "DctermsSubject"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsSubject


class DctermsDescription(DcDescription):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["description"]
    class_class_curie: ClassVar[str] = "dct:description"
    class_name: ClassVar[str] = "DctermsDescription"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsDescription


class DctermsPublisher(DcPublisher):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["publisher"]
    class_class_curie: ClassVar[str] = "dct:publisher"
    class_name: ClassVar[str] = "DctermsPublisher"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsPublisher


class DctermsContributor(DcContributor):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["contributor"]
    class_class_curie: ClassVar[str] = "dct:contributor"
    class_name: ClassVar[str] = "DctermsContributor"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsContributor


class DctermsDate(DcDate):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["date"]
    class_class_curie: ClassVar[str] = "dct:date"
    class_name: ClassVar[str] = "DctermsDate"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsDate


class DctermsType(DcType):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["type"]
    class_class_curie: ClassVar[str] = "dct:type"
    class_name: ClassVar[str] = "DctermsType"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsType


class DctermsFormat(DcFormat):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["format"]
    class_class_curie: ClassVar[str] = "dct:format"
    class_name: ClassVar[str] = "DctermsFormat"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsFormat


class DctermsIdentifier(DcIdentifier):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["identifier"]
    class_class_curie: ClassVar[str] = "dct:identifier"
    class_name: ClassVar[str] = "DctermsIdentifier"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsIdentifier


class DctermsSource(DcSource):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["source"]
    class_class_curie: ClassVar[str] = "dct:source"
    class_name: ClassVar[str] = "DctermsSource"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsSource


class DctermsLanguage(DcLanguage):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["language"]
    class_class_curie: ClassVar[str] = "dct:language"
    class_name: ClassVar[str] = "DctermsLanguage"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsLanguage


class DctermsRelation(DcRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["relation"]
    class_class_curie: ClassVar[str] = "dct:relation"
    class_name: ClassVar[str] = "DctermsRelation"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsRelation


class DctermsCoverage(DcCoverage):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["coverage"]
    class_class_curie: ClassVar[str] = "dct:coverage"
    class_name: ClassVar[str] = "DctermsCoverage"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsCoverage


class DctermsRights(DcRights):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["rights"]
    class_class_curie: ClassVar[str] = "dct:rights"
    class_name: ClassVar[str] = "DctermsRights"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsRights


class DctermsAlternative(DctermsTitle):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["alternative"]
    class_class_curie: ClassVar[str] = "dct:alternative"
    class_name: ClassVar[str] = "DctermsAlternative"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsAlternative


class DctermsTableOfContents(DctermsDescription):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["tableOfContents"]
    class_class_curie: ClassVar[str] = "dct:tableOfContents"
    class_name: ClassVar[str] = "DctermsTableOfContents"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsTableOfContents


class DctermsAbstract(DctermsDescription):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["abstract"]
    class_class_curie: ClassVar[str] = "dct:abstract"
    class_name: ClassVar[str] = "DctermsAbstract"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsAbstract


class DctermsCreated(DctermsDate):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["created"]
    class_class_curie: ClassVar[str] = "dct:created"
    class_name: ClassVar[str] = "DctermsCreated"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsCreated


class DctermsValid(DctermsDate):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["valid"]
    class_class_curie: ClassVar[str] = "dct:valid"
    class_name: ClassVar[str] = "DctermsValid"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsValid


class DctermsAvailable(DctermsDate):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["available"]
    class_class_curie: ClassVar[str] = "dct:available"
    class_name: ClassVar[str] = "DctermsAvailable"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsAvailable


class DctermsIssued(DctermsDate):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["issued"]
    class_class_curie: ClassVar[str] = "dct:issued"
    class_name: ClassVar[str] = "DctermsIssued"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsIssued


class DctermsModified(DctermsDate):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["modified"]
    class_class_curie: ClassVar[str] = "dct:modified"
    class_name: ClassVar[str] = "DctermsModified"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsModified


class DctermsDateAccepted(DctermsDate):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["dateAccepted"]
    class_class_curie: ClassVar[str] = "dct:dateAccepted"
    class_name: ClassVar[str] = "DctermsDateAccepted"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsDateAccepted


class DctermsDateCopyrighted(DctermsDate):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["dateCopyrighted"]
    class_class_curie: ClassVar[str] = "dct:dateCopyrighted"
    class_name: ClassVar[str] = "DctermsDateCopyrighted"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsDateCopyrighted


class DctermsDateSubmitted(DctermsDate):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["dateSubmitted"]
    class_class_curie: ClassVar[str] = "dct:dateSubmitted"
    class_name: ClassVar[str] = "DctermsDateSubmitted"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsDateSubmitted


class DctermsExtent(DctermsFormat):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["extent"]
    class_class_curie: ClassVar[str] = "dct:extent"
    class_name: ClassVar[str] = "DctermsExtent"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsExtent


class DctermsMedium(DctermsFormat):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["medium"]
    class_class_curie: ClassVar[str] = "dct:medium"
    class_name: ClassVar[str] = "DctermsMedium"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsMedium


class DctermsIsVersionOf(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["isVersionOf"]
    class_class_curie: ClassVar[str] = "dct:isVersionOf"
    class_name: ClassVar[str] = "DctermsIsVersionOf"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsIsVersionOf


class DctermsHasVersion(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["hasVersion"]
    class_class_curie: ClassVar[str] = "dct:hasVersion"
    class_name: ClassVar[str] = "DctermsHasVersion"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsHasVersion


class DctermsIsReplacedBy(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["isReplacedBy"]
    class_class_curie: ClassVar[str] = "dct:isReplacedBy"
    class_name: ClassVar[str] = "DctermsIsReplacedBy"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsIsReplacedBy


class DctermsReplaces(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["replaces"]
    class_class_curie: ClassVar[str] = "dct:replaces"
    class_name: ClassVar[str] = "DctermsReplaces"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsReplaces


class DctermsIsRequiredBy(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["isRequiredBy"]
    class_class_curie: ClassVar[str] = "dct:isRequiredBy"
    class_name: ClassVar[str] = "DctermsIsRequiredBy"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsIsRequiredBy


class DctermsRequires(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["requires"]
    class_class_curie: ClassVar[str] = "dct:requires"
    class_name: ClassVar[str] = "DctermsRequires"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsRequires


class DctermsIsPartOf(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["isPartOf"]
    class_class_curie: ClassVar[str] = "dct:isPartOf"
    class_name: ClassVar[str] = "DctermsIsPartOf"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsIsPartOf


class DctermsHasPart(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["hasPart"]
    class_class_curie: ClassVar[str] = "dct:hasPart"
    class_name: ClassVar[str] = "DctermsHasPart"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsHasPart


class DctermsIsReferencedBy(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["isReferencedBy"]
    class_class_curie: ClassVar[str] = "dct:isReferencedBy"
    class_name: ClassVar[str] = "DctermsIsReferencedBy"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsIsReferencedBy


class DctermsReferences(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["references"]
    class_class_curie: ClassVar[str] = "dct:references"
    class_name: ClassVar[str] = "DctermsReferences"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsReferences


class DctermsIsFormatOf(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["isFormatOf"]
    class_class_curie: ClassVar[str] = "dct:isFormatOf"
    class_name: ClassVar[str] = "DctermsIsFormatOf"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsIsFormatOf


class DctermsHasFormat(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["hasFormat"]
    class_class_curie: ClassVar[str] = "dct:hasFormat"
    class_name: ClassVar[str] = "DctermsHasFormat"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsHasFormat


class DctermsConformsTo(DctermsRelation):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["conformsTo"]
    class_class_curie: ClassVar[str] = "dct:conformsTo"
    class_name: ClassVar[str] = "DctermsConformsTo"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsConformsTo


class DctermsSpatial(DctermsCoverage):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["spatial"]
    class_class_curie: ClassVar[str] = "dct:spatial"
    class_name: ClassVar[str] = "DctermsSpatial"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsSpatial


class DctermsTemporal(DctermsCoverage):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["temporal"]
    class_class_curie: ClassVar[str] = "dct:temporal"
    class_name: ClassVar[str] = "DctermsTemporal"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsTemporal


class DctermsAudience(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["audience"]
    class_class_curie: ClassVar[str] = "dct:audience"
    class_name: ClassVar[str] = "DctermsAudience"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsAudience


class DctermsAccrualMethod(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["accrualMethod"]
    class_class_curie: ClassVar[str] = "dct:accrualMethod"
    class_name: ClassVar[str] = "DctermsAccrualMethod"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsAccrualMethod


class DctermsAccrualPeriodicity(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["accrualPeriodicity"]
    class_class_curie: ClassVar[str] = "dct:accrualPeriodicity"
    class_name: ClassVar[str] = "DctermsAccrualPeriodicity"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsAccrualPeriodicity


class DctermsAccrualPolicy(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["accrualPolicy"]
    class_class_curie: ClassVar[str] = "dct:accrualPolicy"
    class_name: ClassVar[str] = "DctermsAccrualPolicy"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsAccrualPolicy


class DctermsInstructionalMethod(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["instructionalMethod"]
    class_class_curie: ClassVar[str] = "dct:instructionalMethod"
    class_name: ClassVar[str] = "DctermsInstructionalMethod"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsInstructionalMethod


class DctermsProvenance(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["provenance"]
    class_class_curie: ClassVar[str] = "dct:provenance"
    class_name: ClassVar[str] = "DctermsProvenance"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsProvenance


class DctermsRightsHolder(DcAny):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["rightsHolder"]
    class_class_curie: ClassVar[str] = "dct:rightsHolder"
    class_name: ClassVar[str] = "DctermsRightsHolder"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsRightsHolder


class DctermsMediator(DctermsAudience):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["mediator"]
    class_class_curie: ClassVar[str] = "dct:mediator"
    class_name: ClassVar[str] = "DctermsMediator"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsMediator


class DctermsEducationLevel(DctermsAudience):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["educationLevel"]
    class_class_curie: ClassVar[str] = "dct:educationLevel"
    class_name: ClassVar[str] = "DctermsEducationLevel"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsEducationLevel


class DctermsAccessRights(DctermsRights):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["accessRights"]
    class_class_curie: ClassVar[str] = "dct:accessRights"
    class_name: ClassVar[str] = "DctermsAccessRights"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsAccessRights


class DctermsLicense(DctermsRights):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["license"]
    class_class_curie: ClassVar[str] = "dct:license"
    class_name: ClassVar[str] = "DctermsLicense"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsLicense


class DctermsBibliographicCitation(DctermsIdentifier):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["bibliographicCitation"]
    class_class_curie: ClassVar[str] = "dct:bibliographicCitation"
    class_name: ClassVar[str] = "DctermsBibliographicCitation"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsBibliographicCitation


class DctermsElementsAndRefinementsGroup(YAMLRoot):
    """
    This group is included as a convenience for schema authors who need to refer to all the DC elements and element
    refinements in the http://purl.org/dc/elements/1.1/ and http://purl.org/dc/terms namespaces. N.B. Refinements
    available via substitution groups.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCT["elementsAndRefinementsGroup"]
    class_class_curie: ClassVar[str] = "dct:elementsAndRefinementsGroup"
    class_name: ClassVar[str] = "DctermsElementsAndRefinementsGroup"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.DctermsElementsAndRefinementsGroup


@dataclass(repr=False)
class XmlSpecialAttrs(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XML["specialAttrs"]
    class_class_curie: ClassVar[str] = "xml:specialAttrs"
    class_name: ClassVar[str] = "XmlSpecialAttrs"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.XmlSpecialAttrs

    base: Optional[str] = None
    lang: Optional[str] = None
    space: Optional[str] = None
    id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.base is not None and not isinstance(self.base, str):
            self.base = str(self.base)

        if self.lang is not None and not isinstance(self.lang, str):
            self.lang = str(self.lang)

        if self.space is not None and not isinstance(self.space, str):
            self.space = str(self.space)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XmlGlobalAttributes(YAMLRoot):
    """
    Container for the global <xs:attribute> declarations defined in xml.xsd. Each attribute here is referenceable from
    other XSDs via ``ref="xml:<name>"``.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = XML["GlobalAttributes"]
    class_class_curie: ClassVar[str] = "xml:GlobalAttributes"
    class_name: ClassVar[str] = "XmlGlobalAttributes"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.XmlGlobalAttributes

    lang: Optional[Union[str, XmlLangType]] = None
    space: Optional[Union[str, "XmlSpaceType"]] = None
    base: Optional[Union[str, URI]] = None
    id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.lang is not None and not isinstance(self.lang, XmlLangType):
            self.lang = XmlLangType(self.lang)

        if self.space is not None and not isinstance(self.space, XmlSpaceType):
            self.space = XmlSpaceType(self.space)

        if self.base is not None and not isinstance(self.base, URI):
            self.base = URI(self.base)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class CatComponentType(EnumDefinitionImpl):

    Field = PermissibleValue(text="Field")
    Message = PermissibleValue(text="Message")

    _defn = EnumDefinition(
        name="CatComponentType",
    )

class CatIncludeFile(EnumDefinitionImpl):

    components = PermissibleValue(text="components")
    fields = PermissibleValue(text="fields")

    _defn = EnumDefinition(
        name="CatIncludeFile",
    )

class ChangeType(EnumDefinitionImpl):

    Editorial = PermissibleValue(text="Editorial")
    Definitional = PermissibleValue(text="Definitional")

    _defn = EnumDefinition(
        name="ChangeType",
    )

class DatatypeStandardEnum(EnumDefinitionImpl):

    ISO11404 = PermissibleValue(
        text="ISO11404",
        description="General Purpose Datatypes")
    GPB = PermissibleValue(
        text="GPB",
        description="Google Protocol Buffers")
    JSON = PermissibleValue(
        text="JSON",
        description="JSON Schema")
    SBE = PermissibleValue(
        text="SBE",
        description="Simple Binary Encoding")
    XML = PermissibleValue(
        text="XML",
        description="XML Schema and FIXML")
    TAG_VALUE = PermissibleValue(
        text="TAG_VALUE",
        description="FIX classic encoding")

    _defn = EnumDefinition(
        name="DatatypeStandardEnum",
    )

class MemberType(EnumDefinitionImpl):

    oneOf = PermissibleValue(
        text="oneOf",
        description="Members are mutually exclusive; exactly one must be present.")
    anyOf = PermissibleValue(
        text="anyOf",
        description="At least one of the members must be present.")

    _defn = EnumDefinition(
        name="MemberType",
    )

class Presence(EnumDefinitionImpl):

    optional = PermissibleValue(
        text="optional",
        description="The field or component MAY be present; it may be conditionally required based on a rule.")
    required = PermissibleValue(
        text="required",
        description="The field or component MUST be present.")
    forbidden = PermissibleValue(
        text="forbidden",
        description="The field or component MUST NOT be present.")
    ignored = PermissibleValue(
        text="ignored",
        description="The field or component MAY be present but is not validated.")
    constant = PermissibleValue(
        text="constant",
        description="The field has a constant value; in some encodings it need not be sent on the wire.")

    _defn = EnumDefinition(
        name="Presence",
    )

class PurposeEnum(EnumDefinitionImpl):
    """
    Recommended annotation purposes
    """
    SYNOPSIS = PermissibleValue(
        text="SYNOPSIS",
        description="""Brief summary of the element, typically highlighting its key function or purpose, restricted to one paragraph for conciseness.""")
    ELABORATION = PermissibleValue(
        text="ELABORATION",
        description="Detailed explanation of the element, clarifying its usage, functionality, or background.")
    EXAMPLE = PermissibleValue(
        text="EXAMPLE",
        description="Sample or illustration demonstrating how the element is used in practice.")
    DISPLAY = PermissibleValue(
        text="DISPLAY",
        description="For UI when different from canonical name; may have multi-language displays.")
    CAPTION = PermissibleValue(
        text="CAPTION",
        description="""Descriptive label or title for the element, may be used for tables, figures, headings or brief annotations.""")
    TOOLTIP = PermissibleValue(
        text="TOOLTIP",
        description="""Short message or hint that appears when hovering over the element, usually explaining its function or use.""")
    DEFINITION = PermissibleValue(
        text="DEFINITION",
        description="""Precise and formal explanation of the element, restricted to one sentence in length to ensure brevity.""")

    _defn = EnumDefinition(
        name="PurposeEnum",
        description="Recommended annotation purposes",
    )

class Reliability(EnumDefinitionImpl):
    """
    Message delivery gurantee
    """
    bestEffort = PermissibleValue(text="bestEffort")
    idempotent = PermissibleValue(text="idempotent")
    recoverable = PermissibleValue(text="recoverable")

    _defn = EnumDefinition(
        name="Reliability",
        description="Message delivery gurantee",
    )

class SupportType(EnumDefinitionImpl):
    """
    Support level
    """
    supported = PermissibleValue(text="supported")
    forbidden = PermissibleValue(text="forbidden")
    ignored = PermissibleValue(text="ignored")

    _defn = EnumDefinition(
        name="SupportType",
        description="Support level",
    )

class Synchronization(EnumDefinitionImpl):

    asynchronous = PermissibleValue(
        text="asynchronous",
        description="Event timing is completely independent")
    synchronous = PermissibleValue(
        text="synchronous",
        description="Requests in-progress block subsequent requests")
    pipelined = PermissibleValue(
        text="pipelined",
        description="Response timing is dependent on a request, but multiple requests can be in-flight")

    _defn = EnumDefinition(
        name="Synchronization",
    )

class TimerOperation(EnumDefinitionImpl):

    START = PermissibleValue(text="START")
    CANCEL = PermissibleValue(text="CANCEL")
    RESET = PermissibleValue(
        text="RESET",
        description="Cancel and restart")

    _defn = EnumDefinition(
        name="TimerOperation",
    )

class Unbounded(EnumDefinitionImpl):

    unbounded = PermissibleValue(text="unbounded")

    _defn = EnumDefinition(
        name="Unbounded",
    )

class UnionDataType(EnumDefinitionImpl):
    """
    A second domain of valid values. The 'Reserved' types should only be applied Code Sets.
    """
    Qty = PermissibleValue(text="Qty")
    Reserved100Plus = PermissibleValue(text="Reserved100Plus")
    Reserved1000Plus = PermissibleValue(text="Reserved1000Plus")
    Reserved4000Plus = PermissibleValue(text="Reserved4000Plus")
    Tenor = PermissibleValue(text="Tenor")

    _defn = EnumDefinition(
        name="UnionDataType",
        description="A second domain of valid values. The 'Reserved' types should only be applied Code Sets.",
    )

class Layer(EnumDefinitionImpl):

    application = PermissibleValue(text="application")
    presentation = PermissibleValue(text="presentation")
    session = PermissibleValue(text="session")
    transport = PermissibleValue(text="transport")

    _defn = EnumDefinition(
        name="Layer",
    )

class MessageCast(EnumDefinitionImpl):

    unicast = PermissibleValue(text="unicast")
    multicast = PermissibleValue(text="multicast")
    broadcast = PermissibleValue(text="broadcast")

    _defn = EnumDefinition(
        name="MessageCast",
    )

class ProtocolEnum(EnumDefinitionImpl):
    """
    List of FIX protocols to standardize spelling
    """
    FIX4 = PermissibleValue(
        text="FIX4",
        description="FIX 4.x session layer")
    FIXT = PermissibleValue(
        text="FIXT",
        description="FIX Transport Session Protocol")
    FIXP = PermissibleValue(
        text="FIXP",
        description="FIX Performance Session Layer")
    tagvalue = PermissibleValue(
        text="tagvalue",
        description="Tag Value encoding (classic FIX)")
    FIXML = PermissibleValue(
        text="FIXML",
        description="XML Schema")
    FAST = PermissibleValue(
        text="FAST",
        description="FIX Adapted for Streaming")
    SBE = PermissibleValue(
        text="SBE",
        description="Simple Binary Encoding")
    SOFH = PermissibleValue(
        text="SOFH",
        description="Simple Open Framing Header")
    GPB = PermissibleValue(
        text="GPB",
        description="Google Protocol Buffers")
    JSON = PermissibleValue(
        text="JSON",
        description="Javascript Object Notation")
    FIXS = PermissibleValue(
        text="FIXS",
        description="FIX over TLS security recommendation")

    _defn = EnumDefinition(
        name="ProtocolEnum",
        description="List of FIX protocols to standardize spelling",
    )

class InterfacePurposeEnum(EnumDefinitionImpl):
    """
    Recommended annotation purposes
    """
    SYNOPSIS = PermissibleValue(text="SYNOPSIS")
    ELABORATION = PermissibleValue(text="ELABORATION")
    EXAMPLE = PermissibleValue(text="EXAMPLE")
    DISPLAY = PermissibleValue(
        text="DISPLAY",
        description="For UI when different from canonical name; may have multi-language displays")

    _defn = EnumDefinition(
        name="InterfacePurposeEnum",
        description="Recommended annotation purposes",
    )

class InterfaceReliability(EnumDefinitionImpl):

    bestEffort = PermissibleValue(text="bestEffort")
    idempotent = PermissibleValue(text="idempotent")
    recoverable = PermissibleValue(text="recoverable")

    _defn = EnumDefinition(
        name="InterfaceReliability",
    )

class Role(EnumDefinitionImpl):

    initiator = PermissibleValue(text="initiator")
    acceptor = PermissibleValue(text="acceptor")
    client = PermissibleValue(text="client")
    server = PermissibleValue(text="server")

    _defn = EnumDefinition(
        name="Role",
    )

class TransportUseEnum(EnumDefinitionImpl):

    primary = PermissibleValue(text="primary")
    secondary = PermissibleValue(text="secondary")
    alternate = PermissibleValue(text="alternate")

    _defn = EnumDefinition(
        name="TransportUseEnum",
    )

class XmlSpaceType(EnumDefinitionImpl):
    """
    Anonymous simpleType for xml:space (from xml.xsd).
    """
    default = PermissibleValue(text="default")
    preserve = PermissibleValue(text="preserve")

    _defn = EnumDefinition(
        name="XmlSpaceType",
        description="Anonymous simpleType for xml:space (from xml.xsd).",
    )

# Slots
class slots:
    pass

slots.added = Slot(uri=FIXR.added, name="added", curie=FIXR.curie('added'),
                   model_uri=FIX_ORCHESTRA.added, domain=None, range=Optional[Union[str, Version]])

slots.added_ep = Slot(uri=FIXR.addedEP, name="added_ep", curie=FIXR.curie('addedEP'),
                   model_uri=FIX_ORCHESTRA.added_ep, domain=None, range=Optional[Union[int, EP]])

slots.change_type = Slot(uri=FIXR.changeType, name="change_type", curie=FIXR.curie('changeType'),
                   model_uri=FIX_ORCHESTRA.change_type, domain=None, range=Optional[Union[str, "ChangeType"]])

slots.deprecated_ep = Slot(uri=FIXR.deprecatedEP, name="deprecated_ep", curie=FIXR.curie('deprecatedEP'),
                   model_uri=FIX_ORCHESTRA.deprecated_ep, domain=None, range=Optional[Union[int, EP]])

slots.issue = Slot(uri=FIXR.issue, name="issue", curie=FIXR.curie('issue'),
                   model_uri=FIX_ORCHESTRA.issue, domain=None, range=Optional[str])

slots.last_modified = Slot(uri=FIXR.lastModified, name="last_modified", curie=FIXR.curie('lastModified'),
                   model_uri=FIX_ORCHESTRA.last_modified, domain=None, range=Optional[Union[str, Version]])

slots.replaced = Slot(uri=FIXR.replaced, name="replaced", curie=FIXR.curie('replaced'),
                   model_uri=FIX_ORCHESTRA.replaced, domain=None, range=Optional[Union[str, Version]])

slots.replaced_ep = Slot(uri=FIXR.replacedEP, name="replaced_ep", curie=FIXR.curie('replacedEP'),
                   model_uri=FIX_ORCHESTRA.replaced_ep, domain=None, range=Optional[Union[int, EP]])

slots.replaced_by_field = Slot(uri=FIXR.replacedByField, name="replaced_by_field", curie=FIXR.curie('replacedByField'),
                   model_uri=FIX_ORCHESTRA.replaced_by_field, domain=None, range=Optional[Union[int, Id]])

slots.supported = Slot(uri=FIXR.supported, name="supported", curie=FIXR.curie('supported'),
                   model_uri=FIX_ORCHESTRA.supported, domain=None, range=Optional[Union[str, "SupportType"]])

slots.updated = Slot(uri=FIXR.updated, name="updated", curie=FIXR.curie('updated'),
                   model_uri=FIX_ORCHESTRA.updated, domain=None, range=Optional[Union[str, Version]])

slots.updated_ep = Slot(uri=FIXR.updatedEP, name="updated_ep", curie=FIXR.curie('updatedEP'),
                   model_uri=FIX_ORCHESTRA.updated_ep, domain=None, range=Optional[Union[int, EP]])

slots.min_inclusive = Slot(uri=FIXR.minInclusive, name="min_inclusive", curie=FIXR.curie('minInclusive'),
                   model_uri=FIX_ORCHESTRA.min_inclusive, domain=None, range=Optional[str])

slots.max_inclusive = Slot(uri=FIXR.maxInclusive, name="max_inclusive", curie=FIXR.curie('maxInclusive'),
                   model_uri=FIX_ORCHESTRA.max_inclusive, domain=None, range=Optional[str])

slots.impl_length = Slot(uri=FIXR.implLength, name="impl_length", curie=FIXR.curie('implLength'),
                   model_uri=FIX_ORCHESTRA.impl_length, domain=None, range=Optional[int])

slots.impl_min_length = Slot(uri=FIXR.implMinLength, name="impl_min_length", curie=FIXR.curie('implMinLength'),
                   model_uri=FIX_ORCHESTRA.impl_min_length, domain=None, range=Optional[int])

slots.impl_max_length = Slot(uri=FIXR.implMaxLength, name="impl_max_length", curie=FIXR.curie('implMaxLength'),
                   model_uri=FIX_ORCHESTRA.impl_max_length, domain=None, range=Optional[int])

slots.presence = Slot(uri=FIXR.presence, name="presence", curie=FIXR.curie('presence'),
                   model_uri=FIX_ORCHESTRA.presence, domain=None, range=Optional[Union[str, "Presence"]])

slots.rendering = Slot(uri=FIXR.rendering, name="rendering", curie=FIXR.curie('rendering'),
                   model_uri=FIX_ORCHESTRA.rendering, domain=None, range=Optional[str])

slots.abbr_name = Slot(uri=FIXR.abbrName, name="abbr_name", curie=FIXR.curie('abbrName'),
                   model_uri=FIX_ORCHESTRA.abbr_name, domain=None, range=Optional[Union[str, Name]])

slots.scenario_id = Slot(uri=FIXR.scenarioId, name="scenario_id", curie=FIXR.curie('scenarioId'),
                   model_uri=FIX_ORCHESTRA.scenario_id, domain=None, range=Optional[Union[int, Id]])

slots.scenario_ref_id = Slot(uri=FIXR.scenarioRefId, name="scenario_ref_id", curie=FIXR.curie('scenarioRefId'),
                   model_uri=FIX_ORCHESTRA.scenario_ref_id, domain=None, range=Optional[Union[int, Id]])

slots.scenario_ref = Slot(uri=FIXR.scenarioRef, name="scenario_ref", curie=FIXR.curie('scenarioRef'),
                   model_uri=FIX_ORCHESTRA.scenario_ref, domain=None, range=Optional[Union[str, Name]])

slots.field = Slot(uri=FIXR.field, name="field", curie=FIXR.curie('field'),
                   model_uri=FIX_ORCHESTRA.field, domain=None, range=Optional[Union[Union[dict, FieldType], list[Union[dict, FieldType]]]])

slots.field_ref = Slot(uri=FIXR.fieldRef, name="field_ref", curie=FIXR.curie('fieldRef'),
                   model_uri=FIX_ORCHESTRA.field_ref, domain=None, range=Optional[Union[Union[dict, FieldRefType], list[Union[dict, FieldRefType]]]])

slots.component = Slot(uri=FIXR.component, name="component", curie=FIXR.curie('component'),
                   model_uri=FIX_ORCHESTRA.component, domain=None, range=Optional[Union[Union[dict, ComponentType], list[Union[dict, ComponentType]]]])

slots.component_ref = Slot(uri=FIXR.componentRef, name="component_ref", curie=FIXR.curie('componentRef'),
                   model_uri=FIX_ORCHESTRA.component_ref, domain=None, range=Optional[Union[Union[dict, ComponentRefType], list[Union[dict, ComponentRefType]]]])

slots.group_ref = Slot(uri=FIXR.groupRef, name="group_ref", curie=FIXR.curie('groupRef'),
                   model_uri=FIX_ORCHESTRA.group_ref, domain=None, range=Optional[Union[Union[dict, GroupRefType], list[Union[dict, GroupRefType]]]])

slots.message_ref = Slot(uri=FIXR.messageRef, name="message_ref", curie=FIXR.curie('messageRef'),
                   model_uri=FIX_ORCHESTRA.message_ref, domain=None, range=Optional[Union[Union[dict, MessageRefType], list[Union[dict, MessageRefType]]]])

slots.trigger = Slot(uri=FIXR.trigger, name="trigger", curie=FIXR.curie('trigger'),
                   model_uri=FIX_ORCHESTRA.trigger, domain=None, range=Optional[Union[Union[dict, TriggerType], list[Union[dict, TriggerType]]]])

slots.timer_schedule = Slot(uri=FIXR.timerSchedule, name="timer_schedule", curie=FIXR.curie('timerSchedule'),
                   model_uri=FIX_ORCHESTRA.timer_schedule, domain=None, range=Optional[Union[Union[dict, TimerSchedule], list[Union[dict, TimerSchedule]]]])

slots.states = Slot(uri=FIXR.states, name="states", curie=FIXR.curie('states'),
                   model_uri=FIX_ORCHESTRA.states, domain=None, range=Optional[Union[Union[dict, StateMachineType], list[Union[dict, StateMachineType]]]])

slots.timer = Slot(uri=FIXR.timer, name="timer", curie=FIXR.curie('timer'),
                   model_uri=FIX_ORCHESTRA.timer, domain=None, range=Optional[Union[Union[dict, TimerType], list[Union[dict, TimerType]]]])

slots.spec_url = Slot(uri=FIXR.specUrl, name="spec_url", curie=FIXR.curie('specUrl'),
                   model_uri=FIX_ORCHESTRA.spec_url, domain=None, range=Optional[Union[str, URI]])

slots.extra_attributes = Slot(uri=FIX_ORCHESTRA.extra_attributes, name="extra_attributes", curie=FIX_ORCHESTRA.curie('extra_attributes'),
                   model_uri=FIX_ORCHESTRA.extra_attributes, domain=None, range=Optional[Union[str, list[str]]])

slots.fixml_file_name = Slot(uri=FIXR.FIXMLFileName, name="fixml_file_name", curie=FIXR.curie('FIXMLFileName'),
                   model_uri=FIX_ORCHESTRA.fixml_file_name, domain=None, range=Optional[Union[str, Name]])

slots.component_type = Slot(uri=FIXR.componentType, name="component_type", curie=FIXR.curie('componentType'),
                   model_uri=FIX_ORCHESTRA.component_type, domain=None, range=Optional[Union[str, "CatComponentType"]])

slots.include_file = Slot(uri=FIXR.includeFile, name="include_file", curie=FIXR.curie('includeFile'),
                   model_uri=FIX_ORCHESTRA.include_file, domain=None, range=Optional[Union[str, "CatIncludeFile"]])

slots.code = Slot(uri=FIXR.code, name="code", curie=FIXR.curie('code'),
                   model_uri=FIX_ORCHESTRA.code, domain=None, range=Optional[Union[Union[dict, CodeType], list[Union[dict, CodeType]]]])

slots.default = Slot(uri=FIXR.default, name="default", curie=FIXR.curie('default'),
                   model_uri=FIX_ORCHESTRA.default, domain=None, range=Optional[str])

slots.union_data_type = Slot(uri=FIXR.unionDataType, name="union_data_type", curie=FIXR.curie('unionDataType'),
                   model_uri=FIX_ORCHESTRA.union_data_type, domain=None, range=Optional[Union[str, "UnionDataType"]])

slots.sort = Slot(uri=FIXR.sort, name="sort", curie=FIXR.curie('sort'),
                   model_uri=FIX_ORCHESTRA.sort, domain=None, range=Optional[int])

slots.block_assignment = Slot(uri=FIXR.blockAssignment, name="block_assignment", curie=FIXR.curie('blockAssignment'),
                   model_uri=FIX_ORCHESTRA.block_assignment, domain=None, range=Optional[Union[Union[dict, BlockAssignmentType], list[Union[dict, BlockAssignmentType]]]])

slots.when = Slot(uri=FIXR.when, name="when", curie=FIXR.curie('when'),
                   model_uri=FIX_ORCHESTRA.when, domain=None, range=Optional[Union[str, ExpressionType]])

slots.which = Slot(uri=FIXR.which, name="which", curie=FIXR.curie('which'),
                   model_uri=FIX_ORCHESTRA.which, domain=None, range=Optional[Union[str, "MemberType"]])

slots.length_id = Slot(uri=FIXR.lengthId, name="length_id", curie=FIXR.curie('lengthId'),
                   model_uri=FIX_ORCHESTRA.length_id, domain=None, range=Optional[Union[int, Id]])

slots.non_encoded_field_id = Slot(uri=FIXR.nonEncodedFieldId, name="non_encoded_field_id", curie=FIXR.curie('nonEncodedFieldId'),
                   model_uri=FIX_ORCHESTRA.non_encoded_field_id, domain=None, range=Optional[Union[int, Id]])

slots.unique = Slot(uri=FIXR.unique, name="unique", curie=FIXR.curie('unique'),
                   model_uri=FIX_ORCHESTRA.unique, domain=None, range=Optional[Union[dict, UniqueInline]])

slots.discriminator_id = Slot(uri=FIXR.discriminatorId, name="discriminator_id", curie=FIXR.curie('discriminatorId'),
                   model_uri=FIX_ORCHESTRA.discriminator_id, domain=None, range=Optional[Union[int, Id]])

slots.base_category = Slot(uri=FIXR.baseCategory, name="base_category", curie=FIXR.curie('baseCategory'),
                   model_uri=FIX_ORCHESTRA.base_category, domain=None, range=Optional[Union[str, Name]])

slots.base_category_abbr_name = Slot(uri=FIXR.baseCategoryAbbrName, name="base_category_abbr_name", curie=FIXR.curie('baseCategoryAbbrName'),
                   model_uri=FIX_ORCHESTRA.base_category_abbr_name, domain=None, range=Optional[Union[str, Name]])

slots.destination = Slot(uri=FIXR.destination, name="destination", curie=FIXR.curie('destination'),
                   model_uri=FIX_ORCHESTRA.destination, domain=None, range=str)

slots.impl_min_occurs = Slot(uri=FIXR.implMinOccurs, name="impl_min_occurs", curie=FIXR.curie('implMinOccurs'),
                   model_uri=FIX_ORCHESTRA.impl_min_occurs, domain=None, range=Optional[int])

slots.impl_max_occurs = Slot(uri=FIXR.implMaxOccurs, name="impl_max_occurs", curie=FIXR.curie('implMaxOccurs'),
                   model_uri=FIX_ORCHESTRA.impl_max_occurs, domain=None, range=Optional[Union[str, UnboundedIntType]])

slots.num_in_group = Slot(uri=FIXR.numInGroup, name="num_in_group", curie=FIXR.curie('numInGroup'),
                   model_uri=FIX_ORCHESTRA.num_in_group, domain=None, range=Optional[Union[dict, FieldRefType]])

slots.correlate = Slot(uri=FIXR.correlate, name="correlate", curie=FIXR.curie('correlate'),
                   model_uri=FIX_ORCHESTRA.correlate, domain=None, range=Optional[Union[Union[dict, IdentifierType], list[Union[dict, IdentifierType]]]])

slots.extension = Slot(uri=FIXR.extension, name="extension", curie=FIXR.curie('extension'),
                   model_uri=FIX_ORCHESTRA.extension, domain=None, range=Optional[Union[dict, ExtensionInline]])

slots.standard = Slot(uri=FIXR.standard, name="standard", curie=FIXR.curie('standard'),
                   model_uri=FIX_ORCHESTRA.standard, domain=None, range=Union[str, DatatypeStandard])

slots.builtin = Slot(uri=FIXR.builtin, name="builtin", curie=FIXR.curie('builtin'),
                   model_uri=FIX_ORCHESTRA.builtin, domain=None, range=Optional[Union[bool, Bool]])

slots.pattern = Slot(uri=FIXR.pattern, name="pattern", curie=FIXR.curie('pattern'),
                   model_uri=FIX_ORCHESTRA.pattern, domain=None, range=Optional[str])

slots.element = Slot(uri=FIXR.element, name="element", curie=FIXR.curie('element'),
                   model_uri=FIX_ORCHESTRA.element, domain=None, range=Optional[str])

slots.size = Slot(uri=FIXR.size, name="size", curie=FIXR.curie('size'),
                   model_uri=FIX_ORCHESTRA.size, domain=None, range=Optional[int])

slots.parameter = Slot(uri=FIXR.parameter, name="parameter", curie=FIXR.curie('parameter'),
                   model_uri=FIX_ORCHESTRA.parameter, domain=None, range=Optional[str])

slots.identifiers = Slot(uri=FIXR.identifiers, name="identifiers", curie=FIXR.curie('identifiers'),
                   model_uri=FIX_ORCHESTRA.identifiers, domain=None, range=Optional[Union[dict, IdentifiersType]])

slots.msg_type = Slot(uri=FIXR.msgType, name="msg_type", curie=FIXR.curie('msgType'),
                   model_uri=FIX_ORCHESTRA.msg_type, domain=None, range=Optional[Union[str, MsgType]])

slots.response = Slot(uri=FIXR.response, name="response", curie=FIXR.curie('response'),
                   model_uri=FIX_ORCHESTRA.response, domain=None, range=Union[Union[dict, ResponseType], list[Union[dict, ResponseType]]])

slots.structure = Slot(uri=FIXR.structure, name="structure", curie=FIXR.curie('structure'),
                   model_uri=FIX_ORCHESTRA.structure, domain=None, range=Optional[Union[dict, StructureInline]])

slots.responses = Slot(uri=FIXR.responses, name="responses", curie=FIXR.curie('responses'),
                   model_uri=FIX_ORCHESTRA.responses, domain=None, range=Optional[Union[dict, ResponsesInline]])

slots.sync = Slot(uri=FIXR.sync, name="sync", curie=FIXR.curie('sync'),
                   model_uri=FIX_ORCHESTRA.sync, domain=None, range=Optional[Union[str, "Synchronization"]])

slots.display_order = Slot(uri=FIXR.displayOrder, name="display_order", curie=FIXR.curie('displayOrder'),
                   model_uri=FIX_ORCHESTRA.display_order, domain=None, range=Optional[int])

slots.initial = Slot(uri=FIXR.initial, name="initial", curie=FIXR.curie('initial'),
                   model_uri=FIX_ORCHESTRA.initial, domain=None, range=Union[dict, StateType])

slots.state = Slot(uri=FIXR.state, name="state", curie=FIXR.curie('state'),
                   model_uri=FIX_ORCHESTRA.state, domain=None, range=Union[Union[dict, StateType], list[Union[dict, StateType]]])

slots.transition = Slot(uri=FIXR.transition, name="transition", curie=FIXR.curie('transition'),
                   model_uri=FIX_ORCHESTRA.transition, domain=None, range=Optional[Union[Union[dict, TransitionType], list[Union[dict, TransitionType]]]])

slots.onentry = Slot(uri=FIXR.onentry, name="onentry", curie=FIXR.curie('onentry'),
                   model_uri=FIX_ORCHESTRA.onentry, domain=None, range=Optional[Union[dict, ActionType]])

slots.activity = Slot(uri=FIXR.activity, name="activity", curie=FIXR.curie('activity'),
                   model_uri=FIX_ORCHESTRA.activity, domain=None, range=Optional[Union[dict, ActionType]])

slots.onexit = Slot(uri=FIXR.onexit, name="onexit", curie=FIXR.curie('onexit'),
                   model_uri=FIX_ORCHESTRA.onexit, domain=None, range=Optional[Union[dict, ActionType]])

slots.operation = Slot(uri=FIXR.operation, name="operation", curie=FIXR.curie('operation'),
                   model_uri=FIX_ORCHESTRA.operation, domain=None, range=Union[str, "TimerOperation"])

slots.interval = Slot(uri=FIXR.interval, name="interval", curie=FIXR.curie('interval'),
                   model_uri=FIX_ORCHESTRA.interval, domain=None, range=Optional[str])

slots.target = Slot(uri=FIXR.target, name="target", curie=FIXR.curie('target'),
                   model_uri=FIX_ORCHESTRA.target, domain=None, range=str)

slots.state_machine = Slot(uri=FIXR.stateMachine, name="state_machine", curie=FIXR.curie('stateMachine'),
                   model_uri=FIX_ORCHESTRA.state_machine, domain=None, range=str)

slots.service = Slot(uri=FIXI.service, name="service", curie=FIXI.curie('service'),
                   model_uri=FIX_ORCHESTRA.service, domain=None, range=Optional[Union[Union[dict, ServiceType], list[Union[dict, ServiceType]]]])

slots.user_interface = Slot(uri=FIXI.userInterface, name="user_interface", curie=FIXI.curie('userInterface'),
                   model_uri=FIX_ORCHESTRA.user_interface, domain=None, range=Optional[Union[Union[dict, UserInterfaceType], list[Union[dict, UserInterfaceType]]]])

slots.session_protocol = Slot(uri=FIXI.sessionProtocol, name="session_protocol", curie=FIXI.curie('sessionProtocol'),
                   model_uri=FIX_ORCHESTRA.session_protocol, domain=None, range=Optional[Union[Union[dict, SessionProtocolType], list[Union[dict, SessionProtocolType]]]])

slots.protocol = Slot(uri=FIXI.protocol, name="protocol", curie=FIXI.curie('protocol'),
                   model_uri=FIX_ORCHESTRA.protocol, domain=None, range=Optional[Union[Union[dict, ProtocolType], list[Union[dict, ProtocolType]]]])

slots.transport = Slot(uri=FIXI.transport, name="transport", curie=FIXI.curie('transport'),
                   model_uri=FIX_ORCHESTRA.transport, domain=None, range=Optional[Union[Union[dict, TransportProtocolType], list[Union[dict, TransportProtocolType]]]])

slots.session = Slot(uri=FIXI.session, name="session", curie=FIXI.curie('session'),
                   model_uri=FIX_ORCHESTRA.session, domain=None, range=Union[Union[dict, SessionType], list[Union[dict, SessionType]]])

slots.sessions = Slot(uri=FIXI.sessions, name="sessions", curie=FIXI.curie('sessions'),
                   model_uri=FIX_ORCHESTRA.sessions, domain=None, range=Optional[Union[dict, SessionsInline]])

slots.activation_time = Slot(uri=FIXI.activationTime, name="activation_time", curie=FIXI.curie('activationTime'),
                   model_uri=FIX_ORCHESTRA.activation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.deactivation_time = Slot(uri=FIXI.deactivationTime, name="deactivation_time", curie=FIXI.curie('deactivationTime'),
                   model_uri=FIX_ORCHESTRA.deactivation_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.layer = Slot(uri=FIXI.layer, name="layer", curie=FIXI.curie('layer'),
                   model_uri=FIX_ORCHESTRA.layer, domain=None, range=Optional[Union[str, "Layer"]])

slots.orchestration = Slot(uri=FIXI.orchestration, name="orchestration", curie=FIXI.curie('orchestration'),
                   model_uri=FIX_ORCHESTRA.orchestration, domain=None, range=Optional[Union[str, URI]])

slots.role = Slot(uri=FIXI.role, name="role", curie=FIXI.curie('role'),
                   model_uri=FIX_ORCHESTRA.role, domain=None, range=Optional[Union[str, "Role"]])

slots.security_keys = Slot(uri=FIXI.securityKeys, name="security_keys", curie=FIXI.curie('securityKeys'),
                   model_uri=FIX_ORCHESTRA.security_keys, domain=None, range=Optional[str])

slots.address = Slot(uri=FIXI.address, name="address", curie=FIXI.curie('address'),
                   model_uri=FIX_ORCHESTRA.address, domain=None, range=Optional[str])

slots.message_cast = Slot(uri=FIXI.messageCast, name="message_cast", curie=FIXI.curie('messageCast'),
                   model_uri=FIX_ORCHESTRA.message_cast, domain=None, range=Optional[Union[str, "MessageCast"]])

slots.use = Slot(uri=FIXI.use, name="use", curie=FIXI.curie('use'),
                   model_uri=FIX_ORCHESTRA.use, domain=None, range=Optional[Union[str, TransportUse]])

slots.mapped_datatype = Slot(uri=FIXR.mappedDatatype, name="mapped_datatype", curie=FIXR.curie('mappedDatatype'),
                   model_uri=FIX_ORCHESTRA.mapped_datatype, domain=None, range=Optional[Union[Union[dict, MappedDatatype], list[Union[dict, MappedDatatype]]]])

slots.base_type = Slot(uri=FIXR.baseType, name="base_type", curie=FIXR.curie('baseType'),
                   model_uri=FIX_ORCHESTRA.base_type, domain=None, range=Optional[Union[str, Name]])

slots.concept = Slot(uri=FIXR.concept, name="concept", curie=FIXR.curie('concept'),
                   model_uri=FIX_ORCHESTRA.concept, domain=None, range=Optional[Union[Union[dict, ConceptType], list[Union[dict, ConceptType]]]])

slots.datatype = Slot(uri=FIXR.datatype, name="datatype", curie=FIXR.curie('datatype'),
                   model_uri=FIX_ORCHESTRA.datatype, domain=None, range=Optional[Union[Union[dict, Datatype], list[Union[dict, Datatype]]]])

slots.message = Slot(uri=FIXR.message, name="message", curie=FIXR.curie('message'),
                   model_uri=FIX_ORCHESTRA.message, domain=None, range=Optional[Union[Union[dict, MessageType], list[Union[dict, MessageType]]]])

slots.metadata = Slot(uri=FIXR.metadata, name="metadata", curie=FIXR.curie('metadata'),
                   model_uri=FIX_ORCHESTRA.metadata, domain=None, range=Union[dict, DctermsElementOrRefinementContainer])

slots.categories = Slot(uri=FIXR.categories, name="categories", curie=FIXR.curie('categories'),
                   model_uri=FIX_ORCHESTRA.categories, domain=None, range=Optional[Union[dict, Categories]])

slots.sections = Slot(uri=FIXR.sections, name="sections", curie=FIXR.curie('sections'),
                   model_uri=FIX_ORCHESTRA.sections, domain=None, range=Optional[Union[dict, Sections]])

slots.datatypes = Slot(uri=FIXR.datatypes, name="datatypes", curie=FIXR.curie('datatypes'),
                   model_uri=FIX_ORCHESTRA.datatypes, domain=None, range=Union[dict, Datatypes])

slots.code_sets = Slot(uri=FIXR.codeSets, name="code_sets", curie=FIXR.curie('codeSets'),
                   model_uri=FIX_ORCHESTRA.code_sets, domain=None, range=Optional[Union[dict, CodeSets]])

slots.fields = Slot(uri=FIXR.fields, name="fields", curie=FIXR.curie('fields'),
                   model_uri=FIX_ORCHESTRA.fields, domain=None, range=Union[dict, Fields])

slots.actors = Slot(uri=FIXR.actors, name="actors", curie=FIXR.curie('actors'),
                   model_uri=FIX_ORCHESTRA.actors, domain=None, range=Optional[Union[dict, Actors]])

slots.components = Slot(uri=FIXR.components, name="components", curie=FIXR.curie('components'),
                   model_uri=FIX_ORCHESTRA.components, domain=None, range=Optional[Union[dict, Components]])

slots.groups = Slot(uri=FIXR.groups, name="groups", curie=FIXR.curie('groups'),
                   model_uri=FIX_ORCHESTRA.groups, domain=None, range=Optional[Union[dict, Groups]])

slots.messages = Slot(uri=FIXR.messages, name="messages", curie=FIXR.curie('messages'),
                   model_uri=FIX_ORCHESTRA.messages, domain=None, range=Union[dict, Messages])

slots.concepts = Slot(uri=FIXR.concepts, name="concepts", curie=FIXR.curie('concepts'),
                   model_uri=FIX_ORCHESTRA.concepts, domain=None, range=Optional[Union[dict, Concepts]])

slots.scenarios = Slot(uri=FIXR.scenarios, name="scenarios", curie=FIXR.curie('scenarios'),
                   model_uri=FIX_ORCHESTRA.scenarios, domain=None, range=Optional[Union[dict, Scenarios]])

slots.guid = Slot(uri=FIXR.guid, name="guid", curie=FIXR.curie('guid'),
                   model_uri=FIX_ORCHESTRA.guid, domain=None, range=Optional[str])

slots.namespace = Slot(uri=FIXR.namespace, name="namespace", curie=FIXR.curie('namespace'),
                   model_uri=FIX_ORCHESTRA.namespace, domain=None, range=Optional[Union[str, URI]])

slots.expression_language = Slot(uri=FIXR.expressionLanguage, name="expression_language", curie=FIXR.curie('expressionLanguage'),
                   model_uri=FIX_ORCHESTRA.expression_language, domain=None, range=Optional[str])

slots.interface = Slot(uri=FIXI.interface, name="interface", curie=FIXI.curie('interface'),
                   model_uri=FIX_ORCHESTRA.interface, domain=None, range=Optional[Union[Union[dict, InterfaceType], list[Union[dict, InterfaceType]]]])

slots.value = Slot(uri=FIX_ORCHESTRA.value, name="value", curie=FIX_ORCHESTRA.curie('value'),
                   model_uri=FIX_ORCHESTRA.value, domain=None, range=Optional[str])

slots.content = Slot(uri=FIX_ORCHESTRA.content, name="content", curie=FIX_ORCHESTRA.curie('content'),
                   model_uri=FIX_ORCHESTRA.content, domain=None, range=Optional[Union[str, list[str]]])

slots.title = Slot(uri=DCT.title, name="title", curie=DCT.curie('title'),
                   model_uri=FIX_ORCHESTRA.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=FIX_ORCHESTRA.description, domain=None, range=Optional[str])

slots.creator = Slot(uri=DCT.creator, name="creator", curie=DCT.curie('creator'),
                   model_uri=FIX_ORCHESTRA.creator, domain=None, range=Optional[str])

slots.rights = Slot(uri=DCT.rights, name="rights", curie=DCT.curie('rights'),
                   model_uri=FIX_ORCHESTRA.rights, domain=None, range=Optional[str])

slots.date = Slot(uri=DCT.date, name="date", curie=DCT.curie('date'),
                   model_uri=FIX_ORCHESTRA.date, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DCT.publisher, name="publisher", curie=DCT.curie('publisher'),
                   model_uri=FIX_ORCHESTRA.publisher, domain=None, range=Optional[str])

slots.subject = Slot(uri=DCT.subject, name="subject", curie=DCT.curie('subject'),
                   model_uri=FIX_ORCHESTRA.subject, domain=None, range=Optional[str])

slots.contributor = Slot(uri=DCT.contributor, name="contributor", curie=DCT.curie('contributor'),
                   model_uri=FIX_ORCHESTRA.contributor, domain=None, range=Optional[str])

slots.format = Slot(uri=DCT.format, name="format", curie=DCT.curie('format'),
                   model_uri=FIX_ORCHESTRA.format, domain=None, range=Optional[str])

slots.source = Slot(uri=DCT.source, name="source", curie=DCT.curie('source'),
                   model_uri=FIX_ORCHESTRA.source, domain=None, range=Optional[str])

slots.language = Slot(uri=DCT.language, name="language", curie=DCT.curie('language'),
                   model_uri=FIX_ORCHESTRA.language, domain=None, range=Optional[str])

slots.relation = Slot(uri=DCT.relation, name="relation", curie=DCT.curie('relation'),
                   model_uri=FIX_ORCHESTRA.relation, domain=None, range=Optional[str])

slots.coverage = Slot(uri=DCT.coverage, name="coverage", curie=DCT.curie('coverage'),
                   model_uri=FIX_ORCHESTRA.coverage, domain=None, range=Optional[str])

slots.alternative = Slot(uri=DCT.alternative, name="alternative", curie=DCT.curie('alternative'),
                   model_uri=FIX_ORCHESTRA.alternative, domain=None, range=Optional[str])

slots.table_of_contents = Slot(uri=DCT.tableOfContents, name="table_of_contents", curie=DCT.curie('tableOfContents'),
                   model_uri=FIX_ORCHESTRA.table_of_contents, domain=None, range=Optional[str])

slots.abstract = Slot(uri=DCT.abstract, name="abstract", curie=DCT.curie('abstract'),
                   model_uri=FIX_ORCHESTRA.abstract, domain=None, range=Optional[str])

slots.created = Slot(uri=DCT.created, name="created", curie=DCT.curie('created'),
                   model_uri=FIX_ORCHESTRA.created, domain=None, range=Optional[str])

slots.valid = Slot(uri=DCT.valid, name="valid", curie=DCT.curie('valid'),
                   model_uri=FIX_ORCHESTRA.valid, domain=None, range=Optional[str])

slots.available = Slot(uri=DCT.available, name="available", curie=DCT.curie('available'),
                   model_uri=FIX_ORCHESTRA.available, domain=None, range=Optional[str])

slots.issued = Slot(uri=DCT.issued, name="issued", curie=DCT.curie('issued'),
                   model_uri=FIX_ORCHESTRA.issued, domain=None, range=Optional[str])

slots.modified = Slot(uri=DCT.modified, name="modified", curie=DCT.curie('modified'),
                   model_uri=FIX_ORCHESTRA.modified, domain=None, range=Optional[str])

slots.date_accepted = Slot(uri=DCT.dateAccepted, name="date_accepted", curie=DCT.curie('dateAccepted'),
                   model_uri=FIX_ORCHESTRA.date_accepted, domain=None, range=Optional[str])

slots.date_copyrighted = Slot(uri=DCT.dateCopyrighted, name="date_copyrighted", curie=DCT.curie('dateCopyrighted'),
                   model_uri=FIX_ORCHESTRA.date_copyrighted, domain=None, range=Optional[str])

slots.date_submitted = Slot(uri=DCT.dateSubmitted, name="date_submitted", curie=DCT.curie('dateSubmitted'),
                   model_uri=FIX_ORCHESTRA.date_submitted, domain=None, range=Optional[str])

slots.extent = Slot(uri=DCT.extent, name="extent", curie=DCT.curie('extent'),
                   model_uri=FIX_ORCHESTRA.extent, domain=None, range=Optional[str])

slots.medium = Slot(uri=DCT.medium, name="medium", curie=DCT.curie('medium'),
                   model_uri=FIX_ORCHESTRA.medium, domain=None, range=Optional[str])

slots.is_version_of = Slot(uri=DCT.isVersionOf, name="is_version_of", curie=DCT.curie('isVersionOf'),
                   model_uri=FIX_ORCHESTRA.is_version_of, domain=None, range=Optional[str])

slots.has_version = Slot(uri=DCT.hasVersion, name="has_version", curie=DCT.curie('hasVersion'),
                   model_uri=FIX_ORCHESTRA.has_version, domain=None, range=Optional[str])

slots.is_replaced_by = Slot(uri=DCT.isReplacedBy, name="is_replaced_by", curie=DCT.curie('isReplacedBy'),
                   model_uri=FIX_ORCHESTRA.is_replaced_by, domain=None, range=Optional[str])

slots.replaces = Slot(uri=DCT.replaces, name="replaces", curie=DCT.curie('replaces'),
                   model_uri=FIX_ORCHESTRA.replaces, domain=None, range=Optional[str])

slots.is_required_by = Slot(uri=DCT.isRequiredBy, name="is_required_by", curie=DCT.curie('isRequiredBy'),
                   model_uri=FIX_ORCHESTRA.is_required_by, domain=None, range=Optional[str])

slots.requires = Slot(uri=DCT.requires, name="requires", curie=DCT.curie('requires'),
                   model_uri=FIX_ORCHESTRA.requires, domain=None, range=Optional[str])

slots.is_part_of = Slot(uri=DCT.isPartOf, name="is_part_of", curie=DCT.curie('isPartOf'),
                   model_uri=FIX_ORCHESTRA.is_part_of, domain=None, range=Optional[str])

slots.has_part = Slot(uri=DCT.hasPart, name="has_part", curie=DCT.curie('hasPart'),
                   model_uri=FIX_ORCHESTRA.has_part, domain=None, range=Optional[str])

slots.is_referenced_by = Slot(uri=DCT.isReferencedBy, name="is_referenced_by", curie=DCT.curie('isReferencedBy'),
                   model_uri=FIX_ORCHESTRA.is_referenced_by, domain=None, range=Optional[str])

slots.references = Slot(uri=DCT.references, name="references", curie=DCT.curie('references'),
                   model_uri=FIX_ORCHESTRA.references, domain=None, range=Optional[str])

slots.is_format_of = Slot(uri=DCT.isFormatOf, name="is_format_of", curie=DCT.curie('isFormatOf'),
                   model_uri=FIX_ORCHESTRA.is_format_of, domain=None, range=Optional[str])

slots.has_format = Slot(uri=DCT.hasFormat, name="has_format", curie=DCT.curie('hasFormat'),
                   model_uri=FIX_ORCHESTRA.has_format, domain=None, range=Optional[str])

slots.conforms_to = Slot(uri=DCT.conformsTo, name="conforms_to", curie=DCT.curie('conformsTo'),
                   model_uri=FIX_ORCHESTRA.conforms_to, domain=None, range=Optional[str])

slots.spatial = Slot(uri=DCT.spatial, name="spatial", curie=DCT.curie('spatial'),
                   model_uri=FIX_ORCHESTRA.spatial, domain=None, range=Optional[str])

slots.temporal = Slot(uri=DCT.temporal, name="temporal", curie=DCT.curie('temporal'),
                   model_uri=FIX_ORCHESTRA.temporal, domain=None, range=Optional[str])

slots.audience = Slot(uri=DCT.audience, name="audience", curie=DCT.curie('audience'),
                   model_uri=FIX_ORCHESTRA.audience, domain=None, range=Optional[str])

slots.accrual_method = Slot(uri=DCT.accrualMethod, name="accrual_method", curie=DCT.curie('accrualMethod'),
                   model_uri=FIX_ORCHESTRA.accrual_method, domain=None, range=Optional[str])

slots.accrual_periodicity = Slot(uri=DCT.accrualPeriodicity, name="accrual_periodicity", curie=DCT.curie('accrualPeriodicity'),
                   model_uri=FIX_ORCHESTRA.accrual_periodicity, domain=None, range=Optional[str])

slots.accrual_policy = Slot(uri=DCT.accrualPolicy, name="accrual_policy", curie=DCT.curie('accrualPolicy'),
                   model_uri=FIX_ORCHESTRA.accrual_policy, domain=None, range=Optional[str])

slots.instructional_method = Slot(uri=DCT.instructionalMethod, name="instructional_method", curie=DCT.curie('instructionalMethod'),
                   model_uri=FIX_ORCHESTRA.instructional_method, domain=None, range=Optional[str])

slots.provenance = Slot(uri=DCT.provenance, name="provenance", curie=DCT.curie('provenance'),
                   model_uri=FIX_ORCHESTRA.provenance, domain=None, range=Optional[str])

slots.rights_holder = Slot(uri=DCT.rightsHolder, name="rights_holder", curie=DCT.curie('rightsHolder'),
                   model_uri=FIX_ORCHESTRA.rights_holder, domain=None, range=Optional[str])

slots.mediator = Slot(uri=DCT.mediator, name="mediator", curie=DCT.curie('mediator'),
                   model_uri=FIX_ORCHESTRA.mediator, domain=None, range=Optional[str])

slots.education_level = Slot(uri=DCT.educationLevel, name="education_level", curie=DCT.curie('educationLevel'),
                   model_uri=FIX_ORCHESTRA.education_level, domain=None, range=Optional[str])

slots.access_rights = Slot(uri=DCT.accessRights, name="access_rights", curie=DCT.curie('accessRights'),
                   model_uri=FIX_ORCHESTRA.access_rights, domain=None, range=Optional[str])

slots.license = Slot(uri=DCT.license, name="license", curie=DCT.curie('license'),
                   model_uri=FIX_ORCHESTRA.license, domain=None, range=Optional[str])

slots.bibliographic_citation = Slot(uri=DCT.bibliographicCitation, name="bibliographic_citation", curie=DCT.curie('bibliographicCitation'),
                   model_uri=FIX_ORCHESTRA.bibliographic_citation, domain=None, range=Optional[str])

slots.entityAttribGrp__deprecated = Slot(uri=FIXR.deprecated, name="entityAttribGrp__deprecated", curie=FIXR.curie('deprecated'),
                   model_uri=FIX_ORCHESTRA.entityAttribGrp__deprecated, domain=None, range=Optional[Union[str, Version]])

slots.fieldAttribGrp__encoding = Slot(uri=FIXR.encoding, name="fieldAttribGrp__encoding", curie=FIXR.curie('encoding'),
                   model_uri=FIX_ORCHESTRA.fieldAttribGrp__encoding, domain=None, range=Optional[str])

slots.oidGrp__id = Slot(uri=FIXR.id, name="oidGrp__id", curie=FIXR.curie('id'),
                   model_uri=FIX_ORCHESTRA.oidGrp__id, domain=None, range=Union[int, Id])

slots.oidGrp__name = Slot(uri=FIXR.name, name="oidGrp__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.oidGrp__name, domain=None, range=Union[str, Name])

slots.oidGrp__scenario = Slot(uri=FIXR.scenario, name="oidGrp__scenario", curie=FIXR.curie('scenario'),
                   model_uri=FIX_ORCHESTRA.oidGrp__scenario, domain=None, range=Optional[Union[str, Name]])

slots.refidGrp__id = Slot(uri=FIXR.id, name="refidGrp__id", curie=FIXR.curie('id'),
                   model_uri=FIX_ORCHESTRA.refidGrp__id, domain=None, range=Union[int, Id])

slots.refidGrp__name = Slot(uri=FIXR.name, name="refidGrp__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.refidGrp__name, domain=None, range=Optional[Union[str, Name]])

slots.refidGrp__scenario = Slot(uri=FIXR.scenario, name="refidGrp__scenario", curie=FIXR.curie('scenario'),
                   model_uri=FIX_ORCHESTRA.refidGrp__scenario, domain=None, range=Optional[Union[str, Name]])

slots.actionType__group = Slot(uri=FIXR.group, name="actionType__group", curie=FIXR.curie('group'),
                   model_uri=FIX_ORCHESTRA.actionType__group, domain=None, range=Optional[Union[Union[dict, GroupType], list[Union[dict, GroupType]]]])

slots.actionType__assign = Slot(uri=FIXR.assign, name="actionType__assign", curie=FIXR.curie('assign'),
                   model_uri=FIX_ORCHESTRA.actionType__assign, domain=None, range=Optional[Union[Union[str, ExpressionType], list[Union[str, ExpressionType]]]])

slots.actorType__group = Slot(uri=FIXR.group, name="actorType__group", curie=FIXR.curie('group'),
                   model_uri=FIX_ORCHESTRA.actorType__group, domain=None, range=Optional[Union[Union[dict, GroupType], list[Union[dict, GroupType]]]])

slots.actorType__annotation = Slot(uri=FIXR.annotation, name="actorType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.actorType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.actorType__name = Slot(uri=FIXR.name, name="actorType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.actorType__name, domain=None, range=Union[str, Name])

slots.annotation__documentation = Slot(uri=FIXR.documentation, name="annotation__documentation", curie=FIXR.curie('documentation'),
                   model_uri=FIX_ORCHESTRA.annotation__documentation, domain=None, range=Optional[Union[Union[dict, Documentation], list[Union[dict, Documentation]]]])

slots.annotation__appinfo = Slot(uri=FIXR.appinfo, name="annotation__appinfo", curie=FIXR.curie('appinfo'),
                   model_uri=FIX_ORCHESTRA.annotation__appinfo, domain=None, range=Optional[Union[Union[dict, Appinfo], list[Union[dict, Appinfo]]]])

slots.appinfo__lang_id = Slot(uri=FIXR.langId, name="appinfo__lang_id", curie=FIXR.curie('langId'),
                   model_uri=FIX_ORCHESTRA.appinfo__lang_id, domain=None, range=Optional[Union[str, Language]])

slots.appinfo__purpose = Slot(uri=FIXR.purpose, name="appinfo__purpose", curie=FIXR.curie('purpose'),
                   model_uri=FIX_ORCHESTRA.appinfo__purpose, domain=None, range=Optional[Union[str, Purpose]])

slots.categoryType__annotation = Slot(uri=FIXR.annotation, name="categoryType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.categoryType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.categoryType__name = Slot(uri=FIXR.name, name="categoryType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.categoryType__name, domain=None, range=Union[str, Name])

slots.categoryType__section = Slot(uri=FIXR.section, name="categoryType__section", curie=FIXR.curie('section'),
                   model_uri=FIX_ORCHESTRA.categoryType__section, domain=None, range=Optional[Union[str, Name]])

slots.codeSetType__annotation = Slot(uri=FIXR.annotation, name="codeSetType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.codeSetType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.codeSetType__type = Slot(uri=FIXR.type, name="codeSetType__type", curie=FIXR.curie('type'),
                   model_uri=FIX_ORCHESTRA.codeSetType__type, domain=None, range=Union[str, Name])

slots.codeType__annotation = Slot(uri=FIXR.annotation, name="codeType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.codeType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.codeType__group = Slot(uri=FIXR.group, name="codeType__group", curie=FIXR.curie('group'),
                   model_uri=FIX_ORCHESTRA.codeType__group, domain=None, range=Optional[str])

slots.componentRefType__rule = Slot(uri=FIXR.rule, name="componentRefType__rule", curie=FIXR.curie('rule'),
                   model_uri=FIX_ORCHESTRA.componentRefType__rule, domain=None, range=Optional[Union[Union[dict, ComponentRuleType], list[Union[dict, ComponentRuleType]]]])

slots.componentRefType__annotation = Slot(uri=FIXR.annotation, name="componentRefType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.componentRefType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.componentRefType__instance_name = Slot(uri=FIXR.instanceName, name="componentRefType__instance_name", curie=FIXR.curie('instanceName'),
                   model_uri=FIX_ORCHESTRA.componentRefType__instance_name, domain=None, range=Optional[Union[str, ComponentName]])

slots.componentRuleType__name = Slot(uri=FIXR.name, name="componentRuleType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.componentRuleType__name, domain=None, range=Optional[Union[str, Name]])

slots.componentType__annotation = Slot(uri=FIXR.annotation, name="componentType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.componentType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.componentType__category = Slot(uri=FIXR.category, name="componentType__category", curie=FIXR.curie('category'),
                   model_uri=FIX_ORCHESTRA.componentType__category, domain=None, range=Optional[Union[str, Name]])

slots.conceptType__annotation = Slot(uri=FIXR.annotation, name="conceptType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.conceptType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.conceptType__name = Slot(uri=FIXR.name, name="conceptType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.conceptType__name, domain=None, range=Union[str, Name])

slots.documentation__lang_id = Slot(uri=FIXR.langId, name="documentation__lang_id", curie=FIXR.curie('langId'),
                   model_uri=FIX_ORCHESTRA.documentation__lang_id, domain=None, range=Optional[Union[str, Language]])

slots.documentation__purpose = Slot(uri=FIXR.purpose, name="documentation__purpose", curie=FIXR.curie('purpose'),
                   model_uri=FIX_ORCHESTRA.documentation__purpose, domain=None, range=Optional[Union[str, Purpose]])

slots.documentation__content_type = Slot(uri=FIXR.contentType, name="documentation__content_type", curie=FIXR.curie('contentType'),
                   model_uri=FIX_ORCHESTRA.documentation__content_type, domain=None, range=Optional[Union[str, Mime]])

slots.fieldRefType__rule = Slot(uri=FIXR.rule, name="fieldRefType__rule", curie=FIXR.curie('rule'),
                   model_uri=FIX_ORCHESTRA.fieldRefType__rule, domain=None, range=Optional[Union[Union[dict, FieldRuleType], list[Union[dict, FieldRuleType]]]])

slots.fieldRefType__assign = Slot(uri=FIXR.assign, name="fieldRefType__assign", curie=FIXR.curie('assign'),
                   model_uri=FIX_ORCHESTRA.fieldRefType__assign, domain=None, range=Optional[Union[str, ExpressionType]])

slots.fieldRefType__annotation = Slot(uri=FIXR.annotation, name="fieldRefType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.fieldRefType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.fieldRefType__instance_name = Slot(uri=FIXR.instanceName, name="fieldRefType__instance_name", curie=FIXR.curie('instanceName'),
                   model_uri=FIX_ORCHESTRA.fieldRefType__instance_name, domain=None, range=Optional[Union[str, Name]])

slots.fieldRuleType__assign = Slot(uri=FIXR.assign, name="fieldRuleType__assign", curie=FIXR.curie('assign'),
                   model_uri=FIX_ORCHESTRA.fieldRuleType__assign, domain=None, range=Optional[Union[Union[str, ExpressionType], list[Union[str, ExpressionType]]]])

slots.fieldRuleType__name = Slot(uri=FIXR.name, name="fieldRuleType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.fieldRuleType__name, domain=None, range=Optional[Union[str, Name]])

slots.fieldRuleType__type = Slot(uri=FIXR.type, name="fieldRuleType__type", curie=FIXR.curie('type'),
                   model_uri=FIX_ORCHESTRA.fieldRuleType__type, domain=None, range=Optional[Union[str, Name]])

slots.fieldType__rule = Slot(uri=FIXR.rule, name="fieldType__rule", curie=FIXR.curie('rule'),
                   model_uri=FIX_ORCHESTRA.fieldType__rule, domain=None, range=Optional[Union[Union[dict, FieldRuleType], list[Union[dict, FieldRuleType]]]])

slots.fieldType__assign = Slot(uri=FIXR.assign, name="fieldType__assign", curie=FIXR.curie('assign'),
                   model_uri=FIX_ORCHESTRA.fieldType__assign, domain=None, range=Optional[Union[str, ExpressionType]])

slots.fieldType__annotation = Slot(uri=FIXR.annotation, name="fieldType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.fieldType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.fieldType__type = Slot(uri=FIXR.type, name="fieldType__type", curie=FIXR.curie('type'),
                   model_uri=FIX_ORCHESTRA.fieldType__type, domain=None, range=Optional[Union[str, Name]])

slots.fieldType__code_set = Slot(uri=FIXR.codeSet, name="fieldType__code_set", curie=FIXR.curie('codeSet'),
                   model_uri=FIX_ORCHESTRA.fieldType__code_set, domain=None, range=Optional[Union[str, Name]])

slots.flowType__annotation = Slot(uri=FIXR.annotation, name="flowType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.flowType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.flowType__name = Slot(uri=FIXR.name, name="flowType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.flowType__name, domain=None, range=Union[str, Name])

slots.flowType__reliability = Slot(uri=FIXR.reliability, name="flowType__reliability", curie=FIXR.curie('reliability'),
                   model_uri=FIX_ORCHESTRA.flowType__reliability, domain=None, range=Optional[Union[str, "Reliability"]])

slots.groupType__annotation = Slot(uri=FIXR.annotation, name="groupType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.groupType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.groupType__category = Slot(uri=FIXR.category, name="groupType__category", curie=FIXR.curie('category'),
                   model_uri=FIX_ORCHESTRA.groupType__category, domain=None, range=Optional[Union[str, Name]])

slots.identifiersType__assign = Slot(uri=FIXR.assign, name="identifiersType__assign", curie=FIXR.curie('assign'),
                   model_uri=FIX_ORCHESTRA.identifiersType__assign, domain=None, range=Optional[Union[Union[dict, IdentifierType], list[Union[dict, IdentifierType]]]])

slots.identifiersType__annotation = Slot(uri=FIXR.annotation, name="identifiersType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.identifiersType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.identifierType__name = Slot(uri=FIXI.name, name="identifierType__name", curie=FIXI.curie('name'),
                   model_uri=FIX_ORCHESTRA.identifierType__name, domain=None, range=Optional[str])

slots.mappedDatatype__annotation = Slot(uri=FIXR.annotation, name="mappedDatatype__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.mappedDatatype__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.mappedDatatype__base = Slot(uri=FIXR.base, name="mappedDatatype__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.mappedDatatype__base, domain=None, range=Optional[str])

slots.messageType__annotation = Slot(uri=FIXR.annotation, name="messageType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.messageType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.messageType__category = Slot(uri=FIXR.category, name="messageType__category", curie=FIXR.curie('category'),
                   model_uri=FIX_ORCHESTRA.messageType__category, domain=None, range=Optional[Union[str, Name]])

slots.messageType__flow = Slot(uri=FIXR.flow, name="messageType__flow", curie=FIXR.curie('flow'),
                   model_uri=FIX_ORCHESTRA.messageType__flow, domain=None, range=Optional[Union[str, Name]])

slots.responseType__annotation = Slot(uri=FIXR.annotation, name="responseType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.responseType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.responseType__name = Slot(uri=FIXR.name, name="responseType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.responseType__name, domain=None, range=Optional[Union[str, Name]])

slots.scenarioType__annotation = Slot(uri=FIXR.annotation, name="scenarioType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.scenarioType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.scenarioType__id = Slot(uri=FIXR.id, name="scenarioType__id", curie=FIXR.curie('id'),
                   model_uri=FIX_ORCHESTRA.scenarioType__id, domain=None, range=Optional[Union[int, Id]])

slots.scenarioType__name = Slot(uri=FIXR.name, name="scenarioType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.scenarioType__name, domain=None, range=Optional[Union[str, Name]])

slots.sectionType__annotation = Slot(uri=FIXR.annotation, name="sectionType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.sectionType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.sectionType__name = Slot(uri=FIXR.name, name="sectionType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.sectionType__name, domain=None, range=Union[str, Name])

slots.stateMachineType__annotation = Slot(uri=FIXR.annotation, name="stateMachineType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.stateMachineType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.stateMachineType__name = Slot(uri=FIXR.name, name="stateMachineType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.stateMachineType__name, domain=None, range=Union[str, Name])

slots.stateType__annotation = Slot(uri=FIXR.annotation, name="stateType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.stateType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.stateType__name = Slot(uri=FIXR.name, name="stateType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.stateType__name, domain=None, range=Union[str, Name])

slots.timerSchedule__actor = Slot(uri=FIXR.actor, name="timerSchedule__actor", curie=FIXR.curie('actor'),
                   model_uri=FIX_ORCHESTRA.timerSchedule__actor, domain=None, range=Union[str, Name])

slots.timerSchedule__name = Slot(uri=FIXR.name, name="timerSchedule__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.timerSchedule__name, domain=None, range=Union[str, Name])

slots.timerType__name = Slot(uri=FIXR.name, name="timerType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.timerType__name, domain=None, range=Union[str, Name])

slots.transitionType__annotation = Slot(uri=FIXR.annotation, name="transitionType__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.transitionType__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.transitionType__name = Slot(uri=FIXR.name, name="transitionType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.transitionType__name, domain=None, range=Union[str, Name])

slots.triggerType__actor = Slot(uri=FIXR.actor, name="triggerType__actor", curie=FIXR.curie('actor'),
                   model_uri=FIX_ORCHESTRA.triggerType__actor, domain=None, range=Union[str, Name])

slots.triggerType__name = Slot(uri=FIXR.name, name="triggerType__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.triggerType__name, domain=None, range=Union[str, Name])

slots.interfaceAnnotation__documentation = Slot(uri=FIXI.documentation, name="interfaceAnnotation__documentation", curie=FIXI.curie('documentation'),
                   model_uri=FIX_ORCHESTRA.interfaceAnnotation__documentation, domain=None, range=Optional[Union[Union[dict, InterfaceDocumentation], list[Union[dict, InterfaceDocumentation]]]])

slots.interfaceAnnotation__appinfo = Slot(uri=FIXI.appinfo, name="interfaceAnnotation__appinfo", curie=FIXI.curie('appinfo'),
                   model_uri=FIX_ORCHESTRA.interfaceAnnotation__appinfo, domain=None, range=Optional[Union[Union[dict, InterfaceAppinfo], list[Union[dict, InterfaceAppinfo]]]])

slots.interfaceAppinfo__lang_id = Slot(uri=FIXI.langId, name="interfaceAppinfo__lang_id", curie=FIXI.curie('langId'),
                   model_uri=FIX_ORCHESTRA.interfaceAppinfo__lang_id, domain=None, range=Optional[str])

slots.interfaceAppinfo__purpose = Slot(uri=FIXI.purpose, name="interfaceAppinfo__purpose", curie=FIXI.curie('purpose'),
                   model_uri=FIX_ORCHESTRA.interfaceAppinfo__purpose, domain=None, range=Optional[Union[str, InterfacePurpose]])

slots.baseInterfaceType__encoding = Slot(uri=FIXI.encoding, name="baseInterfaceType__encoding", curie=FIXI.curie('encoding'),
                   model_uri=FIX_ORCHESTRA.baseInterfaceType__encoding, domain=None, range=Optional[Union[Union[dict, EncodingType], list[Union[dict, EncodingType]]]])

slots.baseInterfaceType__annotation = Slot(uri=FIXI.annotation, name="baseInterfaceType__annotation", curie=FIXI.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.baseInterfaceType__annotation, domain=None, range=Optional[Union[dict, InterfaceAnnotation]])

slots.baseInterfaceType__name = Slot(uri=FIXI.name, name="baseInterfaceType__name", curie=FIXI.curie('name'),
                   model_uri=FIX_ORCHESTRA.baseInterfaceType__name, domain=None, range=str)

slots.interfaceDocumentation__lang_id = Slot(uri=FIXI.langId, name="interfaceDocumentation__lang_id", curie=FIXI.curie('langId'),
                   model_uri=FIX_ORCHESTRA.interfaceDocumentation__lang_id, domain=None, range=Optional[str])

slots.interfaceDocumentation__purpose = Slot(uri=FIXI.purpose, name="interfaceDocumentation__purpose", curie=FIXI.curie('purpose'),
                   model_uri=FIX_ORCHESTRA.interfaceDocumentation__purpose, domain=None, range=Optional[Union[str, InterfacePurpose]])

slots.interfaceDocumentation__content_type = Slot(uri=FIXI.contentType, name="interfaceDocumentation__content_type", curie=FIXI.curie('contentType'),
                   model_uri=FIX_ORCHESTRA.interfaceDocumentation__content_type, domain=None, range=Optional[str])

slots.protocolType__annotation = Slot(uri=FIXI.annotation, name="protocolType__annotation", curie=FIXI.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.protocolType__annotation, domain=None, range=Optional[Union[dict, InterfaceAnnotation]])

slots.protocolType__name = Slot(uri=FIXI.name, name="protocolType__name", curie=FIXI.curie('name'),
                   model_uri=FIX_ORCHESTRA.protocolType__name, domain=None, range=Optional[Union[str, ProtocolName]])

slots.protocolType__version = Slot(uri=FIXI.version, name="protocolType__version", curie=FIXI.curie('version'),
                   model_uri=FIX_ORCHESTRA.protocolType__version, domain=None, range=Optional[str])

slots.protocolType__deprecated = Slot(uri=FIXI.deprecated, name="protocolType__deprecated", curie=FIXI.curie('deprecated'),
                   model_uri=FIX_ORCHESTRA.protocolType__deprecated, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.protocolType__reliability = Slot(uri=FIXI.reliability, name="protocolType__reliability", curie=FIXI.curie('reliability'),
                   model_uri=FIX_ORCHESTRA.protocolType__reliability, domain=None, range=Optional[Union[str, "InterfaceReliability"]])

slots.sessionType__identifier = Slot(uri=FIXI.identifier, name="sessionType__identifier", curie=FIXI.curie('identifier'),
                   model_uri=FIX_ORCHESTRA.sessionType__identifier, domain=None, range=Optional[Union[Union[dict, IdentifierType], list[Union[dict, IdentifierType]]]])

slots.datatype__annotation = Slot(uri=FIXR.annotation, name="datatype__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.datatype__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.datatype__name = Slot(uri=FIXR.name, name="datatype__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.datatype__name, domain=None, range=Union[str, Name])

slots.datatype__scenario = Slot(uri=FIXR.scenario, name="datatype__scenario", curie=FIXR.curie('scenario'),
                   model_uri=FIX_ORCHESTRA.datatype__scenario, domain=None, range=Optional[Union[str, Name]])

slots.actors__actor = Slot(uri=FIXR.actor, name="actors__actor", curie=FIXR.curie('actor'),
                   model_uri=FIX_ORCHESTRA.actors__actor, domain=None, range=Optional[Union[Union[dict, ActorType], list[Union[dict, ActorType]]]])

slots.actors__flow = Slot(uri=FIXR.flow, name="actors__flow", curie=FIXR.curie('flow'),
                   model_uri=FIX_ORCHESTRA.actors__flow, domain=None, range=Optional[Union[Union[dict, FlowType], list[Union[dict, FlowType]]]])

slots.actors__annotation = Slot(uri=FIXR.annotation, name="actors__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.actors__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.actors__base = Slot(uri=FIXR.base, name="actors__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.actors__base, domain=None, range=Optional[str])

slots.categories__category = Slot(uri=FIXR.category, name="categories__category", curie=FIXR.curie('category'),
                   model_uri=FIX_ORCHESTRA.categories__category, domain=None, range=Optional[Union[Union[dict, CategoryType], list[Union[dict, CategoryType]]]])

slots.categories__annotation = Slot(uri=FIXR.annotation, name="categories__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.categories__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.categories__base = Slot(uri=FIXR.base, name="categories__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.categories__base, domain=None, range=Optional[str])

slots.codeSets__code_set = Slot(uri=FIXR.codeSet, name="codeSets__code_set", curie=FIXR.curie('codeSet'),
                   model_uri=FIX_ORCHESTRA.codeSets__code_set, domain=None, range=Optional[Union[Union[dict, CodeSetType], list[Union[dict, CodeSetType]]]])

slots.codeSets__annotation = Slot(uri=FIXR.annotation, name="codeSets__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.codeSets__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.codeSets__base = Slot(uri=FIXR.base, name="codeSets__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.codeSets__base, domain=None, range=Optional[str])

slots.components__annotation = Slot(uri=FIXR.annotation, name="components__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.components__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.components__base = Slot(uri=FIXR.base, name="components__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.components__base, domain=None, range=Optional[str])

slots.concepts__annotation = Slot(uri=FIXR.annotation, name="concepts__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.concepts__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.concepts__base = Slot(uri=FIXR.base, name="concepts__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.concepts__base, domain=None, range=Optional[str])

slots.datatypes__annotation = Slot(uri=FIXR.annotation, name="datatypes__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.datatypes__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.datatypes__base = Slot(uri=FIXR.base, name="datatypes__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.datatypes__base, domain=None, range=Optional[str])

slots.fields__annotation = Slot(uri=FIXR.annotation, name="fields__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.fields__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.fields__base = Slot(uri=FIXR.base, name="fields__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.fields__base, domain=None, range=Optional[str])

slots.groups__group = Slot(uri=FIXR.group, name="groups__group", curie=FIXR.curie('group'),
                   model_uri=FIX_ORCHESTRA.groups__group, domain=None, range=Optional[Union[Union[dict, GroupType], list[Union[dict, GroupType]]]])

slots.groups__annotation = Slot(uri=FIXR.annotation, name="groups__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.groups__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.groups__base = Slot(uri=FIXR.base, name="groups__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.groups__base, domain=None, range=Optional[str])

slots.messages__annotation = Slot(uri=FIXR.annotation, name="messages__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.messages__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.messages__base = Slot(uri=FIXR.base, name="messages__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.messages__base, domain=None, range=Optional[str])

slots.repository__annotation = Slot(uri=FIXR.annotation, name="repository__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.repository__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.repository__name = Slot(uri=FIXR.name, name="repository__name", curie=FIXR.curie('name'),
                   model_uri=FIX_ORCHESTRA.repository__name, domain=None, range=str)

slots.repository__version = Slot(uri=FIXR.version, name="repository__version", curie=FIXR.curie('version'),
                   model_uri=FIX_ORCHESTRA.repository__version, domain=None, range=Union[str, Version])

slots.scenarios__scenario = Slot(uri=FIXR.scenario, name="scenarios__scenario", curie=FIXR.curie('scenario'),
                   model_uri=FIX_ORCHESTRA.scenarios__scenario, domain=None, range=Optional[Union[Union[dict, ScenarioType], list[Union[dict, ScenarioType]]]])

slots.scenarios__annotation = Slot(uri=FIXR.annotation, name="scenarios__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.scenarios__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.scenarios__base = Slot(uri=FIXR.base, name="scenarios__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.scenarios__base, domain=None, range=Optional[str])

slots.sections__section = Slot(uri=FIXR.section, name="sections__section", curie=FIXR.curie('section'),
                   model_uri=FIX_ORCHESTRA.sections__section, domain=None, range=Optional[Union[Union[dict, SectionType], list[Union[dict, SectionType]]]])

slots.sections__annotation = Slot(uri=FIXR.annotation, name="sections__annotation", curie=FIXR.curie('annotation'),
                   model_uri=FIX_ORCHESTRA.sections__annotation, domain=None, range=Optional[Union[dict, Annotation]])

slots.sections__base = Slot(uri=FIXR.base, name="sections__base", curie=FIXR.curie('base'),
                   model_uri=FIX_ORCHESTRA.sections__base, domain=None, range=Optional[str])

slots.dcSimpleLiteral__lang = Slot(uri=FIX_ORCHESTRA.lang, name="dcSimpleLiteral__lang", curie=FIX_ORCHESTRA.curie('lang'),
                   model_uri=FIX_ORCHESTRA.dcSimpleLiteral__lang, domain=None, range=Optional[str])

slots.dcElementContainer__type = Slot(uri=DCT.type, name="dcElementContainer__type", curie=DCT.curie('type'),
                   model_uri=FIX_ORCHESTRA.dcElementContainer__type, domain=None, range=Optional[str])

slots.dcElementContainer__identifier = Slot(uri=DCT.identifier, name="dcElementContainer__identifier", curie=DCT.curie('identifier'),
                   model_uri=FIX_ORCHESTRA.dcElementContainer__identifier, domain=None, range=Optional[str])

slots.dctermsElementOrRefinementContainer__type = Slot(uri=DCT.type, name="dctermsElementOrRefinementContainer__type", curie=DCT.curie('type'),
                   model_uri=FIX_ORCHESTRA.dctermsElementOrRefinementContainer__type, domain=None, range=Optional[str])

slots.dctermsElementOrRefinementContainer__identifier = Slot(uri=DCT.identifier, name="dctermsElementOrRefinementContainer__identifier", curie=DCT.curie('identifier'),
                   model_uri=FIX_ORCHESTRA.dctermsElementOrRefinementContainer__identifier, domain=None, range=Optional[str])

slots.xmlSpecialAttrs__base = Slot(uri=FIX_ORCHESTRA.base, name="xmlSpecialAttrs__base", curie=FIX_ORCHESTRA.curie('base'),
                   model_uri=FIX_ORCHESTRA.xmlSpecialAttrs__base, domain=None, range=Optional[str])

slots.xmlSpecialAttrs__lang = Slot(uri=FIX_ORCHESTRA.lang, name="xmlSpecialAttrs__lang", curie=FIX_ORCHESTRA.curie('lang'),
                   model_uri=FIX_ORCHESTRA.xmlSpecialAttrs__lang, domain=None, range=Optional[str])

slots.xmlSpecialAttrs__space = Slot(uri=FIX_ORCHESTRA.space, name="xmlSpecialAttrs__space", curie=FIX_ORCHESTRA.curie('space'),
                   model_uri=FIX_ORCHESTRA.xmlSpecialAttrs__space, domain=None, range=Optional[str])

slots.xmlSpecialAttrs__id = Slot(uri=FIX_ORCHESTRA.id, name="xmlSpecialAttrs__id", curie=FIX_ORCHESTRA.curie('id'),
                   model_uri=FIX_ORCHESTRA.xmlSpecialAttrs__id, domain=None, range=Optional[str])

slots.xmlGlobalAttributes__lang = Slot(uri=XML.lang, name="xmlGlobalAttributes__lang", curie=XML.curie('lang'),
                   model_uri=FIX_ORCHESTRA.xmlGlobalAttributes__lang, domain=None, range=Optional[Union[str, XmlLangType]])

slots.xmlGlobalAttributes__space = Slot(uri=XML.space, name="xmlGlobalAttributes__space", curie=XML.curie('space'),
                   model_uri=FIX_ORCHESTRA.xmlGlobalAttributes__space, domain=None, range=Optional[Union[str, "XmlSpaceType"]])

slots.xmlGlobalAttributes__base = Slot(uri=XML.base, name="xmlGlobalAttributes__base", curie=XML.curie('base'),
                   model_uri=FIX_ORCHESTRA.xmlGlobalAttributes__base, domain=None, range=Optional[Union[str, URI]])

slots.xmlGlobalAttributes__id = Slot(uri=XML.id, name="xmlGlobalAttributes__id", curie=XML.curie('id'),
                   model_uri=FIX_ORCHESTRA.xmlGlobalAttributes__id, domain=None, range=Optional[str])

slots.FieldAttribGrp_presence = Slot(uri=FIXR.presence, name="FieldAttribGrp_presence", curie=FIXR.curie('presence'),
                   model_uri=FIX_ORCHESTRA.FieldAttribGrp_presence, domain=None, range=Optional[Union[str, "Presence"]])

slots.FieldAttribGrp_value = Slot(uri=FIXR.value, name="FieldAttribGrp_value", curie=FIXR.curie('value'),
                   model_uri=FIX_ORCHESTRA.FieldAttribGrp_value, domain=None, range=Optional[str])

slots.ActionType_field_ref = Slot(uri=FIXR.fieldRef, name="ActionType_field_ref", curie=FIXR.curie('fieldRef'),
                   model_uri=FIX_ORCHESTRA.ActionType_field_ref, domain=ActionType, range=Optional[Union[Union[dict, "FieldRefType"], list[Union[dict, "FieldRefType"]]]])

slots.ActorType_field_ref = Slot(uri=FIXR.fieldRef, name="ActorType_field_ref", curie=FIXR.curie('fieldRef'),
                   model_uri=FIX_ORCHESTRA.ActorType_field_ref, domain=ActorType, range=Optional[Union[Union[dict, "FieldRefType"], list[Union[dict, "FieldRefType"]]]])

slots.BlockAssignmentType_field_ref = Slot(uri=FIXR.fieldRef, name="BlockAssignmentType_field_ref", curie=FIXR.curie('fieldRef'),
                   model_uri=FIX_ORCHESTRA.BlockAssignmentType_field_ref, domain=BlockAssignmentType, range=Optional[Union[Union[dict, "FieldRefType"], list[Union[dict, "FieldRefType"]]]])

slots.CodeSetType_spec_url = Slot(uri=FIXR.specUrl, name="CodeSetType_spec_url", curie=FIXR.curie('specUrl'),
                   model_uri=FIX_ORCHESTRA.CodeSetType_spec_url, domain=CodeSetType, range=Optional[Union[str, URI]])

slots.CodeType_value = Slot(uri=FIXR.value, name="CodeType_value", curie=FIXR.curie('value'),
                   model_uri=FIX_ORCHESTRA.CodeType_value, domain=CodeType, range=str)

slots.ComponentRefType_presence = Slot(uri=FIXR.presence, name="ComponentRefType_presence", curie=FIXR.curie('presence'),
                   model_uri=FIX_ORCHESTRA.ComponentRefType_presence, domain=ComponentRefType, range=Optional[Union[str, "Presence"]])

slots.ComponentRuleType_when = Slot(uri=FIXR.when, name="ComponentRuleType_when", curie=FIXR.curie('when'),
                   model_uri=FIX_ORCHESTRA.ComponentRuleType_when, domain=ComponentRuleType, range=Union[str, ExpressionType])

slots.ComponentRuleType_presence = Slot(uri=FIXR.presence, name="ComponentRuleType_presence", curie=FIXR.curie('presence'),
                   model_uri=FIX_ORCHESTRA.ComponentRuleType_presence, domain=ComponentRuleType, range=Optional[Union[str, "Presence"]])

slots.ComponentType_field_ref = Slot(uri=FIXR.fieldRef, name="ComponentType_field_ref", curie=FIXR.curie('fieldRef'),
                   model_uri=FIX_ORCHESTRA.ComponentType_field_ref, domain=ComponentType, range=Optional[Union[Union[dict, "FieldRefType"], list[Union[dict, "FieldRefType"]]]])

slots.ComponentType_which = Slot(uri=FIXR.which, name="ComponentType_which", curie=FIXR.curie('which'),
                   model_uri=FIX_ORCHESTRA.ComponentType_which, domain=ComponentType, range=Optional[Union[str, "MemberType"]])

slots.ConceptType_field_ref = Slot(uri=FIXR.fieldRef, name="ConceptType_field_ref", curie=FIXR.curie('fieldRef'),
                   model_uri=FIX_ORCHESTRA.ConceptType_field_ref, domain=ConceptType, range=Optional[Union[Union[dict, "FieldRefType"], list[Union[dict, "FieldRefType"]]]])

slots.ConceptType_message_ref = Slot(uri=FIXR.messageRef, name="ConceptType_message_ref", curie=FIXR.curie('messageRef'),
                   model_uri=FIX_ORCHESTRA.ConceptType_message_ref, domain=ConceptType, range=Optional[Union[Union[dict, "MessageRefType"], list[Union[dict, "MessageRefType"]]]])

slots.FieldRuleType_when = Slot(uri=FIXR.when, name="FieldRuleType_when", curie=FIXR.curie('when'),
                   model_uri=FIX_ORCHESTRA.FieldRuleType_when, domain=FieldRuleType, range=Union[str, ExpressionType])

slots.FlowType_source = Slot(uri=FIXR.source, name="FlowType_source", curie=FIXR.curie('source'),
                   model_uri=FIX_ORCHESTRA.FlowType_source, domain=FlowType, range=str)

slots.GroupRefType_impl_min_occurs = Slot(uri=FIXR.implMinOccurs, name="GroupRefType_impl_min_occurs", curie=FIXR.curie('implMinOccurs'),
                   model_uri=FIX_ORCHESTRA.GroupRefType_impl_min_occurs, domain=GroupRefType, range=Optional[int])

slots.GroupRefType_impl_max_occurs = Slot(uri=FIXR.implMaxOccurs, name="GroupRefType_impl_max_occurs", curie=FIXR.curie('implMaxOccurs'),
                   model_uri=FIX_ORCHESTRA.GroupRefType_impl_max_occurs, domain=GroupRefType, range=Optional[Union[str, UnboundedIntType]])

slots.GroupType_field_ref = Slot(uri=FIXR.fieldRef, name="GroupType_field_ref", curie=FIXR.curie('fieldRef'),
                   model_uri=FIX_ORCHESTRA.GroupType_field_ref, domain=GroupType, range=Optional[Union[Union[dict, FieldRefType], list[Union[dict, FieldRefType]]]])

slots.GroupType_impl_max_occurs = Slot(uri=FIXR.implMaxOccurs, name="GroupType_impl_max_occurs", curie=FIXR.curie('implMaxOccurs'),
                   model_uri=FIX_ORCHESTRA.GroupType_impl_max_occurs, domain=GroupType, range=Optional[Union[str, UnboundedIntType]])

slots.MappedDatatype_min_inclusive = Slot(uri=FIXR.minInclusive, name="MappedDatatype_min_inclusive", curie=FIXR.curie('minInclusive'),
                   model_uri=FIX_ORCHESTRA.MappedDatatype_min_inclusive, domain=MappedDatatype, range=Optional[str])

slots.MappedDatatype_max_inclusive = Slot(uri=FIXR.maxInclusive, name="MappedDatatype_max_inclusive", curie=FIXR.curie('maxInclusive'),
                   model_uri=FIX_ORCHESTRA.MappedDatatype_max_inclusive, domain=MappedDatatype, range=Optional[str])

slots.MessageRefType_impl_min_occurs = Slot(uri=FIXR.implMinOccurs, name="MessageRefType_impl_min_occurs", curie=FIXR.curie('implMinOccurs'),
                   model_uri=FIX_ORCHESTRA.MessageRefType_impl_min_occurs, domain=MessageRefType, range=Optional[int])

slots.MessageRefType_impl_max_occurs = Slot(uri=FIXR.implMaxOccurs, name="MessageRefType_impl_max_occurs", curie=FIXR.curie('implMaxOccurs'),
                   model_uri=FIX_ORCHESTRA.MessageRefType_impl_max_occurs, domain=MessageRefType, range=Optional[Union[str, UnboundedIntType]])

slots.StructureInline_field_ref = Slot(uri=FIXR.fieldRef, name="StructureInline_field_ref", curie=FIXR.curie('fieldRef'),
                   model_uri=FIX_ORCHESTRA.StructureInline_field_ref, domain=StructureInline, range=Optional[Union[Union[dict, FieldRefType], list[Union[dict, FieldRefType]]]])

slots.StructureInline_which = Slot(uri=FIXR.which, name="StructureInline_which", curie=FIXR.curie('which'),
                   model_uri=FIX_ORCHESTRA.StructureInline_which, domain=StructureInline, range=Optional[Union[str, "MemberType"]])

slots.ResponseType_when = Slot(uri=FIXR.when, name="ResponseType_when", curie=FIXR.curie('when'),
                   model_uri=FIX_ORCHESTRA.ResponseType_when, domain=ResponseType, range=Optional[Union[str, ExpressionType]])

slots.TimerSchedule_activity = Slot(uri=FIXR.activity, name="TimerSchedule_activity", curie=FIXR.curie('activity'),
                   model_uri=FIX_ORCHESTRA.TimerSchedule_activity, domain=TimerSchedule, range=Union[dict, ActionType])

slots.TransitionType_when = Slot(uri=FIXR.when, name="TransitionType_when", curie=FIXR.curie('when'),
                   model_uri=FIX_ORCHESTRA.TransitionType_when, domain=TransitionType, range=Optional[Union[str, ExpressionType]])

slots.InterfaceAppinfo_spec_url = Slot(uri=FIXI.specUrl, name="InterfaceAppinfo_spec_url", curie=FIXI.curie('specUrl'),
                   model_uri=FIX_ORCHESTRA.InterfaceAppinfo_spec_url, domain=InterfaceAppinfo, range=Optional[Union[str, URI]])

slots.SessionType_activation_time = Slot(uri=FIXI.activationTime, name="SessionType_activation_time", curie=FIXI.curie('activationTime'),
                   model_uri=FIX_ORCHESTRA.SessionType_activation_time, domain=SessionType, range=Optional[Union[str, XSDDateTime]])

slots.SessionType_deactivation_time = Slot(uri=FIXI.deactivationTime, name="SessionType_deactivation_time", curie=FIXI.curie('deactivationTime'),
                   model_uri=FIX_ORCHESTRA.SessionType_deactivation_time, domain=SessionType, range=Optional[Union[str, XSDDateTime]])

slots.Interfaces_metadata = Slot(uri=FIXI.metadata, name="Interfaces_metadata", curie=FIXI.curie('metadata'),
                   model_uri=FIX_ORCHESTRA.Interfaces_metadata, domain=Interfaces, range=Union[dict, "DctermsElementOrRefinementContainer"])
