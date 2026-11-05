# Auto generated from fix_orchestra.yaml by pythongen.py version: 0.0.1
# Schema: fix_orchestra
#
# id: https://w3id.org/lmodel/fix-orchestra
# description: A LinkML model of FIX Orchestra, the FIX Trading Community's standard for rules of engagement that a machine can read. It renders two editions from their XSDs, the v1.0 Technical Standard and the v1.1 third release candidate, so that an Orchestra repository or interfaces file of either edition converts to records that validate here.
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

from linkml_runtime.linkml_model.types import Boolean, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI

metamodel_version = "1.12.0"
version = "1.0, 1.1-rc3"

# Namespaces
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
FIX_ORCHESTRA = CurieNamespace('fix_orchestra', 'https://w3id.org/lmodel/fix-orchestra/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = FIX_ORCHESTRA


# Types

# Class references



@dataclass(repr=False)
class OrchestraMetadata(YAMLRoot):
    """
    The Dublin Core description at the top of a repository or interfaces file. Each key holds the values of one Dublin
    Core element or term.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMetadata"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMetadata"
    class_name: ClassVar[str] = "OrchestraMetadata"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMetadata

    dc_title: Optional[Union[str, list[str]]] = empty_list()
    dc_creator: Optional[Union[str, list[str]]] = empty_list()
    dc_subject: Optional[Union[str, list[str]]] = empty_list()
    dc_description: Optional[Union[str, list[str]]] = empty_list()
    dc_publisher: Optional[Union[str, list[str]]] = empty_list()
    dc_contributor: Optional[Union[str, list[str]]] = empty_list()
    dc_date: Optional[Union[str, list[str]]] = empty_list()
    dc_type: Optional[Union[str, list[str]]] = empty_list()
    dc_format: Optional[Union[str, list[str]]] = empty_list()
    dc_identifier: Optional[Union[str, list[str]]] = empty_list()
    dc_source: Optional[Union[str, list[str]]] = empty_list()
    dc_language: Optional[Union[str, list[str]]] = empty_list()
    dc_relation: Optional[Union[str, list[str]]] = empty_list()
    dc_coverage: Optional[Union[str, list[str]]] = empty_list()
    dc_rights: Optional[Union[str, list[str]]] = empty_list()
    dcterms_title: Optional[Union[str, list[str]]] = empty_list()
    dcterms_creator: Optional[Union[str, list[str]]] = empty_list()
    dcterms_subject: Optional[Union[str, list[str]]] = empty_list()
    dcterms_description: Optional[Union[str, list[str]]] = empty_list()
    dcterms_publisher: Optional[Union[str, list[str]]] = empty_list()
    dcterms_contributor: Optional[Union[str, list[str]]] = empty_list()
    dcterms_date: Optional[Union[str, list[str]]] = empty_list()
    dcterms_type: Optional[Union[str, list[str]]] = empty_list()
    dcterms_format: Optional[Union[str, list[str]]] = empty_list()
    dcterms_identifier: Optional[Union[str, list[str]]] = empty_list()
    dcterms_source: Optional[Union[str, list[str]]] = empty_list()
    dcterms_language: Optional[Union[str, list[str]]] = empty_list()
    dcterms_relation: Optional[Union[str, list[str]]] = empty_list()
    dcterms_coverage: Optional[Union[str, list[str]]] = empty_list()
    dcterms_rights: Optional[Union[str, list[str]]] = empty_list()
    dcterms_alternative: Optional[Union[str, list[str]]] = empty_list()
    dcterms_table_of_contents: Optional[Union[str, list[str]]] = empty_list()
    dcterms_abstract: Optional[Union[str, list[str]]] = empty_list()
    dcterms_created: Optional[Union[str, list[str]]] = empty_list()
    dcterms_valid: Optional[Union[str, list[str]]] = empty_list()
    dcterms_available: Optional[Union[str, list[str]]] = empty_list()
    dcterms_issued: Optional[Union[str, list[str]]] = empty_list()
    dcterms_modified: Optional[Union[str, list[str]]] = empty_list()
    dcterms_date_accepted: Optional[Union[str, list[str]]] = empty_list()
    dcterms_date_copyrighted: Optional[Union[str, list[str]]] = empty_list()
    dcterms_date_submitted: Optional[Union[str, list[str]]] = empty_list()
    dcterms_extent: Optional[Union[str, list[str]]] = empty_list()
    dcterms_medium: Optional[Union[str, list[str]]] = empty_list()
    dcterms_is_version_of: Optional[Union[str, list[str]]] = empty_list()
    dcterms_has_version: Optional[Union[str, list[str]]] = empty_list()
    dcterms_is_replaced_by: Optional[Union[str, list[str]]] = empty_list()
    dcterms_replaces: Optional[Union[str, list[str]]] = empty_list()
    dcterms_is_required_by: Optional[Union[str, list[str]]] = empty_list()
    dcterms_requires: Optional[Union[str, list[str]]] = empty_list()
    dcterms_is_part_of: Optional[Union[str, list[str]]] = empty_list()
    dcterms_has_part: Optional[Union[str, list[str]]] = empty_list()
    dcterms_is_referenced_by: Optional[Union[str, list[str]]] = empty_list()
    dcterms_references: Optional[Union[str, list[str]]] = empty_list()
    dcterms_is_format_of: Optional[Union[str, list[str]]] = empty_list()
    dcterms_has_format: Optional[Union[str, list[str]]] = empty_list()
    dcterms_conforms_to: Optional[Union[str, list[str]]] = empty_list()
    dcterms_spatial: Optional[Union[str, list[str]]] = empty_list()
    dcterms_temporal: Optional[Union[str, list[str]]] = empty_list()
    dcterms_audience: Optional[Union[str, list[str]]] = empty_list()
    dcterms_accrual_method: Optional[Union[str, list[str]]] = empty_list()
    dcterms_accrual_periodicity: Optional[Union[str, list[str]]] = empty_list()
    dcterms_accrual_policy: Optional[Union[str, list[str]]] = empty_list()
    dcterms_instructional_method: Optional[Union[str, list[str]]] = empty_list()
    dcterms_provenance: Optional[Union[str, list[str]]] = empty_list()
    dcterms_rights_holder: Optional[Union[str, list[str]]] = empty_list()
    dcterms_mediator: Optional[Union[str, list[str]]] = empty_list()
    dcterms_education_level: Optional[Union[str, list[str]]] = empty_list()
    dcterms_access_rights: Optional[Union[str, list[str]]] = empty_list()
    dcterms_license: Optional[Union[str, list[str]]] = empty_list()
    dcterms_bibliographic_citation: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.dc_title, list):
            self.dc_title = [self.dc_title] if self.dc_title is not None else []
        self.dc_title = [v if isinstance(v, str) else str(v) for v in self.dc_title]

        if not isinstance(self.dc_creator, list):
            self.dc_creator = [self.dc_creator] if self.dc_creator is not None else []
        self.dc_creator = [v if isinstance(v, str) else str(v) for v in self.dc_creator]

        if not isinstance(self.dc_subject, list):
            self.dc_subject = [self.dc_subject] if self.dc_subject is not None else []
        self.dc_subject = [v if isinstance(v, str) else str(v) for v in self.dc_subject]

        if not isinstance(self.dc_description, list):
            self.dc_description = [self.dc_description] if self.dc_description is not None else []
        self.dc_description = [v if isinstance(v, str) else str(v) for v in self.dc_description]

        if not isinstance(self.dc_publisher, list):
            self.dc_publisher = [self.dc_publisher] if self.dc_publisher is not None else []
        self.dc_publisher = [v if isinstance(v, str) else str(v) for v in self.dc_publisher]

        if not isinstance(self.dc_contributor, list):
            self.dc_contributor = [self.dc_contributor] if self.dc_contributor is not None else []
        self.dc_contributor = [v if isinstance(v, str) else str(v) for v in self.dc_contributor]

        if not isinstance(self.dc_date, list):
            self.dc_date = [self.dc_date] if self.dc_date is not None else []
        self.dc_date = [v if isinstance(v, str) else str(v) for v in self.dc_date]

        if not isinstance(self.dc_type, list):
            self.dc_type = [self.dc_type] if self.dc_type is not None else []
        self.dc_type = [v if isinstance(v, str) else str(v) for v in self.dc_type]

        if not isinstance(self.dc_format, list):
            self.dc_format = [self.dc_format] if self.dc_format is not None else []
        self.dc_format = [v if isinstance(v, str) else str(v) for v in self.dc_format]

        if not isinstance(self.dc_identifier, list):
            self.dc_identifier = [self.dc_identifier] if self.dc_identifier is not None else []
        self.dc_identifier = [v if isinstance(v, str) else str(v) for v in self.dc_identifier]

        if not isinstance(self.dc_source, list):
            self.dc_source = [self.dc_source] if self.dc_source is not None else []
        self.dc_source = [v if isinstance(v, str) else str(v) for v in self.dc_source]

        if not isinstance(self.dc_language, list):
            self.dc_language = [self.dc_language] if self.dc_language is not None else []
        self.dc_language = [v if isinstance(v, str) else str(v) for v in self.dc_language]

        if not isinstance(self.dc_relation, list):
            self.dc_relation = [self.dc_relation] if self.dc_relation is not None else []
        self.dc_relation = [v if isinstance(v, str) else str(v) for v in self.dc_relation]

        if not isinstance(self.dc_coverage, list):
            self.dc_coverage = [self.dc_coverage] if self.dc_coverage is not None else []
        self.dc_coverage = [v if isinstance(v, str) else str(v) for v in self.dc_coverage]

        if not isinstance(self.dc_rights, list):
            self.dc_rights = [self.dc_rights] if self.dc_rights is not None else []
        self.dc_rights = [v if isinstance(v, str) else str(v) for v in self.dc_rights]

        if not isinstance(self.dcterms_title, list):
            self.dcterms_title = [self.dcterms_title] if self.dcterms_title is not None else []
        self.dcterms_title = [v if isinstance(v, str) else str(v) for v in self.dcterms_title]

        if not isinstance(self.dcterms_creator, list):
            self.dcterms_creator = [self.dcterms_creator] if self.dcterms_creator is not None else []
        self.dcterms_creator = [v if isinstance(v, str) else str(v) for v in self.dcterms_creator]

        if not isinstance(self.dcterms_subject, list):
            self.dcterms_subject = [self.dcterms_subject] if self.dcterms_subject is not None else []
        self.dcterms_subject = [v if isinstance(v, str) else str(v) for v in self.dcterms_subject]

        if not isinstance(self.dcterms_description, list):
            self.dcterms_description = [self.dcterms_description] if self.dcterms_description is not None else []
        self.dcterms_description = [v if isinstance(v, str) else str(v) for v in self.dcterms_description]

        if not isinstance(self.dcterms_publisher, list):
            self.dcterms_publisher = [self.dcterms_publisher] if self.dcterms_publisher is not None else []
        self.dcterms_publisher = [v if isinstance(v, str) else str(v) for v in self.dcterms_publisher]

        if not isinstance(self.dcterms_contributor, list):
            self.dcterms_contributor = [self.dcterms_contributor] if self.dcterms_contributor is not None else []
        self.dcterms_contributor = [v if isinstance(v, str) else str(v) for v in self.dcterms_contributor]

        if not isinstance(self.dcterms_date, list):
            self.dcterms_date = [self.dcterms_date] if self.dcterms_date is not None else []
        self.dcterms_date = [v if isinstance(v, str) else str(v) for v in self.dcterms_date]

        if not isinstance(self.dcterms_type, list):
            self.dcterms_type = [self.dcterms_type] if self.dcterms_type is not None else []
        self.dcterms_type = [v if isinstance(v, str) else str(v) for v in self.dcterms_type]

        if not isinstance(self.dcterms_format, list):
            self.dcterms_format = [self.dcterms_format] if self.dcterms_format is not None else []
        self.dcterms_format = [v if isinstance(v, str) else str(v) for v in self.dcterms_format]

        if not isinstance(self.dcterms_identifier, list):
            self.dcterms_identifier = [self.dcterms_identifier] if self.dcterms_identifier is not None else []
        self.dcterms_identifier = [v if isinstance(v, str) else str(v) for v in self.dcterms_identifier]

        if not isinstance(self.dcterms_source, list):
            self.dcterms_source = [self.dcterms_source] if self.dcterms_source is not None else []
        self.dcterms_source = [v if isinstance(v, str) else str(v) for v in self.dcterms_source]

        if not isinstance(self.dcterms_language, list):
            self.dcterms_language = [self.dcterms_language] if self.dcterms_language is not None else []
        self.dcterms_language = [v if isinstance(v, str) else str(v) for v in self.dcterms_language]

        if not isinstance(self.dcterms_relation, list):
            self.dcterms_relation = [self.dcterms_relation] if self.dcterms_relation is not None else []
        self.dcterms_relation = [v if isinstance(v, str) else str(v) for v in self.dcterms_relation]

        if not isinstance(self.dcterms_coverage, list):
            self.dcterms_coverage = [self.dcterms_coverage] if self.dcterms_coverage is not None else []
        self.dcterms_coverage = [v if isinstance(v, str) else str(v) for v in self.dcterms_coverage]

        if not isinstance(self.dcterms_rights, list):
            self.dcterms_rights = [self.dcterms_rights] if self.dcterms_rights is not None else []
        self.dcterms_rights = [v if isinstance(v, str) else str(v) for v in self.dcterms_rights]

        if not isinstance(self.dcterms_alternative, list):
            self.dcterms_alternative = [self.dcterms_alternative] if self.dcterms_alternative is not None else []
        self.dcterms_alternative = [v if isinstance(v, str) else str(v) for v in self.dcterms_alternative]

        if not isinstance(self.dcterms_table_of_contents, list):
            self.dcterms_table_of_contents = [self.dcterms_table_of_contents] if self.dcterms_table_of_contents is not None else []
        self.dcterms_table_of_contents = [v if isinstance(v, str) else str(v) for v in self.dcterms_table_of_contents]

        if not isinstance(self.dcterms_abstract, list):
            self.dcterms_abstract = [self.dcterms_abstract] if self.dcterms_abstract is not None else []
        self.dcterms_abstract = [v if isinstance(v, str) else str(v) for v in self.dcterms_abstract]

        if not isinstance(self.dcterms_created, list):
            self.dcterms_created = [self.dcterms_created] if self.dcterms_created is not None else []
        self.dcterms_created = [v if isinstance(v, str) else str(v) for v in self.dcterms_created]

        if not isinstance(self.dcterms_valid, list):
            self.dcterms_valid = [self.dcterms_valid] if self.dcterms_valid is not None else []
        self.dcterms_valid = [v if isinstance(v, str) else str(v) for v in self.dcterms_valid]

        if not isinstance(self.dcterms_available, list):
            self.dcterms_available = [self.dcterms_available] if self.dcterms_available is not None else []
        self.dcterms_available = [v if isinstance(v, str) else str(v) for v in self.dcterms_available]

        if not isinstance(self.dcterms_issued, list):
            self.dcterms_issued = [self.dcterms_issued] if self.dcterms_issued is not None else []
        self.dcterms_issued = [v if isinstance(v, str) else str(v) for v in self.dcterms_issued]

        if not isinstance(self.dcterms_modified, list):
            self.dcterms_modified = [self.dcterms_modified] if self.dcterms_modified is not None else []
        self.dcterms_modified = [v if isinstance(v, str) else str(v) for v in self.dcterms_modified]

        if not isinstance(self.dcterms_date_accepted, list):
            self.dcterms_date_accepted = [self.dcterms_date_accepted] if self.dcterms_date_accepted is not None else []
        self.dcterms_date_accepted = [v if isinstance(v, str) else str(v) for v in self.dcterms_date_accepted]

        if not isinstance(self.dcterms_date_copyrighted, list):
            self.dcterms_date_copyrighted = [self.dcterms_date_copyrighted] if self.dcterms_date_copyrighted is not None else []
        self.dcterms_date_copyrighted = [v if isinstance(v, str) else str(v) for v in self.dcterms_date_copyrighted]

        if not isinstance(self.dcterms_date_submitted, list):
            self.dcterms_date_submitted = [self.dcterms_date_submitted] if self.dcterms_date_submitted is not None else []
        self.dcterms_date_submitted = [v if isinstance(v, str) else str(v) for v in self.dcterms_date_submitted]

        if not isinstance(self.dcterms_extent, list):
            self.dcterms_extent = [self.dcterms_extent] if self.dcterms_extent is not None else []
        self.dcterms_extent = [v if isinstance(v, str) else str(v) for v in self.dcterms_extent]

        if not isinstance(self.dcterms_medium, list):
            self.dcterms_medium = [self.dcterms_medium] if self.dcterms_medium is not None else []
        self.dcterms_medium = [v if isinstance(v, str) else str(v) for v in self.dcterms_medium]

        if not isinstance(self.dcterms_is_version_of, list):
            self.dcterms_is_version_of = [self.dcterms_is_version_of] if self.dcterms_is_version_of is not None else []
        self.dcterms_is_version_of = [v if isinstance(v, str) else str(v) for v in self.dcterms_is_version_of]

        if not isinstance(self.dcterms_has_version, list):
            self.dcterms_has_version = [self.dcterms_has_version] if self.dcterms_has_version is not None else []
        self.dcterms_has_version = [v if isinstance(v, str) else str(v) for v in self.dcterms_has_version]

        if not isinstance(self.dcterms_is_replaced_by, list):
            self.dcterms_is_replaced_by = [self.dcterms_is_replaced_by] if self.dcterms_is_replaced_by is not None else []
        self.dcterms_is_replaced_by = [v if isinstance(v, str) else str(v) for v in self.dcterms_is_replaced_by]

        if not isinstance(self.dcterms_replaces, list):
            self.dcterms_replaces = [self.dcterms_replaces] if self.dcterms_replaces is not None else []
        self.dcterms_replaces = [v if isinstance(v, str) else str(v) for v in self.dcterms_replaces]

        if not isinstance(self.dcterms_is_required_by, list):
            self.dcterms_is_required_by = [self.dcterms_is_required_by] if self.dcterms_is_required_by is not None else []
        self.dcterms_is_required_by = [v if isinstance(v, str) else str(v) for v in self.dcterms_is_required_by]

        if not isinstance(self.dcterms_requires, list):
            self.dcterms_requires = [self.dcterms_requires] if self.dcterms_requires is not None else []
        self.dcterms_requires = [v if isinstance(v, str) else str(v) for v in self.dcterms_requires]

        if not isinstance(self.dcterms_is_part_of, list):
            self.dcterms_is_part_of = [self.dcterms_is_part_of] if self.dcterms_is_part_of is not None else []
        self.dcterms_is_part_of = [v if isinstance(v, str) else str(v) for v in self.dcterms_is_part_of]

        if not isinstance(self.dcterms_has_part, list):
            self.dcterms_has_part = [self.dcterms_has_part] if self.dcterms_has_part is not None else []
        self.dcterms_has_part = [v if isinstance(v, str) else str(v) for v in self.dcterms_has_part]

        if not isinstance(self.dcterms_is_referenced_by, list):
            self.dcterms_is_referenced_by = [self.dcterms_is_referenced_by] if self.dcterms_is_referenced_by is not None else []
        self.dcterms_is_referenced_by = [v if isinstance(v, str) else str(v) for v in self.dcterms_is_referenced_by]

        if not isinstance(self.dcterms_references, list):
            self.dcterms_references = [self.dcterms_references] if self.dcterms_references is not None else []
        self.dcterms_references = [v if isinstance(v, str) else str(v) for v in self.dcterms_references]

        if not isinstance(self.dcterms_is_format_of, list):
            self.dcterms_is_format_of = [self.dcterms_is_format_of] if self.dcterms_is_format_of is not None else []
        self.dcterms_is_format_of = [v if isinstance(v, str) else str(v) for v in self.dcterms_is_format_of]

        if not isinstance(self.dcterms_has_format, list):
            self.dcterms_has_format = [self.dcterms_has_format] if self.dcterms_has_format is not None else []
        self.dcterms_has_format = [v if isinstance(v, str) else str(v) for v in self.dcterms_has_format]

        if not isinstance(self.dcterms_conforms_to, list):
            self.dcterms_conforms_to = [self.dcterms_conforms_to] if self.dcterms_conforms_to is not None else []
        self.dcterms_conforms_to = [v if isinstance(v, str) else str(v) for v in self.dcterms_conforms_to]

        if not isinstance(self.dcterms_spatial, list):
            self.dcterms_spatial = [self.dcterms_spatial] if self.dcterms_spatial is not None else []
        self.dcterms_spatial = [v if isinstance(v, str) else str(v) for v in self.dcterms_spatial]

        if not isinstance(self.dcterms_temporal, list):
            self.dcterms_temporal = [self.dcterms_temporal] if self.dcterms_temporal is not None else []
        self.dcterms_temporal = [v if isinstance(v, str) else str(v) for v in self.dcterms_temporal]

        if not isinstance(self.dcterms_audience, list):
            self.dcterms_audience = [self.dcterms_audience] if self.dcterms_audience is not None else []
        self.dcterms_audience = [v if isinstance(v, str) else str(v) for v in self.dcterms_audience]

        if not isinstance(self.dcterms_accrual_method, list):
            self.dcterms_accrual_method = [self.dcterms_accrual_method] if self.dcterms_accrual_method is not None else []
        self.dcterms_accrual_method = [v if isinstance(v, str) else str(v) for v in self.dcterms_accrual_method]

        if not isinstance(self.dcterms_accrual_periodicity, list):
            self.dcterms_accrual_periodicity = [self.dcterms_accrual_periodicity] if self.dcterms_accrual_periodicity is not None else []
        self.dcterms_accrual_periodicity = [v if isinstance(v, str) else str(v) for v in self.dcterms_accrual_periodicity]

        if not isinstance(self.dcterms_accrual_policy, list):
            self.dcterms_accrual_policy = [self.dcterms_accrual_policy] if self.dcterms_accrual_policy is not None else []
        self.dcterms_accrual_policy = [v if isinstance(v, str) else str(v) for v in self.dcterms_accrual_policy]

        if not isinstance(self.dcterms_instructional_method, list):
            self.dcterms_instructional_method = [self.dcterms_instructional_method] if self.dcterms_instructional_method is not None else []
        self.dcterms_instructional_method = [v if isinstance(v, str) else str(v) for v in self.dcterms_instructional_method]

        if not isinstance(self.dcterms_provenance, list):
            self.dcterms_provenance = [self.dcterms_provenance] if self.dcterms_provenance is not None else []
        self.dcterms_provenance = [v if isinstance(v, str) else str(v) for v in self.dcterms_provenance]

        if not isinstance(self.dcterms_rights_holder, list):
            self.dcterms_rights_holder = [self.dcterms_rights_holder] if self.dcterms_rights_holder is not None else []
        self.dcterms_rights_holder = [v if isinstance(v, str) else str(v) for v in self.dcterms_rights_holder]

        if not isinstance(self.dcterms_mediator, list):
            self.dcterms_mediator = [self.dcterms_mediator] if self.dcterms_mediator is not None else []
        self.dcterms_mediator = [v if isinstance(v, str) else str(v) for v in self.dcterms_mediator]

        if not isinstance(self.dcterms_education_level, list):
            self.dcterms_education_level = [self.dcterms_education_level] if self.dcterms_education_level is not None else []
        self.dcterms_education_level = [v if isinstance(v, str) else str(v) for v in self.dcterms_education_level]

        if not isinstance(self.dcterms_access_rights, list):
            self.dcterms_access_rights = [self.dcterms_access_rights] if self.dcterms_access_rights is not None else []
        self.dcterms_access_rights = [v if isinstance(v, str) else str(v) for v in self.dcterms_access_rights]

        if not isinstance(self.dcterms_license, list):
            self.dcterms_license = [self.dcterms_license] if self.dcterms_license is not None else []
        self.dcterms_license = [v if isinstance(v, str) else str(v) for v in self.dcterms_license]

        if not isinstance(self.dcterms_bibliographic_citation, list):
            self.dcterms_bibliographic_citation = [self.dcterms_bibliographic_citation] if self.dcterms_bibliographic_citation is not None else []
        self.dcterms_bibliographic_citation = [v if isinstance(v, str) else str(v) for v in self.dcterms_bibliographic_citation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraXmlElement(YAMLRoot):
    """
    An XML element in a place where the XSDs accept any content, kept as written so that the file converts back
    unchanged.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraXmlElement"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraXmlElement"
    class_name: ClassVar[str] = "OrchestraXmlElement"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraXmlElement

    xml_name: str = None
    xml_attributes: Optional[Union[Union[dict, "OrchestraXmlAttribute"], list[Union[dict, "OrchestraXmlAttribute"]]]] = empty_list()
    xml_text: Optional[str] = None
    xml_children: Optional[Union[Union[dict, "OrchestraXmlElement"], list[Union[dict, "OrchestraXmlElement"]]]] = empty_list()
    xml_tail: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.xml_name):
            self.MissingRequiredField("xml_name")
        if not isinstance(self.xml_name, str):
            self.xml_name = str(self.xml_name)

        self._normalize_inlined_as_list(slot_name="xml_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        if self.xml_text is not None and not isinstance(self.xml_text, str):
            self.xml_text = str(self.xml_text)

        self._normalize_inlined_as_list(slot_name="xml_children", slot_type=OrchestraXmlElement, key_name="xml_name", keyed=False)

        if self.xml_tail is not None and not isinstance(self.xml_tail, str):
            self.xml_tail = str(self.xml_tail)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraXmlAttribute(YAMLRoot):
    """
    An XML attribute from another namespace, kept as written.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraXmlAttribute"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraXmlAttribute"
    class_name: ClassVar[str] = "OrchestraXmlAttribute"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraXmlAttribute

    xml_name: str = None
    xml_value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.xml_name):
            self.MissingRequiredField("xml_name")
        if not isinstance(self.xml_name, str):
            self.xml_name = str(self.xml_name)

        if self._is_empty(self.xml_value):
            self.MissingRequiredField("xml_value")
        if not isinstance(self.xml_value, str):
            self.xml_value = str(self.xml_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActionParameterV10(YAMLRoot):
    """
    One input to an action, which is a field, component or group, defined in place or named by reference. It holds
    exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActionParameterV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActionParameterV10"
    class_name: ClassVar[str] = "OrchestraActionParameterV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActionParameterV10

    fixr_field: Optional[Union[dict, "OrchestraFieldV10"]] = None
    fixr_field_ref: Optional[Union[dict, "OrchestraFieldRefV10"]] = None
    fixr_component: Optional[Union[dict, "OrchestraComponentV10"]] = None
    fixr_component_ref: Optional[Union[dict, "OrchestraComponentRefV10"]] = None
    fixr_group: Optional[Union[dict, "OrchestraGroupV10"]] = None
    fixr_group_ref: Optional[Union[dict, "OrchestraGroupRefV10"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_field is not None and not isinstance(self.fixr_field, OrchestraFieldV10):
            self.fixr_field = OrchestraFieldV10(**as_dict(self.fixr_field))

        if self.fixr_field_ref is not None and not isinstance(self.fixr_field_ref, OrchestraFieldRefV10):
            self.fixr_field_ref = OrchestraFieldRefV10(**as_dict(self.fixr_field_ref))

        if self.fixr_component is not None and not isinstance(self.fixr_component, OrchestraComponentV10):
            self.fixr_component = OrchestraComponentV10(**as_dict(self.fixr_component))

        if self.fixr_component_ref is not None and not isinstance(self.fixr_component_ref, OrchestraComponentRefV10):
            self.fixr_component_ref = OrchestraComponentRefV10(**as_dict(self.fixr_component_ref))

        if self.fixr_group is not None and not isinstance(self.fixr_group, OrchestraGroupV10):
            self.fixr_group = OrchestraGroupV10(**as_dict(self.fixr_group))

        if self.fixr_group_ref is not None and not isinstance(self.fixr_group_ref, OrchestraGroupRefV10):
            self.fixr_group_ref = OrchestraGroupRefV10(**as_dict(self.fixr_group_ref))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActionStepV10(YAMLRoot):
    """
    One thing an action does: send a message, set a value, fire a transition or schedule a timer. It holds exactly one
    of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActionStepV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActionStepV10"
    class_name: ClassVar[str] = "OrchestraActionStepV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActionStepV10

    fixr_message_ref: Optional[Union[dict, "OrchestraMessageRefV10"]] = None
    fixr_assign: Optional[str] = None
    fixr_trigger: Optional[Union[dict, "OrchestraTriggerV10"]] = None
    fixr_timer_schedule: Optional[Union[dict, "OrchestraTimerScheduleV10"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_message_ref is not None and not isinstance(self.fixr_message_ref, OrchestraMessageRefV10):
            self.fixr_message_ref = OrchestraMessageRefV10(**as_dict(self.fixr_message_ref))

        if self.fixr_assign is not None and not isinstance(self.fixr_assign, str):
            self.fixr_assign = str(self.fixr_assign)

        if self.fixr_trigger is not None and not isinstance(self.fixr_trigger, OrchestraTriggerV10):
            self.fixr_trigger = OrchestraTriggerV10(**as_dict(self.fixr_trigger))

        if self.fixr_timer_schedule is not None and not isinstance(self.fixr_timer_schedule, OrchestraTimerScheduleV10):
            self.fixr_timer_schedule = OrchestraTimerScheduleV10(**as_dict(self.fixr_timer_schedule))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActionV10(YAMLRoot):
    """
    Things that happen together, such as when a response fires or a state is entered: messages sent, values set,
    transitions fired and timers scheduled, with their inputs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActionV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActionV10"
    class_name: ClassVar[str] = "OrchestraActionV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActionV10

    fixr_actions: Union[Union[dict, OrchestraActionStepV10], list[Union[dict, OrchestraActionStepV10]]] = None
    fixr_parameters: Optional[Union[Union[dict, OrchestraActionParameterV10], list[Union[dict, OrchestraActionParameterV10]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_actions):
            self.MissingRequiredField("fixr_actions")
        if not isinstance(self.fixr_actions, list):
            self.fixr_actions = [self.fixr_actions] if self.fixr_actions is not None else []
        self.fixr_actions = [v if isinstance(v, OrchestraActionStepV10) else OrchestraActionStepV10(**as_dict(v)) for v in self.fixr_actions]

        if not isinstance(self.fixr_parameters, list):
            self.fixr_parameters = [self.fixr_parameters] if self.fixr_parameters is not None else []
        self.fixr_parameters = [v if isinstance(v, OrchestraActionParameterV10) else OrchestraActionParameterV10(**as_dict(v)) for v in self.fixr_parameters]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActorMemberV10(YAMLRoot):
    """
    One thing an actor keeps: a variable given as a field, component or group, a state machine or a timer. It holds
    exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActorMemberV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActorMemberV10"
    class_name: ClassVar[str] = "OrchestraActorMemberV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActorMemberV10

    fixr_field: Optional[Union[dict, "OrchestraFieldV10"]] = None
    fixr_field_ref: Optional[Union[dict, "OrchestraFieldRefV10"]] = None
    fixr_component: Optional[Union[dict, "OrchestraComponentV10"]] = None
    fixr_component_ref: Optional[Union[dict, "OrchestraComponentRefV10"]] = None
    fixr_group: Optional[Union[dict, "OrchestraGroupV10"]] = None
    fixr_group_ref: Optional[Union[dict, "OrchestraGroupRefV10"]] = None
    fixr_states: Optional[Union[dict, "OrchestraStateMachineV10"]] = None
    fixr_timer: Optional[Union[dict, "OrchestraTimerV10"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_field is not None and not isinstance(self.fixr_field, OrchestraFieldV10):
            self.fixr_field = OrchestraFieldV10(**as_dict(self.fixr_field))

        if self.fixr_field_ref is not None and not isinstance(self.fixr_field_ref, OrchestraFieldRefV10):
            self.fixr_field_ref = OrchestraFieldRefV10(**as_dict(self.fixr_field_ref))

        if self.fixr_component is not None and not isinstance(self.fixr_component, OrchestraComponentV10):
            self.fixr_component = OrchestraComponentV10(**as_dict(self.fixr_component))

        if self.fixr_component_ref is not None and not isinstance(self.fixr_component_ref, OrchestraComponentRefV10):
            self.fixr_component_ref = OrchestraComponentRefV10(**as_dict(self.fixr_component_ref))

        if self.fixr_group is not None and not isinstance(self.fixr_group, OrchestraGroupV10):
            self.fixr_group = OrchestraGroupV10(**as_dict(self.fixr_group))

        if self.fixr_group_ref is not None and not isinstance(self.fixr_group_ref, OrchestraGroupRefV10):
            self.fixr_group_ref = OrchestraGroupRefV10(**as_dict(self.fixr_group_ref))

        if self.fixr_states is not None and not isinstance(self.fixr_states, OrchestraStateMachineV10):
            self.fixr_states = OrchestraStateMachineV10(**as_dict(self.fixr_states))

        if self.fixr_timer is not None and not isinstance(self.fixr_timer, OrchestraTimerV10):
            self.fixr_timer = OrchestraTimerV10(**as_dict(self.fixr_timer))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActorV10(YAMLRoot):
    """
    A kind of party in an exchange, such as a buy-side firm or a venue, with the state it keeps: its variables, state
    machines and timers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActorV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActorV10"
    class_name: ClassVar[str] = "OrchestraActorV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActorV10

    fixr_name: str = None
    fixr_members: Optional[Union[Union[dict, OrchestraActorMemberV10], list[Union[dict, OrchestraActorMemberV10]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, "OrchestraAnnotationV10"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraActorMemberV10) else OrchestraActorMemberV10(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActorsMemberV10(YAMLRoot):
    """
    One entry of the actors list, an actor or a flow. It holds exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActorsMemberV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActorsMemberV10"
    class_name: ClassVar[str] = "OrchestraActorsMemberV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActorsMemberV10

    fixr_actor: Optional[Union[dict, OrchestraActorV10]] = None
    fixr_flow: Optional[Union[dict, "OrchestraFlowV10"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_actor is not None and not isinstance(self.fixr_actor, OrchestraActorV10):
            self.fixr_actor = OrchestraActorV10(**as_dict(self.fixr_actor))

        if self.fixr_flow is not None and not isinstance(self.fixr_flow, OrchestraFlowV10):
            self.fixr_flow = OrchestraFlowV10(**as_dict(self.fixr_flow))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActorsV10(YAMLRoot):
    """
    The parties a repository describes and the one-way flows between them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActorsV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActorsV10"
    class_name: ClassVar[str] = "OrchestraActorsV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActorsV10

    fixr_members: Union[Union[dict, OrchestraActorsMemberV10], list[Union[dict, OrchestraActorsMemberV10]]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraActorsMemberV10) else OrchestraActorsMemberV10(**as_dict(v)) for v in self.fixr_members]

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraAnnotationMemberV10(YAMLRoot):
    """
    One part of an annotation, a piece of text or a hint for software. It holds exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraAnnotationMemberV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraAnnotationMemberV10"
    class_name: ClassVar[str] = "OrchestraAnnotationMemberV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraAnnotationMemberV10

    fixr_documentation: Optional[Union[dict, "OrchestraDocumentationV10"]] = None
    fixr_appinfo: Optional[Union[dict, "OrchestraAppinfoV10"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_documentation is not None and not isinstance(self.fixr_documentation, OrchestraDocumentationV10):
            self.fixr_documentation = OrchestraDocumentationV10(**as_dict(self.fixr_documentation))

        if self.fixr_appinfo is not None and not isinstance(self.fixr_appinfo, OrchestraAppinfoV10):
            self.fixr_appinfo = OrchestraAppinfoV10(**as_dict(self.fixr_appinfo))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraAnnotationV10(YAMLRoot):
    """
    Notes for readers and hints for software, attached to an element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraAnnotationV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraAnnotationV10"
    class_name: ClassVar[str] = "OrchestraAnnotationV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraAnnotationV10

    fixr_members: Union[Union[dict, OrchestraAnnotationMemberV10], list[Union[dict, OrchestraAnnotationMemberV10]]] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraAnnotationMemberV10) else OrchestraAnnotationMemberV10(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraAppinfoV10(YAMLRoot):
    """
    A hint for a particular tool or encoding, such as how FIXML renders an element, held as text and open XML.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraAppinfoV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraAppinfoV10"
    class_name: ClassVar[str] = "OrchestraAppinfoV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraAppinfoV10

    fixr_text: Optional[str] = None
    fixr_any: Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]] = empty_list()
    fixr_spec_url: Optional[Union[str, URI]] = None
    fixr_lang_id: Optional[str] = None
    fixr_purpose: Optional[Union[str, "OrchestraPurpose"]] = None
    fixr_other_attributes: Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]] = empty_list()
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_text is not None and not isinstance(self.fixr_text, str):
            self.fixr_text = str(self.fixr_text)

        self._normalize_inlined_as_list(slot_name="fixr_any", slot_type=OrchestraXmlElement, key_name="xml_name", keyed=False)

        if self.fixr_spec_url is not None and not isinstance(self.fixr_spec_url, URI):
            self.fixr_spec_url = URI(self.fixr_spec_url)

        if self.fixr_lang_id is not None and not isinstance(self.fixr_lang_id, str):
            self.fixr_lang_id = str(self.fixr_lang_id)

        if self.fixr_purpose is not None and not isinstance(self.fixr_purpose, (OrchestraPurpose, str)):
            value = self.fixr_purpose
            for _coerce in (lambda: OrchestraPurpose(value), lambda: str(value)):
                try:
                    self.fixr_purpose = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraPurpose, str] could be constructed from {value!r} for slot fixr_purpose")

        self._normalize_inlined_as_list(slot_name="fixr_other_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraBaseInterfaceV10(YAMLRoot):
    """
    What an interface and a session share: the services, encodings and protocols of a connection, layer by layer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraBaseInterfaceV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraBaseInterfaceV10"
    class_name: ClassVar[str] = "OrchestraBaseInterfaceV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraBaseInterfaceV10

    fixi_name: str = None
    fixi_service: Optional[Union[Union[dict, "OrchestraServiceV10"], list[Union[dict, "OrchestraServiceV10"]]]] = empty_list()
    fixi_user_interface: Optional[Union[Union[dict, "OrchestraUserInterfaceV10"], list[Union[dict, "OrchestraUserInterfaceV10"]]]] = empty_list()
    fixi_encoding: Optional[Union[Union[dict, "OrchestraEncodingV10"], list[Union[dict, "OrchestraEncodingV10"]]]] = empty_list()
    fixi_session_protocol: Optional[Union[Union[dict, "OrchestraSessionProtocolV10"], list[Union[dict, "OrchestraSessionProtocolV10"]]]] = empty_list()
    fixi_protocol: Optional[Union[Union[dict, "OrchestraProtocolV10"], list[Union[dict, "OrchestraProtocolV10"]]]] = empty_list()
    fixi_transport: Optional[Union[Union[dict, "OrchestraTransportV10"], list[Union[dict, "OrchestraTransportV10"]]]] = empty_list()
    fixi_annotation: Optional[Union[dict, "OrchestraInterfaceAnnotationV10"]] = None
    fixi_other_attributes: Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixi_name):
            self.MissingRequiredField("fixi_name")
        if not isinstance(self.fixi_name, str):
            self.fixi_name = str(self.fixi_name)

        if not isinstance(self.fixi_service, list):
            self.fixi_service = [self.fixi_service] if self.fixi_service is not None else []
        self.fixi_service = [v if isinstance(v, OrchestraServiceV10) else OrchestraServiceV10(**as_dict(v)) for v in self.fixi_service]

        if not isinstance(self.fixi_user_interface, list):
            self.fixi_user_interface = [self.fixi_user_interface] if self.fixi_user_interface is not None else []
        self.fixi_user_interface = [v if isinstance(v, OrchestraUserInterfaceV10) else OrchestraUserInterfaceV10(**as_dict(v)) for v in self.fixi_user_interface]

        if not isinstance(self.fixi_encoding, list):
            self.fixi_encoding = [self.fixi_encoding] if self.fixi_encoding is not None else []
        self.fixi_encoding = [v if isinstance(v, OrchestraEncodingV10) else OrchestraEncodingV10(**as_dict(v)) for v in self.fixi_encoding]

        if not isinstance(self.fixi_session_protocol, list):
            self.fixi_session_protocol = [self.fixi_session_protocol] if self.fixi_session_protocol is not None else []
        self.fixi_session_protocol = [v if isinstance(v, OrchestraSessionProtocolV10) else OrchestraSessionProtocolV10(**as_dict(v)) for v in self.fixi_session_protocol]

        if not isinstance(self.fixi_protocol, list):
            self.fixi_protocol = [self.fixi_protocol] if self.fixi_protocol is not None else []
        self.fixi_protocol = [v if isinstance(v, OrchestraProtocolV10) else OrchestraProtocolV10(**as_dict(v)) for v in self.fixi_protocol]

        if not isinstance(self.fixi_transport, list):
            self.fixi_transport = [self.fixi_transport] if self.fixi_transport is not None else []
        self.fixi_transport = [v if isinstance(v, OrchestraTransportV10) else OrchestraTransportV10(**as_dict(v)) for v in self.fixi_transport]

        if self.fixi_annotation is not None and not isinstance(self.fixi_annotation, OrchestraInterfaceAnnotationV10):
            self.fixi_annotation = OrchestraInterfaceAnnotationV10(**as_dict(self.fixi_annotation))

        self._normalize_inlined_as_list(slot_name="fixi_other_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraBlockAssignmentV10(YAMLRoot):
    """
    How every entry of a group, or a single use of a component, gets its values: the fields, groups and components it
    sets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraBlockAssignmentV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraBlockAssignmentV10"
    class_name: ClassVar[str] = "OrchestraBlockAssignmentV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraBlockAssignmentV10

    fixr_members: Union[Union[dict, "OrchestraStructureMemberV10"], list[Union[dict, "OrchestraStructureMemberV10"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraStructureMemberV10) else OrchestraStructureMemberV10(**as_dict(v)) for v in self.fixr_members]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraCategoriesV10(YAMLRoot):
    """
    The categories a repository sorts its messages and fields into.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraCategoriesV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraCategoriesV10"
    class_name: ClassVar[str] = "OrchestraCategoriesV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraCategoriesV10

    fixr_category: Union[Union[dict, "OrchestraCategoryV10"], list[Union[dict, "OrchestraCategoryV10"]]] = None
    xml_base: Optional[Union[str, URI]] = None
    fixr_latest_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_category):
            self.MissingRequiredField("fixr_category")
        if not isinstance(self.fixr_category, list):
            self.fixr_category = [self.fixr_category] if self.fixr_category is not None else []
        self.fixr_category = [v if isinstance(v, OrchestraCategoryV10) else OrchestraCategoryV10(**as_dict(v)) for v in self.fixr_category]

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        if self.fixr_latest_ep is not None and not isinstance(self.fixr_latest_ep, int):
            self.fixr_latest_ep = int(self.fixr_latest_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraCategoryV10(YAMLRoot):
    """
    A business process grouping within a section, such as order handling or market data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraCategoryV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraCategoryV10"
    class_name: ClassVar[str] = "OrchestraCategoryV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraCategoryV10

    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_name: Optional[str] = None
    fixr_fixml_file_name: Optional[str] = None
    fixr_component_type: Optional[Union[str, "OrchestraCategoryContentV10"]] = None
    fixr_section: Optional[str] = None
    fixr_include_file: Optional[Union[str, "OrchestraCategoryIncludeFileV10"]] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_fixml_file_name is not None and not isinstance(self.fixr_fixml_file_name, str):
            self.fixr_fixml_file_name = str(self.fixr_fixml_file_name)

        if self.fixr_component_type is not None and not isinstance(self.fixr_component_type, OrchestraCategoryContentV10):
            self.fixr_component_type = OrchestraCategoryContentV10(self.fixr_component_type)

        if self.fixr_section is not None and not isinstance(self.fixr_section, str):
            self.fixr_section = str(self.fixr_section)

        if self.fixr_include_file is not None and not isinstance(self.fixr_include_file, OrchestraCategoryIncludeFileV10):
            self.fixr_include_file = OrchestraCategoryIncludeFileV10(self.fixr_include_file)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraCodeSetV10(YAMLRoot):
    """
    A named list of the values a field may take, each with a name of its own, over one underlying datatype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraCodeSetV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraCodeSetV10"
    class_name: ClassVar[str] = "OrchestraCodeSetV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraCodeSetV10

    fixr_type: str = None
    fixr_id: int = None
    fixr_name: str = None
    fixr_code: Optional[Union[Union[dict, "OrchestraCodeV10"], list[Union[dict, "OrchestraCodeV10"]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_default: Optional[str] = None
    fixr_spec_url: Optional[Union[str, URI]] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_type):
            self.MissingRequiredField("fixr_type")
        if not isinstance(self.fixr_type, str):
            self.fixr_type = str(self.fixr_type)

        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        self._normalize_inlined_as_list(slot_name="fixr_code", slot_type=OrchestraCodeV10, key_name="fixr_value", keyed=False)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_default is not None and not isinstance(self.fixr_default, str):
            self.fixr_default = str(self.fixr_default)

        if self.fixr_spec_url is not None and not isinstance(self.fixr_spec_url, URI):
            self.fixr_spec_url = URI(self.fixr_spec_url)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraCodeSetsV10(YAMLRoot):
    """
    The code sets a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraCodeSetsV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraCodeSetsV10"
    class_name: ClassVar[str] = "OrchestraCodeSetsV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraCodeSetsV10

    fixr_code_set: Union[Union[dict, OrchestraCodeSetV10], list[Union[dict, OrchestraCodeSetV10]]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_code_set):
            self.MissingRequiredField("fixr_code_set")
        self._normalize_inlined_as_list(slot_name="fixr_code_set", slot_type=OrchestraCodeSetV10, key_name="fixr_type", keyed=False)

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraCodeV10(YAMLRoot):
    """
    One permitted value of the set, with its name and what goes on the wire.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraCodeV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraCodeV10"
    class_name: ClassVar[str] = "OrchestraCodeV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraCodeV10

    fixr_value: str = None
    fixr_id: int = None
    fixr_name: str = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_sort: Optional[str] = None
    fixr_group: Optional[str] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_value):
            self.MissingRequiredField("fixr_value")
        if not isinstance(self.fixr_value, str):
            self.fixr_value = str(self.fixr_value)

        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_sort is not None and not isinstance(self.fixr_sort, str):
            self.fixr_sort = str(self.fixr_sort)

        if self.fixr_group is not None and not isinstance(self.fixr_group, str):
            self.fixr_group = str(self.fixr_group)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraComponentRefV10(YAMLRoot):
    """
    Where a message or block includes a component, by its number, with its presence and any rules that make it
    conditional.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraComponentRefV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraComponentRefV10"
    class_name: ClassVar[str] = "OrchestraComponentRefV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraComponentRefV10

    fixr_id: int = None
    fixr_block_assignment: Optional[Union[Union[dict, OrchestraBlockAssignmentV10], list[Union[dict, OrchestraBlockAssignmentV10]]]] = empty_list()
    fixr_rule: Optional[Union[Union[dict, "OrchestraComponentRuleV10"], list[Union[dict, "OrchestraComponentRuleV10"]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = 'optional'
    fixr_instance_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if not isinstance(self.fixr_block_assignment, list):
            self.fixr_block_assignment = [self.fixr_block_assignment] if self.fixr_block_assignment is not None else []
        self.fixr_block_assignment = [v if isinstance(v, OrchestraBlockAssignmentV10) else OrchestraBlockAssignmentV10(**as_dict(v)) for v in self.fixr_block_assignment]

        self._normalize_inlined_as_list(slot_name="fixr_rule", slot_type=OrchestraComponentRuleV10, key_name="fixr_when", keyed=False)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        if self.fixr_instance_name is not None and not isinstance(self.fixr_instance_name, str):
            self.fixr_instance_name = str(self.fixr_instance_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraComponentRuleV10(YAMLRoot):
    """
    A condition that changes a component's presence, such as making it required.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraComponentRuleV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraComponentRuleV10"
    class_name: ClassVar[str] = "OrchestraComponentRuleV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraComponentRuleV10

    fixr_when: str = None
    fixr_name: Optional[str] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_when):
            self.MissingRequiredField("fixr_when")
        if not isinstance(self.fixr_when, str):
            self.fixr_when = str(self.fixr_when)

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraComponentV10(YAMLRoot):
    """
    A named block of fields, groups and components that messages and other blocks include by reference.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraComponentV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraComponentV10"
    class_name: ClassVar[str] = "OrchestraComponentV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraComponentV10

    fixr_members: Union[Union[dict, "OrchestraStructureMemberV10"], list[Union[dict, "OrchestraStructureMemberV10"]]] = None
    fixr_id: int = None
    fixr_name: str = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_category: Optional[str] = None
    fixr_rendering: Optional[str] = None
    fixr_which: Optional[Union[str, "OrchestraMemberSelection"]] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraStructureMemberV10) else OrchestraStructureMemberV10(**as_dict(v)) for v in self.fixr_members]

        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_category is not None and not isinstance(self.fixr_category, str):
            self.fixr_category = str(self.fixr_category)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        if self.fixr_which is not None and not isinstance(self.fixr_which, OrchestraMemberSelection):
            self.fixr_which = OrchestraMemberSelection(self.fixr_which)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraComponentsV10(YAMLRoot):
    """
    The components a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraComponentsV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraComponentsV10"
    class_name: ClassVar[str] = "OrchestraComponentsV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraComponentsV10

    fixr_component: Union[Union[dict, OrchestraComponentV10], list[Union[dict, OrchestraComponentV10]]] = None
    xml_base: Optional[Union[str, URI]] = None
    fixr_latest_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_component):
            self.MissingRequiredField("fixr_component")
        self._normalize_inlined_as_list(slot_name="fixr_component", slot_type=OrchestraComponentV10, key_name="fixr_id", keyed=False)

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        if self.fixr_latest_ep is not None and not isinstance(self.fixr_latest_ep, int):
            self.fixr_latest_ep = int(self.fixr_latest_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraConceptMemberV10(YAMLRoot):
    """
    One element a concept ties together, named by reference, which is a message, field, component or group. It holds
    exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraConceptMemberV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraConceptMemberV10"
    class_name: ClassVar[str] = "OrchestraConceptMemberV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraConceptMemberV10

    fixr_component_ref: Optional[Union[dict, OrchestraComponentRefV10]] = None
    fixr_group_ref: Optional[Union[dict, "OrchestraGroupRefV10"]] = None
    fixr_field_ref: Optional[Union[dict, "OrchestraFieldRefV10"]] = None
    fixr_message_ref: Optional[Union[dict, "OrchestraMessageRefV10"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_component_ref is not None and not isinstance(self.fixr_component_ref, OrchestraComponentRefV10):
            self.fixr_component_ref = OrchestraComponentRefV10(**as_dict(self.fixr_component_ref))

        if self.fixr_group_ref is not None and not isinstance(self.fixr_group_ref, OrchestraGroupRefV10):
            self.fixr_group_ref = OrchestraGroupRefV10(**as_dict(self.fixr_group_ref))

        if self.fixr_field_ref is not None and not isinstance(self.fixr_field_ref, OrchestraFieldRefV10):
            self.fixr_field_ref = OrchestraFieldRefV10(**as_dict(self.fixr_field_ref))

        if self.fixr_message_ref is not None and not isinstance(self.fixr_message_ref, OrchestraMessageRefV10):
            self.fixr_message_ref = OrchestraMessageRefV10(**as_dict(self.fixr_message_ref))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraConceptV10(YAMLRoot):
    """
    A named business idea that ties together the fields, components, groups and messages that express it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraConceptV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraConceptV10"
    class_name: ClassVar[str] = "OrchestraConceptV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraConceptV10

    fixr_members: Union[Union[dict, OrchestraConceptMemberV10], list[Union[dict, OrchestraConceptMemberV10]]] = None
    fixr_name: str = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraConceptMemberV10) else OrchestraConceptMemberV10(**as_dict(v)) for v in self.fixr_members]

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraConceptsV10(YAMLRoot):
    """
    The concepts a repository names.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraConceptsV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraConceptsV10"
    class_name: ClassVar[str] = "OrchestraConceptsV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraConceptsV10

    fixr_concept: Union[Union[dict, OrchestraConceptV10], list[Union[dict, OrchestraConceptV10]]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_concept):
            self.MissingRequiredField("fixr_concept")
        self._normalize_inlined_as_list(slot_name="fixr_concept", slot_type=OrchestraConceptV10, key_name="fixr_name", keyed=False)

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraContainerV10Mixin(YAMLRoot):
    """
    The extension pack that a list of elements is up to date with.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraContainerV10Mixin"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraContainerV10Mixin"
    class_name: ClassVar[str] = "OrchestraContainerV10Mixin"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraContainerV10Mixin

    fixr_latest_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_latest_ep is not None and not isinstance(self.fixr_latest_ep, int):
            self.fixr_latest_ep = int(self.fixr_latest_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraDatatypeExtensionV10(YAMLRoot):
    """
    XML from the target standard's own schema that a datatype mapping carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraDatatypeExtensionV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraDatatypeExtensionV10"
    class_name: ClassVar[str] = "OrchestraDatatypeExtensionV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraDatatypeExtensionV10

    fixr_any: Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_any", slot_type=OrchestraXmlElement, key_name="xml_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraDatatypeV10(YAMLRoot):
    """
    A FIX datatype, such as Price or UTCTimestamp, with how it maps to the types of other standards.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraDatatypeV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraDatatypeV10"
    class_name: ClassVar[str] = "OrchestraDatatypeV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraDatatypeV10

    fixr_name: str = None
    fixr_mapped_datatype: Optional[Union[Union[dict, "OrchestraMappedDatatypeV10"], list[Union[dict, "OrchestraMappedDatatypeV10"]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_base_type: Optional[str] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        self._normalize_inlined_as_list(slot_name="fixr_mapped_datatype", slot_type=OrchestraMappedDatatypeV10, key_name="fixr_standard", keyed=False)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_base_type is not None and not isinstance(self.fixr_base_type, str):
            self.fixr_base_type = str(self.fixr_base_type)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraDatatypesV10(YAMLRoot):
    """
    The datatypes a repository uses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraDatatypesV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraDatatypesV10"
    class_name: ClassVar[str] = "OrchestraDatatypesV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraDatatypesV10

    fixr_datatype: Union[Union[dict, OrchestraDatatypeV10], list[Union[dict, OrchestraDatatypeV10]]] = None
    xml_base: Optional[Union[str, URI]] = None
    fixr_latest_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_datatype):
            self.MissingRequiredField("fixr_datatype")
        self._normalize_inlined_as_list(slot_name="fixr_datatype", slot_type=OrchestraDatatypeV10, key_name="fixr_name", keyed=False)

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        if self.fixr_latest_ep is not None and not isinstance(self.fixr_latest_ep, int):
            self.fixr_latest_ep = int(self.fixr_latest_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraDocumentationV10(YAMLRoot):
    """
    Text about an element, with its language, purpose and media type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraDocumentationV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraDocumentationV10"
    class_name: ClassVar[str] = "OrchestraDocumentationV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraDocumentationV10

    fixr_text: Optional[str] = None
    fixr_any: Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]] = empty_list()
    fixr_lang_id: Optional[str] = None
    fixr_purpose: Optional[Union[str, "OrchestraPurpose"]] = None
    fixr_content_type: Optional[str] = "text/plain"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_text is not None and not isinstance(self.fixr_text, str):
            self.fixr_text = str(self.fixr_text)

        self._normalize_inlined_as_list(slot_name="fixr_any", slot_type=OrchestraXmlElement, key_name="xml_name", keyed=False)

        if self.fixr_lang_id is not None and not isinstance(self.fixr_lang_id, str):
            self.fixr_lang_id = str(self.fixr_lang_id)

        if self.fixr_purpose is not None and not isinstance(self.fixr_purpose, (OrchestraPurpose, str)):
            value = self.fixr_purpose
            for _coerce in (lambda: OrchestraPurpose(value), lambda: str(value)):
                try:
                    self.fixr_purpose = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraPurpose, str] could be constructed from {value!r} for slot fixr_purpose")

        if self.fixr_content_type is not None and not isinstance(self.fixr_content_type, str):
            self.fixr_content_type = str(self.fixr_content_type)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFieldConstraintsV10Mixin(YAMLRoot):
    """
    The limits on a field's value that a field, a use of it or a rule may set: range, length, presence, fixed or
    default value, character set and a display hint.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFieldConstraintsV10Mixin"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFieldConstraintsV10Mixin"
    class_name: ClassVar[str] = "OrchestraFieldConstraintsV10Mixin"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFieldConstraintsV10Mixin

    fixr_min_inclusive: Optional[str] = None
    fixr_max_inclusive: Optional[str] = None
    fixr_impl_length: Optional[int] = None
    fixr_impl_min_length: Optional[int] = None
    fixr_impl_max_length: Optional[int] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = 'optional'
    fixr_encoding: Optional[str] = None
    fixr_value: Optional[str] = None
    fixr_rendering: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_min_inclusive is not None and not isinstance(self.fixr_min_inclusive, str):
            self.fixr_min_inclusive = str(self.fixr_min_inclusive)

        if self.fixr_max_inclusive is not None and not isinstance(self.fixr_max_inclusive, str):
            self.fixr_max_inclusive = str(self.fixr_max_inclusive)

        if self.fixr_impl_length is not None and not isinstance(self.fixr_impl_length, int):
            self.fixr_impl_length = int(self.fixr_impl_length)

        if self.fixr_impl_min_length is not None and not isinstance(self.fixr_impl_min_length, int):
            self.fixr_impl_min_length = int(self.fixr_impl_min_length)

        if self.fixr_impl_max_length is not None and not isinstance(self.fixr_impl_max_length, int):
            self.fixr_impl_max_length = int(self.fixr_impl_max_length)

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        if self.fixr_encoding is not None and not isinstance(self.fixr_encoding, str):
            self.fixr_encoding = str(self.fixr_encoding)

        if self.fixr_value is not None and not isinstance(self.fixr_value, str):
            self.fixr_value = str(self.fixr_value)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFieldRefV10(YAMLRoot):
    """
    Where a message or block includes a field, by its tag number, with its presence, value limits and any rules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFieldRefV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFieldRefV10"
    class_name: ClassVar[str] = "OrchestraFieldRefV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFieldRefV10

    fixr_id: int = None
    fixr_rule: Optional[Union[Union[dict, "OrchestraFieldRuleV10"], list[Union[dict, "OrchestraFieldRuleV10"]]]] = empty_list()
    fixr_assign: Optional[str] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_length_id: Optional[int] = None
    fixr_instance_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None
    fixr_min_inclusive: Optional[str] = None
    fixr_max_inclusive: Optional[str] = None
    fixr_impl_length: Optional[int] = None
    fixr_impl_min_length: Optional[int] = None
    fixr_impl_max_length: Optional[int] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = 'optional'
    fixr_encoding: Optional[str] = None
    fixr_value: Optional[str] = None
    fixr_rendering: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        self._normalize_inlined_as_list(slot_name="fixr_rule", slot_type=OrchestraFieldRuleV10, key_name="fixr_when", keyed=False)

        if self.fixr_assign is not None and not isinstance(self.fixr_assign, str):
            self.fixr_assign = str(self.fixr_assign)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_length_id is not None and not isinstance(self.fixr_length_id, int):
            self.fixr_length_id = int(self.fixr_length_id)

        if self.fixr_instance_name is not None and not isinstance(self.fixr_instance_name, str):
            self.fixr_instance_name = str(self.fixr_instance_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        if self.fixr_min_inclusive is not None and not isinstance(self.fixr_min_inclusive, str):
            self.fixr_min_inclusive = str(self.fixr_min_inclusive)

        if self.fixr_max_inclusive is not None and not isinstance(self.fixr_max_inclusive, str):
            self.fixr_max_inclusive = str(self.fixr_max_inclusive)

        if self.fixr_impl_length is not None and not isinstance(self.fixr_impl_length, int):
            self.fixr_impl_length = int(self.fixr_impl_length)

        if self.fixr_impl_min_length is not None and not isinstance(self.fixr_impl_min_length, int):
            self.fixr_impl_min_length = int(self.fixr_impl_min_length)

        if self.fixr_impl_max_length is not None and not isinstance(self.fixr_impl_max_length, int):
            self.fixr_impl_max_length = int(self.fixr_impl_max_length)

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        if self.fixr_encoding is not None and not isinstance(self.fixr_encoding, str):
            self.fixr_encoding = str(self.fixr_encoding)

        if self.fixr_value is not None and not isinstance(self.fixr_value, str):
            self.fixr_value = str(self.fixr_value)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFieldRuleV10(YAMLRoot):
    """
    A condition that changes a field's presence, datatype or limits, or a check its value must pass.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFieldRuleV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFieldRuleV10"
    class_name: ClassVar[str] = "OrchestraFieldRuleV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFieldRuleV10

    fixr_when: str = None
    fixr_unique: Optional[Union[dict, "OrchestraUniqueV10"]] = None
    fixr_assign: Optional[Union[str, list[str]]] = empty_list()
    fixr_name: Optional[str] = None
    fixr_type: Optional[str] = None
    fixr_min_inclusive: Optional[str] = None
    fixr_max_inclusive: Optional[str] = None
    fixr_impl_length: Optional[int] = None
    fixr_impl_min_length: Optional[int] = None
    fixr_impl_max_length: Optional[int] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = 'optional'
    fixr_encoding: Optional[str] = None
    fixr_value: Optional[str] = None
    fixr_rendering: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_when):
            self.MissingRequiredField("fixr_when")
        if not isinstance(self.fixr_when, str):
            self.fixr_when = str(self.fixr_when)

        if self.fixr_unique is not None and not isinstance(self.fixr_unique, OrchestraUniqueV10):
            self.fixr_unique = OrchestraUniqueV10(**as_dict(self.fixr_unique))

        if not isinstance(self.fixr_assign, list):
            self.fixr_assign = [self.fixr_assign] if self.fixr_assign is not None else []
        self.fixr_assign = [v if isinstance(v, str) else str(v) for v in self.fixr_assign]

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_type is not None and not isinstance(self.fixr_type, str):
            self.fixr_type = str(self.fixr_type)

        if self.fixr_min_inclusive is not None and not isinstance(self.fixr_min_inclusive, str):
            self.fixr_min_inclusive = str(self.fixr_min_inclusive)

        if self.fixr_max_inclusive is not None and not isinstance(self.fixr_max_inclusive, str):
            self.fixr_max_inclusive = str(self.fixr_max_inclusive)

        if self.fixr_impl_length is not None and not isinstance(self.fixr_impl_length, int):
            self.fixr_impl_length = int(self.fixr_impl_length)

        if self.fixr_impl_min_length is not None and not isinstance(self.fixr_impl_min_length, int):
            self.fixr_impl_min_length = int(self.fixr_impl_min_length)

        if self.fixr_impl_max_length is not None and not isinstance(self.fixr_impl_max_length, int):
            self.fixr_impl_max_length = int(self.fixr_impl_max_length)

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        if self.fixr_encoding is not None and not isinstance(self.fixr_encoding, str):
            self.fixr_encoding = str(self.fixr_encoding)

        if self.fixr_value is not None and not isinstance(self.fixr_value, str):
            self.fixr_value = str(self.fixr_value)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFieldV10(YAMLRoot):
    """
    A FIX field: its tag number, its name, its datatype or its code set, and the limits on its value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFieldV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFieldV10"
    class_name: ClassVar[str] = "OrchestraFieldV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFieldV10

    fixr_type: str = None
    fixr_id: int = None
    fixr_name: str = None
    fixr_rule: Optional[Union[Union[dict, OrchestraFieldRuleV10], list[Union[dict, OrchestraFieldRuleV10]]]] = empty_list()
    fixr_assign: Optional[str] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_length_id: Optional[int] = None
    fixr_discriminator_id: Optional[int] = None
    fixr_base_category: Optional[str] = None
    fixr_base_category_abbr_name: Optional[str] = None
    fixr_union_data_type: Optional[Union[str, "OrchestraUnionDatatypeV10"]] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None
    fixr_min_inclusive: Optional[str] = None
    fixr_max_inclusive: Optional[str] = None
    fixr_impl_length: Optional[int] = None
    fixr_impl_min_length: Optional[int] = None
    fixr_impl_max_length: Optional[int] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = 'optional'
    fixr_encoding: Optional[str] = None
    fixr_value: Optional[str] = None
    fixr_rendering: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_type):
            self.MissingRequiredField("fixr_type")
        if not isinstance(self.fixr_type, str):
            self.fixr_type = str(self.fixr_type)

        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        self._normalize_inlined_as_list(slot_name="fixr_rule", slot_type=OrchestraFieldRuleV10, key_name="fixr_when", keyed=False)

        if self.fixr_assign is not None and not isinstance(self.fixr_assign, str):
            self.fixr_assign = str(self.fixr_assign)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_length_id is not None and not isinstance(self.fixr_length_id, int):
            self.fixr_length_id = int(self.fixr_length_id)

        if self.fixr_discriminator_id is not None and not isinstance(self.fixr_discriminator_id, int):
            self.fixr_discriminator_id = int(self.fixr_discriminator_id)

        if self.fixr_base_category is not None and not isinstance(self.fixr_base_category, str):
            self.fixr_base_category = str(self.fixr_base_category)

        if self.fixr_base_category_abbr_name is not None and not isinstance(self.fixr_base_category_abbr_name, str):
            self.fixr_base_category_abbr_name = str(self.fixr_base_category_abbr_name)

        if self.fixr_union_data_type is not None and not isinstance(self.fixr_union_data_type, OrchestraUnionDatatypeV10):
            self.fixr_union_data_type = OrchestraUnionDatatypeV10(self.fixr_union_data_type)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        if self.fixr_min_inclusive is not None and not isinstance(self.fixr_min_inclusive, str):
            self.fixr_min_inclusive = str(self.fixr_min_inclusive)

        if self.fixr_max_inclusive is not None and not isinstance(self.fixr_max_inclusive, str):
            self.fixr_max_inclusive = str(self.fixr_max_inclusive)

        if self.fixr_impl_length is not None and not isinstance(self.fixr_impl_length, int):
            self.fixr_impl_length = int(self.fixr_impl_length)

        if self.fixr_impl_min_length is not None and not isinstance(self.fixr_impl_min_length, int):
            self.fixr_impl_min_length = int(self.fixr_impl_min_length)

        if self.fixr_impl_max_length is not None and not isinstance(self.fixr_impl_max_length, int):
            self.fixr_impl_max_length = int(self.fixr_impl_max_length)

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        if self.fixr_encoding is not None and not isinstance(self.fixr_encoding, str):
            self.fixr_encoding = str(self.fixr_encoding)

        if self.fixr_value is not None and not isinstance(self.fixr_value, str):
            self.fixr_value = str(self.fixr_value)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFieldsV10(YAMLRoot):
    """
    The fields a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFieldsV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFieldsV10"
    class_name: ClassVar[str] = "OrchestraFieldsV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFieldsV10

    fixr_field: Union[Union[dict, OrchestraFieldV10], list[Union[dict, OrchestraFieldV10]]] = None
    fixr_latest_ep: Optional[int] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_field):
            self.MissingRequiredField("fixr_field")
        self._normalize_inlined_as_list(slot_name="fixr_field", slot_type=OrchestraFieldV10, key_name="fixr_type", keyed=False)

        if self.fixr_latest_ep is not None and not isinstance(self.fixr_latest_ep, int):
            self.fixr_latest_ep = int(self.fixr_latest_ep)

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFlowV10(YAMLRoot):
    """
    Messages that travel one way, from a sending actor to a receiving one, with their delivery guarantee.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFlowV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFlowV10"
    class_name: ClassVar[str] = "OrchestraFlowV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFlowV10

    fixr_name: str = None
    fixr_source: str = None
    fixr_destination: str = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_reliability: Optional[Union[str, "OrchestraReliability"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self._is_empty(self.fixr_source):
            self.MissingRequiredField("fixr_source")
        if not isinstance(self.fixr_source, str):
            self.fixr_source = str(self.fixr_source)

        if self._is_empty(self.fixr_destination):
            self.MissingRequiredField("fixr_destination")
        if not isinstance(self.fixr_destination, str):
            self.fixr_destination = str(self.fixr_destination)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_reliability is not None and not isinstance(self.fixr_reliability, OrchestraReliability):
            self.fixr_reliability = OrchestraReliability(self.fixr_reliability)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraGroupRefV10(OrchestraComponentRefV10):
    """
    Where a message or block includes a repeating group, by its number, with how many entries it may hold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraGroupRefV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraGroupRefV10"
    class_name: ClassVar[str] = "OrchestraGroupRefV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraGroupRefV10

    fixr_id: int = None
    fixr_impl_min_occurs: Optional[int] = None
    fixr_impl_max_occurs: Optional[str] = "unbounded"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_impl_min_occurs is not None and not isinstance(self.fixr_impl_min_occurs, int):
            self.fixr_impl_min_occurs = int(self.fixr_impl_min_occurs)

        if self.fixr_impl_max_occurs is not None and not isinstance(self.fixr_impl_max_occurs, str):
            self.fixr_impl_max_occurs = str(self.fixr_impl_max_occurs)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraGroupV10(YAMLRoot):
    """
    A block whose entries repeat, each with the same fields, groups and components, and whose count a NumInGroup field
    carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraGroupV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraGroupV10"
    class_name: ClassVar[str] = "OrchestraGroupV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraGroupV10

    fixr_members: Union[Union[dict, "OrchestraStructureMemberV10"], list[Union[dict, "OrchestraStructureMemberV10"]]] = None
    fixr_id: int = None
    fixr_name: str = None
    fixr_num_in_group: Optional[Union[dict, OrchestraFieldRefV10]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_category: Optional[str] = None
    fixr_rendering: Optional[str] = None
    fixr_impl_min_occurs: Optional[int] = None
    fixr_impl_max_occurs: Optional[str] = "unbounded"
    fixr_which: Optional[Union[str, "OrchestraMemberSelection"]] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraStructureMemberV10) else OrchestraStructureMemberV10(**as_dict(v)) for v in self.fixr_members]

        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_num_in_group is not None and not isinstance(self.fixr_num_in_group, OrchestraFieldRefV10):
            self.fixr_num_in_group = OrchestraFieldRefV10(**as_dict(self.fixr_num_in_group))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_category is not None and not isinstance(self.fixr_category, str):
            self.fixr_category = str(self.fixr_category)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        if self.fixr_impl_min_occurs is not None and not isinstance(self.fixr_impl_min_occurs, int):
            self.fixr_impl_min_occurs = int(self.fixr_impl_min_occurs)

        if self.fixr_impl_max_occurs is not None and not isinstance(self.fixr_impl_max_occurs, str):
            self.fixr_impl_max_occurs = str(self.fixr_impl_max_occurs)

        if self.fixr_which is not None and not isinstance(self.fixr_which, OrchestraMemberSelection):
            self.fixr_which = OrchestraMemberSelection(self.fixr_which)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraGroupsV10(YAMLRoot):
    """
    The repeating groups a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraGroupsV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraGroupsV10"
    class_name: ClassVar[str] = "OrchestraGroupsV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraGroupsV10

    fixr_group: Union[Union[dict, OrchestraGroupV10], list[Union[dict, OrchestraGroupV10]]] = None
    xml_base: Optional[Union[str, URI]] = None
    fixr_latest_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_group):
            self.MissingRequiredField("fixr_group")
        self._normalize_inlined_as_list(slot_name="fixr_group", slot_type=OrchestraGroupV10, key_name="fixr_id", keyed=False)

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        if self.fixr_latest_ep is not None and not isinstance(self.fixr_latest_ep, int):
            self.fixr_latest_ep = int(self.fixr_latest_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraIdentifierV10(YAMLRoot):
    """
    A field that a message sent by an action sets, or carries over from the message received, by tag number.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraIdentifierV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraIdentifierV10"
    class_name: ClassVar[str] = "OrchestraIdentifierV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraIdentifierV10

    fixr_id: int = None
    fixr_source_id: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self.fixr_source_id is not None and not isinstance(self.fixr_source_id, int):
            self.fixr_source_id = int(self.fixr_source_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraIdentifiersMemberV10(YAMLRoot):
    """
    One entry of a message's identifiers, a field carried over or a field set. It holds exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraIdentifiersMemberV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraIdentifiersMemberV10"
    class_name: ClassVar[str] = "OrchestraIdentifiersMemberV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraIdentifiersMemberV10

    fixr_correlate: Optional[Union[dict, OrchestraIdentifierV10]] = None
    fixr_assign: Optional[Union[dict, OrchestraIdentifierV10]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_correlate is not None and not isinstance(self.fixr_correlate, OrchestraIdentifierV10):
            self.fixr_correlate = OrchestraIdentifierV10(**as_dict(self.fixr_correlate))

        if self.fixr_assign is not None and not isinstance(self.fixr_assign, OrchestraIdentifierV10):
            self.fixr_assign = OrchestraIdentifierV10(**as_dict(self.fixr_assign))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraIdentifiersV10(YAMLRoot):
    """
    The fields a message sent by an action sets or carries over.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraIdentifiersV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraIdentifiersV10"
    class_name: ClassVar[str] = "OrchestraIdentifiersV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraIdentifiersV10

    fixr_members: Union[Union[dict, OrchestraIdentifiersMemberV10], list[Union[dict, OrchestraIdentifiersMemberV10]]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraIdentifiersMemberV10) else OrchestraIdentifiersMemberV10(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraIdentityV10Mixin(YAMLRoot):
    """
    The keys of a defined element, its number, name, short name and scenario.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraIdentityV10Mixin"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraIdentityV10Mixin"
    class_name: ClassVar[str] = "OrchestraIdentityV10Mixin"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraIdentityV10Mixin

    fixr_id: int = None
    fixr_name: str = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfaceAnnotationMemberV10(YAMLRoot):
    """
    One part of an annotation in an interfaces file, a text or a hint for software. It holds exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfaceAnnotationMemberV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfaceAnnotationMemberV10"
    class_name: ClassVar[str] = "OrchestraInterfaceAnnotationMemberV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfaceAnnotationMemberV10

    fixi_documentation: Optional[Union[dict, "OrchestraInterfaceDocumentationV10"]] = None
    fixi_appinfo: Optional[Union[dict, "OrchestraInterfaceAppinfoV10"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_documentation is not None and not isinstance(self.fixi_documentation, OrchestraInterfaceDocumentationV10):
            self.fixi_documentation = OrchestraInterfaceDocumentationV10(**as_dict(self.fixi_documentation))

        if self.fixi_appinfo is not None and not isinstance(self.fixi_appinfo, OrchestraInterfaceAppinfoV10):
            self.fixi_appinfo = OrchestraInterfaceAppinfoV10(**as_dict(self.fixi_appinfo))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfaceAnnotationV10(YAMLRoot):
    """
    Notes for readers and hints for software, attached to an element of an interfaces file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfaceAnnotationV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfaceAnnotationV10"
    class_name: ClassVar[str] = "OrchestraInterfaceAnnotationV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfaceAnnotationV10

    fixi_members: Union[Union[dict, OrchestraInterfaceAnnotationMemberV10], list[Union[dict, OrchestraInterfaceAnnotationMemberV10]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixi_members):
            self.MissingRequiredField("fixi_members")
        if not isinstance(self.fixi_members, list):
            self.fixi_members = [self.fixi_members] if self.fixi_members is not None else []
        self.fixi_members = [v if isinstance(v, OrchestraInterfaceAnnotationMemberV10) else OrchestraInterfaceAnnotationMemberV10(**as_dict(v)) for v in self.fixi_members]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfaceAppinfoV10(YAMLRoot):
    """
    A hint for a particular tool on an element of an interfaces file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfaceAppinfoV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfaceAppinfoV10"
    class_name: ClassVar[str] = "OrchestraInterfaceAppinfoV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfaceAppinfoV10

    fixi_text: Optional[str] = None
    fixi_any: Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]] = empty_list()
    fixi_spec_url: Optional[Union[str, URI]] = None
    fixi_lang_id: Optional[str] = None
    fixi_purpose: Optional[Union[str, "OrchestraPurpose"]] = None
    fixi_other_attributes: Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_text is not None and not isinstance(self.fixi_text, str):
            self.fixi_text = str(self.fixi_text)

        self._normalize_inlined_as_list(slot_name="fixi_any", slot_type=OrchestraXmlElement, key_name="xml_name", keyed=False)

        if self.fixi_spec_url is not None and not isinstance(self.fixi_spec_url, URI):
            self.fixi_spec_url = URI(self.fixi_spec_url)

        if self.fixi_lang_id is not None and not isinstance(self.fixi_lang_id, str):
            self.fixi_lang_id = str(self.fixi_lang_id)

        if self.fixi_purpose is not None and not isinstance(self.fixi_purpose, (OrchestraPurpose, str)):
            value = self.fixi_purpose
            for _coerce in (lambda: OrchestraPurpose(value), lambda: str(value)):
                try:
                    self.fixi_purpose = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraPurpose, str] could be constructed from {value!r} for slot fixi_purpose")

        self._normalize_inlined_as_list(slot_name="fixi_other_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfaceDocumentationV10(YAMLRoot):
    """
    Text about an element of an interfaces file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfaceDocumentationV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfaceDocumentationV10"
    class_name: ClassVar[str] = "OrchestraInterfaceDocumentationV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfaceDocumentationV10

    fixi_text: Optional[str] = None
    fixi_any: Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]] = empty_list()
    fixi_lang_id: Optional[str] = None
    fixi_purpose: Optional[Union[str, "OrchestraPurpose"]] = None
    fixi_content_type: Optional[str] = "text/plain"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_text is not None and not isinstance(self.fixi_text, str):
            self.fixi_text = str(self.fixi_text)

        self._normalize_inlined_as_list(slot_name="fixi_any", slot_type=OrchestraXmlElement, key_name="xml_name", keyed=False)

        if self.fixi_lang_id is not None and not isinstance(self.fixi_lang_id, str):
            self.fixi_lang_id = str(self.fixi_lang_id)

        if self.fixi_purpose is not None and not isinstance(self.fixi_purpose, (OrchestraPurpose, str)):
            value = self.fixi_purpose
            for _coerce in (lambda: OrchestraPurpose(value), lambda: str(value)):
                try:
                    self.fixi_purpose = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraPurpose, str] could be constructed from {value!r} for slot fixi_purpose")

        if self.fixi_content_type is not None and not isinstance(self.fixi_content_type, str):
            self.fixi_content_type = str(self.fixi_content_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfaceV10(OrchestraBaseInterfaceV10):
    """
    A named service offering and the sessions it carries, with the protocols on each layer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfaceV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfaceV10"
    class_name: ClassVar[str] = "OrchestraInterfaceV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfaceV10

    fixi_name: str = None
    fixi_sessions: Optional[Union[dict, "OrchestraSessionsV10"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_sessions is not None and not isinstance(self.fixi_sessions, OrchestraSessionsV10):
            self.fixi_sessions = OrchestraSessionsV10(**as_dict(self.fixi_sessions))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfacesV10(YAMLRoot):
    """
    A description of the services and sessions a party offers and how to reach them, headed by its Dublin Core
    metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfacesV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfacesV10"
    class_name: ClassVar[str] = "OrchestraInterfacesV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfacesV10

    fixi_metadata: Union[dict, OrchestraMetadata] = None
    fixi_interface: Optional[Union[Union[dict, OrchestraInterfaceV10], list[Union[dict, OrchestraInterfaceV10]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixi_metadata):
            self.MissingRequiredField("fixi_metadata")
        if not isinstance(self.fixi_metadata, OrchestraMetadata):
            self.fixi_metadata = OrchestraMetadata(**as_dict(self.fixi_metadata))

        self._normalize_inlined_as_list(slot_name="fixi_interface", slot_type=OrchestraInterfaceV10, key_name="fixi_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraMappedDatatypeV10(YAMLRoot):
    """
    How a FIX datatype is written in another standard, such as XML Schema or protocol buffers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMappedDatatypeV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMappedDatatypeV10"
    class_name: ClassVar[str] = "OrchestraMappedDatatypeV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMappedDatatypeV10

    fixr_standard: Union[str, "OrchestraDatatypeStandardV10"] = None
    fixr_extension: Optional[Union[dict, OrchestraDatatypeExtensionV10]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_builtin: Optional[Union[bool, Bool]] = None
    fixr_base: Optional[str] = None
    fixr_pattern: Optional[str] = None
    fixr_element: Optional[str] = None
    fixr_parameter: Optional[str] = None
    fixr_min_inclusive: Optional[str] = None
    fixr_max_inclusive: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_standard):
            self.MissingRequiredField("fixr_standard")
        if not isinstance(self.fixr_standard, (OrchestraDatatypeStandardV10, str)):
            value = self.fixr_standard
            for _coerce in (lambda: OrchestraDatatypeStandardV10(value), lambda: str(value)):
                try:
                    self.fixr_standard = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraDatatypeStandardV10, str] could be constructed from {value!r} for slot fixr_standard")

        if self.fixr_extension is not None and not isinstance(self.fixr_extension, OrchestraDatatypeExtensionV10):
            self.fixr_extension = OrchestraDatatypeExtensionV10(**as_dict(self.fixr_extension))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_builtin is not None and not isinstance(self.fixr_builtin, Bool):
            self.fixr_builtin = Bool(self.fixr_builtin)

        if self.fixr_base is not None and not isinstance(self.fixr_base, str):
            self.fixr_base = str(self.fixr_base)

        if self.fixr_pattern is not None and not isinstance(self.fixr_pattern, str):
            self.fixr_pattern = str(self.fixr_pattern)

        if self.fixr_element is not None and not isinstance(self.fixr_element, str):
            self.fixr_element = str(self.fixr_element)

        if self.fixr_parameter is not None and not isinstance(self.fixr_parameter, str):
            self.fixr_parameter = str(self.fixr_parameter)

        if self.fixr_min_inclusive is not None and not isinstance(self.fixr_min_inclusive, str):
            self.fixr_min_inclusive = str(self.fixr_min_inclusive)

        if self.fixr_max_inclusive is not None and not isinstance(self.fixr_max_inclusive, str):
            self.fixr_max_inclusive = str(self.fixr_max_inclusive)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraMessageRefV10(YAMLRoot):
    """
    A message an action sends, by its number and type code, with the fields it sets or carries over.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMessageRefV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMessageRefV10"
    class_name: ClassVar[str] = "OrchestraMessageRefV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMessageRefV10

    fixr_name: str = None
    fixr_id: int = None
    fixr_identifiers: Optional[Union[dict, OrchestraIdentifiersV10]] = None
    fixr_msg_type: Optional[str] = None
    fixr_impl_min_occurs: Optional[int] = 1
    fixr_impl_max_occurs: Optional[str] = "unbounded"
    fixr_scenario: Optional[str] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self.fixr_identifiers is not None and not isinstance(self.fixr_identifiers, OrchestraIdentifiersV10):
            self.fixr_identifiers = OrchestraIdentifiersV10(**as_dict(self.fixr_identifiers))

        if self.fixr_msg_type is not None and not isinstance(self.fixr_msg_type, str):
            self.fixr_msg_type = str(self.fixr_msg_type)

        if self.fixr_impl_min_occurs is not None and not isinstance(self.fixr_impl_min_occurs, int):
            self.fixr_impl_min_occurs = int(self.fixr_impl_min_occurs)

        if self.fixr_impl_max_occurs is not None and not isinstance(self.fixr_impl_max_occurs, str):
            self.fixr_impl_max_occurs = str(self.fixr_impl_max_occurs)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraMessageStructureV10(YAMLRoot):
    """
    The ordered fields, groups and components of a message.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMessageStructureV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMessageStructureV10"
    class_name: ClassVar[str] = "OrchestraMessageStructureV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMessageStructureV10

    fixr_members: Union[Union[dict, "OrchestraStructureMemberV10"], list[Union[dict, "OrchestraStructureMemberV10"]]] = None
    fixr_which: Optional[Union[str, "OrchestraMemberSelection"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraStructureMemberV10) else OrchestraStructureMemberV10(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_which is not None and not isinstance(self.fixr_which, OrchestraMemberSelection):
            self.fixr_which = OrchestraMemberSelection(self.fixr_which)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraMessageV10(YAMLRoot):
    """
    A FIX message: its type code, the fields, groups and components it carries in order, and the responses it can
    cause.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMessageV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMessageV10"
    class_name: ClassVar[str] = "OrchestraMessageV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMessageV10

    fixr_structure: Union[dict, OrchestraMessageStructureV10] = None
    fixr_id: int = None
    fixr_name: str = None
    fixr_responses: Optional[Union[dict, "OrchestraResponsesV10"]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_msg_type: Optional[str] = None
    fixr_category: Optional[str] = None
    fixr_flow: Optional[str] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_structure):
            self.MissingRequiredField("fixr_structure")
        if not isinstance(self.fixr_structure, OrchestraMessageStructureV10):
            self.fixr_structure = OrchestraMessageStructureV10(**as_dict(self.fixr_structure))

        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_responses is not None and not isinstance(self.fixr_responses, OrchestraResponsesV10):
            self.fixr_responses = OrchestraResponsesV10(**as_dict(self.fixr_responses))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_msg_type is not None and not isinstance(self.fixr_msg_type, str):
            self.fixr_msg_type = str(self.fixr_msg_type)

        if self.fixr_category is not None and not isinstance(self.fixr_category, str):
            self.fixr_category = str(self.fixr_category)

        if self.fixr_flow is not None and not isinstance(self.fixr_flow, str):
            self.fixr_flow = str(self.fixr_flow)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraMessagesV10(YAMLRoot):
    """
    The messages a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMessagesV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMessagesV10"
    class_name: ClassVar[str] = "OrchestraMessagesV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMessagesV10

    fixr_message: Union[Union[dict, OrchestraMessageV10], list[Union[dict, OrchestraMessageV10]]] = None
    xml_base: Optional[Union[str, URI]] = None
    fixr_latest_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_message):
            self.MissingRequiredField("fixr_message")
        self._normalize_inlined_as_list(slot_name="fixr_message", slot_type=OrchestraMessageV10, key_name="fixr_id", keyed=False)

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        if self.fixr_latest_ep is not None and not isinstance(self.fixr_latest_ep, int):
            self.fixr_latest_ep = int(self.fixr_latest_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraPedigreeV10Mixin(YAMLRoot):
    """
    When an element was added, changed, deprecated or replaced, by FIX version and extension pack, and whether it is
    supported.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraPedigreeV10Mixin"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraPedigreeV10Mixin"
    class_name: ClassVar[str] = "OrchestraPedigreeV10Mixin"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraPedigreeV10Mixin

    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraProtocolV10(YAMLRoot):
    """
    A protocol used on one layer of an interface or session, with its version, layer and delivery guarantee.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraProtocolV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraProtocolV10"
    class_name: ClassVar[str] = "OrchestraProtocolV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraProtocolV10

    fixi_annotation: Optional[Union[dict, OrchestraInterfaceAnnotationV10]] = None
    fixi_name: Optional[Union[str, "OrchestraProtocolName"]] = None
    fixi_version: Optional[str] = None
    fixi_layer: Optional[Union[str, "OrchestraLayer"]] = None
    fixi_reliability: Optional[Union[str, "OrchestraReliability"]] = None
    fixi_orchestration: Optional[Union[str, URI]] = None
    fixi_other_attributes: Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_annotation is not None and not isinstance(self.fixi_annotation, OrchestraInterfaceAnnotationV10):
            self.fixi_annotation = OrchestraInterfaceAnnotationV10(**as_dict(self.fixi_annotation))

        if self.fixi_name is not None and not isinstance(self.fixi_name, (OrchestraProtocolName, str)):
            value = self.fixi_name
            for _coerce in (lambda: OrchestraProtocolName(value), lambda: str(value)):
                try:
                    self.fixi_name = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraProtocolName, str] could be constructed from {value!r} for slot fixi_name")

        if self.fixi_version is not None and not isinstance(self.fixi_version, str):
            self.fixi_version = str(self.fixi_version)

        if self.fixi_layer is not None and not isinstance(self.fixi_layer, OrchestraLayer):
            self.fixi_layer = OrchestraLayer(self.fixi_layer)

        if self.fixi_reliability is not None and not isinstance(self.fixi_reliability, OrchestraReliability):
            self.fixi_reliability = OrchestraReliability(self.fixi_reliability)

        if self.fixi_orchestration is not None and not isinstance(self.fixi_orchestration, URI):
            self.fixi_orchestration = URI(self.fixi_orchestration)

        self._normalize_inlined_as_list(slot_name="fixi_other_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        super().__post_init__(**kwargs)


class OrchestraEncodingV10(OrchestraProtocolV10):
    """
    An encoding used on an interface or session, such as tag=value, FIXML or SBE.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraEncodingV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraEncodingV10"
    class_name: ClassVar[str] = "OrchestraEncodingV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraEncodingV10


@dataclass(repr=False)
class OrchestraReferenceV10Mixin(YAMLRoot):
    """
    The keys by which a use points at a defined element: its number, its scenario and, as a convenience, its name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraReferenceV10Mixin"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraReferenceV10Mixin"
    class_name: ClassVar[str] = "OrchestraReferenceV10Mixin"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraReferenceV10Mixin

    fixr_id: int = None
    fixr_scenario: Optional[str] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraRepositoryV10(YAMLRoot):
    """
    A machine-readable set of rules of engagement: the datatypes, code sets, fields, components, groups and messages
    it defines, and the actors and workflows that use them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraRepositoryV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraRepositoryV10"
    class_name: ClassVar[str] = "OrchestraRepositoryV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraRepositoryV10

    fixr_metadata: Union[dict, OrchestraMetadata] = None
    fixr_datatypes: Union[dict, OrchestraDatatypesV10] = None
    fixr_code_sets: Union[dict, OrchestraCodeSetsV10] = None
    fixr_fields: Union[dict, OrchestraFieldsV10] = None
    fixr_messages: Union[dict, OrchestraMessagesV10] = None
    fixr_name: str = None
    fixr_version: str = None
    fixr_categories: Optional[Union[dict, OrchestraCategoriesV10]] = None
    fixr_sections: Optional[Union[dict, "OrchestraSectionsV10"]] = None
    fixr_actors: Optional[Union[dict, OrchestraActorsV10]] = None
    fixr_components: Optional[Union[dict, OrchestraComponentsV10]] = None
    fixr_groups: Optional[Union[dict, OrchestraGroupsV10]] = None
    fixr_concepts: Optional[Union[dict, OrchestraConceptsV10]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_guid: Optional[str] = None
    fixr_spec_url: Optional[Union[str, URI]] = None
    fixr_namespace: Optional[Union[str, URI]] = None
    fixr_appl_ver_id: Optional[str] = None
    fixr_expression_language: Optional[str] = "Score"
    fixr_latest_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_metadata):
            self.MissingRequiredField("fixr_metadata")
        if not isinstance(self.fixr_metadata, OrchestraMetadata):
            self.fixr_metadata = OrchestraMetadata(**as_dict(self.fixr_metadata))

        if self._is_empty(self.fixr_datatypes):
            self.MissingRequiredField("fixr_datatypes")
        if not isinstance(self.fixr_datatypes, OrchestraDatatypesV10):
            self.fixr_datatypes = OrchestraDatatypesV10(**as_dict(self.fixr_datatypes))

        if self._is_empty(self.fixr_code_sets):
            self.MissingRequiredField("fixr_code_sets")
        if not isinstance(self.fixr_code_sets, OrchestraCodeSetsV10):
            self.fixr_code_sets = OrchestraCodeSetsV10(**as_dict(self.fixr_code_sets))

        if self._is_empty(self.fixr_fields):
            self.MissingRequiredField("fixr_fields")
        if not isinstance(self.fixr_fields, OrchestraFieldsV10):
            self.fixr_fields = OrchestraFieldsV10(**as_dict(self.fixr_fields))

        if self._is_empty(self.fixr_messages):
            self.MissingRequiredField("fixr_messages")
        if not isinstance(self.fixr_messages, OrchestraMessagesV10):
            self.fixr_messages = OrchestraMessagesV10(**as_dict(self.fixr_messages))

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self._is_empty(self.fixr_version):
            self.MissingRequiredField("fixr_version")
        if not isinstance(self.fixr_version, str):
            self.fixr_version = str(self.fixr_version)

        if self.fixr_categories is not None and not isinstance(self.fixr_categories, OrchestraCategoriesV10):
            self.fixr_categories = OrchestraCategoriesV10(**as_dict(self.fixr_categories))

        if self.fixr_sections is not None and not isinstance(self.fixr_sections, OrchestraSectionsV10):
            self.fixr_sections = OrchestraSectionsV10(**as_dict(self.fixr_sections))

        if self.fixr_actors is not None and not isinstance(self.fixr_actors, OrchestraActorsV10):
            self.fixr_actors = OrchestraActorsV10(**as_dict(self.fixr_actors))

        if self.fixr_components is not None and not isinstance(self.fixr_components, OrchestraComponentsV10):
            self.fixr_components = OrchestraComponentsV10(**as_dict(self.fixr_components))

        if self.fixr_groups is not None and not isinstance(self.fixr_groups, OrchestraGroupsV10):
            self.fixr_groups = OrchestraGroupsV10(**as_dict(self.fixr_groups))

        if self.fixr_concepts is not None and not isinstance(self.fixr_concepts, OrchestraConceptsV10):
            self.fixr_concepts = OrchestraConceptsV10(**as_dict(self.fixr_concepts))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_guid is not None and not isinstance(self.fixr_guid, str):
            self.fixr_guid = str(self.fixr_guid)

        if self.fixr_spec_url is not None and not isinstance(self.fixr_spec_url, URI):
            self.fixr_spec_url = URI(self.fixr_spec_url)

        if self.fixr_namespace is not None and not isinstance(self.fixr_namespace, URI):
            self.fixr_namespace = URI(self.fixr_namespace)

        if self.fixr_appl_ver_id is not None and not isinstance(self.fixr_appl_ver_id, str):
            self.fixr_appl_ver_id = str(self.fixr_appl_ver_id)

        if self.fixr_expression_language is not None and not isinstance(self.fixr_expression_language, str):
            self.fixr_expression_language = str(self.fixr_expression_language)

        if self.fixr_latest_ep is not None and not isinstance(self.fixr_latest_ep, int):
            self.fixr_latest_ep = int(self.fixr_latest_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraResponseV10(OrchestraActionV10):
    """
    What happens when a message arrives, under an optional condition: messages sent, values set, transitions fired and
    timers scheduled.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraResponseV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraResponseV10"
    class_name: ClassVar[str] = "OrchestraResponseV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraResponseV10

    fixr_actions: Union[Union[dict, OrchestraActionStepV10], list[Union[dict, OrchestraActionStepV10]]] = None
    fixr_when: Optional[str] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_name: Optional[str] = None
    fixr_sync: Optional[Union[str, "OrchestraSynchronization"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_when is not None and not isinstance(self.fixr_when, str):
            self.fixr_when = str(self.fixr_when)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_sync is not None and not isinstance(self.fixr_sync, OrchestraSynchronization):
            self.fixr_sync = OrchestraSynchronization(self.fixr_sync)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraResponsesV10(YAMLRoot):
    """
    The responses a message can cause, tried one after another as given.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraResponsesV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraResponsesV10"
    class_name: ClassVar[str] = "OrchestraResponsesV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraResponsesV10

    fixr_response: Union[Union[dict, OrchestraResponseV10], list[Union[dict, OrchestraResponseV10]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_response):
            self.MissingRequiredField("fixr_response")
        if not isinstance(self.fixr_response, list):
            self.fixr_response = [self.fixr_response] if self.fixr_response is not None else []
        self.fixr_response = [v if isinstance(v, OrchestraResponseV10) else OrchestraResponseV10(**as_dict(v)) for v in self.fixr_response]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraSectionV10(YAMLRoot):
    """
    A broad business area, such as pre-trade or post-trade, that categories fall under.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSectionV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSectionV10"
    class_name: ClassVar[str] = "OrchestraSectionV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSectionV10

    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None
    fixr_name: Optional[str] = None
    fixr_display_order: Optional[int] = None
    fixr_fixml_file_name: Optional[str] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_display_order is not None and not isinstance(self.fixr_display_order, int):
            self.fixr_display_order = int(self.fixr_display_order)

        if self.fixr_fixml_file_name is not None and not isinstance(self.fixr_fixml_file_name, str):
            self.fixr_fixml_file_name = str(self.fixr_fixml_file_name)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraSectionsV10(YAMLRoot):
    """
    The sections a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSectionsV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSectionsV10"
    class_name: ClassVar[str] = "OrchestraSectionsV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSectionsV10

    fixr_section: Union[Union[dict, OrchestraSectionV10], list[Union[dict, OrchestraSectionV10]]] = None
    xml_base: Optional[Union[str, URI]] = None
    fixr_latest_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_section):
            self.MissingRequiredField("fixr_section")
        if not isinstance(self.fixr_section, list):
            self.fixr_section = [self.fixr_section] if self.fixr_section is not None else []
        self.fixr_section = [v if isinstance(v, OrchestraSectionV10) else OrchestraSectionV10(**as_dict(v)) for v in self.fixr_section]

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        if self.fixr_latest_ep is not None and not isinstance(self.fixr_latest_ep, int):
            self.fixr_latest_ep = int(self.fixr_latest_ep)

        super().__post_init__(**kwargs)


class OrchestraServiceV10(OrchestraProtocolV10):
    """
    An application-level service an interface offers, such as order routing, with the Orchestra repository that sets
    out its rules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraServiceV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraServiceV10"
    class_name: ClassVar[str] = "OrchestraServiceV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraServiceV10


@dataclass(repr=False)
class OrchestraSessionIdentifierV10(YAMLRoot):
    """
    A value, with what kind it is, that picks out a session, such as a sender or target ID.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSessionIdentifierV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSessionIdentifierV10"
    class_name: ClassVar[str] = "OrchestraSessionIdentifierV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSessionIdentifierV10

    fixi_text: Optional[str] = None
    fixi_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_text is not None and not isinstance(self.fixi_text, str):
            self.fixi_text = str(self.fixi_text)

        if self.fixi_name is not None and not isinstance(self.fixi_name, str):
            self.fixi_name = str(self.fixi_name)

        super().__post_init__(**kwargs)


class OrchestraSessionProtocolV10(OrchestraProtocolV10):
    """
    The session-level protocol of an interface or session, such as FIXT or FIXP.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSessionProtocolV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSessionProtocolV10"
    class_name: ClassVar[str] = "OrchestraSessionProtocolV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSessionProtocolV10


@dataclass(repr=False)
class OrchestraSessionV10(OrchestraBaseInterfaceV10):
    """
    One connection between two parties, with the identifiers, role, activation times and security keys that set it up.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSessionV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSessionV10"
    class_name: ClassVar[str] = "OrchestraSessionV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSessionV10

    fixi_name: str = None
    fixi_identifier: Optional[Union[Union[dict, OrchestraSessionIdentifierV10], list[Union[dict, OrchestraSessionIdentifierV10]]]] = empty_list()
    fixi_activation_time: Optional[str] = None
    fixi_deactivation_time: Optional[str] = None
    fixi_role: Optional[Union[str, "OrchestraRole"]] = None
    fixi_security_keys: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.fixi_identifier, list):
            self.fixi_identifier = [self.fixi_identifier] if self.fixi_identifier is not None else []
        self.fixi_identifier = [v if isinstance(v, OrchestraSessionIdentifierV10) else OrchestraSessionIdentifierV10(**as_dict(v)) for v in self.fixi_identifier]

        if self.fixi_activation_time is not None and not isinstance(self.fixi_activation_time, str):
            self.fixi_activation_time = str(self.fixi_activation_time)

        if self.fixi_deactivation_time is not None and not isinstance(self.fixi_deactivation_time, str):
            self.fixi_deactivation_time = str(self.fixi_deactivation_time)

        if self.fixi_role is not None and not isinstance(self.fixi_role, OrchestraRole):
            self.fixi_role = OrchestraRole(self.fixi_role)

        if self.fixi_security_keys is not None and not isinstance(self.fixi_security_keys, str):
            self.fixi_security_keys = str(self.fixi_security_keys)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraSessionsV10(YAMLRoot):
    """
    The sessions an interface carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSessionsV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSessionsV10"
    class_name: ClassVar[str] = "OrchestraSessionsV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSessionsV10

    fixi_session: Union[Union[dict, OrchestraSessionV10], list[Union[dict, OrchestraSessionV10]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixi_session):
            self.MissingRequiredField("fixi_session")
        self._normalize_inlined_as_list(slot_name="fixi_session", slot_type=OrchestraSessionV10, key_name="fixi_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraStateMachineV10(YAMLRoot):
    """
    A named set of states that an actor moves through, from an initial state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraStateMachineV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraStateMachineV10"
    class_name: ClassVar[str] = "OrchestraStateMachineV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraStateMachineV10

    fixr_initial: Union[dict, "OrchestraStateV10"] = None
    fixr_state: Union[Union[dict, "OrchestraStateV10"], list[Union[dict, "OrchestraStateV10"]]] = None
    fixr_name: str = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_initial):
            self.MissingRequiredField("fixr_initial")
        if not isinstance(self.fixr_initial, OrchestraStateV10):
            self.fixr_initial = OrchestraStateV10(**as_dict(self.fixr_initial))

        if self._is_empty(self.fixr_state):
            self.MissingRequiredField("fixr_state")
        self._normalize_inlined_as_list(slot_name="fixr_state", slot_type=OrchestraStateV10, key_name="fixr_name", keyed=False)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraStateV10(YAMLRoot):
    """
    One of a state machine's states, with the transitions out of it and what happens on entry, while active and on
    exit.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraStateV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraStateV10"
    class_name: ClassVar[str] = "OrchestraStateV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraStateV10

    fixr_name: str = None
    fixr_transition: Optional[Union[Union[dict, "OrchestraTransitionV10"], list[Union[dict, "OrchestraTransitionV10"]]]] = empty_list()
    fixr_onentry: Optional[Union[dict, OrchestraActionV10]] = None
    fixr_activity: Optional[Union[dict, OrchestraActionV10]] = None
    fixr_onexit: Optional[Union[dict, OrchestraActionV10]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        self._normalize_inlined_as_list(slot_name="fixr_transition", slot_type=OrchestraTransitionV10, key_name="fixr_name", keyed=False)

        if self.fixr_onentry is not None and not isinstance(self.fixr_onentry, OrchestraActionV10):
            self.fixr_onentry = OrchestraActionV10(**as_dict(self.fixr_onentry))

        if self.fixr_activity is not None and not isinstance(self.fixr_activity, OrchestraActionV10):
            self.fixr_activity = OrchestraActionV10(**as_dict(self.fixr_activity))

        if self.fixr_onexit is not None and not isinstance(self.fixr_onexit, OrchestraActionV10):
            self.fixr_onexit = OrchestraActionV10(**as_dict(self.fixr_onexit))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraStructureMemberV10(YAMLRoot):
    """
    One item of an ordered structure, a component, a group or a field, by reference. It holds exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraStructureMemberV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraStructureMemberV10"
    class_name: ClassVar[str] = "OrchestraStructureMemberV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraStructureMemberV10

    fixr_component_ref: Optional[Union[dict, OrchestraComponentRefV10]] = None
    fixr_group_ref: Optional[Union[dict, OrchestraGroupRefV10]] = None
    fixr_field_ref: Optional[Union[dict, OrchestraFieldRefV10]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_component_ref is not None and not isinstance(self.fixr_component_ref, OrchestraComponentRefV10):
            self.fixr_component_ref = OrchestraComponentRefV10(**as_dict(self.fixr_component_ref))

        if self.fixr_group_ref is not None and not isinstance(self.fixr_group_ref, OrchestraGroupRefV10):
            self.fixr_group_ref = OrchestraGroupRefV10(**as_dict(self.fixr_group_ref))

        if self.fixr_field_ref is not None and not isinstance(self.fixr_field_ref, OrchestraFieldRefV10):
            self.fixr_field_ref = OrchestraFieldRefV10(**as_dict(self.fixr_field_ref))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraTimerScheduleV10(YAMLRoot):
    """
    A step that starts, stops or restarts an actor's timer, with its interval and what to do when it runs out.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraTimerScheduleV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraTimerScheduleV10"
    class_name: ClassVar[str] = "OrchestraTimerScheduleV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraTimerScheduleV10

    fixr_activity: Union[dict, OrchestraActionV10] = None
    fixr_actor: str = None
    fixr_name: str = None
    fixr_operation: Union[str, "OrchestraTimerOperation"] = None
    fixr_interval: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_activity):
            self.MissingRequiredField("fixr_activity")
        if not isinstance(self.fixr_activity, OrchestraActionV10):
            self.fixr_activity = OrchestraActionV10(**as_dict(self.fixr_activity))

        if self._is_empty(self.fixr_actor):
            self.MissingRequiredField("fixr_actor")
        if not isinstance(self.fixr_actor, str):
            self.fixr_actor = str(self.fixr_actor)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self._is_empty(self.fixr_operation):
            self.MissingRequiredField("fixr_operation")
        if not isinstance(self.fixr_operation, OrchestraTimerOperation):
            self.fixr_operation = OrchestraTimerOperation(self.fixr_operation)

        if self.fixr_interval is not None and not isinstance(self.fixr_interval, str):
            self.fixr_interval = str(self.fixr_interval)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraTimerV10(YAMLRoot):
    """
    A named timer that an actor owns.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraTimerV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraTimerV10"
    class_name: ClassVar[str] = "OrchestraTimerV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraTimerV10

    fixr_name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraTransitionV10(YAMLRoot):
    """
    A move from one state to a named target state, with the condition that allows it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraTransitionV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraTransitionV10"
    class_name: ClassVar[str] = "OrchestraTransitionV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraTransitionV10

    fixr_name: str = None
    fixr_target: str = None
    fixr_when: Optional[str] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV10]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self._is_empty(self.fixr_target):
            self.MissingRequiredField("fixr_target")
        if not isinstance(self.fixr_target, str):
            self.fixr_target = str(self.fixr_target)

        if self.fixr_when is not None and not isinstance(self.fixr_when, str):
            self.fixr_when = str(self.fixr_when)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV10):
            self.fixr_annotation = OrchestraAnnotationV10(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraTransportV10(OrchestraProtocolV10):
    """
    The transport-level protocol of an interface or session, with its address, how messages are cast and its use.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraTransportV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraTransportV10"
    class_name: ClassVar[str] = "OrchestraTransportV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraTransportV10

    fixi_address: Optional[str] = None
    fixi_message_cast: Optional[Union[str, "OrchestraMessageCast"]] = 'unicast'
    fixi_use: Optional[Union[str, "OrchestraTransportUse"]] = None
    fixi_other_attributes: Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_address is not None and not isinstance(self.fixi_address, str):
            self.fixi_address = str(self.fixi_address)

        if self.fixi_message_cast is not None and not isinstance(self.fixi_message_cast, OrchestraMessageCast):
            self.fixi_message_cast = OrchestraMessageCast(self.fixi_message_cast)

        if self.fixi_use is not None and not isinstance(self.fixi_use, (OrchestraTransportUse, str)):
            value = self.fixi_use
            for _coerce in (lambda: OrchestraTransportUse(value), lambda: str(value)):
                try:
                    self.fixi_use = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraTransportUse, str] could be constructed from {value!r} for slot fixi_use")

        self._normalize_inlined_as_list(slot_name="fixi_other_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraTriggerV10(YAMLRoot):
    """
    A step that fires a named transition of an actor's state machine.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraTriggerV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraTriggerV10"
    class_name: ClassVar[str] = "OrchestraTriggerV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraTriggerV10

    fixr_state_machine: str = None
    fixr_actor: str = None
    fixr_name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_state_machine):
            self.MissingRequiredField("fixr_state_machine")
        if not isinstance(self.fixr_state_machine, str):
            self.fixr_state_machine = str(self.fixr_state_machine)

        if self._is_empty(self.fixr_actor):
            self.MissingRequiredField("fixr_actor")
        if not isinstance(self.fixr_actor, str):
            self.fixr_actor = str(self.fixr_actor)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraUniqueV10(YAMLRoot):
    """
    A check that a field's value is unique among the values that share the other fields it names, or among all values
    when it names none.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraUniqueV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraUniqueV10"
    class_name: ClassVar[str] = "OrchestraUniqueV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraUniqueV10

    fixr_field_ref: Optional[Union[Union[dict, OrchestraFieldRefV10], list[Union[dict, OrchestraFieldRefV10]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_field_ref", slot_type=OrchestraFieldRefV10, key_name="fixr_id", keyed=False)

        super().__post_init__(**kwargs)


class OrchestraUserInterfaceV10(OrchestraProtocolV10):
    """
    A user interface an interface offers, such as a trading screen, described as a protocol.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraUserInterfaceV10"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraUserInterfaceV10"
    class_name: ClassVar[str] = "OrchestraUserInterfaceV10"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraUserInterfaceV10


@dataclass(repr=False)
class OrchestraActionParameterV11(YAMLRoot):
    """
    One input to an action, which is a field, component or group, defined in place or named by reference. It holds
    exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActionParameterV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActionParameterV11"
    class_name: ClassVar[str] = "OrchestraActionParameterV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActionParameterV11

    fixr_field: Optional[Union[dict, "OrchestraFieldV11"]] = None
    fixr_field_ref: Optional[Union[dict, "OrchestraFieldRefV11"]] = None
    fixr_component: Optional[Union[dict, "OrchestraComponentV11"]] = None
    fixr_component_ref: Optional[Union[dict, "OrchestraComponentRefV11"]] = None
    fixr_group: Optional[Union[dict, "OrchestraGroupV11"]] = None
    fixr_group_ref: Optional[Union[dict, "OrchestraGroupRefV11"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_field is not None and not isinstance(self.fixr_field, OrchestraFieldV11):
            self.fixr_field = OrchestraFieldV11(**as_dict(self.fixr_field))

        if self.fixr_field_ref is not None and not isinstance(self.fixr_field_ref, OrchestraFieldRefV11):
            self.fixr_field_ref = OrchestraFieldRefV11(**as_dict(self.fixr_field_ref))

        if self.fixr_component is not None and not isinstance(self.fixr_component, OrchestraComponentV11):
            self.fixr_component = OrchestraComponentV11(**as_dict(self.fixr_component))

        if self.fixr_component_ref is not None and not isinstance(self.fixr_component_ref, OrchestraComponentRefV11):
            self.fixr_component_ref = OrchestraComponentRefV11(**as_dict(self.fixr_component_ref))

        if self.fixr_group is not None and not isinstance(self.fixr_group, OrchestraGroupV11):
            self.fixr_group = OrchestraGroupV11(**as_dict(self.fixr_group))

        if self.fixr_group_ref is not None and not isinstance(self.fixr_group_ref, OrchestraGroupRefV11):
            self.fixr_group_ref = OrchestraGroupRefV11(**as_dict(self.fixr_group_ref))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActionStepV11(YAMLRoot):
    """
    One thing an action does: send a message, set a value, fire a transition or schedule a timer. It holds exactly one
    of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActionStepV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActionStepV11"
    class_name: ClassVar[str] = "OrchestraActionStepV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActionStepV11

    fixr_message_ref: Optional[Union[dict, "OrchestraMessageRefV11"]] = None
    fixr_assign: Optional[str] = None
    fixr_trigger: Optional[Union[dict, "OrchestraTriggerV11"]] = None
    fixr_timer_schedule: Optional[Union[dict, "OrchestraTimerScheduleV11"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_message_ref is not None and not isinstance(self.fixr_message_ref, OrchestraMessageRefV11):
            self.fixr_message_ref = OrchestraMessageRefV11(**as_dict(self.fixr_message_ref))

        if self.fixr_assign is not None and not isinstance(self.fixr_assign, str):
            self.fixr_assign = str(self.fixr_assign)

        if self.fixr_trigger is not None and not isinstance(self.fixr_trigger, OrchestraTriggerV11):
            self.fixr_trigger = OrchestraTriggerV11(**as_dict(self.fixr_trigger))

        if self.fixr_timer_schedule is not None and not isinstance(self.fixr_timer_schedule, OrchestraTimerScheduleV11):
            self.fixr_timer_schedule = OrchestraTimerScheduleV11(**as_dict(self.fixr_timer_schedule))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActionV11(YAMLRoot):
    """
    Things that happen together, such as when a response fires or a state is entered: messages sent, values set,
    transitions fired and timers scheduled, with their inputs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActionV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActionV11"
    class_name: ClassVar[str] = "OrchestraActionV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActionV11

    fixr_actions: Union[Union[dict, OrchestraActionStepV11], list[Union[dict, OrchestraActionStepV11]]] = None
    fixr_parameters: Optional[Union[Union[dict, OrchestraActionParameterV11], list[Union[dict, OrchestraActionParameterV11]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_actions):
            self.MissingRequiredField("fixr_actions")
        if not isinstance(self.fixr_actions, list):
            self.fixr_actions = [self.fixr_actions] if self.fixr_actions is not None else []
        self.fixr_actions = [v if isinstance(v, OrchestraActionStepV11) else OrchestraActionStepV11(**as_dict(v)) for v in self.fixr_actions]

        if not isinstance(self.fixr_parameters, list):
            self.fixr_parameters = [self.fixr_parameters] if self.fixr_parameters is not None else []
        self.fixr_parameters = [v if isinstance(v, OrchestraActionParameterV11) else OrchestraActionParameterV11(**as_dict(v)) for v in self.fixr_parameters]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActorMemberV11(YAMLRoot):
    """
    One thing an actor keeps: a variable given as a field, component or group, a state machine or a timer. It holds
    exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActorMemberV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActorMemberV11"
    class_name: ClassVar[str] = "OrchestraActorMemberV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActorMemberV11

    fixr_field: Optional[Union[dict, "OrchestraFieldV11"]] = None
    fixr_field_ref: Optional[Union[dict, "OrchestraFieldRefV11"]] = None
    fixr_component: Optional[Union[dict, "OrchestraComponentV11"]] = None
    fixr_component_ref: Optional[Union[dict, "OrchestraComponentRefV11"]] = None
    fixr_group: Optional[Union[dict, "OrchestraGroupV11"]] = None
    fixr_group_ref: Optional[Union[dict, "OrchestraGroupRefV11"]] = None
    fixr_states: Optional[Union[dict, "OrchestraStateMachineV11"]] = None
    fixr_timer: Optional[Union[dict, "OrchestraTimerV11"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_field is not None and not isinstance(self.fixr_field, OrchestraFieldV11):
            self.fixr_field = OrchestraFieldV11(**as_dict(self.fixr_field))

        if self.fixr_field_ref is not None and not isinstance(self.fixr_field_ref, OrchestraFieldRefV11):
            self.fixr_field_ref = OrchestraFieldRefV11(**as_dict(self.fixr_field_ref))

        if self.fixr_component is not None and not isinstance(self.fixr_component, OrchestraComponentV11):
            self.fixr_component = OrchestraComponentV11(**as_dict(self.fixr_component))

        if self.fixr_component_ref is not None and not isinstance(self.fixr_component_ref, OrchestraComponentRefV11):
            self.fixr_component_ref = OrchestraComponentRefV11(**as_dict(self.fixr_component_ref))

        if self.fixr_group is not None and not isinstance(self.fixr_group, OrchestraGroupV11):
            self.fixr_group = OrchestraGroupV11(**as_dict(self.fixr_group))

        if self.fixr_group_ref is not None and not isinstance(self.fixr_group_ref, OrchestraGroupRefV11):
            self.fixr_group_ref = OrchestraGroupRefV11(**as_dict(self.fixr_group_ref))

        if self.fixr_states is not None and not isinstance(self.fixr_states, OrchestraStateMachineV11):
            self.fixr_states = OrchestraStateMachineV11(**as_dict(self.fixr_states))

        if self.fixr_timer is not None and not isinstance(self.fixr_timer, OrchestraTimerV11):
            self.fixr_timer = OrchestraTimerV11(**as_dict(self.fixr_timer))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActorV11(YAMLRoot):
    """
    A kind of party in an exchange, such as a buy-side firm or a venue, with the state it keeps: its variables, state
    machines and timers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActorV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActorV11"
    class_name: ClassVar[str] = "OrchestraActorV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActorV11

    fixr_name: str = None
    fixr_members: Optional[Union[Union[dict, OrchestraActorMemberV11], list[Union[dict, OrchestraActorMemberV11]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, "OrchestraAnnotationV11"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraActorMemberV11) else OrchestraActorMemberV11(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActorsMemberV11(YAMLRoot):
    """
    One entry of the actors list, an actor or a flow. It holds exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActorsMemberV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActorsMemberV11"
    class_name: ClassVar[str] = "OrchestraActorsMemberV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActorsMemberV11

    fixr_actor: Optional[Union[dict, OrchestraActorV11]] = None
    fixr_flow: Optional[Union[dict, "OrchestraFlowV11"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_actor is not None and not isinstance(self.fixr_actor, OrchestraActorV11):
            self.fixr_actor = OrchestraActorV11(**as_dict(self.fixr_actor))

        if self.fixr_flow is not None and not isinstance(self.fixr_flow, OrchestraFlowV11):
            self.fixr_flow = OrchestraFlowV11(**as_dict(self.fixr_flow))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraActorsV11(YAMLRoot):
    """
    The parties a repository describes and the one-way flows between them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraActorsV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraActorsV11"
    class_name: ClassVar[str] = "OrchestraActorsV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraActorsV11

    fixr_members: Optional[Union[Union[dict, OrchestraActorsMemberV11], list[Union[dict, OrchestraActorsMemberV11]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, "OrchestraAnnotationV11"]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraActorsMemberV11) else OrchestraActorsMemberV11(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraAnnotationMemberV11(YAMLRoot):
    """
    One part of an annotation, a piece of text or a hint for software. It holds exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraAnnotationMemberV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraAnnotationMemberV11"
    class_name: ClassVar[str] = "OrchestraAnnotationMemberV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraAnnotationMemberV11

    fixr_documentation: Optional[Union[dict, "OrchestraDocumentationV11"]] = None
    fixr_appinfo: Optional[Union[dict, "OrchestraAppinfoV11"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_documentation is not None and not isinstance(self.fixr_documentation, OrchestraDocumentationV11):
            self.fixr_documentation = OrchestraDocumentationV11(**as_dict(self.fixr_documentation))

        if self.fixr_appinfo is not None and not isinstance(self.fixr_appinfo, OrchestraAppinfoV11):
            self.fixr_appinfo = OrchestraAppinfoV11(**as_dict(self.fixr_appinfo))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraAnnotationV11(YAMLRoot):
    """
    Notes for readers and hints for software, attached to an element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraAnnotationV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraAnnotationV11"
    class_name: ClassVar[str] = "OrchestraAnnotationV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraAnnotationV11

    fixr_members: Union[Union[dict, OrchestraAnnotationMemberV11], list[Union[dict, OrchestraAnnotationMemberV11]]] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraAnnotationMemberV11) else OrchestraAnnotationMemberV11(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraAppinfoV11(YAMLRoot):
    """
    A hint for a particular tool or encoding, such as how FIXML renders an element, held as text and open XML.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraAppinfoV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraAppinfoV11"
    class_name: ClassVar[str] = "OrchestraAppinfoV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraAppinfoV11

    fixr_text: Optional[str] = None
    fixr_any: Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]] = empty_list()
    fixr_spec_url: Optional[Union[str, URI]] = None
    fixr_lang_id: Optional[str] = None
    fixr_purpose: Optional[Union[str, "OrchestraPurposeV11"]] = None
    fixr_other_attributes: Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]] = empty_list()
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_text is not None and not isinstance(self.fixr_text, str):
            self.fixr_text = str(self.fixr_text)

        self._normalize_inlined_as_list(slot_name="fixr_any", slot_type=OrchestraXmlElement, key_name="xml_name", keyed=False)

        if self.fixr_spec_url is not None and not isinstance(self.fixr_spec_url, URI):
            self.fixr_spec_url = URI(self.fixr_spec_url)

        if self.fixr_lang_id is not None and not isinstance(self.fixr_lang_id, str):
            self.fixr_lang_id = str(self.fixr_lang_id)

        if self.fixr_purpose is not None and not isinstance(self.fixr_purpose, (OrchestraPurposeV11, str)):
            value = self.fixr_purpose
            for _coerce in (lambda: OrchestraPurposeV11(value), lambda: str(value)):
                try:
                    self.fixr_purpose = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraPurposeV11, str] could be constructed from {value!r} for slot fixr_purpose")

        self._normalize_inlined_as_list(slot_name="fixr_other_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraBaseEncodingV11(YAMLRoot):
    """
    What every encoding block shares: notes, and XML in another namespace that says how an element is encoded.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraBaseEncodingV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraBaseEncodingV11"
    class_name: ClassVar[str] = "OrchestraBaseEncodingV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraBaseEncodingV11

    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_any: Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        self._normalize_inlined_as_list(slot_name="fixr_any", slot_type=OrchestraXmlElement, key_name="xml_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraBaseInterfaceV11(YAMLRoot):
    """
    What an interface and a session share: the services, encodings and protocols of a connection, layer by layer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraBaseInterfaceV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraBaseInterfaceV11"
    class_name: ClassVar[str] = "OrchestraBaseInterfaceV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraBaseInterfaceV11

    fixi_name: str = None
    fixi_service: Optional[Union[Union[dict, "OrchestraServiceV11"], list[Union[dict, "OrchestraServiceV11"]]]] = empty_list()
    fixi_user_interface: Optional[Union[Union[dict, "OrchestraUserInterfaceV11"], list[Union[dict, "OrchestraUserInterfaceV11"]]]] = empty_list()
    fixi_encoding: Optional[Union[Union[dict, "OrchestraEncodingV11"], list[Union[dict, "OrchestraEncodingV11"]]]] = empty_list()
    fixi_session_protocol: Optional[Union[Union[dict, "OrchestraSessionProtocolV11"], list[Union[dict, "OrchestraSessionProtocolV11"]]]] = empty_list()
    fixi_protocol: Optional[Union[Union[dict, "OrchestraProtocolV11"], list[Union[dict, "OrchestraProtocolV11"]]]] = empty_list()
    fixi_transport: Optional[Union[Union[dict, "OrchestraTransportV11"], list[Union[dict, "OrchestraTransportV11"]]]] = empty_list()
    fixi_annotation: Optional[Union[dict, "OrchestraInterfaceAnnotationV11"]] = None
    fixi_other_attributes: Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixi_name):
            self.MissingRequiredField("fixi_name")
        if not isinstance(self.fixi_name, str):
            self.fixi_name = str(self.fixi_name)

        if not isinstance(self.fixi_service, list):
            self.fixi_service = [self.fixi_service] if self.fixi_service is not None else []
        self.fixi_service = [v if isinstance(v, OrchestraServiceV11) else OrchestraServiceV11(**as_dict(v)) for v in self.fixi_service]

        if not isinstance(self.fixi_user_interface, list):
            self.fixi_user_interface = [self.fixi_user_interface] if self.fixi_user_interface is not None else []
        self.fixi_user_interface = [v if isinstance(v, OrchestraUserInterfaceV11) else OrchestraUserInterfaceV11(**as_dict(v)) for v in self.fixi_user_interface]

        if not isinstance(self.fixi_encoding, list):
            self.fixi_encoding = [self.fixi_encoding] if self.fixi_encoding is not None else []
        self.fixi_encoding = [v if isinstance(v, OrchestraEncodingV11) else OrchestraEncodingV11(**as_dict(v)) for v in self.fixi_encoding]

        if not isinstance(self.fixi_session_protocol, list):
            self.fixi_session_protocol = [self.fixi_session_protocol] if self.fixi_session_protocol is not None else []
        self.fixi_session_protocol = [v if isinstance(v, OrchestraSessionProtocolV11) else OrchestraSessionProtocolV11(**as_dict(v)) for v in self.fixi_session_protocol]

        if not isinstance(self.fixi_protocol, list):
            self.fixi_protocol = [self.fixi_protocol] if self.fixi_protocol is not None else []
        self.fixi_protocol = [v if isinstance(v, OrchestraProtocolV11) else OrchestraProtocolV11(**as_dict(v)) for v in self.fixi_protocol]

        if not isinstance(self.fixi_transport, list):
            self.fixi_transport = [self.fixi_transport] if self.fixi_transport is not None else []
        self.fixi_transport = [v if isinstance(v, OrchestraTransportV11) else OrchestraTransportV11(**as_dict(v)) for v in self.fixi_transport]

        if self.fixi_annotation is not None and not isinstance(self.fixi_annotation, OrchestraInterfaceAnnotationV11):
            self.fixi_annotation = OrchestraInterfaceAnnotationV11(**as_dict(self.fixi_annotation))

        self._normalize_inlined_as_list(slot_name="fixi_other_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraBlockAssignmentV11(YAMLRoot):
    """
    How every entry of a group, or a single use of a component, gets its values: the fields, groups and components it
    sets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraBlockAssignmentV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraBlockAssignmentV11"
    class_name: ClassVar[str] = "OrchestraBlockAssignmentV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraBlockAssignmentV11

    fixr_members: Union[Union[dict, "OrchestraStructureMemberV11"], list[Union[dict, "OrchestraStructureMemberV11"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraStructureMemberV11) else OrchestraStructureMemberV11(**as_dict(v)) for v in self.fixr_members]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraCategoriesV11(YAMLRoot):
    """
    The categories a repository sorts its messages and fields into.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraCategoriesV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraCategoriesV11"
    class_name: ClassVar[str] = "OrchestraCategoriesV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraCategoriesV11

    fixr_category: Optional[Union[Union[dict, "OrchestraCategoryV11"], list[Union[dict, "OrchestraCategoryV11"]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_category", slot_type=OrchestraCategoryV11, key_name="fixr_name", keyed=False)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraCategoryV11(YAMLRoot):
    """
    A business process grouping within a section, such as order handling or market data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraCategoryV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraCategoryV11"
    class_name: ClassVar[str] = "OrchestraCategoryV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraCategoryV11

    fixr_name: str = None
    fixr_section: str = None
    fixr_encodings: Optional[Union[dict, "OrchestraEncodingsV11"]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self._is_empty(self.fixr_section):
            self.MissingRequiredField("fixr_section")
        if not isinstance(self.fixr_section, str):
            self.fixr_section = str(self.fixr_section)

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraCodeSetV11(YAMLRoot):
    """
    A named list of the values a field may take, each with a name of its own, over one underlying datatype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraCodeSetV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraCodeSetV11"
    class_name: ClassVar[str] = "OrchestraCodeSetV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraCodeSetV11

    fixr_type: str = None
    fixr_id: int = None
    fixr_name: str = None
    fixr_code: Optional[Union[Union[dict, "OrchestraCodeV11"], list[Union[dict, "OrchestraCodeV11"]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_encodings: Optional[Union[dict, "OrchestraEncodingsV11"]] = None
    fixr_default: Optional[str] = None
    fixr_spec_url: Optional[Union[str, URI]] = None
    fixr_union_data_type: Optional[str] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_scenario_ref_id: Optional[int] = None
    fixr_scenario_ref: Optional[str] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_type):
            self.MissingRequiredField("fixr_type")
        if not isinstance(self.fixr_type, str):
            self.fixr_type = str(self.fixr_type)

        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        self._normalize_inlined_as_list(slot_name="fixr_code", slot_type=OrchestraCodeV11, key_name="fixr_value", keyed=False)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_default is not None and not isinstance(self.fixr_default, str):
            self.fixr_default = str(self.fixr_default)

        if self.fixr_spec_url is not None and not isinstance(self.fixr_spec_url, URI):
            self.fixr_spec_url = URI(self.fixr_spec_url)

        if self.fixr_union_data_type is not None and not isinstance(self.fixr_union_data_type, str):
            self.fixr_union_data_type = str(self.fixr_union_data_type)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_scenario_ref_id is not None and not isinstance(self.fixr_scenario_ref_id, int):
            self.fixr_scenario_ref_id = int(self.fixr_scenario_ref_id)

        if self.fixr_scenario_ref is not None and not isinstance(self.fixr_scenario_ref, str):
            self.fixr_scenario_ref = str(self.fixr_scenario_ref)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraCodeSetsV11(YAMLRoot):
    """
    The code sets a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraCodeSetsV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraCodeSetsV11"
    class_name: ClassVar[str] = "OrchestraCodeSetsV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraCodeSetsV11

    fixr_code_set: Optional[Union[Union[dict, OrchestraCodeSetV11], list[Union[dict, OrchestraCodeSetV11]]]] = empty_list()
    fixr_encodings: Optional[Union[dict, "OrchestraEncodingsV11"]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_code_set", slot_type=OrchestraCodeSetV11, key_name="fixr_type", keyed=False)

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraCodeV11(YAMLRoot):
    """
    One permitted value of the set, with its name and what goes on the wire.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraCodeV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraCodeV11"
    class_name: ClassVar[str] = "OrchestraCodeV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraCodeV11

    fixr_value: str = None
    fixr_id: int = None
    fixr_name: str = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_sort: Optional[int] = None
    fixr_group: Optional[str] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_value):
            self.MissingRequiredField("fixr_value")
        if not isinstance(self.fixr_value, str):
            self.fixr_value = str(self.fixr_value)

        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_sort is not None and not isinstance(self.fixr_sort, int):
            self.fixr_sort = int(self.fixr_sort)

        if self.fixr_group is not None and not isinstance(self.fixr_group, str):
            self.fixr_group = str(self.fixr_group)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraComponentRefV11(YAMLRoot):
    """
    Where a message or block includes a component, by its number, with its presence and any rules that make it
    conditional.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraComponentRefV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraComponentRefV11"
    class_name: ClassVar[str] = "OrchestraComponentRefV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraComponentRefV11

    fixr_id: int = None
    fixr_block_assignment: Optional[Union[Union[dict, OrchestraBlockAssignmentV11], list[Union[dict, OrchestraBlockAssignmentV11]]]] = empty_list()
    fixr_rule: Optional[Union[Union[dict, "OrchestraComponentRuleV11"], list[Union[dict, "OrchestraComponentRuleV11"]]]] = empty_list()
    fixr_encodings: Optional[Union[dict, "OrchestraEncodingsV11"]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = 'optional'
    fixr_instance_name: Optional[str] = None
    fixr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if not isinstance(self.fixr_block_assignment, list):
            self.fixr_block_assignment = [self.fixr_block_assignment] if self.fixr_block_assignment is not None else []
        self.fixr_block_assignment = [v if isinstance(v, OrchestraBlockAssignmentV11) else OrchestraBlockAssignmentV11(**as_dict(v)) for v in self.fixr_block_assignment]

        self._normalize_inlined_as_list(slot_name="fixr_rule", slot_type=OrchestraComponentRuleV11, key_name="fixr_when", keyed=False)

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        if self.fixr_instance_name is not None and not isinstance(self.fixr_instance_name, str):
            self.fixr_instance_name = str(self.fixr_instance_name)

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraComponentRuleV11(YAMLRoot):
    """
    A condition that changes a component's presence, such as making it required.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraComponentRuleV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraComponentRuleV11"
    class_name: ClassVar[str] = "OrchestraComponentRuleV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraComponentRuleV11

    fixr_when: str = None
    fixr_name: Optional[str] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_when):
            self.MissingRequiredField("fixr_when")
        if not isinstance(self.fixr_when, str):
            self.fixr_when = str(self.fixr_when)

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraComponentV11(YAMLRoot):
    """
    A named block of fields, groups and components that messages and other blocks include by reference.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraComponentV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraComponentV11"
    class_name: ClassVar[str] = "OrchestraComponentV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraComponentV11

    fixr_id: int = None
    fixr_name: str = None
    fixr_members: Optional[Union[Union[dict, "OrchestraStructureMemberV11"], list[Union[dict, "OrchestraStructureMemberV11"]]]] = empty_list()
    fixr_encodings: Optional[Union[dict, "OrchestraEncodingsV11"]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_category: Optional[str] = None
    fixr_rendering: Optional[str] = None
    fixr_which: Optional[Union[str, "OrchestraMemberSelection"]] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_scenario_ref_id: Optional[int] = None
    fixr_scenario_ref: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraStructureMemberV11) else OrchestraStructureMemberV11(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_category is not None and not isinstance(self.fixr_category, str):
            self.fixr_category = str(self.fixr_category)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        if self.fixr_which is not None and not isinstance(self.fixr_which, OrchestraMemberSelection):
            self.fixr_which = OrchestraMemberSelection(self.fixr_which)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_scenario_ref_id is not None and not isinstance(self.fixr_scenario_ref_id, int):
            self.fixr_scenario_ref_id = int(self.fixr_scenario_ref_id)

        if self.fixr_scenario_ref is not None and not isinstance(self.fixr_scenario_ref, str):
            self.fixr_scenario_ref = str(self.fixr_scenario_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraComponentsV11(YAMLRoot):
    """
    The components a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraComponentsV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraComponentsV11"
    class_name: ClassVar[str] = "OrchestraComponentsV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraComponentsV11

    fixr_component: Optional[Union[Union[dict, OrchestraComponentV11], list[Union[dict, OrchestraComponentV11]]]] = empty_list()
    fixr_encodings: Optional[Union[dict, "OrchestraEncodingsV11"]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_component", slot_type=OrchestraComponentV11, key_name="fixr_id", keyed=False)

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraConceptMemberV11(YAMLRoot):
    """
    One element a concept ties together, named by reference, which is a message, field, component or group. It holds
    exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraConceptMemberV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraConceptMemberV11"
    class_name: ClassVar[str] = "OrchestraConceptMemberV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraConceptMemberV11

    fixr_component_ref: Optional[Union[dict, OrchestraComponentRefV11]] = None
    fixr_group_ref: Optional[Union[dict, "OrchestraGroupRefV11"]] = None
    fixr_field_ref: Optional[Union[dict, "OrchestraFieldRefV11"]] = None
    fixr_message_ref: Optional[Union[dict, "OrchestraMessageRefV11"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_component_ref is not None and not isinstance(self.fixr_component_ref, OrchestraComponentRefV11):
            self.fixr_component_ref = OrchestraComponentRefV11(**as_dict(self.fixr_component_ref))

        if self.fixr_group_ref is not None and not isinstance(self.fixr_group_ref, OrchestraGroupRefV11):
            self.fixr_group_ref = OrchestraGroupRefV11(**as_dict(self.fixr_group_ref))

        if self.fixr_field_ref is not None and not isinstance(self.fixr_field_ref, OrchestraFieldRefV11):
            self.fixr_field_ref = OrchestraFieldRefV11(**as_dict(self.fixr_field_ref))

        if self.fixr_message_ref is not None and not isinstance(self.fixr_message_ref, OrchestraMessageRefV11):
            self.fixr_message_ref = OrchestraMessageRefV11(**as_dict(self.fixr_message_ref))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraConceptV11(YAMLRoot):
    """
    A named business idea that ties together the fields, components, groups and messages that express it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraConceptV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraConceptV11"
    class_name: ClassVar[str] = "OrchestraConceptV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraConceptV11

    fixr_members: Union[Union[dict, OrchestraConceptMemberV11], list[Union[dict, OrchestraConceptMemberV11]]] = None
    fixr_name: str = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraConceptMemberV11) else OrchestraConceptMemberV11(**as_dict(v)) for v in self.fixr_members]

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraConceptsV11(YAMLRoot):
    """
    The concepts a repository names.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraConceptsV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraConceptsV11"
    class_name: ClassVar[str] = "OrchestraConceptsV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraConceptsV11

    fixr_concept: Optional[Union[Union[dict, OrchestraConceptV11], list[Union[dict, OrchestraConceptV11]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_concept", slot_type=OrchestraConceptV11, key_name="fixr_name", keyed=False)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraDatatypeV11(YAMLRoot):
    """
    A FIX datatype, such as Price or UTCTimestamp, with how it maps to the types of other standards.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraDatatypeV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraDatatypeV11"
    class_name: ClassVar[str] = "OrchestraDatatypeV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraDatatypeV11

    fixr_name: str = None
    fixr_mapped_datatype: Optional[Union[Union[dict, "OrchestraMappedDatatypeV11"], list[Union[dict, "OrchestraMappedDatatypeV11"]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_base_type: Optional[str] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        self._normalize_inlined_as_list(slot_name="fixr_mapped_datatype", slot_type=OrchestraMappedDatatypeV11, key_name="fixr_standard", keyed=False)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_base_type is not None and not isinstance(self.fixr_base_type, str):
            self.fixr_base_type = str(self.fixr_base_type)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraDatatypesV11(YAMLRoot):
    """
    The datatypes a repository uses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraDatatypesV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraDatatypesV11"
    class_name: ClassVar[str] = "OrchestraDatatypesV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraDatatypesV11

    fixr_datatype: Optional[Union[Union[dict, OrchestraDatatypeV11], list[Union[dict, OrchestraDatatypeV11]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_datatype", slot_type=OrchestraDatatypeV11, key_name="fixr_name", keyed=False)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraDocumentationV11(YAMLRoot):
    """
    Text about an element, with its language, purpose and media type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraDocumentationV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraDocumentationV11"
    class_name: ClassVar[str] = "OrchestraDocumentationV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraDocumentationV11

    fixr_text: Optional[str] = None
    fixr_lang_id: Optional[str] = None
    fixr_purpose: Optional[Union[str, "OrchestraPurposeV11"]] = None
    fixr_content_type: Optional[str] = "text/plain"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_text is not None and not isinstance(self.fixr_text, str):
            self.fixr_text = str(self.fixr_text)

        if self.fixr_lang_id is not None and not isinstance(self.fixr_lang_id, str):
            self.fixr_lang_id = str(self.fixr_lang_id)

        if self.fixr_purpose is not None and not isinstance(self.fixr_purpose, (OrchestraPurposeV11, str)):
            value = self.fixr_purpose
            for _coerce in (lambda: OrchestraPurposeV11(value), lambda: str(value)):
                try:
                    self.fixr_purpose = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraPurposeV11, str] could be constructed from {value!r} for slot fixr_purpose")

        if self.fixr_content_type is not None and not isinstance(self.fixr_content_type, str):
            self.fixr_content_type = str(self.fixr_content_type)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraEncodingStandardV11(YAMLRoot):
    """
    An encoding standard a repository uses, with a name to show and its general encoding information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraEncodingStandardV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraEncodingStandardV11"
    class_name: ClassVar[str] = "OrchestraEncodingStandardV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraEncodingStandardV11

    fixr_name: str = None
    fixr_encoding: Optional[Union[dict, "OrchestraUnnamedEncodingV11"]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_display_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_encoding is not None and not isinstance(self.fixr_encoding, OrchestraUnnamedEncodingV11):
            self.fixr_encoding = OrchestraUnnamedEncodingV11(**as_dict(self.fixr_encoding))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_display_name is not None and not isinstance(self.fixr_display_name, str):
            self.fixr_display_name = str(self.fixr_display_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraEncodingStandardsV11(YAMLRoot):
    """
    The encoding standards that a repository's encoding blocks name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraEncodingStandardsV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraEncodingStandardsV11"
    class_name: ClassVar[str] = "OrchestraEncodingStandardsV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraEncodingStandardsV11

    fixr_encoding_standard: Optional[Union[Union[dict, OrchestraEncodingStandardV11], list[Union[dict, OrchestraEncodingStandardV11]]]] = empty_list()
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_encoding_standard", slot_type=OrchestraEncodingStandardV11, key_name="fixr_name", keyed=False)

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraEncodingsV11(YAMLRoot):
    """
    The encoding blocks of one element, one for each encoding standard that needs more information about it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraEncodingsV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraEncodingsV11"
    class_name: ClassVar[str] = "OrchestraEncodingsV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraEncodingsV11

    fixr_encoding: Optional[Union[Union[dict, "OrchestraNamedEncodingV11"], list[Union[dict, "OrchestraNamedEncodingV11"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_encoding", slot_type=OrchestraNamedEncodingV11, key_name="fixr_standard", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFieldConstraintsV11Mixin(YAMLRoot):
    """
    The limits on a field's value that a field, a use of it or a rule may set: range, length, presence, fixed or
    default value, character set and a display hint.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFieldConstraintsV11Mixin"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFieldConstraintsV11Mixin"
    class_name: ClassVar[str] = "OrchestraFieldConstraintsV11Mixin"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFieldConstraintsV11Mixin

    fixr_min_inclusive: Optional[str] = None
    fixr_max_inclusive: Optional[str] = None
    fixr_impl_length: Optional[int] = None
    fixr_impl_min_length: Optional[int] = None
    fixr_impl_max_length: Optional[int] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = 'optional'
    fixr_encoding: Optional[str] = None
    fixr_value: Optional[str] = None
    fixr_rendering: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_min_inclusive is not None and not isinstance(self.fixr_min_inclusive, str):
            self.fixr_min_inclusive = str(self.fixr_min_inclusive)

        if self.fixr_max_inclusive is not None and not isinstance(self.fixr_max_inclusive, str):
            self.fixr_max_inclusive = str(self.fixr_max_inclusive)

        if self.fixr_impl_length is not None and not isinstance(self.fixr_impl_length, int):
            self.fixr_impl_length = int(self.fixr_impl_length)

        if self.fixr_impl_min_length is not None and not isinstance(self.fixr_impl_min_length, int):
            self.fixr_impl_min_length = int(self.fixr_impl_min_length)

        if self.fixr_impl_max_length is not None and not isinstance(self.fixr_impl_max_length, int):
            self.fixr_impl_max_length = int(self.fixr_impl_max_length)

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        if self.fixr_encoding is not None and not isinstance(self.fixr_encoding, str):
            self.fixr_encoding = str(self.fixr_encoding)

        if self.fixr_value is not None and not isinstance(self.fixr_value, str):
            self.fixr_value = str(self.fixr_value)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFieldRefV11(YAMLRoot):
    """
    Where a message or block includes a field, by its tag number, with its presence, value limits and any rules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFieldRefV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFieldRefV11"
    class_name: ClassVar[str] = "OrchestraFieldRefV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFieldRefV11

    fixr_id: int = None
    fixr_rule: Optional[Union[Union[dict, "OrchestraFieldRuleV11"], list[Union[dict, "OrchestraFieldRuleV11"]]]] = empty_list()
    fixr_assign: Optional[str] = None
    fixr_encodings: Optional[Union[dict, OrchestraEncodingsV11]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_length_id: Optional[int] = None
    fixr_non_encoded_field_id: Optional[int] = None
    fixr_instance_name: Optional[str] = None
    fixr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None
    fixr_min_inclusive: Optional[str] = None
    fixr_max_inclusive: Optional[str] = None
    fixr_impl_length: Optional[int] = None
    fixr_impl_min_length: Optional[int] = None
    fixr_impl_max_length: Optional[int] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = 'optional'
    fixr_encoding: Optional[str] = None
    fixr_value: Optional[str] = None
    fixr_rendering: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        self._normalize_inlined_as_list(slot_name="fixr_rule", slot_type=OrchestraFieldRuleV11, key_name="fixr_when", keyed=False)

        if self.fixr_assign is not None and not isinstance(self.fixr_assign, str):
            self.fixr_assign = str(self.fixr_assign)

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_length_id is not None and not isinstance(self.fixr_length_id, int):
            self.fixr_length_id = int(self.fixr_length_id)

        if self.fixr_non_encoded_field_id is not None and not isinstance(self.fixr_non_encoded_field_id, int):
            self.fixr_non_encoded_field_id = int(self.fixr_non_encoded_field_id)

        if self.fixr_instance_name is not None and not isinstance(self.fixr_instance_name, str):
            self.fixr_instance_name = str(self.fixr_instance_name)

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        if self.fixr_min_inclusive is not None and not isinstance(self.fixr_min_inclusive, str):
            self.fixr_min_inclusive = str(self.fixr_min_inclusive)

        if self.fixr_max_inclusive is not None and not isinstance(self.fixr_max_inclusive, str):
            self.fixr_max_inclusive = str(self.fixr_max_inclusive)

        if self.fixr_impl_length is not None and not isinstance(self.fixr_impl_length, int):
            self.fixr_impl_length = int(self.fixr_impl_length)

        if self.fixr_impl_min_length is not None and not isinstance(self.fixr_impl_min_length, int):
            self.fixr_impl_min_length = int(self.fixr_impl_min_length)

        if self.fixr_impl_max_length is not None and not isinstance(self.fixr_impl_max_length, int):
            self.fixr_impl_max_length = int(self.fixr_impl_max_length)

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        if self.fixr_encoding is not None and not isinstance(self.fixr_encoding, str):
            self.fixr_encoding = str(self.fixr_encoding)

        if self.fixr_value is not None and not isinstance(self.fixr_value, str):
            self.fixr_value = str(self.fixr_value)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFieldRuleV11(YAMLRoot):
    """
    A condition that changes a field's presence, datatype or limits, or a check its value must pass.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFieldRuleV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFieldRuleV11"
    class_name: ClassVar[str] = "OrchestraFieldRuleV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFieldRuleV11

    fixr_when: str = None
    fixr_unique: Optional[Union[dict, "OrchestraUniqueV11"]] = None
    fixr_assign: Optional[Union[str, list[str]]] = empty_list()
    fixr_name: Optional[str] = None
    fixr_type: Optional[str] = None
    fixr_min_inclusive: Optional[str] = None
    fixr_max_inclusive: Optional[str] = None
    fixr_impl_length: Optional[int] = None
    fixr_impl_min_length: Optional[int] = None
    fixr_impl_max_length: Optional[int] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = 'optional'
    fixr_encoding: Optional[str] = None
    fixr_value: Optional[str] = None
    fixr_rendering: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_when):
            self.MissingRequiredField("fixr_when")
        if not isinstance(self.fixr_when, str):
            self.fixr_when = str(self.fixr_when)

        if self.fixr_unique is not None and not isinstance(self.fixr_unique, OrchestraUniqueV11):
            self.fixr_unique = OrchestraUniqueV11(**as_dict(self.fixr_unique))

        if not isinstance(self.fixr_assign, list):
            self.fixr_assign = [self.fixr_assign] if self.fixr_assign is not None else []
        self.fixr_assign = [v if isinstance(v, str) else str(v) for v in self.fixr_assign]

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_type is not None and not isinstance(self.fixr_type, str):
            self.fixr_type = str(self.fixr_type)

        if self.fixr_min_inclusive is not None and not isinstance(self.fixr_min_inclusive, str):
            self.fixr_min_inclusive = str(self.fixr_min_inclusive)

        if self.fixr_max_inclusive is not None and not isinstance(self.fixr_max_inclusive, str):
            self.fixr_max_inclusive = str(self.fixr_max_inclusive)

        if self.fixr_impl_length is not None and not isinstance(self.fixr_impl_length, int):
            self.fixr_impl_length = int(self.fixr_impl_length)

        if self.fixr_impl_min_length is not None and not isinstance(self.fixr_impl_min_length, int):
            self.fixr_impl_min_length = int(self.fixr_impl_min_length)

        if self.fixr_impl_max_length is not None and not isinstance(self.fixr_impl_max_length, int):
            self.fixr_impl_max_length = int(self.fixr_impl_max_length)

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        if self.fixr_encoding is not None and not isinstance(self.fixr_encoding, str):
            self.fixr_encoding = str(self.fixr_encoding)

        if self.fixr_value is not None and not isinstance(self.fixr_value, str):
            self.fixr_value = str(self.fixr_value)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFieldV11(YAMLRoot):
    """
    A FIX field: its tag number, its name, its datatype or its code set, and the limits on its value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFieldV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFieldV11"
    class_name: ClassVar[str] = "OrchestraFieldV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFieldV11

    fixr_id: int = None
    fixr_name: str = None
    fixr_rule: Optional[Union[Union[dict, OrchestraFieldRuleV11], list[Union[dict, OrchestraFieldRuleV11]]]] = empty_list()
    fixr_assign: Optional[str] = None
    fixr_encodings: Optional[Union[dict, OrchestraEncodingsV11]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_type: Optional[str] = None
    fixr_code_set: Optional[str] = None
    fixr_length_id: Optional[int] = None
    fixr_non_encoded_field_id: Optional[int] = None
    fixr_discriminator_id: Optional[int] = None
    fixr_base_category: Optional[str] = None
    fixr_base_category_abbr_name: Optional[str] = None
    fixr_union_data_type: Optional[str] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None
    fixr_min_inclusive: Optional[str] = None
    fixr_max_inclusive: Optional[str] = None
    fixr_impl_length: Optional[int] = None
    fixr_impl_min_length: Optional[int] = None
    fixr_impl_max_length: Optional[int] = None
    fixr_presence: Optional[Union[str, "OrchestraPresence"]] = 'optional'
    fixr_encoding: Optional[str] = None
    fixr_value: Optional[str] = None
    fixr_rendering: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        self._normalize_inlined_as_list(slot_name="fixr_rule", slot_type=OrchestraFieldRuleV11, key_name="fixr_when", keyed=False)

        if self.fixr_assign is not None and not isinstance(self.fixr_assign, str):
            self.fixr_assign = str(self.fixr_assign)

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_type is not None and not isinstance(self.fixr_type, str):
            self.fixr_type = str(self.fixr_type)

        if self.fixr_code_set is not None and not isinstance(self.fixr_code_set, str):
            self.fixr_code_set = str(self.fixr_code_set)

        if self.fixr_length_id is not None and not isinstance(self.fixr_length_id, int):
            self.fixr_length_id = int(self.fixr_length_id)

        if self.fixr_non_encoded_field_id is not None and not isinstance(self.fixr_non_encoded_field_id, int):
            self.fixr_non_encoded_field_id = int(self.fixr_non_encoded_field_id)

        if self.fixr_discriminator_id is not None and not isinstance(self.fixr_discriminator_id, int):
            self.fixr_discriminator_id = int(self.fixr_discriminator_id)

        if self.fixr_base_category is not None and not isinstance(self.fixr_base_category, str):
            self.fixr_base_category = str(self.fixr_base_category)

        if self.fixr_base_category_abbr_name is not None and not isinstance(self.fixr_base_category_abbr_name, str):
            self.fixr_base_category_abbr_name = str(self.fixr_base_category_abbr_name)

        if self.fixr_union_data_type is not None and not isinstance(self.fixr_union_data_type, str):
            self.fixr_union_data_type = str(self.fixr_union_data_type)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        if self.fixr_min_inclusive is not None and not isinstance(self.fixr_min_inclusive, str):
            self.fixr_min_inclusive = str(self.fixr_min_inclusive)

        if self.fixr_max_inclusive is not None and not isinstance(self.fixr_max_inclusive, str):
            self.fixr_max_inclusive = str(self.fixr_max_inclusive)

        if self.fixr_impl_length is not None and not isinstance(self.fixr_impl_length, int):
            self.fixr_impl_length = int(self.fixr_impl_length)

        if self.fixr_impl_min_length is not None and not isinstance(self.fixr_impl_min_length, int):
            self.fixr_impl_min_length = int(self.fixr_impl_min_length)

        if self.fixr_impl_max_length is not None and not isinstance(self.fixr_impl_max_length, int):
            self.fixr_impl_max_length = int(self.fixr_impl_max_length)

        if self.fixr_presence is not None and not isinstance(self.fixr_presence, OrchestraPresence):
            self.fixr_presence = OrchestraPresence(self.fixr_presence)

        if self.fixr_encoding is not None and not isinstance(self.fixr_encoding, str):
            self.fixr_encoding = str(self.fixr_encoding)

        if self.fixr_value is not None and not isinstance(self.fixr_value, str):
            self.fixr_value = str(self.fixr_value)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFieldsV11(YAMLRoot):
    """
    The fields a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFieldsV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFieldsV11"
    class_name: ClassVar[str] = "OrchestraFieldsV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFieldsV11

    fixr_field: Optional[Union[Union[dict, OrchestraFieldV11], list[Union[dict, OrchestraFieldV11]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_field", slot_type=OrchestraFieldV11, key_name="fixr_id", keyed=False)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraFlowV11(YAMLRoot):
    """
    Messages that travel one way, from a sending actor to a receiving one, with their delivery guarantee.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraFlowV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraFlowV11"
    class_name: ClassVar[str] = "OrchestraFlowV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraFlowV11

    fixr_name: str = None
    fixr_source: str = None
    fixr_destination: str = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_reliability: Optional[Union[str, "OrchestraReliability"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self._is_empty(self.fixr_source):
            self.MissingRequiredField("fixr_source")
        if not isinstance(self.fixr_source, str):
            self.fixr_source = str(self.fixr_source)

        if self._is_empty(self.fixr_destination):
            self.MissingRequiredField("fixr_destination")
        if not isinstance(self.fixr_destination, str):
            self.fixr_destination = str(self.fixr_destination)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_reliability is not None and not isinstance(self.fixr_reliability, OrchestraReliability):
            self.fixr_reliability = OrchestraReliability(self.fixr_reliability)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraGroupRefV11(OrchestraComponentRefV11):
    """
    Where a message or block includes a repeating group, by its number, with how many entries it may hold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraGroupRefV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraGroupRefV11"
    class_name: ClassVar[str] = "OrchestraGroupRefV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraGroupRefV11

    fixr_id: int = None
    fixr_impl_min_occurs: Optional[int] = None
    fixr_impl_max_occurs: Optional[str] = "unbounded"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_impl_min_occurs is not None and not isinstance(self.fixr_impl_min_occurs, int):
            self.fixr_impl_min_occurs = int(self.fixr_impl_min_occurs)

        if self.fixr_impl_max_occurs is not None and not isinstance(self.fixr_impl_max_occurs, str):
            self.fixr_impl_max_occurs = str(self.fixr_impl_max_occurs)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraGroupV11(YAMLRoot):
    """
    A block whose entries repeat, each with the same fields, groups and components, and whose count a NumInGroup field
    carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraGroupV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraGroupV11"
    class_name: ClassVar[str] = "OrchestraGroupV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraGroupV11

    fixr_id: int = None
    fixr_name: str = None
    fixr_num_in_group: Optional[Union[dict, OrchestraFieldRefV11]] = None
    fixr_members: Optional[Union[Union[dict, "OrchestraStructureMemberV11"], list[Union[dict, "OrchestraStructureMemberV11"]]]] = empty_list()
    fixr_encodings: Optional[Union[dict, OrchestraEncodingsV11]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_category: Optional[str] = None
    fixr_rendering: Optional[str] = None
    fixr_impl_min_occurs: Optional[int] = None
    fixr_impl_max_occurs: Optional[str] = None
    fixr_which: Optional[Union[str, "OrchestraMemberSelection"]] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_scenario_ref_id: Optional[int] = None
    fixr_scenario_ref: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_num_in_group is not None and not isinstance(self.fixr_num_in_group, OrchestraFieldRefV11):
            self.fixr_num_in_group = OrchestraFieldRefV11(**as_dict(self.fixr_num_in_group))

        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraStructureMemberV11) else OrchestraStructureMemberV11(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_category is not None and not isinstance(self.fixr_category, str):
            self.fixr_category = str(self.fixr_category)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        if self.fixr_impl_min_occurs is not None and not isinstance(self.fixr_impl_min_occurs, int):
            self.fixr_impl_min_occurs = int(self.fixr_impl_min_occurs)

        if self.fixr_impl_max_occurs is not None and not isinstance(self.fixr_impl_max_occurs, str):
            self.fixr_impl_max_occurs = str(self.fixr_impl_max_occurs)

        if self.fixr_which is not None and not isinstance(self.fixr_which, OrchestraMemberSelection):
            self.fixr_which = OrchestraMemberSelection(self.fixr_which)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_scenario_ref_id is not None and not isinstance(self.fixr_scenario_ref_id, int):
            self.fixr_scenario_ref_id = int(self.fixr_scenario_ref_id)

        if self.fixr_scenario_ref is not None and not isinstance(self.fixr_scenario_ref, str):
            self.fixr_scenario_ref = str(self.fixr_scenario_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraGroupsV11(YAMLRoot):
    """
    The repeating groups a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraGroupsV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraGroupsV11"
    class_name: ClassVar[str] = "OrchestraGroupsV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraGroupsV11

    fixr_group: Optional[Union[Union[dict, OrchestraGroupV11], list[Union[dict, OrchestraGroupV11]]]] = empty_list()
    fixr_encodings: Optional[Union[dict, OrchestraEncodingsV11]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_group", slot_type=OrchestraGroupV11, key_name="fixr_id", keyed=False)

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraIdentifierV11(YAMLRoot):
    """
    A field that a message sent by an action sets, or carries over from the message received, by tag number.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraIdentifierV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraIdentifierV11"
    class_name: ClassVar[str] = "OrchestraIdentifierV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraIdentifierV11

    fixr_id: int = None
    fixr_name: Optional[str] = None
    fixr_source_id: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_source_id is not None and not isinstance(self.fixr_source_id, int):
            self.fixr_source_id = int(self.fixr_source_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraIdentifiersMemberV11(YAMLRoot):
    """
    One entry of a message's identifiers, a field carried over or a field set. It holds exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraIdentifiersMemberV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraIdentifiersMemberV11"
    class_name: ClassVar[str] = "OrchestraIdentifiersMemberV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraIdentifiersMemberV11

    fixr_correlate: Optional[Union[dict, OrchestraIdentifierV11]] = None
    fixr_assign: Optional[Union[dict, OrchestraIdentifierV11]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_correlate is not None and not isinstance(self.fixr_correlate, OrchestraIdentifierV11):
            self.fixr_correlate = OrchestraIdentifierV11(**as_dict(self.fixr_correlate))

        if self.fixr_assign is not None and not isinstance(self.fixr_assign, OrchestraIdentifierV11):
            self.fixr_assign = OrchestraIdentifierV11(**as_dict(self.fixr_assign))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraIdentifiersV11(YAMLRoot):
    """
    The fields a message sent by an action sets or carries over.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraIdentifiersV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraIdentifiersV11"
    class_name: ClassVar[str] = "OrchestraIdentifiersV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraIdentifiersV11

    fixr_members: Union[Union[dict, OrchestraIdentifiersMemberV11], list[Union[dict, OrchestraIdentifiersMemberV11]]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_members):
            self.MissingRequiredField("fixr_members")
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraIdentifiersMemberV11) else OrchestraIdentifiersMemberV11(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraIdentityV11Mixin(YAMLRoot):
    """
    The keys of a defined element, its number, name, short name and scenario.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraIdentityV11Mixin"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraIdentityV11Mixin"
    class_name: ClassVar[str] = "OrchestraIdentityV11Mixin"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraIdentityV11Mixin

    fixr_id: int = None
    fixr_name: str = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfaceAnnotationMemberV11(YAMLRoot):
    """
    One part of an annotation in an interfaces file, a text or a hint for software. It holds exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfaceAnnotationMemberV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfaceAnnotationMemberV11"
    class_name: ClassVar[str] = "OrchestraInterfaceAnnotationMemberV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfaceAnnotationMemberV11

    fixi_documentation: Optional[Union[dict, "OrchestraInterfaceDocumentationV11"]] = None
    fixi_appinfo: Optional[Union[dict, "OrchestraInterfaceAppinfoV11"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_documentation is not None and not isinstance(self.fixi_documentation, OrchestraInterfaceDocumentationV11):
            self.fixi_documentation = OrchestraInterfaceDocumentationV11(**as_dict(self.fixi_documentation))

        if self.fixi_appinfo is not None and not isinstance(self.fixi_appinfo, OrchestraInterfaceAppinfoV11):
            self.fixi_appinfo = OrchestraInterfaceAppinfoV11(**as_dict(self.fixi_appinfo))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfaceAnnotationV11(YAMLRoot):
    """
    Notes for readers and hints for software, attached to an element of an interfaces file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfaceAnnotationV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfaceAnnotationV11"
    class_name: ClassVar[str] = "OrchestraInterfaceAnnotationV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfaceAnnotationV11

    fixi_members: Union[Union[dict, OrchestraInterfaceAnnotationMemberV11], list[Union[dict, OrchestraInterfaceAnnotationMemberV11]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixi_members):
            self.MissingRequiredField("fixi_members")
        if not isinstance(self.fixi_members, list):
            self.fixi_members = [self.fixi_members] if self.fixi_members is not None else []
        self.fixi_members = [v if isinstance(v, OrchestraInterfaceAnnotationMemberV11) else OrchestraInterfaceAnnotationMemberV11(**as_dict(v)) for v in self.fixi_members]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfaceAppinfoV11(YAMLRoot):
    """
    A hint for a particular tool on an element of an interfaces file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfaceAppinfoV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfaceAppinfoV11"
    class_name: ClassVar[str] = "OrchestraInterfaceAppinfoV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfaceAppinfoV11

    fixi_text: Optional[str] = None
    fixi_any: Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]] = empty_list()
    fixi_spec_url: Optional[Union[str, URI]] = None
    fixi_lang_id: Optional[str] = None
    fixi_purpose: Optional[Union[str, "OrchestraPurpose"]] = None
    fixi_other_attributes: Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_text is not None and not isinstance(self.fixi_text, str):
            self.fixi_text = str(self.fixi_text)

        self._normalize_inlined_as_list(slot_name="fixi_any", slot_type=OrchestraXmlElement, key_name="xml_name", keyed=False)

        if self.fixi_spec_url is not None and not isinstance(self.fixi_spec_url, URI):
            self.fixi_spec_url = URI(self.fixi_spec_url)

        if self.fixi_lang_id is not None and not isinstance(self.fixi_lang_id, str):
            self.fixi_lang_id = str(self.fixi_lang_id)

        if self.fixi_purpose is not None and not isinstance(self.fixi_purpose, (OrchestraPurpose, str)):
            value = self.fixi_purpose
            for _coerce in (lambda: OrchestraPurpose(value), lambda: str(value)):
                try:
                    self.fixi_purpose = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraPurpose, str] could be constructed from {value!r} for slot fixi_purpose")

        self._normalize_inlined_as_list(slot_name="fixi_other_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfaceDocumentationV11(YAMLRoot):
    """
    Text about an element of an interfaces file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfaceDocumentationV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfaceDocumentationV11"
    class_name: ClassVar[str] = "OrchestraInterfaceDocumentationV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfaceDocumentationV11

    fixi_text: Optional[str] = None
    fixi_any: Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]] = empty_list()
    fixi_lang_id: Optional[str] = None
    fixi_purpose: Optional[Union[str, "OrchestraPurpose"]] = None
    fixi_content_type: Optional[str] = "text/plain"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_text is not None and not isinstance(self.fixi_text, str):
            self.fixi_text = str(self.fixi_text)

        self._normalize_inlined_as_list(slot_name="fixi_any", slot_type=OrchestraXmlElement, key_name="xml_name", keyed=False)

        if self.fixi_lang_id is not None and not isinstance(self.fixi_lang_id, str):
            self.fixi_lang_id = str(self.fixi_lang_id)

        if self.fixi_purpose is not None and not isinstance(self.fixi_purpose, (OrchestraPurpose, str)):
            value = self.fixi_purpose
            for _coerce in (lambda: OrchestraPurpose(value), lambda: str(value)):
                try:
                    self.fixi_purpose = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraPurpose, str] could be constructed from {value!r} for slot fixi_purpose")

        if self.fixi_content_type is not None and not isinstance(self.fixi_content_type, str):
            self.fixi_content_type = str(self.fixi_content_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfaceV11(OrchestraBaseInterfaceV11):
    """
    A named service offering and the sessions it carries, with the protocols on each layer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfaceV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfaceV11"
    class_name: ClassVar[str] = "OrchestraInterfaceV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfaceV11

    fixi_name: str = None
    fixi_sessions: Optional[Union[dict, "OrchestraSessionsV11"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_sessions is not None and not isinstance(self.fixi_sessions, OrchestraSessionsV11):
            self.fixi_sessions = OrchestraSessionsV11(**as_dict(self.fixi_sessions))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraInterfacesV11(YAMLRoot):
    """
    A description of the services and sessions a party offers and how to reach them, headed by its Dublin Core
    metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraInterfacesV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraInterfacesV11"
    class_name: ClassVar[str] = "OrchestraInterfacesV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraInterfacesV11

    fixi_metadata: Union[dict, OrchestraMetadata] = None
    fixi_interface: Optional[Union[Union[dict, OrchestraInterfaceV11], list[Union[dict, OrchestraInterfaceV11]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixi_metadata):
            self.MissingRequiredField("fixi_metadata")
        if not isinstance(self.fixi_metadata, OrchestraMetadata):
            self.fixi_metadata = OrchestraMetadata(**as_dict(self.fixi_metadata))

        self._normalize_inlined_as_list(slot_name="fixi_interface", slot_type=OrchestraInterfaceV11, key_name="fixi_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraMappedDatatypeV11(YAMLRoot):
    """
    How a FIX datatype is written in another standard, such as XML Schema or protocol buffers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMappedDatatypeV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMappedDatatypeV11"
    class_name: ClassVar[str] = "OrchestraMappedDatatypeV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMappedDatatypeV11

    fixr_standard: str = None
    fixr_encoding: Optional[Union[dict, "OrchestraUnnamedEncodingV11"]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_builtin: Optional[Union[bool, Bool]] = None
    fixr_base: Optional[str] = None
    fixr_pattern: Optional[str] = None
    fixr_element: Optional[str] = None
    fixr_size: Optional[int] = None
    fixr_parameter: Optional[str] = None
    fixr_min_inclusive: Optional[str] = None
    fixr_max_inclusive: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_standard):
            self.MissingRequiredField("fixr_standard")
        if not isinstance(self.fixr_standard, str):
            self.fixr_standard = str(self.fixr_standard)

        if self.fixr_encoding is not None and not isinstance(self.fixr_encoding, OrchestraUnnamedEncodingV11):
            self.fixr_encoding = OrchestraUnnamedEncodingV11(**as_dict(self.fixr_encoding))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_builtin is not None and not isinstance(self.fixr_builtin, Bool):
            self.fixr_builtin = Bool(self.fixr_builtin)

        if self.fixr_base is not None and not isinstance(self.fixr_base, str):
            self.fixr_base = str(self.fixr_base)

        if self.fixr_pattern is not None and not isinstance(self.fixr_pattern, str):
            self.fixr_pattern = str(self.fixr_pattern)

        if self.fixr_element is not None and not isinstance(self.fixr_element, str):
            self.fixr_element = str(self.fixr_element)

        if self.fixr_size is not None and not isinstance(self.fixr_size, int):
            self.fixr_size = int(self.fixr_size)

        if self.fixr_parameter is not None and not isinstance(self.fixr_parameter, str):
            self.fixr_parameter = str(self.fixr_parameter)

        if self.fixr_min_inclusive is not None and not isinstance(self.fixr_min_inclusive, str):
            self.fixr_min_inclusive = str(self.fixr_min_inclusive)

        if self.fixr_max_inclusive is not None and not isinstance(self.fixr_max_inclusive, str):
            self.fixr_max_inclusive = str(self.fixr_max_inclusive)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraMessageRefV11(YAMLRoot):
    """
    A message an action sends, by its number and type code, with the fields it sets or carries over.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMessageRefV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMessageRefV11"
    class_name: ClassVar[str] = "OrchestraMessageRefV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMessageRefV11

    fixr_id: int = None
    fixr_identifiers: Optional[Union[dict, OrchestraIdentifiersV11]] = None
    fixr_msg_type: Optional[str] = None
    fixr_impl_min_occurs: Optional[int] = 1
    fixr_impl_max_occurs: Optional[str] = "unbounded"
    fixr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self.fixr_identifiers is not None and not isinstance(self.fixr_identifiers, OrchestraIdentifiersV11):
            self.fixr_identifiers = OrchestraIdentifiersV11(**as_dict(self.fixr_identifiers))

        if self.fixr_msg_type is not None and not isinstance(self.fixr_msg_type, str):
            self.fixr_msg_type = str(self.fixr_msg_type)

        if self.fixr_impl_min_occurs is not None and not isinstance(self.fixr_impl_min_occurs, int):
            self.fixr_impl_min_occurs = int(self.fixr_impl_min_occurs)

        if self.fixr_impl_max_occurs is not None and not isinstance(self.fixr_impl_max_occurs, str):
            self.fixr_impl_max_occurs = str(self.fixr_impl_max_occurs)

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraMessageStructureV11(YAMLRoot):
    """
    The ordered fields, groups and components of a message.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMessageStructureV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMessageStructureV11"
    class_name: ClassVar[str] = "OrchestraMessageStructureV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMessageStructureV11

    fixr_members: Optional[Union[Union[dict, "OrchestraStructureMemberV11"], list[Union[dict, "OrchestraStructureMemberV11"]]]] = empty_list()
    fixr_which: Optional[Union[str, "OrchestraMemberSelection"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.fixr_members, list):
            self.fixr_members = [self.fixr_members] if self.fixr_members is not None else []
        self.fixr_members = [v if isinstance(v, OrchestraStructureMemberV11) else OrchestraStructureMemberV11(**as_dict(v)) for v in self.fixr_members]

        if self.fixr_which is not None and not isinstance(self.fixr_which, OrchestraMemberSelection):
            self.fixr_which = OrchestraMemberSelection(self.fixr_which)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraMessageV11(YAMLRoot):
    """
    A FIX message: its type code, the fields, groups and components it carries in order, and the responses it can
    cause.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMessageV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMessageV11"
    class_name: ClassVar[str] = "OrchestraMessageV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMessageV11

    fixr_id: int = None
    fixr_name: str = None
    fixr_structure: Optional[Union[dict, OrchestraMessageStructureV11]] = None
    fixr_when: Optional[str] = None
    fixr_responses: Optional[Union[dict, "OrchestraResponsesV11"]] = None
    fixr_encodings: Optional[Union[dict, OrchestraEncodingsV11]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_msg_type: Optional[str] = None
    fixr_category: Optional[str] = None
    fixr_flow: Optional[str] = None
    fixr_rendering: Optional[str] = None
    fixr_abbr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"
    fixr_scenario_ref_id: Optional[int] = None
    fixr_scenario_ref: Optional[str] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_structure is not None and not isinstance(self.fixr_structure, OrchestraMessageStructureV11):
            self.fixr_structure = OrchestraMessageStructureV11(**as_dict(self.fixr_structure))

        if self.fixr_when is not None and not isinstance(self.fixr_when, str):
            self.fixr_when = str(self.fixr_when)

        if self.fixr_responses is not None and not isinstance(self.fixr_responses, OrchestraResponsesV11):
            self.fixr_responses = OrchestraResponsesV11(**as_dict(self.fixr_responses))

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_msg_type is not None and not isinstance(self.fixr_msg_type, str):
            self.fixr_msg_type = str(self.fixr_msg_type)

        if self.fixr_category is not None and not isinstance(self.fixr_category, str):
            self.fixr_category = str(self.fixr_category)

        if self.fixr_flow is not None and not isinstance(self.fixr_flow, str):
            self.fixr_flow = str(self.fixr_flow)

        if self.fixr_rendering is not None and not isinstance(self.fixr_rendering, str):
            self.fixr_rendering = str(self.fixr_rendering)

        if self.fixr_abbr_name is not None and not isinstance(self.fixr_abbr_name, str):
            self.fixr_abbr_name = str(self.fixr_abbr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        if self.fixr_scenario_ref_id is not None and not isinstance(self.fixr_scenario_ref_id, int):
            self.fixr_scenario_ref_id = int(self.fixr_scenario_ref_id)

        if self.fixr_scenario_ref is not None and not isinstance(self.fixr_scenario_ref, str):
            self.fixr_scenario_ref = str(self.fixr_scenario_ref)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraMessagesV11(YAMLRoot):
    """
    The messages a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraMessagesV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraMessagesV11"
    class_name: ClassVar[str] = "OrchestraMessagesV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraMessagesV11

    fixr_message: Optional[Union[Union[dict, OrchestraMessageV11], list[Union[dict, OrchestraMessageV11]]]] = empty_list()
    fixr_encodings: Optional[Union[dict, OrchestraEncodingsV11]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_message", slot_type=OrchestraMessageV11, key_name="fixr_id", keyed=False)

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraNamedEncodingV11(OrchestraBaseEncodingV11):
    """
    An encoding block that names the encoding standard it is for.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraNamedEncodingV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraNamedEncodingV11"
    class_name: ClassVar[str] = "OrchestraNamedEncodingV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraNamedEncodingV11

    fixr_standard: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_standard):
            self.MissingRequiredField("fixr_standard")
        if not isinstance(self.fixr_standard, str):
            self.fixr_standard = str(self.fixr_standard)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraPedigreeV11Mixin(YAMLRoot):
    """
    When an element was added, changed, deprecated or replaced, by FIX version and extension pack, and whether it is
    supported.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraPedigreeV11Mixin"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraPedigreeV11Mixin"
    class_name: ClassVar[str] = "OrchestraPedigreeV11Mixin"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraPedigreeV11Mixin

    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraProtocolV11(YAMLRoot):
    """
    A protocol used on one layer of an interface or session, with its version, layer and delivery guarantee.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraProtocolV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraProtocolV11"
    class_name: ClassVar[str] = "OrchestraProtocolV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraProtocolV11

    fixi_annotation: Optional[Union[dict, OrchestraInterfaceAnnotationV11]] = None
    fixi_name: Optional[Union[str, "OrchestraProtocolName"]] = None
    fixi_version: Optional[str] = None
    fixi_activation_time: Optional[str] = None
    fixi_deactivation_time: Optional[str] = None
    fixi_deprecated: Optional[str] = None
    fixi_layer: Optional[Union[str, "OrchestraLayer"]] = None
    fixi_reliability: Optional[Union[str, "OrchestraReliability"]] = None
    fixi_orchestration: Optional[Union[str, URI]] = None
    fixi_other_attributes: Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_annotation is not None and not isinstance(self.fixi_annotation, OrchestraInterfaceAnnotationV11):
            self.fixi_annotation = OrchestraInterfaceAnnotationV11(**as_dict(self.fixi_annotation))

        if self.fixi_name is not None and not isinstance(self.fixi_name, (OrchestraProtocolName, str)):
            value = self.fixi_name
            for _coerce in (lambda: OrchestraProtocolName(value), lambda: str(value)):
                try:
                    self.fixi_name = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraProtocolName, str] could be constructed from {value!r} for slot fixi_name")

        if self.fixi_version is not None and not isinstance(self.fixi_version, str):
            self.fixi_version = str(self.fixi_version)

        if self.fixi_activation_time is not None and not isinstance(self.fixi_activation_time, str):
            self.fixi_activation_time = str(self.fixi_activation_time)

        if self.fixi_deactivation_time is not None and not isinstance(self.fixi_deactivation_time, str):
            self.fixi_deactivation_time = str(self.fixi_deactivation_time)

        if self.fixi_deprecated is not None and not isinstance(self.fixi_deprecated, str):
            self.fixi_deprecated = str(self.fixi_deprecated)

        if self.fixi_layer is not None and not isinstance(self.fixi_layer, OrchestraLayer):
            self.fixi_layer = OrchestraLayer(self.fixi_layer)

        if self.fixi_reliability is not None and not isinstance(self.fixi_reliability, OrchestraReliability):
            self.fixi_reliability = OrchestraReliability(self.fixi_reliability)

        if self.fixi_orchestration is not None and not isinstance(self.fixi_orchestration, URI):
            self.fixi_orchestration = URI(self.fixi_orchestration)

        self._normalize_inlined_as_list(slot_name="fixi_other_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        super().__post_init__(**kwargs)


class OrchestraEncodingV11(OrchestraProtocolV11):
    """
    An encoding used on an interface or session, such as tag=value, FIXML or SBE.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraEncodingV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraEncodingV11"
    class_name: ClassVar[str] = "OrchestraEncodingV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraEncodingV11


@dataclass(repr=False)
class OrchestraReferenceV11Mixin(YAMLRoot):
    """
    The keys by which a use points at a defined element: its number, its scenario and, as a convenience, its name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraReferenceV11Mixin"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraReferenceV11Mixin"
    class_name: ClassVar[str] = "OrchestraReferenceV11Mixin"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraReferenceV11Mixin

    fixr_id: int = None
    fixr_name: Optional[str] = None
    fixr_scenario: Optional[str] = "base"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_id):
            self.MissingRequiredField("fixr_id")
        if not isinstance(self.fixr_id, int):
            self.fixr_id = int(self.fixr_id)

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_scenario is not None and not isinstance(self.fixr_scenario, str):
            self.fixr_scenario = str(self.fixr_scenario)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraRepositoryV11(YAMLRoot):
    """
    A machine-readable set of rules of engagement: the datatypes, code sets, fields, components, groups and messages
    it defines, and the actors and workflows that use them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraRepositoryV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraRepositoryV11"
    class_name: ClassVar[str] = "OrchestraRepositoryV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraRepositoryV11

    fixr_metadata: Union[dict, OrchestraMetadata] = None
    fixr_name: str = None
    fixr_version: str = None
    fixr_categories: Optional[Union[dict, OrchestraCategoriesV11]] = None
    fixr_sections: Optional[Union[dict, "OrchestraSectionsV11"]] = None
    fixr_encoding_standards: Optional[Union[dict, OrchestraEncodingStandardsV11]] = None
    fixr_datatypes: Optional[Union[dict, OrchestraDatatypesV11]] = None
    fixr_code_sets: Optional[Union[dict, OrchestraCodeSetsV11]] = None
    fixr_fields: Optional[Union[dict, OrchestraFieldsV11]] = None
    fixr_actors: Optional[Union[dict, OrchestraActorsV11]] = None
    fixr_components: Optional[Union[dict, OrchestraComponentsV11]] = None
    fixr_groups: Optional[Union[dict, OrchestraGroupsV11]] = None
    fixr_messages: Optional[Union[dict, OrchestraMessagesV11]] = None
    fixr_concepts: Optional[Union[dict, OrchestraConceptsV11]] = None
    fixr_scenarios: Optional[Union[dict, "OrchestraScenariosV11"]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_guid: Optional[str] = None
    fixr_spec_url: Optional[Union[str, URI]] = None
    fixr_namespace: Optional[Union[str, URI]] = None
    fixr_expression_language: Optional[str] = "Score"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_metadata):
            self.MissingRequiredField("fixr_metadata")
        if not isinstance(self.fixr_metadata, OrchestraMetadata):
            self.fixr_metadata = OrchestraMetadata(**as_dict(self.fixr_metadata))

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self._is_empty(self.fixr_version):
            self.MissingRequiredField("fixr_version")
        if not isinstance(self.fixr_version, str):
            self.fixr_version = str(self.fixr_version)

        if self.fixr_categories is not None and not isinstance(self.fixr_categories, OrchestraCategoriesV11):
            self.fixr_categories = OrchestraCategoriesV11(**as_dict(self.fixr_categories))

        if self.fixr_sections is not None and not isinstance(self.fixr_sections, OrchestraSectionsV11):
            self.fixr_sections = OrchestraSectionsV11(**as_dict(self.fixr_sections))

        if self.fixr_encoding_standards is not None and not isinstance(self.fixr_encoding_standards, OrchestraEncodingStandardsV11):
            self.fixr_encoding_standards = OrchestraEncodingStandardsV11(**as_dict(self.fixr_encoding_standards))

        if self.fixr_datatypes is not None and not isinstance(self.fixr_datatypes, OrchestraDatatypesV11):
            self.fixr_datatypes = OrchestraDatatypesV11(**as_dict(self.fixr_datatypes))

        if self.fixr_code_sets is not None and not isinstance(self.fixr_code_sets, OrchestraCodeSetsV11):
            self.fixr_code_sets = OrchestraCodeSetsV11(**as_dict(self.fixr_code_sets))

        if self.fixr_fields is not None and not isinstance(self.fixr_fields, OrchestraFieldsV11):
            self.fixr_fields = OrchestraFieldsV11(**as_dict(self.fixr_fields))

        if self.fixr_actors is not None and not isinstance(self.fixr_actors, OrchestraActorsV11):
            self.fixr_actors = OrchestraActorsV11(**as_dict(self.fixr_actors))

        if self.fixr_components is not None and not isinstance(self.fixr_components, OrchestraComponentsV11):
            self.fixr_components = OrchestraComponentsV11(**as_dict(self.fixr_components))

        if self.fixr_groups is not None and not isinstance(self.fixr_groups, OrchestraGroupsV11):
            self.fixr_groups = OrchestraGroupsV11(**as_dict(self.fixr_groups))

        if self.fixr_messages is not None and not isinstance(self.fixr_messages, OrchestraMessagesV11):
            self.fixr_messages = OrchestraMessagesV11(**as_dict(self.fixr_messages))

        if self.fixr_concepts is not None and not isinstance(self.fixr_concepts, OrchestraConceptsV11):
            self.fixr_concepts = OrchestraConceptsV11(**as_dict(self.fixr_concepts))

        if self.fixr_scenarios is not None and not isinstance(self.fixr_scenarios, OrchestraScenariosV11):
            self.fixr_scenarios = OrchestraScenariosV11(**as_dict(self.fixr_scenarios))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_guid is not None and not isinstance(self.fixr_guid, str):
            self.fixr_guid = str(self.fixr_guid)

        if self.fixr_spec_url is not None and not isinstance(self.fixr_spec_url, URI):
            self.fixr_spec_url = URI(self.fixr_spec_url)

        if self.fixr_namespace is not None and not isinstance(self.fixr_namespace, URI):
            self.fixr_namespace = URI(self.fixr_namespace)

        if self.fixr_expression_language is not None and not isinstance(self.fixr_expression_language, str):
            self.fixr_expression_language = str(self.fixr_expression_language)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraResponseV11(OrchestraActionV11):
    """
    What happens when a message arrives, under an optional condition: messages sent, values set, transitions fired and
    timers scheduled.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraResponseV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraResponseV11"
    class_name: ClassVar[str] = "OrchestraResponseV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraResponseV11

    fixr_actions: Union[Union[dict, OrchestraActionStepV11], list[Union[dict, OrchestraActionStepV11]]] = None
    fixr_when: Optional[str] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_name: Optional[str] = None
    fixr_sync: Optional[Union[str, "OrchestraSynchronization"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_when is not None and not isinstance(self.fixr_when, str):
            self.fixr_when = str(self.fixr_when)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_sync is not None and not isinstance(self.fixr_sync, OrchestraSynchronization):
            self.fixr_sync = OrchestraSynchronization(self.fixr_sync)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraResponsesV11(YAMLRoot):
    """
    The responses a message can cause, tried one after another as given.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraResponsesV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraResponsesV11"
    class_name: ClassVar[str] = "OrchestraResponsesV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraResponsesV11

    fixr_response: Union[Union[dict, OrchestraResponseV11], list[Union[dict, OrchestraResponseV11]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_response):
            self.MissingRequiredField("fixr_response")
        if not isinstance(self.fixr_response, list):
            self.fixr_response = [self.fixr_response] if self.fixr_response is not None else []
        self.fixr_response = [v if isinstance(v, OrchestraResponseV11) else OrchestraResponseV11(**as_dict(v)) for v in self.fixr_response]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraScenarioReferenceV11Mixin(YAMLRoot):
    """
    A pointer from an element to the scenario it belongs to, by number and, if wanted, name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraScenarioReferenceV11Mixin"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraScenarioReferenceV11Mixin"
    class_name: ClassVar[str] = "OrchestraScenarioReferenceV11Mixin"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraScenarioReferenceV11Mixin

    fixr_scenario_ref_id: Optional[int] = None
    fixr_scenario_ref: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_scenario_ref_id is not None and not isinstance(self.fixr_scenario_ref_id, int):
            self.fixr_scenario_ref_id = int(self.fixr_scenario_ref_id)

        if self.fixr_scenario_ref is not None and not isinstance(self.fixr_scenario_ref, str):
            self.fixr_scenario_ref = str(self.fixr_scenario_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraScenarioV11(YAMLRoot):
    """
    A named variant of elements for one use case, such as a workflow or an asset class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraScenarioV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraScenarioV11"
    class_name: ClassVar[str] = "OrchestraScenarioV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraScenarioV11

    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_name: Optional[str] = "base"
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_name is not None and not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraScenariosV11(YAMLRoot):
    """
    The scenarios a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraScenariosV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraScenariosV11"
    class_name: ClassVar[str] = "OrchestraScenariosV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraScenariosV11

    fixr_scenario: Optional[Union[Union[dict, OrchestraScenarioV11], list[Union[dict, OrchestraScenarioV11]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.fixr_scenario, list):
            self.fixr_scenario = [self.fixr_scenario] if self.fixr_scenario is not None else []
        self.fixr_scenario = [v if isinstance(v, OrchestraScenarioV11) else OrchestraScenarioV11(**as_dict(v)) for v in self.fixr_scenario]

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraSectionV11(YAMLRoot):
    """
    A broad business area, such as pre-trade or post-trade, that categories fall under.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSectionV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSectionV11"
    class_name: ClassVar[str] = "OrchestraSectionV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSectionV11

    fixr_name: str = None
    fixr_encodings: Optional[Union[dict, OrchestraEncodingsV11]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    fixr_display_order: Optional[int] = None
    fixr_added: Optional[str] = None
    fixr_added_ep: Optional[int] = None
    fixr_change_type: Optional[Union[str, "OrchestraChangeKind"]] = None
    fixr_deprecated: Optional[str] = None
    fixr_deprecated_ep: Optional[int] = None
    fixr_issue: Optional[str] = None
    fixr_last_modified: Optional[str] = None
    fixr_replaced: Optional[str] = None
    fixr_replaced_ep: Optional[int] = None
    fixr_replaced_by_field: Optional[int] = None
    fixr_supported: Optional[Union[str, "OrchestraSupport"]] = 'supported'
    fixr_updated: Optional[str] = None
    fixr_updated_ep: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_encodings is not None and not isinstance(self.fixr_encodings, OrchestraEncodingsV11):
            self.fixr_encodings = OrchestraEncodingsV11(**as_dict(self.fixr_encodings))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.fixr_display_order is not None and not isinstance(self.fixr_display_order, int):
            self.fixr_display_order = int(self.fixr_display_order)

        if self.fixr_added is not None and not isinstance(self.fixr_added, str):
            self.fixr_added = str(self.fixr_added)

        if self.fixr_added_ep is not None and not isinstance(self.fixr_added_ep, int):
            self.fixr_added_ep = int(self.fixr_added_ep)

        if self.fixr_change_type is not None and not isinstance(self.fixr_change_type, OrchestraChangeKind):
            self.fixr_change_type = OrchestraChangeKind(self.fixr_change_type)

        if self.fixr_deprecated is not None and not isinstance(self.fixr_deprecated, str):
            self.fixr_deprecated = str(self.fixr_deprecated)

        if self.fixr_deprecated_ep is not None and not isinstance(self.fixr_deprecated_ep, int):
            self.fixr_deprecated_ep = int(self.fixr_deprecated_ep)

        if self.fixr_issue is not None and not isinstance(self.fixr_issue, str):
            self.fixr_issue = str(self.fixr_issue)

        if self.fixr_last_modified is not None and not isinstance(self.fixr_last_modified, str):
            self.fixr_last_modified = str(self.fixr_last_modified)

        if self.fixr_replaced is not None and not isinstance(self.fixr_replaced, str):
            self.fixr_replaced = str(self.fixr_replaced)

        if self.fixr_replaced_ep is not None and not isinstance(self.fixr_replaced_ep, int):
            self.fixr_replaced_ep = int(self.fixr_replaced_ep)

        if self.fixr_replaced_by_field is not None and not isinstance(self.fixr_replaced_by_field, int):
            self.fixr_replaced_by_field = int(self.fixr_replaced_by_field)

        if self.fixr_supported is not None and not isinstance(self.fixr_supported, OrchestraSupport):
            self.fixr_supported = OrchestraSupport(self.fixr_supported)

        if self.fixr_updated is not None and not isinstance(self.fixr_updated, str):
            self.fixr_updated = str(self.fixr_updated)

        if self.fixr_updated_ep is not None and not isinstance(self.fixr_updated_ep, int):
            self.fixr_updated_ep = int(self.fixr_updated_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraSectionsV11(YAMLRoot):
    """
    The sections a repository defines.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSectionsV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSectionsV11"
    class_name: ClassVar[str] = "OrchestraSectionsV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSectionsV11

    fixr_section: Optional[Union[Union[dict, OrchestraSectionV11], list[Union[dict, OrchestraSectionV11]]]] = empty_list()
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None
    xml_base: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_section", slot_type=OrchestraSectionV11, key_name="fixr_name", keyed=False)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        if self.xml_base is not None and not isinstance(self.xml_base, URI):
            self.xml_base = URI(self.xml_base)

        super().__post_init__(**kwargs)


class OrchestraServiceV11(OrchestraProtocolV11):
    """
    An application-level service an interface offers, such as order routing, with the Orchestra repository that sets
    out its rules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraServiceV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraServiceV11"
    class_name: ClassVar[str] = "OrchestraServiceV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraServiceV11


@dataclass(repr=False)
class OrchestraSessionIdentifierV11(YAMLRoot):
    """
    A value, with what kind it is, that picks out a session, such as a sender or target ID.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSessionIdentifierV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSessionIdentifierV11"
    class_name: ClassVar[str] = "OrchestraSessionIdentifierV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSessionIdentifierV11

    fixi_text: Optional[str] = None
    fixi_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_text is not None and not isinstance(self.fixi_text, str):
            self.fixi_text = str(self.fixi_text)

        if self.fixi_name is not None and not isinstance(self.fixi_name, str):
            self.fixi_name = str(self.fixi_name)

        super().__post_init__(**kwargs)


class OrchestraSessionProtocolV11(OrchestraProtocolV11):
    """
    The session-level protocol of an interface or session, such as FIXT or FIXP.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSessionProtocolV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSessionProtocolV11"
    class_name: ClassVar[str] = "OrchestraSessionProtocolV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSessionProtocolV11


@dataclass(repr=False)
class OrchestraSessionV11(OrchestraBaseInterfaceV11):
    """
    One connection between two parties, with the identifiers, role, activation times and security keys that set it up.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSessionV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSessionV11"
    class_name: ClassVar[str] = "OrchestraSessionV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSessionV11

    fixi_name: str = None
    fixi_identifier: Optional[Union[Union[dict, OrchestraSessionIdentifierV11], list[Union[dict, OrchestraSessionIdentifierV11]]]] = empty_list()
    fixi_role: Optional[Union[str, "OrchestraRole"]] = None
    fixi_security_keys: Optional[str] = None
    fixi_activation_time: Optional[str] = None
    fixi_deactivation_time: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.fixi_identifier, list):
            self.fixi_identifier = [self.fixi_identifier] if self.fixi_identifier is not None else []
        self.fixi_identifier = [v if isinstance(v, OrchestraSessionIdentifierV11) else OrchestraSessionIdentifierV11(**as_dict(v)) for v in self.fixi_identifier]

        if self.fixi_role is not None and not isinstance(self.fixi_role, OrchestraRole):
            self.fixi_role = OrchestraRole(self.fixi_role)

        if self.fixi_security_keys is not None and not isinstance(self.fixi_security_keys, str):
            self.fixi_security_keys = str(self.fixi_security_keys)

        if self.fixi_activation_time is not None and not isinstance(self.fixi_activation_time, str):
            self.fixi_activation_time = str(self.fixi_activation_time)

        if self.fixi_deactivation_time is not None and not isinstance(self.fixi_deactivation_time, str):
            self.fixi_deactivation_time = str(self.fixi_deactivation_time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraSessionsV11(YAMLRoot):
    """
    The sessions an interface carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraSessionsV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraSessionsV11"
    class_name: ClassVar[str] = "OrchestraSessionsV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraSessionsV11

    fixi_session: Union[Union[dict, OrchestraSessionV11], list[Union[dict, OrchestraSessionV11]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixi_session):
            self.MissingRequiredField("fixi_session")
        self._normalize_inlined_as_list(slot_name="fixi_session", slot_type=OrchestraSessionV11, key_name="fixi_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraStateMachineV11(YAMLRoot):
    """
    A named set of states that an actor moves through, from an initial state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraStateMachineV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraStateMachineV11"
    class_name: ClassVar[str] = "OrchestraStateMachineV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraStateMachineV11

    fixr_initial: Union[dict, "OrchestraStateV11"] = None
    fixr_state: Union[Union[dict, "OrchestraStateV11"], list[Union[dict, "OrchestraStateV11"]]] = None
    fixr_name: str = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_initial):
            self.MissingRequiredField("fixr_initial")
        if not isinstance(self.fixr_initial, OrchestraStateV11):
            self.fixr_initial = OrchestraStateV11(**as_dict(self.fixr_initial))

        if self._is_empty(self.fixr_state):
            self.MissingRequiredField("fixr_state")
        self._normalize_inlined_as_list(slot_name="fixr_state", slot_type=OrchestraStateV11, key_name="fixr_name", keyed=False)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraStateV11(YAMLRoot):
    """
    One of a state machine's states, with the transitions out of it and what happens on entry, while active and on
    exit.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraStateV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraStateV11"
    class_name: ClassVar[str] = "OrchestraStateV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraStateV11

    fixr_name: str = None
    fixr_transition: Optional[Union[Union[dict, "OrchestraTransitionV11"], list[Union[dict, "OrchestraTransitionV11"]]]] = empty_list()
    fixr_onentry: Optional[Union[dict, OrchestraActionV11]] = None
    fixr_activity: Optional[Union[dict, OrchestraActionV11]] = None
    fixr_onexit: Optional[Union[dict, OrchestraActionV11]] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        self._normalize_inlined_as_list(slot_name="fixr_transition", slot_type=OrchestraTransitionV11, key_name="fixr_name", keyed=False)

        if self.fixr_onentry is not None and not isinstance(self.fixr_onentry, OrchestraActionV11):
            self.fixr_onentry = OrchestraActionV11(**as_dict(self.fixr_onentry))

        if self.fixr_activity is not None and not isinstance(self.fixr_activity, OrchestraActionV11):
            self.fixr_activity = OrchestraActionV11(**as_dict(self.fixr_activity))

        if self.fixr_onexit is not None and not isinstance(self.fixr_onexit, OrchestraActionV11):
            self.fixr_onexit = OrchestraActionV11(**as_dict(self.fixr_onexit))

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraStructureMemberV11(YAMLRoot):
    """
    One item of an ordered structure, a component, a group or a field, by reference. It holds exactly one of these.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraStructureMemberV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraStructureMemberV11"
    class_name: ClassVar[str] = "OrchestraStructureMemberV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraStructureMemberV11

    fixr_component_ref: Optional[Union[dict, OrchestraComponentRefV11]] = None
    fixr_group_ref: Optional[Union[dict, OrchestraGroupRefV11]] = None
    fixr_field_ref: Optional[Union[dict, OrchestraFieldRefV11]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixr_component_ref is not None and not isinstance(self.fixr_component_ref, OrchestraComponentRefV11):
            self.fixr_component_ref = OrchestraComponentRefV11(**as_dict(self.fixr_component_ref))

        if self.fixr_group_ref is not None and not isinstance(self.fixr_group_ref, OrchestraGroupRefV11):
            self.fixr_group_ref = OrchestraGroupRefV11(**as_dict(self.fixr_group_ref))

        if self.fixr_field_ref is not None and not isinstance(self.fixr_field_ref, OrchestraFieldRefV11):
            self.fixr_field_ref = OrchestraFieldRefV11(**as_dict(self.fixr_field_ref))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraTimerScheduleV11(YAMLRoot):
    """
    A step that starts, stops or restarts an actor's timer, with its interval and what to do when it runs out.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraTimerScheduleV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraTimerScheduleV11"
    class_name: ClassVar[str] = "OrchestraTimerScheduleV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraTimerScheduleV11

    fixr_activity: Union[dict, OrchestraActionV11] = None
    fixr_actor: str = None
    fixr_name: str = None
    fixr_operation: Union[str, "OrchestraTimerOperation"] = None
    fixr_interval: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_activity):
            self.MissingRequiredField("fixr_activity")
        if not isinstance(self.fixr_activity, OrchestraActionV11):
            self.fixr_activity = OrchestraActionV11(**as_dict(self.fixr_activity))

        if self._is_empty(self.fixr_actor):
            self.MissingRequiredField("fixr_actor")
        if not isinstance(self.fixr_actor, str):
            self.fixr_actor = str(self.fixr_actor)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self._is_empty(self.fixr_operation):
            self.MissingRequiredField("fixr_operation")
        if not isinstance(self.fixr_operation, OrchestraTimerOperation):
            self.fixr_operation = OrchestraTimerOperation(self.fixr_operation)

        if self.fixr_interval is not None and not isinstance(self.fixr_interval, str):
            self.fixr_interval = str(self.fixr_interval)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraTimerV11(YAMLRoot):
    """
    A named timer that an actor owns.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraTimerV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraTimerV11"
    class_name: ClassVar[str] = "OrchestraTimerV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraTimerV11

    fixr_name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraTransitionV11(YAMLRoot):
    """
    A move from one state to a named target state, with the condition that allows it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraTransitionV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraTransitionV11"
    class_name: ClassVar[str] = "OrchestraTransitionV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraTransitionV11

    fixr_name: str = None
    fixr_target: str = None
    fixr_when: Optional[str] = None
    fixr_annotation: Optional[Union[dict, OrchestraAnnotationV11]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        if self._is_empty(self.fixr_target):
            self.MissingRequiredField("fixr_target")
        if not isinstance(self.fixr_target, str):
            self.fixr_target = str(self.fixr_target)

        if self.fixr_when is not None and not isinstance(self.fixr_when, str):
            self.fixr_when = str(self.fixr_when)

        if self.fixr_annotation is not None and not isinstance(self.fixr_annotation, OrchestraAnnotationV11):
            self.fixr_annotation = OrchestraAnnotationV11(**as_dict(self.fixr_annotation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraTransportV11(OrchestraProtocolV11):
    """
    The transport-level protocol of an interface or session, with its address, how messages are cast and its use.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraTransportV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraTransportV11"
    class_name: ClassVar[str] = "OrchestraTransportV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraTransportV11

    fixi_address: Optional[str] = None
    fixi_message_cast: Optional[Union[str, "OrchestraMessageCast"]] = 'unicast'
    fixi_use: Optional[Union[str, "OrchestraTransportUse"]] = None
    fixi_other_attributes: Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.fixi_address is not None and not isinstance(self.fixi_address, str):
            self.fixi_address = str(self.fixi_address)

        if self.fixi_message_cast is not None and not isinstance(self.fixi_message_cast, OrchestraMessageCast):
            self.fixi_message_cast = OrchestraMessageCast(self.fixi_message_cast)

        if self.fixi_use is not None and not isinstance(self.fixi_use, (OrchestraTransportUse, str)):
            value = self.fixi_use
            for _coerce in (lambda: OrchestraTransportUse(value), lambda: str(value)):
                try:
                    self.fixi_use = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[OrchestraTransportUse, str] could be constructed from {value!r} for slot fixi_use")

        self._normalize_inlined_as_list(slot_name="fixi_other_attributes", slot_type=OrchestraXmlAttribute, key_name="xml_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraTriggerV11(YAMLRoot):
    """
    A step that fires a named transition of an actor's state machine.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraTriggerV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraTriggerV11"
    class_name: ClassVar[str] = "OrchestraTriggerV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraTriggerV11

    fixr_state_machine: str = None
    fixr_actor: str = None
    fixr_name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.fixr_state_machine):
            self.MissingRequiredField("fixr_state_machine")
        if not isinstance(self.fixr_state_machine, str):
            self.fixr_state_machine = str(self.fixr_state_machine)

        if self._is_empty(self.fixr_actor):
            self.MissingRequiredField("fixr_actor")
        if not isinstance(self.fixr_actor, str):
            self.fixr_actor = str(self.fixr_actor)

        if self._is_empty(self.fixr_name):
            self.MissingRequiredField("fixr_name")
        if not isinstance(self.fixr_name, str):
            self.fixr_name = str(self.fixr_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrchestraUniqueV11(YAMLRoot):
    """
    A check that a field's value is unique among the values that share the other fields it names, or among all values
    when it names none.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraUniqueV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraUniqueV11"
    class_name: ClassVar[str] = "OrchestraUniqueV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraUniqueV11

    fixr_field_ref: Optional[Union[Union[dict, OrchestraFieldRefV11], list[Union[dict, OrchestraFieldRefV11]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="fixr_field_ref", slot_type=OrchestraFieldRefV11, key_name="fixr_id", keyed=False)

        super().__post_init__(**kwargs)


class OrchestraUnnamedEncodingV11(OrchestraBaseEncodingV11):
    """
    An encoding block whose standard is clear from where it sits, so it names none.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraUnnamedEncodingV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraUnnamedEncodingV11"
    class_name: ClassVar[str] = "OrchestraUnnamedEncodingV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraUnnamedEncodingV11


class OrchestraUserInterfaceV11(OrchestraProtocolV11):
    """
    A user interface an interface offers, such as a trading screen, described as a protocol.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_ORCHESTRA["OrchestraUserInterfaceV11"]
    class_class_curie: ClassVar[str] = "fix_orchestra:OrchestraUserInterfaceV11"
    class_name: ClassVar[str] = "OrchestraUserInterfaceV11"
    class_model_uri: ClassVar[URIRef] = FIX_ORCHESTRA.OrchestraUserInterfaceV11


# Enumerations
class OrchestraChangeKind(EnumDefinitionImpl):
    """
    How far an element's latest change reaches.
    """
    Editorial = PermissibleValue(
        text="Editorial",
        description="A change to wording only.")
    Definitional = PermissibleValue(
        text="Definitional",
        description="A change to what the element means.")

    _defn = EnumDefinition(
        name="OrchestraChangeKind",
        description="How far an element's latest change reaches.",
    )

class OrchestraLayer(EnumDefinitionImpl):
    """
    The layer of the communication stack a protocol works on.
    """
    application = PermissibleValue(
        text="application",
        description="The application layer.")
    presentation = PermissibleValue(
        text="presentation",
        description="The presentation layer, where encodings sit.")
    session = PermissibleValue(
        text="session",
        description="The session layer.")
    transport = PermissibleValue(
        text="transport",
        description="The transport layer.")

    _defn = EnumDefinition(
        name="OrchestraLayer",
        description="The layer of the communication stack a protocol works on.",
    )

class OrchestraMemberSelection(EnumDefinitionImpl):
    """
    How many of a block's members must appear.
    """
    oneOf = PermissibleValue(
        text="oneOf",
        description="Exactly one member appears.")
    anyOf = PermissibleValue(
        text="anyOf",
        description="One or more members appear.")

    _defn = EnumDefinition(
        name="OrchestraMemberSelection",
        description="How many of a block's members must appear.",
    )

class OrchestraMessageCast(EnumDefinitionImpl):
    """
    How many receivers a transport sends each message to.
    """
    unicast = PermissibleValue(
        text="unicast",
        description="One receiver.")
    multicast = PermissibleValue(
        text="multicast",
        description="A group of receivers.")
    broadcast = PermissibleValue(
        text="broadcast",
        description="Every receiver.")

    _defn = EnumDefinition(
        name="OrchestraMessageCast",
        description="How many receivers a transport sends each message to.",
    )

class OrchestraPresence(EnumDefinitionImpl):
    """
    Whether an item must, may or must not appear in a message.
    """
    optional = PermissibleValue(
        text="optional",
        description="May appear; a rule can make it required.")
    required = PermissibleValue(
        text="required",
        description="Must appear.")
    forbidden = PermissibleValue(
        text="forbidden",
        description="Must not appear.")
    ignored = PermissibleValue(
        text="ignored",
        description="May appear, and is not checked.")
    constant = PermissibleValue(
        text="constant",
        description="Has a fixed value, which some encodings leave off the wire.")

    _defn = EnumDefinition(
        name="OrchestraPresence",
        description="Whether an item must, may or must not appear in a message.",
    )

class OrchestraProtocolName(EnumDefinitionImpl):
    """
    The FIX protocols the interfaces file names, so that they are spelled one way. A file may name another protocol.
    """
    FIX4 = PermissibleValue(
        text="FIX4",
        description="The FIX 4 session layer.")
    FIXT = PermissibleValue(
        text="FIXT",
        description="FIXT 1.1, the session protocol of FIX 5.")
    FIXP = PermissibleValue(
        text="FIXP",
        description="FIXP, the FIX session protocol built for high performance.")
    tagvalue = PermissibleValue(
        text="tagvalue",
        description="Classic tag=value encoding.")
    FIXML = PermissibleValue(
        text="FIXML",
        description="FIX in XML.")
    FAST = PermissibleValue(
        text="FAST",
        description="The FAST streaming encoding.")
    SBE = PermissibleValue(
        text="SBE",
        description="Simple Binary Encoding.")
    SOFH = PermissibleValue(
        text="SOFH",
        description="The SOFH message framing header.")
    GPB = PermissibleValue(
        text="GPB",
        description="Google's protocol buffers.")
    JSON = PermissibleValue(
        text="JSON",
        description="JSON encoding.")
    FIXS = PermissibleValue(
        text="FIXS",
        description="FIX over TLS.")

    _defn = EnumDefinition(
        name="OrchestraProtocolName",
        description="""The FIX protocols the interfaces file names, so that they are spelled one way. A file may name another protocol.""",
    )

class OrchestraPurpose(EnumDefinitionImpl):
    """
    The kinds of purpose the standard names for a text or hint. A file may give another purpose of its own.
    """
    SYNOPSIS = PermissibleValue(
        text="SYNOPSIS",
        description="A short summary.")
    ELABORATION = PermissibleValue(
        text="ELABORATION",
        description="A longer explanation.")
    EXAMPLE = PermissibleValue(
        text="EXAMPLE",
        description="An example of use.")
    DISPLAY = PermissibleValue(
        text="DISPLAY",
        description="A name to show to people in place of the element's own.")

    _defn = EnumDefinition(
        name="OrchestraPurpose",
        description="""The kinds of purpose the standard names for a text or hint. A file may give another purpose of its own.""",
    )

class OrchestraReliability(EnumDefinitionImpl):
    """
    What a flow or protocol promises about delivering each message.
    """
    bestEffort = PermissibleValue(
        text="bestEffort",
        description="No promise; any message can be lost.")
    idempotent = PermissibleValue(
        text="idempotent",
        description="Each message is acted on at most once; a lost one is not sent again.")
    recoverable = PermissibleValue(
        text="recoverable",
        description="Each message is acted on exactly once; a lost one can be sent again.")

    _defn = EnumDefinition(
        name="OrchestraReliability",
        description="What a flow or protocol promises about delivering each message.",
    )

class OrchestraRole(EnumDefinitionImpl):
    """
    A party's role in setting up a session.
    """
    initiator = PermissibleValue(
        text="initiator",
        description="The party that opens a FIX session.")
    acceptor = PermissibleValue(
        text="acceptor",
        description="The party that answers a request to open a FIX session.")
    client = PermissibleValue(
        text="client",
        description="The party that connects to a server.")
    server = PermissibleValue(
        text="server",
        description="The party that waits for clients to connect.")

    _defn = EnumDefinition(
        name="OrchestraRole",
        description="A party's role in setting up a session.",
    )

class OrchestraSupport(EnumDefinitionImpl):
    """
    How a party treats an element of the standard.
    """
    supported = PermissibleValue(
        text="supported",
        description="The party supports the element.")
    forbidden = PermissibleValue(
        text="forbidden",
        description="The party refuses the element.")
    ignored = PermissibleValue(
        text="ignored",
        description="The party accepts the element and acts on none of it.")

    _defn = EnumDefinition(
        name="OrchestraSupport",
        description="How a party treats an element of the standard.",
    )

class OrchestraSynchronization(EnumDefinitionImpl):
    """
    How the timing of a response relates to the request it answers.
    """
    asynchronous = PermissibleValue(
        text="asynchronous",
        description="The response's timing has no tie to the request's.")
    synchronous = PermissibleValue(
        text="synchronous",
        description="A request waits until the one before it has its answer.")
    pipelined = PermissibleValue(
        text="pipelined",
        description="Each response follows its request, and several requests may wait for answers at once.")

    _defn = EnumDefinition(
        name="OrchestraSynchronization",
        description="How the timing of a response relates to the request it answers.",
    )

class OrchestraTimerOperation(EnumDefinitionImpl):
    """
    What a step does to an actor's timer.
    """
    START = PermissibleValue(
        text="START",
        description="Start the timer.")
    CANCEL = PermissibleValue(
        text="CANCEL",
        description="Stop the timer.")
    RESET = PermissibleValue(
        text="RESET",
        description="Stop the timer and start it again.")

    _defn = EnumDefinition(
        name="OrchestraTimerOperation",
        description="What a step does to an actor's timer.",
    )

class OrchestraTransportUse(EnumDefinitionImpl):
    """
    The roles the interfaces file names for a transport. A file may give another role of its own.
    """
    primary = PermissibleValue(
        text="primary",
        description="The main connection.")
    secondary = PermissibleValue(
        text="secondary",
        description="The backup connection.")
    alternate = PermissibleValue(
        text="alternate",
        description="Another connection, used in turn or by choice.")

    _defn = EnumDefinition(
        name="OrchestraTransportUse",
        description="The roles the interfaces file names for a transport. A file may give another role of its own.",
    )

class OrchestraCategoryContentV10(EnumDefinitionImpl):
    """
    What a category sorts, in v1.0.
    """
    Field = PermissibleValue(
        text="Field",
        description="The category sorts fields.")
    Message = PermissibleValue(
        text="Message",
        description="The category sorts messages.")

    _defn = EnumDefinition(
        name="OrchestraCategoryContentV10",
        description="What a category sorts, in v1.0.",
    )

class OrchestraCategoryIncludeFileV10(EnumDefinitionImpl):
    """
    The shared FIXML file a category's own file includes, in v1.0.
    """
    components = PermissibleValue(
        text="components",
        description="The shared file of components.")
    fields = PermissibleValue(
        text="fields",
        description="The shared file of fields.")

    _defn = EnumDefinition(
        name="OrchestraCategoryIncludeFileV10",
        description="The shared FIXML file a category's own file includes, in v1.0.",
    )

class OrchestraDatatypeStandardV10(EnumDefinitionImpl):
    """
    The standards v1.0 names for mapping a datatype. A file may give another standard of its own.
    """
    ISO11404 = PermissibleValue(
        text="ISO11404",
        description="The general-purpose datatypes of ISO/IEC 11404.")
    GPB = PermissibleValue(
        text="GPB",
        description="Google's protocol buffers.")
    JSON = PermissibleValue(
        text="JSON",
        description="JSON Schema.")
    SBE = PermissibleValue(
        text="SBE",
        description="Simple Binary Encoding.")
    XML = PermissibleValue(
        text="XML",
        description="XML Schema, as FIXML uses it.")
    TAG_VALUE = PermissibleValue(
        text="TAG_VALUE",
        description="The classic tag=value encoding.")

    _defn = EnumDefinition(
        name="OrchestraDatatypeStandardV10",
        description="The standards v1.0 names for mapping a datatype. A file may give another standard of its own.",
    )

class OrchestraUnionDatatypeV10(EnumDefinitionImpl):
    """
    The datatypes v1.0 names whose values a field may hold beside its codes.
    """
    Qty = PermissibleValue(
        text="Qty",
        description="Quantities.")
    Reserved100Plus = PermissibleValue(
        text="Reserved100Plus",
        description="Values from 100 up, kept for user-defined codes.")
    Reserved1000Plus = PermissibleValue(
        text="Reserved1000Plus",
        description="Values from 1000 up, kept for user-defined codes.")
    Reserved4000Plus = PermissibleValue(
        text="Reserved4000Plus",
        description="Values from 4000 up, kept for user-defined codes.")
    Tenor = PermissibleValue(
        text="Tenor",
        description="Tenors, such as 3M.")

    _defn = EnumDefinition(
        name="OrchestraUnionDatatypeV10",
        description="The datatypes v1.0 names whose values a field may hold beside its codes.",
    )

class OrchestraPurposeV11(EnumDefinitionImpl):
    """
    The kinds of purpose the standard names for a text or hint. A file may give another purpose of its own.
    """
    SYNOPSIS = PermissibleValue(
        text="SYNOPSIS",
        description="A short summary.")
    ELABORATION = PermissibleValue(
        text="ELABORATION",
        description="A longer explanation.")
    EXAMPLE = PermissibleValue(
        text="EXAMPLE",
        description="An example of use.")
    DISPLAY = PermissibleValue(
        text="DISPLAY",
        description="A name to show to people in place of the element's own.")
    CAPTION = PermissibleValue(
        text="CAPTION",
        description="A label for a table, a figure or a heading.")
    TOOLTIP = PermissibleValue(
        text="TOOLTIP",
        description="A short hint shown when a pointer rests on the element.")
    DEFINITION = PermissibleValue(
        text="DEFINITION",
        description="A formal definition in one sentence.")

    _defn = EnumDefinition(
        name="OrchestraPurposeV11",
        description="""The kinds of purpose the standard names for a text or hint. A file may give another purpose of its own.""",
    )

# Slots
class slots:
    pass

slots.orchestraMetadata__dc_title = Slot(uri=DC.title, name="orchestraMetadata__dc_title", curie=DC.curie('title'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_title, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_creator = Slot(uri=DC.creator, name="orchestraMetadata__dc_creator", curie=DC.curie('creator'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_creator, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_subject = Slot(uri=DC.subject, name="orchestraMetadata__dc_subject", curie=DC.curie('subject'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_subject, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_description = Slot(uri=DC.description, name="orchestraMetadata__dc_description", curie=DC.curie('description'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_description, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_publisher = Slot(uri=DC.publisher, name="orchestraMetadata__dc_publisher", curie=DC.curie('publisher'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_publisher, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_contributor = Slot(uri=DC.contributor, name="orchestraMetadata__dc_contributor", curie=DC.curie('contributor'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_contributor, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_date = Slot(uri=DC.date, name="orchestraMetadata__dc_date", curie=DC.curie('date'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_date, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_type = Slot(uri=DC.type, name="orchestraMetadata__dc_type", curie=DC.curie('type'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_type, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_format = Slot(uri=DC.format, name="orchestraMetadata__dc_format", curie=DC.curie('format'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_format, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_identifier = Slot(uri=DC.identifier, name="orchestraMetadata__dc_identifier", curie=DC.curie('identifier'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_identifier, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_source = Slot(uri=DC.source, name="orchestraMetadata__dc_source", curie=DC.curie('source'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_source, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_language = Slot(uri=DC.language, name="orchestraMetadata__dc_language", curie=DC.curie('language'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_language, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_relation = Slot(uri=DC.relation, name="orchestraMetadata__dc_relation", curie=DC.curie('relation'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_relation, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_coverage = Slot(uri=DC.coverage, name="orchestraMetadata__dc_coverage", curie=DC.curie('coverage'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_coverage, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dc_rights = Slot(uri=DC.rights, name="orchestraMetadata__dc_rights", curie=DC.curie('rights'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dc_rights, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_title = Slot(uri=DCTERMS.title, name="orchestraMetadata__dcterms_title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_title, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_creator = Slot(uri=DCTERMS.creator, name="orchestraMetadata__dcterms_creator", curie=DCTERMS.curie('creator'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_creator, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_subject = Slot(uri=DCTERMS.subject, name="orchestraMetadata__dcterms_subject", curie=DCTERMS.curie('subject'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_subject, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_description = Slot(uri=DCTERMS.description, name="orchestraMetadata__dcterms_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_description, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_publisher = Slot(uri=DCTERMS.publisher, name="orchestraMetadata__dcterms_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_publisher, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_contributor = Slot(uri=DCTERMS.contributor, name="orchestraMetadata__dcterms_contributor", curie=DCTERMS.curie('contributor'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_contributor, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_date = Slot(uri=DCTERMS.date, name="orchestraMetadata__dcterms_date", curie=DCTERMS.curie('date'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_date, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_type = Slot(uri=DCTERMS.type, name="orchestraMetadata__dcterms_type", curie=DCTERMS.curie('type'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_type, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_format = Slot(uri=DCTERMS.format, name="orchestraMetadata__dcterms_format", curie=DCTERMS.curie('format'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_format, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_identifier = Slot(uri=DCTERMS.identifier, name="orchestraMetadata__dcterms_identifier", curie=DCTERMS.curie('identifier'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_identifier, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_source = Slot(uri=DCTERMS.source, name="orchestraMetadata__dcterms_source", curie=DCTERMS.curie('source'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_source, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_language = Slot(uri=DCTERMS.language, name="orchestraMetadata__dcterms_language", curie=DCTERMS.curie('language'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_language, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_relation = Slot(uri=DCTERMS.relation, name="orchestraMetadata__dcterms_relation", curie=DCTERMS.curie('relation'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_relation, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_coverage = Slot(uri=DCTERMS.coverage, name="orchestraMetadata__dcterms_coverage", curie=DCTERMS.curie('coverage'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_coverage, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_rights = Slot(uri=DCTERMS.rights, name="orchestraMetadata__dcterms_rights", curie=DCTERMS.curie('rights'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_rights, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_alternative = Slot(uri=DCTERMS.alternative, name="orchestraMetadata__dcterms_alternative", curie=DCTERMS.curie('alternative'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_alternative, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_table_of_contents = Slot(uri=DCTERMS.tableOfContents, name="orchestraMetadata__dcterms_table_of_contents", curie=DCTERMS.curie('tableOfContents'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_table_of_contents, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_abstract = Slot(uri=DCTERMS.abstract, name="orchestraMetadata__dcterms_abstract", curie=DCTERMS.curie('abstract'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_abstract, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_created = Slot(uri=DCTERMS.created, name="orchestraMetadata__dcterms_created", curie=DCTERMS.curie('created'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_created, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_valid = Slot(uri=DCTERMS.valid, name="orchestraMetadata__dcterms_valid", curie=DCTERMS.curie('valid'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_valid, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_available = Slot(uri=DCTERMS.available, name="orchestraMetadata__dcterms_available", curie=DCTERMS.curie('available'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_available, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_issued = Slot(uri=DCTERMS.issued, name="orchestraMetadata__dcterms_issued", curie=DCTERMS.curie('issued'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_issued, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_modified = Slot(uri=DCTERMS.modified, name="orchestraMetadata__dcterms_modified", curie=DCTERMS.curie('modified'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_modified, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_date_accepted = Slot(uri=DCTERMS.dateAccepted, name="orchestraMetadata__dcterms_date_accepted", curie=DCTERMS.curie('dateAccepted'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_date_accepted, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_date_copyrighted = Slot(uri=DCTERMS.dateCopyrighted, name="orchestraMetadata__dcterms_date_copyrighted", curie=DCTERMS.curie('dateCopyrighted'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_date_copyrighted, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_date_submitted = Slot(uri=DCTERMS.dateSubmitted, name="orchestraMetadata__dcterms_date_submitted", curie=DCTERMS.curie('dateSubmitted'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_date_submitted, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_extent = Slot(uri=DCTERMS.extent, name="orchestraMetadata__dcterms_extent", curie=DCTERMS.curie('extent'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_extent, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_medium = Slot(uri=DCTERMS.medium, name="orchestraMetadata__dcterms_medium", curie=DCTERMS.curie('medium'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_medium, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_is_version_of = Slot(uri=DCTERMS.isVersionOf, name="orchestraMetadata__dcterms_is_version_of", curie=DCTERMS.curie('isVersionOf'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_is_version_of, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_has_version = Slot(uri=DCTERMS.hasVersion, name="orchestraMetadata__dcterms_has_version", curie=DCTERMS.curie('hasVersion'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_has_version, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_is_replaced_by = Slot(uri=DCTERMS.isReplacedBy, name="orchestraMetadata__dcterms_is_replaced_by", curie=DCTERMS.curie('isReplacedBy'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_is_replaced_by, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_replaces = Slot(uri=DCTERMS.replaces, name="orchestraMetadata__dcterms_replaces", curie=DCTERMS.curie('replaces'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_replaces, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_is_required_by = Slot(uri=DCTERMS.isRequiredBy, name="orchestraMetadata__dcterms_is_required_by", curie=DCTERMS.curie('isRequiredBy'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_is_required_by, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_requires = Slot(uri=DCTERMS.requires, name="orchestraMetadata__dcterms_requires", curie=DCTERMS.curie('requires'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_requires, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_is_part_of = Slot(uri=DCTERMS.isPartOf, name="orchestraMetadata__dcterms_is_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_is_part_of, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_has_part = Slot(uri=DCTERMS.hasPart, name="orchestraMetadata__dcterms_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_has_part, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_is_referenced_by = Slot(uri=DCTERMS.isReferencedBy, name="orchestraMetadata__dcterms_is_referenced_by", curie=DCTERMS.curie('isReferencedBy'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_is_referenced_by, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_references = Slot(uri=DCTERMS.references, name="orchestraMetadata__dcterms_references", curie=DCTERMS.curie('references'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_references, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_is_format_of = Slot(uri=DCTERMS.isFormatOf, name="orchestraMetadata__dcterms_is_format_of", curie=DCTERMS.curie('isFormatOf'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_is_format_of, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_has_format = Slot(uri=DCTERMS.hasFormat, name="orchestraMetadata__dcterms_has_format", curie=DCTERMS.curie('hasFormat'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_has_format, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_conforms_to = Slot(uri=DCTERMS.conformsTo, name="orchestraMetadata__dcterms_conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_conforms_to, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_spatial = Slot(uri=DCTERMS.spatial, name="orchestraMetadata__dcterms_spatial", curie=DCTERMS.curie('spatial'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_spatial, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_temporal = Slot(uri=DCTERMS.temporal, name="orchestraMetadata__dcterms_temporal", curie=DCTERMS.curie('temporal'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_temporal, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_audience = Slot(uri=DCTERMS.audience, name="orchestraMetadata__dcterms_audience", curie=DCTERMS.curie('audience'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_audience, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_accrual_method = Slot(uri=DCTERMS.accrualMethod, name="orchestraMetadata__dcterms_accrual_method", curie=DCTERMS.curie('accrualMethod'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_accrual_method, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_accrual_periodicity = Slot(uri=DCTERMS.accrualPeriodicity, name="orchestraMetadata__dcterms_accrual_periodicity", curie=DCTERMS.curie('accrualPeriodicity'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_accrual_periodicity, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_accrual_policy = Slot(uri=DCTERMS.accrualPolicy, name="orchestraMetadata__dcterms_accrual_policy", curie=DCTERMS.curie('accrualPolicy'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_accrual_policy, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_instructional_method = Slot(uri=DCTERMS.instructionalMethod, name="orchestraMetadata__dcterms_instructional_method", curie=DCTERMS.curie('instructionalMethod'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_instructional_method, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_provenance = Slot(uri=DCTERMS.provenance, name="orchestraMetadata__dcterms_provenance", curie=DCTERMS.curie('provenance'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_provenance, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_rights_holder = Slot(uri=DCTERMS.rightsHolder, name="orchestraMetadata__dcterms_rights_holder", curie=DCTERMS.curie('rightsHolder'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_rights_holder, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_mediator = Slot(uri=DCTERMS.mediator, name="orchestraMetadata__dcterms_mediator", curie=DCTERMS.curie('mediator'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_mediator, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_education_level = Slot(uri=DCTERMS.educationLevel, name="orchestraMetadata__dcterms_education_level", curie=DCTERMS.curie('educationLevel'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_education_level, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_access_rights = Slot(uri=DCTERMS.accessRights, name="orchestraMetadata__dcterms_access_rights", curie=DCTERMS.curie('accessRights'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_access_rights, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_license = Slot(uri=DCTERMS.license, name="orchestraMetadata__dcterms_license", curie=DCTERMS.curie('license'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_license, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraMetadata__dcterms_bibliographic_citation = Slot(uri=DCTERMS.bibliographicCitation, name="orchestraMetadata__dcterms_bibliographic_citation", curie=DCTERMS.curie('bibliographicCitation'),
                   model_uri=FIX_ORCHESTRA.orchestraMetadata__dcterms_bibliographic_citation, domain=None, range=Optional[Union[str, list[str]]])

slots.orchestraXmlElement__xml_name = Slot(uri=FIX_ORCHESTRA.xml_name, name="orchestraXmlElement__xml_name", curie=FIX_ORCHESTRA.curie('xml_name'),
                   model_uri=FIX_ORCHESTRA.orchestraXmlElement__xml_name, domain=None, range=str,
                   pattern=re.compile(r'^(\{[^}]*\})?[^\s{}]+$'))

slots.orchestraXmlElement__xml_attributes = Slot(uri=FIX_ORCHESTRA.xml_attributes, name="orchestraXmlElement__xml_attributes", curie=FIX_ORCHESTRA.curie('xml_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraXmlElement__xml_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraXmlElement__xml_text = Slot(uri=FIX_ORCHESTRA.xml_text, name="orchestraXmlElement__xml_text", curie=FIX_ORCHESTRA.curie('xml_text'),
                   model_uri=FIX_ORCHESTRA.orchestraXmlElement__xml_text, domain=None, range=Optional[str])

slots.orchestraXmlElement__xml_children = Slot(uri=FIX_ORCHESTRA.xml_children, name="orchestraXmlElement__xml_children", curie=FIX_ORCHESTRA.curie('xml_children'),
                   model_uri=FIX_ORCHESTRA.orchestraXmlElement__xml_children, domain=None, range=Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]])

slots.orchestraXmlElement__xml_tail = Slot(uri=FIX_ORCHESTRA.xml_tail, name="orchestraXmlElement__xml_tail", curie=FIX_ORCHESTRA.curie('xml_tail'),
                   model_uri=FIX_ORCHESTRA.orchestraXmlElement__xml_tail, domain=None, range=Optional[str])

slots.orchestraXmlAttribute__xml_name = Slot(uri=FIX_ORCHESTRA.xml_name, name="orchestraXmlAttribute__xml_name", curie=FIX_ORCHESTRA.curie('xml_name'),
                   model_uri=FIX_ORCHESTRA.orchestraXmlAttribute__xml_name, domain=None, range=str,
                   pattern=re.compile(r'^(\{[^}]*\})?[^\s{}]+$'))

slots.orchestraXmlAttribute__xml_value = Slot(uri=FIX_ORCHESTRA.xml_value, name="orchestraXmlAttribute__xml_value", curie=FIX_ORCHESTRA.curie('xml_value'),
                   model_uri=FIX_ORCHESTRA.orchestraXmlAttribute__xml_value, domain=None, range=str)

slots.orchestraActionParameterV10__fixr_field = Slot(uri=FIX_ORCHESTRA.fixr_field, name="orchestraActionParameterV10__fixr_field", curie=FIX_ORCHESTRA.curie('fixr_field'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV10__fixr_field, domain=None, range=Optional[Union[dict, OrchestraFieldV10]])

slots.orchestraActionParameterV10__fixr_field_ref = Slot(uri=FIX_ORCHESTRA.fixr_field_ref, name="orchestraActionParameterV10__fixr_field_ref", curie=FIX_ORCHESTRA.curie('fixr_field_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV10__fixr_field_ref, domain=None, range=Optional[Union[dict, OrchestraFieldRefV10]])

slots.orchestraActionParameterV10__fixr_component = Slot(uri=FIX_ORCHESTRA.fixr_component, name="orchestraActionParameterV10__fixr_component", curie=FIX_ORCHESTRA.curie('fixr_component'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV10__fixr_component, domain=None, range=Optional[Union[dict, OrchestraComponentV10]])

slots.orchestraActionParameterV10__fixr_component_ref = Slot(uri=FIX_ORCHESTRA.fixr_component_ref, name="orchestraActionParameterV10__fixr_component_ref", curie=FIX_ORCHESTRA.curie('fixr_component_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV10__fixr_component_ref, domain=None, range=Optional[Union[dict, OrchestraComponentRefV10]])

slots.orchestraActionParameterV10__fixr_group = Slot(uri=FIX_ORCHESTRA.fixr_group, name="orchestraActionParameterV10__fixr_group", curie=FIX_ORCHESTRA.curie('fixr_group'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV10__fixr_group, domain=None, range=Optional[Union[dict, OrchestraGroupV10]])

slots.orchestraActionParameterV10__fixr_group_ref = Slot(uri=FIX_ORCHESTRA.fixr_group_ref, name="orchestraActionParameterV10__fixr_group_ref", curie=FIX_ORCHESTRA.curie('fixr_group_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV10__fixr_group_ref, domain=None, range=Optional[Union[dict, OrchestraGroupRefV10]])

slots.orchestraActionStepV10__fixr_message_ref = Slot(uri=FIX_ORCHESTRA.fixr_message_ref, name="orchestraActionStepV10__fixr_message_ref", curie=FIX_ORCHESTRA.curie('fixr_message_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActionStepV10__fixr_message_ref, domain=None, range=Optional[Union[dict, OrchestraMessageRefV10]])

slots.orchestraActionStepV10__fixr_assign = Slot(uri=FIX_ORCHESTRA.fixr_assign, name="orchestraActionStepV10__fixr_assign", curie=FIX_ORCHESTRA.curie('fixr_assign'),
                   model_uri=FIX_ORCHESTRA.orchestraActionStepV10__fixr_assign, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraActionStepV10__fixr_trigger = Slot(uri=FIX_ORCHESTRA.fixr_trigger, name="orchestraActionStepV10__fixr_trigger", curie=FIX_ORCHESTRA.curie('fixr_trigger'),
                   model_uri=FIX_ORCHESTRA.orchestraActionStepV10__fixr_trigger, domain=None, range=Optional[Union[dict, OrchestraTriggerV10]])

slots.orchestraActionStepV10__fixr_timer_schedule = Slot(uri=FIX_ORCHESTRA.fixr_timer_schedule, name="orchestraActionStepV10__fixr_timer_schedule", curie=FIX_ORCHESTRA.curie('fixr_timer_schedule'),
                   model_uri=FIX_ORCHESTRA.orchestraActionStepV10__fixr_timer_schedule, domain=None, range=Optional[Union[dict, OrchestraTimerScheduleV10]])

slots.orchestraActionV10__fixr_parameters = Slot(uri=FIX_ORCHESTRA.fixr_parameters, name="orchestraActionV10__fixr_parameters", curie=FIX_ORCHESTRA.curie('fixr_parameters'),
                   model_uri=FIX_ORCHESTRA.orchestraActionV10__fixr_parameters, domain=None, range=Optional[Union[Union[dict, OrchestraActionParameterV10], list[Union[dict, OrchestraActionParameterV10]]]])

slots.orchestraActionV10__fixr_actions = Slot(uri=FIX_ORCHESTRA.fixr_actions, name="orchestraActionV10__fixr_actions", curie=FIX_ORCHESTRA.curie('fixr_actions'),
                   model_uri=FIX_ORCHESTRA.orchestraActionV10__fixr_actions, domain=None, range=Union[Union[dict, OrchestraActionStepV10], list[Union[dict, OrchestraActionStepV10]]])

slots.orchestraActorMemberV10__fixr_field = Slot(uri=FIX_ORCHESTRA.fixr_field, name="orchestraActorMemberV10__fixr_field", curie=FIX_ORCHESTRA.curie('fixr_field'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV10__fixr_field, domain=None, range=Optional[Union[dict, OrchestraFieldV10]])

slots.orchestraActorMemberV10__fixr_field_ref = Slot(uri=FIX_ORCHESTRA.fixr_field_ref, name="orchestraActorMemberV10__fixr_field_ref", curie=FIX_ORCHESTRA.curie('fixr_field_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV10__fixr_field_ref, domain=None, range=Optional[Union[dict, OrchestraFieldRefV10]])

slots.orchestraActorMemberV10__fixr_component = Slot(uri=FIX_ORCHESTRA.fixr_component, name="orchestraActorMemberV10__fixr_component", curie=FIX_ORCHESTRA.curie('fixr_component'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV10__fixr_component, domain=None, range=Optional[Union[dict, OrchestraComponentV10]])

slots.orchestraActorMemberV10__fixr_component_ref = Slot(uri=FIX_ORCHESTRA.fixr_component_ref, name="orchestraActorMemberV10__fixr_component_ref", curie=FIX_ORCHESTRA.curie('fixr_component_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV10__fixr_component_ref, domain=None, range=Optional[Union[dict, OrchestraComponentRefV10]])

slots.orchestraActorMemberV10__fixr_group = Slot(uri=FIX_ORCHESTRA.fixr_group, name="orchestraActorMemberV10__fixr_group", curie=FIX_ORCHESTRA.curie('fixr_group'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV10__fixr_group, domain=None, range=Optional[Union[dict, OrchestraGroupV10]])

slots.orchestraActorMemberV10__fixr_group_ref = Slot(uri=FIX_ORCHESTRA.fixr_group_ref, name="orchestraActorMemberV10__fixr_group_ref", curie=FIX_ORCHESTRA.curie('fixr_group_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV10__fixr_group_ref, domain=None, range=Optional[Union[dict, OrchestraGroupRefV10]])

slots.orchestraActorMemberV10__fixr_states = Slot(uri=FIX_ORCHESTRA.fixr_states, name="orchestraActorMemberV10__fixr_states", curie=FIX_ORCHESTRA.curie('fixr_states'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV10__fixr_states, domain=None, range=Optional[Union[dict, OrchestraStateMachineV10]])

slots.orchestraActorMemberV10__fixr_timer = Slot(uri=FIX_ORCHESTRA.fixr_timer, name="orchestraActorMemberV10__fixr_timer", curie=FIX_ORCHESTRA.curie('fixr_timer'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV10__fixr_timer, domain=None, range=Optional[Union[dict, OrchestraTimerV10]])

slots.orchestraActorV10__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraActorV10__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraActorV10__fixr_members, domain=None, range=Optional[Union[Union[dict, OrchestraActorMemberV10], list[Union[dict, OrchestraActorMemberV10]]]])

slots.orchestraActorV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraActorV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraActorV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraActorV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraActorV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraActorV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraActorsMemberV10__fixr_actor = Slot(uri=FIX_ORCHESTRA.fixr_actor, name="orchestraActorsMemberV10__fixr_actor", curie=FIX_ORCHESTRA.curie('fixr_actor'),
                   model_uri=FIX_ORCHESTRA.orchestraActorsMemberV10__fixr_actor, domain=None, range=Optional[Union[dict, OrchestraActorV10]])

slots.orchestraActorsMemberV10__fixr_flow = Slot(uri=FIX_ORCHESTRA.fixr_flow, name="orchestraActorsMemberV10__fixr_flow", curie=FIX_ORCHESTRA.curie('fixr_flow'),
                   model_uri=FIX_ORCHESTRA.orchestraActorsMemberV10__fixr_flow, domain=None, range=Optional[Union[dict, OrchestraFlowV10]])

slots.orchestraActorsV10__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraActorsV10__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraActorsV10__fixr_members, domain=None, range=Union[Union[dict, OrchestraActorsMemberV10], list[Union[dict, OrchestraActorsMemberV10]]])

slots.orchestraActorsV10__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraActorsV10__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraActorsV10__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraAnnotationMemberV10__fixr_documentation = Slot(uri=FIX_ORCHESTRA.fixr_documentation, name="orchestraAnnotationMemberV10__fixr_documentation", curie=FIX_ORCHESTRA.curie('fixr_documentation'),
                   model_uri=FIX_ORCHESTRA.orchestraAnnotationMemberV10__fixr_documentation, domain=None, range=Optional[Union[dict, OrchestraDocumentationV10]])

slots.orchestraAnnotationMemberV10__fixr_appinfo = Slot(uri=FIX_ORCHESTRA.fixr_appinfo, name="orchestraAnnotationMemberV10__fixr_appinfo", curie=FIX_ORCHESTRA.curie('fixr_appinfo'),
                   model_uri=FIX_ORCHESTRA.orchestraAnnotationMemberV10__fixr_appinfo, domain=None, range=Optional[Union[dict, OrchestraAppinfoV10]])

slots.orchestraAnnotationV10__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraAnnotationV10__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraAnnotationV10__fixr_members, domain=None, range=Union[Union[dict, OrchestraAnnotationMemberV10], list[Union[dict, OrchestraAnnotationMemberV10]]])

slots.orchestraAppinfoV10__fixr_text = Slot(uri=FIX_ORCHESTRA.fixr_text, name="orchestraAppinfoV10__fixr_text", curie=FIX_ORCHESTRA.curie('fixr_text'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV10__fixr_text, domain=None, range=Optional[str])

slots.orchestraAppinfoV10__fixr_any = Slot(uri=FIX_ORCHESTRA.fixr_any, name="orchestraAppinfoV10__fixr_any", curie=FIX_ORCHESTRA.curie('fixr_any'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV10__fixr_any, domain=None, range=Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]])

slots.orchestraAppinfoV10__fixr_spec_url = Slot(uri=FIX_ORCHESTRA.fixr_spec_url, name="orchestraAppinfoV10__fixr_spec_url", curie=FIX_ORCHESTRA.curie('fixr_spec_url'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV10__fixr_spec_url, domain=None, range=Optional[Union[str, URI]])

slots.orchestraAppinfoV10__fixr_lang_id = Slot(uri=FIX_ORCHESTRA.fixr_lang_id, name="orchestraAppinfoV10__fixr_lang_id", curie=FIX_ORCHESTRA.curie('fixr_lang_id'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV10__fixr_lang_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*$'))

slots.orchestraAppinfoV10__fixr_purpose = Slot(uri=FIX_ORCHESTRA.fixr_purpose, name="orchestraAppinfoV10__fixr_purpose", curie=FIX_ORCHESTRA.curie('fixr_purpose'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV10__fixr_purpose, domain=None, range=Optional[Union[str, "OrchestraPurpose"]])

slots.orchestraAppinfoV10__fixr_other_attributes = Slot(uri=FIX_ORCHESTRA.fixr_other_attributes, name="orchestraAppinfoV10__fixr_other_attributes", curie=FIX_ORCHESTRA.curie('fixr_other_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV10__fixr_other_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraBaseInterfaceV10__fixi_service = Slot(uri=FIX_ORCHESTRA.fixi_service, name="orchestraBaseInterfaceV10__fixi_service", curie=FIX_ORCHESTRA.curie('fixi_service'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV10__fixi_service, domain=None, range=Optional[Union[Union[dict, OrchestraServiceV10], list[Union[dict, OrchestraServiceV10]]]])

slots.orchestraBaseInterfaceV10__fixi_user_interface = Slot(uri=FIX_ORCHESTRA.fixi_user_interface, name="orchestraBaseInterfaceV10__fixi_user_interface", curie=FIX_ORCHESTRA.curie('fixi_user_interface'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV10__fixi_user_interface, domain=None, range=Optional[Union[Union[dict, OrchestraUserInterfaceV10], list[Union[dict, OrchestraUserInterfaceV10]]]])

slots.orchestraBaseInterfaceV10__fixi_encoding = Slot(uri=FIX_ORCHESTRA.fixi_encoding, name="orchestraBaseInterfaceV10__fixi_encoding", curie=FIX_ORCHESTRA.curie('fixi_encoding'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV10__fixi_encoding, domain=None, range=Optional[Union[Union[dict, OrchestraEncodingV10], list[Union[dict, OrchestraEncodingV10]]]])

slots.orchestraBaseInterfaceV10__fixi_session_protocol = Slot(uri=FIX_ORCHESTRA.fixi_session_protocol, name="orchestraBaseInterfaceV10__fixi_session_protocol", curie=FIX_ORCHESTRA.curie('fixi_session_protocol'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV10__fixi_session_protocol, domain=None, range=Optional[Union[Union[dict, OrchestraSessionProtocolV10], list[Union[dict, OrchestraSessionProtocolV10]]]])

slots.orchestraBaseInterfaceV10__fixi_protocol = Slot(uri=FIX_ORCHESTRA.fixi_protocol, name="orchestraBaseInterfaceV10__fixi_protocol", curie=FIX_ORCHESTRA.curie('fixi_protocol'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV10__fixi_protocol, domain=None, range=Optional[Union[Union[dict, OrchestraProtocolV10], list[Union[dict, OrchestraProtocolV10]]]])

slots.orchestraBaseInterfaceV10__fixi_transport = Slot(uri=FIX_ORCHESTRA.fixi_transport, name="orchestraBaseInterfaceV10__fixi_transport", curie=FIX_ORCHESTRA.curie('fixi_transport'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV10__fixi_transport, domain=None, range=Optional[Union[Union[dict, OrchestraTransportV10], list[Union[dict, OrchestraTransportV10]]]])

slots.orchestraBaseInterfaceV10__fixi_annotation = Slot(uri=FIX_ORCHESTRA.fixi_annotation, name="orchestraBaseInterfaceV10__fixi_annotation", curie=FIX_ORCHESTRA.curie('fixi_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV10__fixi_annotation, domain=None, range=Optional[Union[dict, OrchestraInterfaceAnnotationV10]])

slots.orchestraBaseInterfaceV10__fixi_name = Slot(uri=FIX_ORCHESTRA.fixi_name, name="orchestraBaseInterfaceV10__fixi_name", curie=FIX_ORCHESTRA.curie('fixi_name'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV10__fixi_name, domain=None, range=str)

slots.orchestraBaseInterfaceV10__fixi_other_attributes = Slot(uri=FIX_ORCHESTRA.fixi_other_attributes, name="orchestraBaseInterfaceV10__fixi_other_attributes", curie=FIX_ORCHESTRA.curie('fixi_other_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV10__fixi_other_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraBlockAssignmentV10__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraBlockAssignmentV10__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraBlockAssignmentV10__fixr_members, domain=None, range=Union[Union[dict, OrchestraStructureMemberV10], list[Union[dict, OrchestraStructureMemberV10]]])

slots.orchestraCategoriesV10__fixr_category = Slot(uri=FIX_ORCHESTRA.fixr_category, name="orchestraCategoriesV10__fixr_category", curie=FIX_ORCHESTRA.curie('fixr_category'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoriesV10__fixr_category, domain=None, range=Union[Union[dict, OrchestraCategoryV10], list[Union[dict, OrchestraCategoryV10]]])

slots.orchestraCategoriesV10__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraCategoriesV10__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoriesV10__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraCategoryV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraCategoryV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoryV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraCategoryV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraCategoryV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoryV10__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraCategoryV10__fixr_fixml_file_name = Slot(uri=FIX_ORCHESTRA.fixr_fixml_file_name, name="orchestraCategoryV10__fixr_fixml_file_name", curie=FIX_ORCHESTRA.curie('fixr_fixml_file_name'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoryV10__fixr_fixml_file_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraCategoryV10__fixr_component_type = Slot(uri=FIX_ORCHESTRA.fixr_component_type, name="orchestraCategoryV10__fixr_component_type", curie=FIX_ORCHESTRA.curie('fixr_component_type'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoryV10__fixr_component_type, domain=None, range=Optional[Union[str, "OrchestraCategoryContentV10"]])

slots.orchestraCategoryV10__fixr_section = Slot(uri=FIX_ORCHESTRA.fixr_section, name="orchestraCategoryV10__fixr_section", curie=FIX_ORCHESTRA.curie('fixr_section'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoryV10__fixr_section, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraCategoryV10__fixr_include_file = Slot(uri=FIX_ORCHESTRA.fixr_include_file, name="orchestraCategoryV10__fixr_include_file", curie=FIX_ORCHESTRA.curie('fixr_include_file'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoryV10__fixr_include_file, domain=None, range=Optional[Union[str, "OrchestraCategoryIncludeFileV10"]])

slots.orchestraCodeSetV10__fixr_code = Slot(uri=FIX_ORCHESTRA.fixr_code, name="orchestraCodeSetV10__fixr_code", curie=FIX_ORCHESTRA.curie('fixr_code'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV10__fixr_code, domain=None, range=Optional[Union[Union[dict, OrchestraCodeV10], list[Union[dict, OrchestraCodeV10]]]])

slots.orchestraCodeSetV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraCodeSetV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraCodeSetV10__fixr_type = Slot(uri=FIX_ORCHESTRA.fixr_type, name="orchestraCodeSetV10__fixr_type", curie=FIX_ORCHESTRA.curie('fixr_type'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV10__fixr_type, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraCodeSetV10__fixr_default = Slot(uri=FIX_ORCHESTRA.fixr_default, name="orchestraCodeSetV10__fixr_default", curie=FIX_ORCHESTRA.curie('fixr_default'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV10__fixr_default, domain=None, range=Optional[str])

slots.orchestraCodeSetV10__fixr_spec_url = Slot(uri=FIX_ORCHESTRA.fixr_spec_url, name="orchestraCodeSetV10__fixr_spec_url", curie=FIX_ORCHESTRA.curie('fixr_spec_url'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV10__fixr_spec_url, domain=None, range=Optional[Union[str, URI]])

slots.orchestraCodeSetsV10__fixr_code_set = Slot(uri=FIX_ORCHESTRA.fixr_code_set, name="orchestraCodeSetsV10__fixr_code_set", curie=FIX_ORCHESTRA.curie('fixr_code_set'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetsV10__fixr_code_set, domain=None, range=Union[Union[dict, OrchestraCodeSetV10], list[Union[dict, OrchestraCodeSetV10]]])

slots.orchestraCodeSetsV10__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraCodeSetsV10__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetsV10__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraCodeV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraCodeV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraCodeV10__fixr_value = Slot(uri=FIX_ORCHESTRA.fixr_value, name="orchestraCodeV10__fixr_value", curie=FIX_ORCHESTRA.curie('fixr_value'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeV10__fixr_value, domain=None, range=str)

slots.orchestraCodeV10__fixr_sort = Slot(uri=FIX_ORCHESTRA.fixr_sort, name="orchestraCodeV10__fixr_sort", curie=FIX_ORCHESTRA.curie('fixr_sort'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeV10__fixr_sort, domain=None, range=Optional[str])

slots.orchestraCodeV10__fixr_group = Slot(uri=FIX_ORCHESTRA.fixr_group, name="orchestraCodeV10__fixr_group", curie=FIX_ORCHESTRA.curie('fixr_group'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeV10__fixr_group, domain=None, range=Optional[str])

slots.orchestraComponentRefV10__fixr_block_assignment = Slot(uri=FIX_ORCHESTRA.fixr_block_assignment, name="orchestraComponentRefV10__fixr_block_assignment", curie=FIX_ORCHESTRA.curie('fixr_block_assignment'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV10__fixr_block_assignment, domain=None, range=Optional[Union[Union[dict, OrchestraBlockAssignmentV10], list[Union[dict, OrchestraBlockAssignmentV10]]]])

slots.orchestraComponentRefV10__fixr_rule = Slot(uri=FIX_ORCHESTRA.fixr_rule, name="orchestraComponentRefV10__fixr_rule", curie=FIX_ORCHESTRA.curie('fixr_rule'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV10__fixr_rule, domain=None, range=Optional[Union[Union[dict, OrchestraComponentRuleV10], list[Union[dict, OrchestraComponentRuleV10]]]])

slots.orchestraComponentRefV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraComponentRefV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraComponentRefV10__fixr_presence = Slot(uri=FIX_ORCHESTRA.fixr_presence, name="orchestraComponentRefV10__fixr_presence", curie=FIX_ORCHESTRA.curie('fixr_presence'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV10__fixr_presence, domain=None, range=Optional[Union[str, "OrchestraPresence"]])

slots.orchestraComponentRefV10__fixr_instance_name = Slot(uri=FIX_ORCHESTRA.fixr_instance_name, name="orchestraComponentRefV10__fixr_instance_name", curie=FIX_ORCHESTRA.curie('fixr_instance_name'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV10__fixr_instance_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraComponentRuleV10__fixr_when = Slot(uri=FIX_ORCHESTRA.fixr_when, name="orchestraComponentRuleV10__fixr_when", curie=FIX_ORCHESTRA.curie('fixr_when'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRuleV10__fixr_when, domain=None, range=str,
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraComponentRuleV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraComponentRuleV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRuleV10__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraComponentRuleV10__fixr_presence = Slot(uri=FIX_ORCHESTRA.fixr_presence, name="orchestraComponentRuleV10__fixr_presence", curie=FIX_ORCHESTRA.curie('fixr_presence'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRuleV10__fixr_presence, domain=None, range=Optional[Union[str, "OrchestraPresence"]])

slots.orchestraComponentV10__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraComponentV10__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV10__fixr_members, domain=None, range=Union[Union[dict, OrchestraStructureMemberV10], list[Union[dict, OrchestraStructureMemberV10]]])

slots.orchestraComponentV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraComponentV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraComponentV10__fixr_category = Slot(uri=FIX_ORCHESTRA.fixr_category, name="orchestraComponentV10__fixr_category", curie=FIX_ORCHESTRA.curie('fixr_category'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV10__fixr_category, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraComponentV10__fixr_rendering = Slot(uri=FIX_ORCHESTRA.fixr_rendering, name="orchestraComponentV10__fixr_rendering", curie=FIX_ORCHESTRA.curie('fixr_rendering'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV10__fixr_rendering, domain=None, range=Optional[str])

slots.orchestraComponentV10__fixr_which = Slot(uri=FIX_ORCHESTRA.fixr_which, name="orchestraComponentV10__fixr_which", curie=FIX_ORCHESTRA.curie('fixr_which'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV10__fixr_which, domain=None, range=Optional[Union[str, "OrchestraMemberSelection"]])

slots.orchestraComponentsV10__fixr_component = Slot(uri=FIX_ORCHESTRA.fixr_component, name="orchestraComponentsV10__fixr_component", curie=FIX_ORCHESTRA.curie('fixr_component'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentsV10__fixr_component, domain=None, range=Union[Union[dict, OrchestraComponentV10], list[Union[dict, OrchestraComponentV10]]])

slots.orchestraComponentsV10__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraComponentsV10__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentsV10__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraConceptMemberV10__fixr_component_ref = Slot(uri=FIX_ORCHESTRA.fixr_component_ref, name="orchestraConceptMemberV10__fixr_component_ref", curie=FIX_ORCHESTRA.curie('fixr_component_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptMemberV10__fixr_component_ref, domain=None, range=Optional[Union[dict, OrchestraComponentRefV10]])

slots.orchestraConceptMemberV10__fixr_group_ref = Slot(uri=FIX_ORCHESTRA.fixr_group_ref, name="orchestraConceptMemberV10__fixr_group_ref", curie=FIX_ORCHESTRA.curie('fixr_group_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptMemberV10__fixr_group_ref, domain=None, range=Optional[Union[dict, OrchestraGroupRefV10]])

slots.orchestraConceptMemberV10__fixr_field_ref = Slot(uri=FIX_ORCHESTRA.fixr_field_ref, name="orchestraConceptMemberV10__fixr_field_ref", curie=FIX_ORCHESTRA.curie('fixr_field_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptMemberV10__fixr_field_ref, domain=None, range=Optional[Union[dict, OrchestraFieldRefV10]])

slots.orchestraConceptMemberV10__fixr_message_ref = Slot(uri=FIX_ORCHESTRA.fixr_message_ref, name="orchestraConceptMemberV10__fixr_message_ref", curie=FIX_ORCHESTRA.curie('fixr_message_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptMemberV10__fixr_message_ref, domain=None, range=Optional[Union[dict, OrchestraMessageRefV10]])

slots.orchestraConceptV10__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraConceptV10__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptV10__fixr_members, domain=None, range=Union[Union[dict, OrchestraConceptMemberV10], list[Union[dict, OrchestraConceptMemberV10]]])

slots.orchestraConceptV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraConceptV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraConceptV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraConceptV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraConceptsV10__fixr_concept = Slot(uri=FIX_ORCHESTRA.fixr_concept, name="orchestraConceptsV10__fixr_concept", curie=FIX_ORCHESTRA.curie('fixr_concept'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptsV10__fixr_concept, domain=None, range=Union[Union[dict, OrchestraConceptV10], list[Union[dict, OrchestraConceptV10]]])

slots.orchestraConceptsV10__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraConceptsV10__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptsV10__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraContainerV10Mixin__fixr_latest_ep = Slot(uri=FIX_ORCHESTRA.fixr_latest_ep, name="orchestraContainerV10Mixin__fixr_latest_ep", curie=FIX_ORCHESTRA.curie('fixr_latest_ep'),
                   model_uri=FIX_ORCHESTRA.orchestraContainerV10Mixin__fixr_latest_ep, domain=None, range=Optional[int])

slots.orchestraDatatypeExtensionV10__fixr_any = Slot(uri=FIX_ORCHESTRA.fixr_any, name="orchestraDatatypeExtensionV10__fixr_any", curie=FIX_ORCHESTRA.curie('fixr_any'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypeExtensionV10__fixr_any, domain=None, range=Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]])

slots.orchestraDatatypeV10__fixr_mapped_datatype = Slot(uri=FIX_ORCHESTRA.fixr_mapped_datatype, name="orchestraDatatypeV10__fixr_mapped_datatype", curie=FIX_ORCHESTRA.curie('fixr_mapped_datatype'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypeV10__fixr_mapped_datatype, domain=None, range=Optional[Union[Union[dict, OrchestraMappedDatatypeV10], list[Union[dict, OrchestraMappedDatatypeV10]]]])

slots.orchestraDatatypeV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraDatatypeV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypeV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraDatatypeV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraDatatypeV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypeV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraDatatypeV10__fixr_base_type = Slot(uri=FIX_ORCHESTRA.fixr_base_type, name="orchestraDatatypeV10__fixr_base_type", curie=FIX_ORCHESTRA.curie('fixr_base_type'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypeV10__fixr_base_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraDatatypesV10__fixr_datatype = Slot(uri=FIX_ORCHESTRA.fixr_datatype, name="orchestraDatatypesV10__fixr_datatype", curie=FIX_ORCHESTRA.curie('fixr_datatype'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypesV10__fixr_datatype, domain=None, range=Union[Union[dict, OrchestraDatatypeV10], list[Union[dict, OrchestraDatatypeV10]]])

slots.orchestraDatatypesV10__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraDatatypesV10__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypesV10__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraDocumentationV10__fixr_text = Slot(uri=FIX_ORCHESTRA.fixr_text, name="orchestraDocumentationV10__fixr_text", curie=FIX_ORCHESTRA.curie('fixr_text'),
                   model_uri=FIX_ORCHESTRA.orchestraDocumentationV10__fixr_text, domain=None, range=Optional[str])

slots.orchestraDocumentationV10__fixr_any = Slot(uri=FIX_ORCHESTRA.fixr_any, name="orchestraDocumentationV10__fixr_any", curie=FIX_ORCHESTRA.curie('fixr_any'),
                   model_uri=FIX_ORCHESTRA.orchestraDocumentationV10__fixr_any, domain=None, range=Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]])

slots.orchestraDocumentationV10__fixr_lang_id = Slot(uri=FIX_ORCHESTRA.fixr_lang_id, name="orchestraDocumentationV10__fixr_lang_id", curie=FIX_ORCHESTRA.curie('fixr_lang_id'),
                   model_uri=FIX_ORCHESTRA.orchestraDocumentationV10__fixr_lang_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*$'))

slots.orchestraDocumentationV10__fixr_purpose = Slot(uri=FIX_ORCHESTRA.fixr_purpose, name="orchestraDocumentationV10__fixr_purpose", curie=FIX_ORCHESTRA.curie('fixr_purpose'),
                   model_uri=FIX_ORCHESTRA.orchestraDocumentationV10__fixr_purpose, domain=None, range=Optional[Union[str, "OrchestraPurpose"]])

slots.orchestraDocumentationV10__fixr_content_type = Slot(uri=FIX_ORCHESTRA.fixr_content_type, name="orchestraDocumentationV10__fixr_content_type", curie=FIX_ORCHESTRA.curie('fixr_content_type'),
                   model_uri=FIX_ORCHESTRA.orchestraDocumentationV10__fixr_content_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{3,}$'))

slots.orchestraFieldConstraintsV10Mixin__fixr_min_inclusive = Slot(uri=FIX_ORCHESTRA.fixr_min_inclusive, name="orchestraFieldConstraintsV10Mixin__fixr_min_inclusive", curie=FIX_ORCHESTRA.curie('fixr_min_inclusive'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV10Mixin__fixr_min_inclusive, domain=None, range=Optional[str])

slots.orchestraFieldConstraintsV10Mixin__fixr_max_inclusive = Slot(uri=FIX_ORCHESTRA.fixr_max_inclusive, name="orchestraFieldConstraintsV10Mixin__fixr_max_inclusive", curie=FIX_ORCHESTRA.curie('fixr_max_inclusive'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV10Mixin__fixr_max_inclusive, domain=None, range=Optional[str])

slots.orchestraFieldConstraintsV10Mixin__fixr_impl_length = Slot(uri=FIX_ORCHESTRA.fixr_impl_length, name="orchestraFieldConstraintsV10Mixin__fixr_impl_length", curie=FIX_ORCHESTRA.curie('fixr_impl_length'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV10Mixin__fixr_impl_length, domain=None, range=Optional[int])

slots.orchestraFieldConstraintsV10Mixin__fixr_impl_min_length = Slot(uri=FIX_ORCHESTRA.fixr_impl_min_length, name="orchestraFieldConstraintsV10Mixin__fixr_impl_min_length", curie=FIX_ORCHESTRA.curie('fixr_impl_min_length'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV10Mixin__fixr_impl_min_length, domain=None, range=Optional[int])

slots.orchestraFieldConstraintsV10Mixin__fixr_impl_max_length = Slot(uri=FIX_ORCHESTRA.fixr_impl_max_length, name="orchestraFieldConstraintsV10Mixin__fixr_impl_max_length", curie=FIX_ORCHESTRA.curie('fixr_impl_max_length'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV10Mixin__fixr_impl_max_length, domain=None, range=Optional[int])

slots.orchestraFieldConstraintsV10Mixin__fixr_presence = Slot(uri=FIX_ORCHESTRA.fixr_presence, name="orchestraFieldConstraintsV10Mixin__fixr_presence", curie=FIX_ORCHESTRA.curie('fixr_presence'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV10Mixin__fixr_presence, domain=None, range=Optional[Union[str, "OrchestraPresence"]])

slots.orchestraFieldConstraintsV10Mixin__fixr_encoding = Slot(uri=FIX_ORCHESTRA.fixr_encoding, name="orchestraFieldConstraintsV10Mixin__fixr_encoding", curie=FIX_ORCHESTRA.curie('fixr_encoding'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV10Mixin__fixr_encoding, domain=None, range=Optional[str])

slots.orchestraFieldConstraintsV10Mixin__fixr_value = Slot(uri=FIX_ORCHESTRA.fixr_value, name="orchestraFieldConstraintsV10Mixin__fixr_value", curie=FIX_ORCHESTRA.curie('fixr_value'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV10Mixin__fixr_value, domain=None, range=Optional[str])

slots.orchestraFieldConstraintsV10Mixin__fixr_rendering = Slot(uri=FIX_ORCHESTRA.fixr_rendering, name="orchestraFieldConstraintsV10Mixin__fixr_rendering", curie=FIX_ORCHESTRA.curie('fixr_rendering'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV10Mixin__fixr_rendering, domain=None, range=Optional[str])

slots.orchestraFieldRefV10__fixr_rule = Slot(uri=FIX_ORCHESTRA.fixr_rule, name="orchestraFieldRefV10__fixr_rule", curie=FIX_ORCHESTRA.curie('fixr_rule'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV10__fixr_rule, domain=None, range=Optional[Union[Union[dict, OrchestraFieldRuleV10], list[Union[dict, OrchestraFieldRuleV10]]]])

slots.orchestraFieldRefV10__fixr_assign = Slot(uri=FIX_ORCHESTRA.fixr_assign, name="orchestraFieldRefV10__fixr_assign", curie=FIX_ORCHESTRA.curie('fixr_assign'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV10__fixr_assign, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraFieldRefV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraFieldRefV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraFieldRefV10__fixr_length_id = Slot(uri=FIX_ORCHESTRA.fixr_length_id, name="orchestraFieldRefV10__fixr_length_id", curie=FIX_ORCHESTRA.curie('fixr_length_id'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV10__fixr_length_id, domain=None, range=Optional[int])

slots.orchestraFieldRefV10__fixr_instance_name = Slot(uri=FIX_ORCHESTRA.fixr_instance_name, name="orchestraFieldRefV10__fixr_instance_name", curie=FIX_ORCHESTRA.curie('fixr_instance_name'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV10__fixr_instance_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraFieldRuleV10__fixr_unique = Slot(uri=FIX_ORCHESTRA.fixr_unique, name="orchestraFieldRuleV10__fixr_unique", curie=FIX_ORCHESTRA.curie('fixr_unique'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRuleV10__fixr_unique, domain=None, range=Optional[Union[dict, OrchestraUniqueV10]])

slots.orchestraFieldRuleV10__fixr_assign = Slot(uri=FIX_ORCHESTRA.fixr_assign, name="orchestraFieldRuleV10__fixr_assign", curie=FIX_ORCHESTRA.curie('fixr_assign'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRuleV10__fixr_assign, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraFieldRuleV10__fixr_when = Slot(uri=FIX_ORCHESTRA.fixr_when, name="orchestraFieldRuleV10__fixr_when", curie=FIX_ORCHESTRA.curie('fixr_when'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRuleV10__fixr_when, domain=None, range=str,
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraFieldRuleV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraFieldRuleV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRuleV10__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraFieldRuleV10__fixr_type = Slot(uri=FIX_ORCHESTRA.fixr_type, name="orchestraFieldRuleV10__fixr_type", curie=FIX_ORCHESTRA.curie('fixr_type'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRuleV10__fixr_type, domain=None, range=Optional[str])

slots.orchestraFieldV10__fixr_rule = Slot(uri=FIX_ORCHESTRA.fixr_rule, name="orchestraFieldV10__fixr_rule", curie=FIX_ORCHESTRA.curie('fixr_rule'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV10__fixr_rule, domain=None, range=Optional[Union[Union[dict, OrchestraFieldRuleV10], list[Union[dict, OrchestraFieldRuleV10]]]])

slots.orchestraFieldV10__fixr_assign = Slot(uri=FIX_ORCHESTRA.fixr_assign, name="orchestraFieldV10__fixr_assign", curie=FIX_ORCHESTRA.curie('fixr_assign'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV10__fixr_assign, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraFieldV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraFieldV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraFieldV10__fixr_type = Slot(uri=FIX_ORCHESTRA.fixr_type, name="orchestraFieldV10__fixr_type", curie=FIX_ORCHESTRA.curie('fixr_type'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV10__fixr_type, domain=None, range=str)

slots.orchestraFieldV10__fixr_length_id = Slot(uri=FIX_ORCHESTRA.fixr_length_id, name="orchestraFieldV10__fixr_length_id", curie=FIX_ORCHESTRA.curie('fixr_length_id'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV10__fixr_length_id, domain=None, range=Optional[int])

slots.orchestraFieldV10__fixr_discriminator_id = Slot(uri=FIX_ORCHESTRA.fixr_discriminator_id, name="orchestraFieldV10__fixr_discriminator_id", curie=FIX_ORCHESTRA.curie('fixr_discriminator_id'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV10__fixr_discriminator_id, domain=None, range=Optional[int])

slots.orchestraFieldV10__fixr_base_category = Slot(uri=FIX_ORCHESTRA.fixr_base_category, name="orchestraFieldV10__fixr_base_category", curie=FIX_ORCHESTRA.curie('fixr_base_category'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV10__fixr_base_category, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraFieldV10__fixr_base_category_abbr_name = Slot(uri=FIX_ORCHESTRA.fixr_base_category_abbr_name, name="orchestraFieldV10__fixr_base_category_abbr_name", curie=FIX_ORCHESTRA.curie('fixr_base_category_abbr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV10__fixr_base_category_abbr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraFieldV10__fixr_union_data_type = Slot(uri=FIX_ORCHESTRA.fixr_union_data_type, name="orchestraFieldV10__fixr_union_data_type", curie=FIX_ORCHESTRA.curie('fixr_union_data_type'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV10__fixr_union_data_type, domain=None, range=Optional[Union[str, "OrchestraUnionDatatypeV10"]])

slots.orchestraFieldsV10__fixr_field = Slot(uri=FIX_ORCHESTRA.fixr_field, name="orchestraFieldsV10__fixr_field", curie=FIX_ORCHESTRA.curie('fixr_field'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldsV10__fixr_field, domain=None, range=Union[Union[dict, OrchestraFieldV10], list[Union[dict, OrchestraFieldV10]]])

slots.orchestraFieldsV10__fixr_latest_ep = Slot(uri=FIX_ORCHESTRA.fixr_latest_ep, name="orchestraFieldsV10__fixr_latest_ep", curie=FIX_ORCHESTRA.curie('fixr_latest_ep'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldsV10__fixr_latest_ep, domain=None, range=Optional[int])

slots.orchestraFieldsV10__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraFieldsV10__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldsV10__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraFlowV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraFlowV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraFlowV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraFlowV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraFlowV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraFlowV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraFlowV10__fixr_source = Slot(uri=FIX_ORCHESTRA.fixr_source, name="orchestraFlowV10__fixr_source", curie=FIX_ORCHESTRA.curie('fixr_source'),
                   model_uri=FIX_ORCHESTRA.orchestraFlowV10__fixr_source, domain=None, range=str)

slots.orchestraFlowV10__fixr_destination = Slot(uri=FIX_ORCHESTRA.fixr_destination, name="orchestraFlowV10__fixr_destination", curie=FIX_ORCHESTRA.curie('fixr_destination'),
                   model_uri=FIX_ORCHESTRA.orchestraFlowV10__fixr_destination, domain=None, range=str)

slots.orchestraFlowV10__fixr_reliability = Slot(uri=FIX_ORCHESTRA.fixr_reliability, name="orchestraFlowV10__fixr_reliability", curie=FIX_ORCHESTRA.curie('fixr_reliability'),
                   model_uri=FIX_ORCHESTRA.orchestraFlowV10__fixr_reliability, domain=None, range=Optional[Union[str, "OrchestraReliability"]])

slots.orchestraGroupRefV10__fixr_impl_min_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_min_occurs, name="orchestraGroupRefV10__fixr_impl_min_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_min_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupRefV10__fixr_impl_min_occurs, domain=None, range=Optional[int])

slots.orchestraGroupRefV10__fixr_impl_max_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_max_occurs, name="orchestraGroupRefV10__fixr_impl_max_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_max_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupRefV10__fixr_impl_max_occurs, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(\d+|unbounded)$'))

slots.orchestraGroupV10__fixr_num_in_group = Slot(uri=FIX_ORCHESTRA.fixr_num_in_group, name="orchestraGroupV10__fixr_num_in_group", curie=FIX_ORCHESTRA.curie('fixr_num_in_group'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV10__fixr_num_in_group, domain=None, range=Optional[Union[dict, OrchestraFieldRefV10]])

slots.orchestraGroupV10__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraGroupV10__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV10__fixr_members, domain=None, range=Union[Union[dict, OrchestraStructureMemberV10], list[Union[dict, OrchestraStructureMemberV10]]])

slots.orchestraGroupV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraGroupV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraGroupV10__fixr_category = Slot(uri=FIX_ORCHESTRA.fixr_category, name="orchestraGroupV10__fixr_category", curie=FIX_ORCHESTRA.curie('fixr_category'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV10__fixr_category, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraGroupV10__fixr_rendering = Slot(uri=FIX_ORCHESTRA.fixr_rendering, name="orchestraGroupV10__fixr_rendering", curie=FIX_ORCHESTRA.curie('fixr_rendering'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV10__fixr_rendering, domain=None, range=Optional[str])

slots.orchestraGroupV10__fixr_impl_min_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_min_occurs, name="orchestraGroupV10__fixr_impl_min_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_min_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV10__fixr_impl_min_occurs, domain=None, range=Optional[int])

slots.orchestraGroupV10__fixr_impl_max_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_max_occurs, name="orchestraGroupV10__fixr_impl_max_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_max_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV10__fixr_impl_max_occurs, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(\d+|unbounded)$'))

slots.orchestraGroupV10__fixr_which = Slot(uri=FIX_ORCHESTRA.fixr_which, name="orchestraGroupV10__fixr_which", curie=FIX_ORCHESTRA.curie('fixr_which'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV10__fixr_which, domain=None, range=Optional[Union[str, "OrchestraMemberSelection"]])

slots.orchestraGroupsV10__fixr_group = Slot(uri=FIX_ORCHESTRA.fixr_group, name="orchestraGroupsV10__fixr_group", curie=FIX_ORCHESTRA.curie('fixr_group'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupsV10__fixr_group, domain=None, range=Union[Union[dict, OrchestraGroupV10], list[Union[dict, OrchestraGroupV10]]])

slots.orchestraGroupsV10__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraGroupsV10__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupsV10__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraIdentifierV10__fixr_id = Slot(uri=FIX_ORCHESTRA.fixr_id, name="orchestraIdentifierV10__fixr_id", curie=FIX_ORCHESTRA.curie('fixr_id'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifierV10__fixr_id, domain=None, range=int)

slots.orchestraIdentifierV10__fixr_source_id = Slot(uri=FIX_ORCHESTRA.fixr_source_id, name="orchestraIdentifierV10__fixr_source_id", curie=FIX_ORCHESTRA.curie('fixr_source_id'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifierV10__fixr_source_id, domain=None, range=Optional[int])

slots.orchestraIdentifiersMemberV10__fixr_correlate = Slot(uri=FIX_ORCHESTRA.fixr_correlate, name="orchestraIdentifiersMemberV10__fixr_correlate", curie=FIX_ORCHESTRA.curie('fixr_correlate'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifiersMemberV10__fixr_correlate, domain=None, range=Optional[Union[dict, OrchestraIdentifierV10]])

slots.orchestraIdentifiersMemberV10__fixr_assign = Slot(uri=FIX_ORCHESTRA.fixr_assign, name="orchestraIdentifiersMemberV10__fixr_assign", curie=FIX_ORCHESTRA.curie('fixr_assign'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifiersMemberV10__fixr_assign, domain=None, range=Optional[Union[dict, OrchestraIdentifierV10]])

slots.orchestraIdentifiersV10__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraIdentifiersV10__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifiersV10__fixr_members, domain=None, range=Union[Union[dict, OrchestraIdentifiersMemberV10], list[Union[dict, OrchestraIdentifiersMemberV10]]])

slots.orchestraIdentifiersV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraIdentifiersV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifiersV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraIdentityV10Mixin__fixr_id = Slot(uri=FIX_ORCHESTRA.fixr_id, name="orchestraIdentityV10Mixin__fixr_id", curie=FIX_ORCHESTRA.curie('fixr_id'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentityV10Mixin__fixr_id, domain=None, range=int)

slots.orchestraIdentityV10Mixin__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraIdentityV10Mixin__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentityV10Mixin__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraIdentityV10Mixin__fixr_abbr_name = Slot(uri=FIX_ORCHESTRA.fixr_abbr_name, name="orchestraIdentityV10Mixin__fixr_abbr_name", curie=FIX_ORCHESTRA.curie('fixr_abbr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentityV10Mixin__fixr_abbr_name, domain=None, range=Optional[str])

slots.orchestraIdentityV10Mixin__fixr_scenario = Slot(uri=FIX_ORCHESTRA.fixr_scenario, name="orchestraIdentityV10Mixin__fixr_scenario", curie=FIX_ORCHESTRA.curie('fixr_scenario'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentityV10Mixin__fixr_scenario, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_|-)*)$'))

slots.orchestraInterfaceAnnotationMemberV10__fixi_documentation = Slot(uri=FIX_ORCHESTRA.fixi_documentation, name="orchestraInterfaceAnnotationMemberV10__fixi_documentation", curie=FIX_ORCHESTRA.curie('fixi_documentation'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAnnotationMemberV10__fixi_documentation, domain=None, range=Optional[Union[dict, OrchestraInterfaceDocumentationV10]])

slots.orchestraInterfaceAnnotationMemberV10__fixi_appinfo = Slot(uri=FIX_ORCHESTRA.fixi_appinfo, name="orchestraInterfaceAnnotationMemberV10__fixi_appinfo", curie=FIX_ORCHESTRA.curie('fixi_appinfo'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAnnotationMemberV10__fixi_appinfo, domain=None, range=Optional[Union[dict, OrchestraInterfaceAppinfoV10]])

slots.orchestraInterfaceAnnotationV10__fixi_members = Slot(uri=FIX_ORCHESTRA.fixi_members, name="orchestraInterfaceAnnotationV10__fixi_members", curie=FIX_ORCHESTRA.curie('fixi_members'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAnnotationV10__fixi_members, domain=None, range=Union[Union[dict, OrchestraInterfaceAnnotationMemberV10], list[Union[dict, OrchestraInterfaceAnnotationMemberV10]]])

slots.orchestraInterfaceAppinfoV10__fixi_text = Slot(uri=FIX_ORCHESTRA.fixi_text, name="orchestraInterfaceAppinfoV10__fixi_text", curie=FIX_ORCHESTRA.curie('fixi_text'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV10__fixi_text, domain=None, range=Optional[str])

slots.orchestraInterfaceAppinfoV10__fixi_any = Slot(uri=FIX_ORCHESTRA.fixi_any, name="orchestraInterfaceAppinfoV10__fixi_any", curie=FIX_ORCHESTRA.curie('fixi_any'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV10__fixi_any, domain=None, range=Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]])

slots.orchestraInterfaceAppinfoV10__fixi_spec_url = Slot(uri=FIX_ORCHESTRA.fixi_spec_url, name="orchestraInterfaceAppinfoV10__fixi_spec_url", curie=FIX_ORCHESTRA.curie('fixi_spec_url'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV10__fixi_spec_url, domain=None, range=Optional[Union[str, URI]])

slots.orchestraInterfaceAppinfoV10__fixi_lang_id = Slot(uri=FIX_ORCHESTRA.fixi_lang_id, name="orchestraInterfaceAppinfoV10__fixi_lang_id", curie=FIX_ORCHESTRA.curie('fixi_lang_id'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV10__fixi_lang_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*$'))

slots.orchestraInterfaceAppinfoV10__fixi_purpose = Slot(uri=FIX_ORCHESTRA.fixi_purpose, name="orchestraInterfaceAppinfoV10__fixi_purpose", curie=FIX_ORCHESTRA.curie('fixi_purpose'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV10__fixi_purpose, domain=None, range=Optional[Union[str, "OrchestraPurpose"]])

slots.orchestraInterfaceAppinfoV10__fixi_other_attributes = Slot(uri=FIX_ORCHESTRA.fixi_other_attributes, name="orchestraInterfaceAppinfoV10__fixi_other_attributes", curie=FIX_ORCHESTRA.curie('fixi_other_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV10__fixi_other_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraInterfaceDocumentationV10__fixi_text = Slot(uri=FIX_ORCHESTRA.fixi_text, name="orchestraInterfaceDocumentationV10__fixi_text", curie=FIX_ORCHESTRA.curie('fixi_text'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceDocumentationV10__fixi_text, domain=None, range=Optional[str])

slots.orchestraInterfaceDocumentationV10__fixi_any = Slot(uri=FIX_ORCHESTRA.fixi_any, name="orchestraInterfaceDocumentationV10__fixi_any", curie=FIX_ORCHESTRA.curie('fixi_any'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceDocumentationV10__fixi_any, domain=None, range=Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]])

slots.orchestraInterfaceDocumentationV10__fixi_lang_id = Slot(uri=FIX_ORCHESTRA.fixi_lang_id, name="orchestraInterfaceDocumentationV10__fixi_lang_id", curie=FIX_ORCHESTRA.curie('fixi_lang_id'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceDocumentationV10__fixi_lang_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*$'))

slots.orchestraInterfaceDocumentationV10__fixi_purpose = Slot(uri=FIX_ORCHESTRA.fixi_purpose, name="orchestraInterfaceDocumentationV10__fixi_purpose", curie=FIX_ORCHESTRA.curie('fixi_purpose'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceDocumentationV10__fixi_purpose, domain=None, range=Optional[Union[str, "OrchestraPurpose"]])

slots.orchestraInterfaceDocumentationV10__fixi_content_type = Slot(uri=FIX_ORCHESTRA.fixi_content_type, name="orchestraInterfaceDocumentationV10__fixi_content_type", curie=FIX_ORCHESTRA.curie('fixi_content_type'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceDocumentationV10__fixi_content_type, domain=None, range=Optional[str])

slots.orchestraInterfaceV10__fixi_sessions = Slot(uri=FIX_ORCHESTRA.fixi_sessions, name="orchestraInterfaceV10__fixi_sessions", curie=FIX_ORCHESTRA.curie('fixi_sessions'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceV10__fixi_sessions, domain=None, range=Optional[Union[dict, OrchestraSessionsV10]])

slots.orchestraInterfacesV10__fixi_metadata = Slot(uri=FIX_ORCHESTRA.fixi_metadata, name="orchestraInterfacesV10__fixi_metadata", curie=FIX_ORCHESTRA.curie('fixi_metadata'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfacesV10__fixi_metadata, domain=None, range=Union[dict, OrchestraMetadata])

slots.orchestraInterfacesV10__fixi_interface = Slot(uri=FIX_ORCHESTRA.fixi_interface, name="orchestraInterfacesV10__fixi_interface", curie=FIX_ORCHESTRA.curie('fixi_interface'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfacesV10__fixi_interface, domain=None, range=Optional[Union[Union[dict, OrchestraInterfaceV10], list[Union[dict, OrchestraInterfaceV10]]]])

slots.orchestraMappedDatatypeV10__fixr_extension = Slot(uri=FIX_ORCHESTRA.fixr_extension, name="orchestraMappedDatatypeV10__fixr_extension", curie=FIX_ORCHESTRA.curie('fixr_extension'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV10__fixr_extension, domain=None, range=Optional[Union[dict, OrchestraDatatypeExtensionV10]])

slots.orchestraMappedDatatypeV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraMappedDatatypeV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraMappedDatatypeV10__fixr_standard = Slot(uri=FIX_ORCHESTRA.fixr_standard, name="orchestraMappedDatatypeV10__fixr_standard", curie=FIX_ORCHESTRA.curie('fixr_standard'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV10__fixr_standard, domain=None, range=Union[str, "OrchestraDatatypeStandardV10"])

slots.orchestraMappedDatatypeV10__fixr_builtin = Slot(uri=FIX_ORCHESTRA.fixr_builtin, name="orchestraMappedDatatypeV10__fixr_builtin", curie=FIX_ORCHESTRA.curie('fixr_builtin'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV10__fixr_builtin, domain=None, range=Optional[Union[bool, Bool]])

slots.orchestraMappedDatatypeV10__fixr_base = Slot(uri=FIX_ORCHESTRA.fixr_base, name="orchestraMappedDatatypeV10__fixr_base", curie=FIX_ORCHESTRA.curie('fixr_base'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV10__fixr_base, domain=None, range=Optional[str])

slots.orchestraMappedDatatypeV10__fixr_pattern = Slot(uri=FIX_ORCHESTRA.fixr_pattern, name="orchestraMappedDatatypeV10__fixr_pattern", curie=FIX_ORCHESTRA.curie('fixr_pattern'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV10__fixr_pattern, domain=None, range=Optional[str])

slots.orchestraMappedDatatypeV10__fixr_element = Slot(uri=FIX_ORCHESTRA.fixr_element, name="orchestraMappedDatatypeV10__fixr_element", curie=FIX_ORCHESTRA.curie('fixr_element'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV10__fixr_element, domain=None, range=Optional[str])

slots.orchestraMappedDatatypeV10__fixr_parameter = Slot(uri=FIX_ORCHESTRA.fixr_parameter, name="orchestraMappedDatatypeV10__fixr_parameter", curie=FIX_ORCHESTRA.curie('fixr_parameter'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV10__fixr_parameter, domain=None, range=Optional[str])

slots.orchestraMappedDatatypeV10__fixr_min_inclusive = Slot(uri=FIX_ORCHESTRA.fixr_min_inclusive, name="orchestraMappedDatatypeV10__fixr_min_inclusive", curie=FIX_ORCHESTRA.curie('fixr_min_inclusive'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV10__fixr_min_inclusive, domain=None, range=Optional[str])

slots.orchestraMappedDatatypeV10__fixr_max_inclusive = Slot(uri=FIX_ORCHESTRA.fixr_max_inclusive, name="orchestraMappedDatatypeV10__fixr_max_inclusive", curie=FIX_ORCHESTRA.curie('fixr_max_inclusive'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV10__fixr_max_inclusive, domain=None, range=Optional[str])

slots.orchestraMessageRefV10__fixr_identifiers = Slot(uri=FIX_ORCHESTRA.fixr_identifiers, name="orchestraMessageRefV10__fixr_identifiers", curie=FIX_ORCHESTRA.curie('fixr_identifiers'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageRefV10__fixr_identifiers, domain=None, range=Optional[Union[dict, OrchestraIdentifiersV10]])

slots.orchestraMessageRefV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraMessageRefV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageRefV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraMessageRefV10__fixr_msg_type = Slot(uri=FIX_ORCHESTRA.fixr_msg_type, name="orchestraMessageRefV10__fixr_msg_type", curie=FIX_ORCHESTRA.curie('fixr_msg_type'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageRefV10__fixr_msg_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,2}$'))

slots.orchestraMessageRefV10__fixr_impl_min_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_min_occurs, name="orchestraMessageRefV10__fixr_impl_min_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_min_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageRefV10__fixr_impl_min_occurs, domain=None, range=Optional[int])

slots.orchestraMessageRefV10__fixr_impl_max_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_max_occurs, name="orchestraMessageRefV10__fixr_impl_max_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_max_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageRefV10__fixr_impl_max_occurs, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(\d+|unbounded)$'))

slots.orchestraMessageStructureV10__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraMessageStructureV10__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageStructureV10__fixr_members, domain=None, range=Union[Union[dict, OrchestraStructureMemberV10], list[Union[dict, OrchestraStructureMemberV10]]])

slots.orchestraMessageStructureV10__fixr_which = Slot(uri=FIX_ORCHESTRA.fixr_which, name="orchestraMessageStructureV10__fixr_which", curie=FIX_ORCHESTRA.curie('fixr_which'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageStructureV10__fixr_which, domain=None, range=Optional[Union[str, "OrchestraMemberSelection"]])

slots.orchestraMessageV10__fixr_structure = Slot(uri=FIX_ORCHESTRA.fixr_structure, name="orchestraMessageV10__fixr_structure", curie=FIX_ORCHESTRA.curie('fixr_structure'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV10__fixr_structure, domain=None, range=Union[dict, OrchestraMessageStructureV10])

slots.orchestraMessageV10__fixr_responses = Slot(uri=FIX_ORCHESTRA.fixr_responses, name="orchestraMessageV10__fixr_responses", curie=FIX_ORCHESTRA.curie('fixr_responses'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV10__fixr_responses, domain=None, range=Optional[Union[dict, OrchestraResponsesV10]])

slots.orchestraMessageV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraMessageV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraMessageV10__fixr_msg_type = Slot(uri=FIX_ORCHESTRA.fixr_msg_type, name="orchestraMessageV10__fixr_msg_type", curie=FIX_ORCHESTRA.curie('fixr_msg_type'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV10__fixr_msg_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,2}$'))

slots.orchestraMessageV10__fixr_category = Slot(uri=FIX_ORCHESTRA.fixr_category, name="orchestraMessageV10__fixr_category", curie=FIX_ORCHESTRA.curie('fixr_category'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV10__fixr_category, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraMessageV10__fixr_flow = Slot(uri=FIX_ORCHESTRA.fixr_flow, name="orchestraMessageV10__fixr_flow", curie=FIX_ORCHESTRA.curie('fixr_flow'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV10__fixr_flow, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraMessagesV10__fixr_message = Slot(uri=FIX_ORCHESTRA.fixr_message, name="orchestraMessagesV10__fixr_message", curie=FIX_ORCHESTRA.curie('fixr_message'),
                   model_uri=FIX_ORCHESTRA.orchestraMessagesV10__fixr_message, domain=None, range=Union[Union[dict, OrchestraMessageV10], list[Union[dict, OrchestraMessageV10]]])

slots.orchestraMessagesV10__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraMessagesV10__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraMessagesV10__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraPedigreeV10Mixin__fixr_added = Slot(uri=FIX_ORCHESTRA.fixr_added, name="orchestraPedigreeV10Mixin__fixr_added", curie=FIX_ORCHESTRA.curie('fixr_added'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_added, domain=None, range=Optional[str],
                   pattern=re.compile(r'^((FIX.2.7)|(FIX.3.0)|(FIX\.4\.[0-4])|((FIX.Latest|(FIX\.5\.0(SP\d{1,2})?))(_EP((9[8-9])|([1-9][0-9][0-9])))?)|(FIXT.1.1)|([0-9]+)\.([0-9]+)|(\d{8}))$'))

slots.orchestraPedigreeV10Mixin__fixr_added_ep = Slot(uri=FIX_ORCHESTRA.fixr_added_ep, name="orchestraPedigreeV10Mixin__fixr_added_ep", curie=FIX_ORCHESTRA.curie('fixr_added_ep'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_added_ep, domain=None, range=Optional[int])

slots.orchestraPedigreeV10Mixin__fixr_change_type = Slot(uri=FIX_ORCHESTRA.fixr_change_type, name="orchestraPedigreeV10Mixin__fixr_change_type", curie=FIX_ORCHESTRA.curie('fixr_change_type'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_change_type, domain=None, range=Optional[Union[str, "OrchestraChangeKind"]])

slots.orchestraPedigreeV10Mixin__fixr_deprecated = Slot(uri=FIX_ORCHESTRA.fixr_deprecated, name="orchestraPedigreeV10Mixin__fixr_deprecated", curie=FIX_ORCHESTRA.curie('fixr_deprecated'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_deprecated, domain=None, range=Optional[str],
                   pattern=re.compile(r'^((FIX.2.7)|(FIX.3.0)|(FIX\.4\.[0-4])|((FIX.Latest|(FIX\.5\.0(SP\d{1,2})?))(_EP((9[8-9])|([1-9][0-9][0-9])))?)|(FIXT.1.1)|([0-9]+)\.([0-9]+)|(\d{8}))$'))

slots.orchestraPedigreeV10Mixin__fixr_deprecated_ep = Slot(uri=FIX_ORCHESTRA.fixr_deprecated_ep, name="orchestraPedigreeV10Mixin__fixr_deprecated_ep", curie=FIX_ORCHESTRA.curie('fixr_deprecated_ep'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_deprecated_ep, domain=None, range=Optional[int])

slots.orchestraPedigreeV10Mixin__fixr_issue = Slot(uri=FIX_ORCHESTRA.fixr_issue, name="orchestraPedigreeV10Mixin__fixr_issue", curie=FIX_ORCHESTRA.curie('fixr_issue'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_issue, domain=None, range=Optional[str])

slots.orchestraPedigreeV10Mixin__fixr_last_modified = Slot(uri=FIX_ORCHESTRA.fixr_last_modified, name="orchestraPedigreeV10Mixin__fixr_last_modified", curie=FIX_ORCHESTRA.curie('fixr_last_modified'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_last_modified, domain=None, range=Optional[str],
                   pattern=re.compile(r'^((FIX.2.7)|(FIX.3.0)|(FIX\.4\.[0-4])|((FIX.Latest|(FIX\.5\.0(SP\d{1,2})?))(_EP((9[8-9])|([1-9][0-9][0-9])))?)|(FIXT.1.1)|([0-9]+)\.([0-9]+)|(\d{8}))$'))

slots.orchestraPedigreeV10Mixin__fixr_replaced = Slot(uri=FIX_ORCHESTRA.fixr_replaced, name="orchestraPedigreeV10Mixin__fixr_replaced", curie=FIX_ORCHESTRA.curie('fixr_replaced'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_replaced, domain=None, range=Optional[str],
                   pattern=re.compile(r'^((FIX.2.7)|(FIX.3.0)|(FIX\.4\.[0-4])|((FIX.Latest|(FIX\.5\.0(SP\d{1,2})?))(_EP((9[8-9])|([1-9][0-9][0-9])))?)|(FIXT.1.1)|([0-9]+)\.([0-9]+)|(\d{8}))$'))

slots.orchestraPedigreeV10Mixin__fixr_replaced_ep = Slot(uri=FIX_ORCHESTRA.fixr_replaced_ep, name="orchestraPedigreeV10Mixin__fixr_replaced_ep", curie=FIX_ORCHESTRA.curie('fixr_replaced_ep'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_replaced_ep, domain=None, range=Optional[int])

slots.orchestraPedigreeV10Mixin__fixr_replaced_by_field = Slot(uri=FIX_ORCHESTRA.fixr_replaced_by_field, name="orchestraPedigreeV10Mixin__fixr_replaced_by_field", curie=FIX_ORCHESTRA.curie('fixr_replaced_by_field'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_replaced_by_field, domain=None, range=Optional[int])

slots.orchestraPedigreeV10Mixin__fixr_supported = Slot(uri=FIX_ORCHESTRA.fixr_supported, name="orchestraPedigreeV10Mixin__fixr_supported", curie=FIX_ORCHESTRA.curie('fixr_supported'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_supported, domain=None, range=Optional[Union[str, "OrchestraSupport"]])

slots.orchestraPedigreeV10Mixin__fixr_updated = Slot(uri=FIX_ORCHESTRA.fixr_updated, name="orchestraPedigreeV10Mixin__fixr_updated", curie=FIX_ORCHESTRA.curie('fixr_updated'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_updated, domain=None, range=Optional[str],
                   pattern=re.compile(r'^((FIX.2.7)|(FIX.3.0)|(FIX\.4\.[0-4])|((FIX.Latest|(FIX\.5\.0(SP\d{1,2})?))(_EP((9[8-9])|([1-9][0-9][0-9])))?)|(FIXT.1.1)|([0-9]+)\.([0-9]+)|(\d{8}))$'))

slots.orchestraPedigreeV10Mixin__fixr_updated_ep = Slot(uri=FIX_ORCHESTRA.fixr_updated_ep, name="orchestraPedigreeV10Mixin__fixr_updated_ep", curie=FIX_ORCHESTRA.curie('fixr_updated_ep'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV10Mixin__fixr_updated_ep, domain=None, range=Optional[int])

slots.orchestraProtocolV10__fixi_annotation = Slot(uri=FIX_ORCHESTRA.fixi_annotation, name="orchestraProtocolV10__fixi_annotation", curie=FIX_ORCHESTRA.curie('fixi_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV10__fixi_annotation, domain=None, range=Optional[Union[dict, OrchestraInterfaceAnnotationV10]])

slots.orchestraProtocolV10__fixi_name = Slot(uri=FIX_ORCHESTRA.fixi_name, name="orchestraProtocolV10__fixi_name", curie=FIX_ORCHESTRA.curie('fixi_name'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV10__fixi_name, domain=None, range=Optional[Union[str, "OrchestraProtocolName"]])

slots.orchestraProtocolV10__fixi_version = Slot(uri=FIX_ORCHESTRA.fixi_version, name="orchestraProtocolV10__fixi_version", curie=FIX_ORCHESTRA.curie('fixi_version'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV10__fixi_version, domain=None, range=Optional[str])

slots.orchestraProtocolV10__fixi_layer = Slot(uri=FIX_ORCHESTRA.fixi_layer, name="orchestraProtocolV10__fixi_layer", curie=FIX_ORCHESTRA.curie('fixi_layer'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV10__fixi_layer, domain=None, range=Optional[Union[str, "OrchestraLayer"]])

slots.orchestraProtocolV10__fixi_reliability = Slot(uri=FIX_ORCHESTRA.fixi_reliability, name="orchestraProtocolV10__fixi_reliability", curie=FIX_ORCHESTRA.curie('fixi_reliability'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV10__fixi_reliability, domain=None, range=Optional[Union[str, "OrchestraReliability"]])

slots.orchestraProtocolV10__fixi_orchestration = Slot(uri=FIX_ORCHESTRA.fixi_orchestration, name="orchestraProtocolV10__fixi_orchestration", curie=FIX_ORCHESTRA.curie('fixi_orchestration'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV10__fixi_orchestration, domain=None, range=Optional[Union[str, URI]])

slots.orchestraProtocolV10__fixi_other_attributes = Slot(uri=FIX_ORCHESTRA.fixi_other_attributes, name="orchestraProtocolV10__fixi_other_attributes", curie=FIX_ORCHESTRA.curie('fixi_other_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV10__fixi_other_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraReferenceV10Mixin__fixr_id = Slot(uri=FIX_ORCHESTRA.fixr_id, name="orchestraReferenceV10Mixin__fixr_id", curie=FIX_ORCHESTRA.curie('fixr_id'),
                   model_uri=FIX_ORCHESTRA.orchestraReferenceV10Mixin__fixr_id, domain=None, range=int)

slots.orchestraReferenceV10Mixin__fixr_scenario = Slot(uri=FIX_ORCHESTRA.fixr_scenario, name="orchestraReferenceV10Mixin__fixr_scenario", curie=FIX_ORCHESTRA.curie('fixr_scenario'),
                   model_uri=FIX_ORCHESTRA.orchestraReferenceV10Mixin__fixr_scenario, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_|-)*)$'))

slots.orchestraRepositoryV10__fixr_metadata = Slot(uri=FIX_ORCHESTRA.fixr_metadata, name="orchestraRepositoryV10__fixr_metadata", curie=FIX_ORCHESTRA.curie('fixr_metadata'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_metadata, domain=None, range=Union[dict, OrchestraMetadata])

slots.orchestraRepositoryV10__fixr_categories = Slot(uri=FIX_ORCHESTRA.fixr_categories, name="orchestraRepositoryV10__fixr_categories", curie=FIX_ORCHESTRA.curie('fixr_categories'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_categories, domain=None, range=Optional[Union[dict, OrchestraCategoriesV10]])

slots.orchestraRepositoryV10__fixr_sections = Slot(uri=FIX_ORCHESTRA.fixr_sections, name="orchestraRepositoryV10__fixr_sections", curie=FIX_ORCHESTRA.curie('fixr_sections'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_sections, domain=None, range=Optional[Union[dict, OrchestraSectionsV10]])

slots.orchestraRepositoryV10__fixr_datatypes = Slot(uri=FIX_ORCHESTRA.fixr_datatypes, name="orchestraRepositoryV10__fixr_datatypes", curie=FIX_ORCHESTRA.curie('fixr_datatypes'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_datatypes, domain=None, range=Union[dict, OrchestraDatatypesV10])

slots.orchestraRepositoryV10__fixr_code_sets = Slot(uri=FIX_ORCHESTRA.fixr_code_sets, name="orchestraRepositoryV10__fixr_code_sets", curie=FIX_ORCHESTRA.curie('fixr_code_sets'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_code_sets, domain=None, range=Union[dict, OrchestraCodeSetsV10])

slots.orchestraRepositoryV10__fixr_fields = Slot(uri=FIX_ORCHESTRA.fixr_fields, name="orchestraRepositoryV10__fixr_fields", curie=FIX_ORCHESTRA.curie('fixr_fields'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_fields, domain=None, range=Union[dict, OrchestraFieldsV10])

slots.orchestraRepositoryV10__fixr_actors = Slot(uri=FIX_ORCHESTRA.fixr_actors, name="orchestraRepositoryV10__fixr_actors", curie=FIX_ORCHESTRA.curie('fixr_actors'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_actors, domain=None, range=Optional[Union[dict, OrchestraActorsV10]])

slots.orchestraRepositoryV10__fixr_components = Slot(uri=FIX_ORCHESTRA.fixr_components, name="orchestraRepositoryV10__fixr_components", curie=FIX_ORCHESTRA.curie('fixr_components'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_components, domain=None, range=Optional[Union[dict, OrchestraComponentsV10]])

slots.orchestraRepositoryV10__fixr_groups = Slot(uri=FIX_ORCHESTRA.fixr_groups, name="orchestraRepositoryV10__fixr_groups", curie=FIX_ORCHESTRA.curie('fixr_groups'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_groups, domain=None, range=Optional[Union[dict, OrchestraGroupsV10]])

slots.orchestraRepositoryV10__fixr_messages = Slot(uri=FIX_ORCHESTRA.fixr_messages, name="orchestraRepositoryV10__fixr_messages", curie=FIX_ORCHESTRA.curie('fixr_messages'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_messages, domain=None, range=Union[dict, OrchestraMessagesV10])

slots.orchestraRepositoryV10__fixr_concepts = Slot(uri=FIX_ORCHESTRA.fixr_concepts, name="orchestraRepositoryV10__fixr_concepts", curie=FIX_ORCHESTRA.curie('fixr_concepts'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_concepts, domain=None, range=Optional[Union[dict, OrchestraConceptsV10]])

slots.orchestraRepositoryV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraRepositoryV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraRepositoryV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraRepositoryV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_name, domain=None, range=str)

slots.orchestraRepositoryV10__fixr_version = Slot(uri=FIX_ORCHESTRA.fixr_version, name="orchestraRepositoryV10__fixr_version", curie=FIX_ORCHESTRA.curie('fixr_version'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_version, domain=None, range=str,
                   pattern=re.compile(r'^((FIX.2.7)|(FIX.3.0)|(FIX\.4\.[0-4])|((FIX.Latest|(FIX\.5\.0(SP\d{1,2})?))(_EP((9[8-9])|([1-9][0-9][0-9])))?)|(FIXT.1.1)|([0-9]+)\.([0-9]+)|(\d{8}))$'))

slots.orchestraRepositoryV10__fixr_guid = Slot(uri=FIX_ORCHESTRA.fixr_guid, name="orchestraRepositoryV10__fixr_guid", curie=FIX_ORCHESTRA.curie('fixr_guid'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_guid, domain=None, range=Optional[str])

slots.orchestraRepositoryV10__fixr_spec_url = Slot(uri=FIX_ORCHESTRA.fixr_spec_url, name="orchestraRepositoryV10__fixr_spec_url", curie=FIX_ORCHESTRA.curie('fixr_spec_url'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_spec_url, domain=None, range=Optional[Union[str, URI]])

slots.orchestraRepositoryV10__fixr_namespace = Slot(uri=FIX_ORCHESTRA.fixr_namespace, name="orchestraRepositoryV10__fixr_namespace", curie=FIX_ORCHESTRA.curie('fixr_namespace'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_namespace, domain=None, range=Optional[Union[str, URI]])

slots.orchestraRepositoryV10__fixr_appl_ver_id = Slot(uri=FIX_ORCHESTRA.fixr_appl_ver_id, name="orchestraRepositoryV10__fixr_appl_ver_id", curie=FIX_ORCHESTRA.curie('fixr_appl_ver_id'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_appl_ver_id, domain=None, range=Optional[str])

slots.orchestraRepositoryV10__fixr_expression_language = Slot(uri=FIX_ORCHESTRA.fixr_expression_language, name="orchestraRepositoryV10__fixr_expression_language", curie=FIX_ORCHESTRA.curie('fixr_expression_language'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV10__fixr_expression_language, domain=None, range=Optional[str])

slots.orchestraResponseV10__fixr_when = Slot(uri=FIX_ORCHESTRA.fixr_when, name="orchestraResponseV10__fixr_when", curie=FIX_ORCHESTRA.curie('fixr_when'),
                   model_uri=FIX_ORCHESTRA.orchestraResponseV10__fixr_when, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraResponseV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraResponseV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraResponseV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraResponseV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraResponseV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraResponseV10__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraResponseV10__fixr_sync = Slot(uri=FIX_ORCHESTRA.fixr_sync, name="orchestraResponseV10__fixr_sync", curie=FIX_ORCHESTRA.curie('fixr_sync'),
                   model_uri=FIX_ORCHESTRA.orchestraResponseV10__fixr_sync, domain=None, range=Optional[Union[str, "OrchestraSynchronization"]])

slots.orchestraResponsesV10__fixr_response = Slot(uri=FIX_ORCHESTRA.fixr_response, name="orchestraResponsesV10__fixr_response", curie=FIX_ORCHESTRA.curie('fixr_response'),
                   model_uri=FIX_ORCHESTRA.orchestraResponsesV10__fixr_response, domain=None, range=Union[Union[dict, OrchestraResponseV10], list[Union[dict, OrchestraResponseV10]]])

slots.orchestraSectionV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraSectionV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraSectionV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraSectionV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionV10__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraSectionV10__fixr_display_order = Slot(uri=FIX_ORCHESTRA.fixr_display_order, name="orchestraSectionV10__fixr_display_order", curie=FIX_ORCHESTRA.curie('fixr_display_order'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionV10__fixr_display_order, domain=None, range=Optional[int])

slots.orchestraSectionV10__fixr_fixml_file_name = Slot(uri=FIX_ORCHESTRA.fixr_fixml_file_name, name="orchestraSectionV10__fixr_fixml_file_name", curie=FIX_ORCHESTRA.curie('fixr_fixml_file_name'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionV10__fixr_fixml_file_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraSectionsV10__fixr_section = Slot(uri=FIX_ORCHESTRA.fixr_section, name="orchestraSectionsV10__fixr_section", curie=FIX_ORCHESTRA.curie('fixr_section'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionsV10__fixr_section, domain=None, range=Union[Union[dict, OrchestraSectionV10], list[Union[dict, OrchestraSectionV10]]])

slots.orchestraSectionsV10__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraSectionsV10__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionsV10__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraSessionIdentifierV10__fixi_text = Slot(uri=FIX_ORCHESTRA.fixi_text, name="orchestraSessionIdentifierV10__fixi_text", curie=FIX_ORCHESTRA.curie('fixi_text'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionIdentifierV10__fixi_text, domain=None, range=Optional[str])

slots.orchestraSessionIdentifierV10__fixi_name = Slot(uri=FIX_ORCHESTRA.fixi_name, name="orchestraSessionIdentifierV10__fixi_name", curie=FIX_ORCHESTRA.curie('fixi_name'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionIdentifierV10__fixi_name, domain=None, range=Optional[str])

slots.orchestraSessionV10__fixi_identifier = Slot(uri=FIX_ORCHESTRA.fixi_identifier, name="orchestraSessionV10__fixi_identifier", curie=FIX_ORCHESTRA.curie('fixi_identifier'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionV10__fixi_identifier, domain=None, range=Optional[Union[Union[dict, OrchestraSessionIdentifierV10], list[Union[dict, OrchestraSessionIdentifierV10]]]])

slots.orchestraSessionV10__fixi_activation_time = Slot(uri=FIX_ORCHESTRA.fixi_activation_time, name="orchestraSessionV10__fixi_activation_time", curie=FIX_ORCHESTRA.curie('fixi_activation_time'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionV10__fixi_activation_time, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?\d{4,}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$'))

slots.orchestraSessionV10__fixi_deactivation_time = Slot(uri=FIX_ORCHESTRA.fixi_deactivation_time, name="orchestraSessionV10__fixi_deactivation_time", curie=FIX_ORCHESTRA.curie('fixi_deactivation_time'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionV10__fixi_deactivation_time, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?\d{4,}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$'))

slots.orchestraSessionV10__fixi_role = Slot(uri=FIX_ORCHESTRA.fixi_role, name="orchestraSessionV10__fixi_role", curie=FIX_ORCHESTRA.curie('fixi_role'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionV10__fixi_role, domain=None, range=Optional[Union[str, "OrchestraRole"]])

slots.orchestraSessionV10__fixi_security_keys = Slot(uri=FIX_ORCHESTRA.fixi_security_keys, name="orchestraSessionV10__fixi_security_keys", curie=FIX_ORCHESTRA.curie('fixi_security_keys'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionV10__fixi_security_keys, domain=None, range=Optional[str])

slots.orchestraSessionsV10__fixi_session = Slot(uri=FIX_ORCHESTRA.fixi_session, name="orchestraSessionsV10__fixi_session", curie=FIX_ORCHESTRA.curie('fixi_session'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionsV10__fixi_session, domain=None, range=Union[Union[dict, OrchestraSessionV10], list[Union[dict, OrchestraSessionV10]]])

slots.orchestraStateMachineV10__fixr_initial = Slot(uri=FIX_ORCHESTRA.fixr_initial, name="orchestraStateMachineV10__fixr_initial", curie=FIX_ORCHESTRA.curie('fixr_initial'),
                   model_uri=FIX_ORCHESTRA.orchestraStateMachineV10__fixr_initial, domain=None, range=Union[dict, OrchestraStateV10])

slots.orchestraStateMachineV10__fixr_state = Slot(uri=FIX_ORCHESTRA.fixr_state, name="orchestraStateMachineV10__fixr_state", curie=FIX_ORCHESTRA.curie('fixr_state'),
                   model_uri=FIX_ORCHESTRA.orchestraStateMachineV10__fixr_state, domain=None, range=Union[Union[dict, OrchestraStateV10], list[Union[dict, OrchestraStateV10]]])

slots.orchestraStateMachineV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraStateMachineV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraStateMachineV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraStateMachineV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraStateMachineV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraStateMachineV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraStateV10__fixr_transition = Slot(uri=FIX_ORCHESTRA.fixr_transition, name="orchestraStateV10__fixr_transition", curie=FIX_ORCHESTRA.curie('fixr_transition'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV10__fixr_transition, domain=None, range=Optional[Union[Union[dict, OrchestraTransitionV10], list[Union[dict, OrchestraTransitionV10]]]])

slots.orchestraStateV10__fixr_onentry = Slot(uri=FIX_ORCHESTRA.fixr_onentry, name="orchestraStateV10__fixr_onentry", curie=FIX_ORCHESTRA.curie('fixr_onentry'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV10__fixr_onentry, domain=None, range=Optional[Union[dict, OrchestraActionV10]])

slots.orchestraStateV10__fixr_activity = Slot(uri=FIX_ORCHESTRA.fixr_activity, name="orchestraStateV10__fixr_activity", curie=FIX_ORCHESTRA.curie('fixr_activity'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV10__fixr_activity, domain=None, range=Optional[Union[dict, OrchestraActionV10]])

slots.orchestraStateV10__fixr_onexit = Slot(uri=FIX_ORCHESTRA.fixr_onexit, name="orchestraStateV10__fixr_onexit", curie=FIX_ORCHESTRA.curie('fixr_onexit'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV10__fixr_onexit, domain=None, range=Optional[Union[dict, OrchestraActionV10]])

slots.orchestraStateV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraStateV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraStateV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraStateV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraStructureMemberV10__fixr_component_ref = Slot(uri=FIX_ORCHESTRA.fixr_component_ref, name="orchestraStructureMemberV10__fixr_component_ref", curie=FIX_ORCHESTRA.curie('fixr_component_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraStructureMemberV10__fixr_component_ref, domain=None, range=Optional[Union[dict, OrchestraComponentRefV10]])

slots.orchestraStructureMemberV10__fixr_group_ref = Slot(uri=FIX_ORCHESTRA.fixr_group_ref, name="orchestraStructureMemberV10__fixr_group_ref", curie=FIX_ORCHESTRA.curie('fixr_group_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraStructureMemberV10__fixr_group_ref, domain=None, range=Optional[Union[dict, OrchestraGroupRefV10]])

slots.orchestraStructureMemberV10__fixr_field_ref = Slot(uri=FIX_ORCHESTRA.fixr_field_ref, name="orchestraStructureMemberV10__fixr_field_ref", curie=FIX_ORCHESTRA.curie('fixr_field_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraStructureMemberV10__fixr_field_ref, domain=None, range=Optional[Union[dict, OrchestraFieldRefV10]])

slots.orchestraTimerScheduleV10__fixr_activity = Slot(uri=FIX_ORCHESTRA.fixr_activity, name="orchestraTimerScheduleV10__fixr_activity", curie=FIX_ORCHESTRA.curie('fixr_activity'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerScheduleV10__fixr_activity, domain=None, range=Union[dict, OrchestraActionV10])

slots.orchestraTimerScheduleV10__fixr_actor = Slot(uri=FIX_ORCHESTRA.fixr_actor, name="orchestraTimerScheduleV10__fixr_actor", curie=FIX_ORCHESTRA.curie('fixr_actor'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerScheduleV10__fixr_actor, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraTimerScheduleV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraTimerScheduleV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerScheduleV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraTimerScheduleV10__fixr_operation = Slot(uri=FIX_ORCHESTRA.fixr_operation, name="orchestraTimerScheduleV10__fixr_operation", curie=FIX_ORCHESTRA.curie('fixr_operation'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerScheduleV10__fixr_operation, domain=None, range=Union[str, "OrchestraTimerOperation"])

slots.orchestraTimerScheduleV10__fixr_interval = Slot(uri=FIX_ORCHESTRA.fixr_interval, name="orchestraTimerScheduleV10__fixr_interval", curie=FIX_ORCHESTRA.curie('fixr_interval'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerScheduleV10__fixr_interval, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?P(?=\d|T\d)(\d+Y)?(\d+M)?(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+(\.\d+)?S)?)?$'))

slots.orchestraTimerV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraTimerV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraTransitionV10__fixr_when = Slot(uri=FIX_ORCHESTRA.fixr_when, name="orchestraTransitionV10__fixr_when", curie=FIX_ORCHESTRA.curie('fixr_when'),
                   model_uri=FIX_ORCHESTRA.orchestraTransitionV10__fixr_when, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraTransitionV10__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraTransitionV10__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraTransitionV10__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV10]])

slots.orchestraTransitionV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraTransitionV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraTransitionV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraTransitionV10__fixr_target = Slot(uri=FIX_ORCHESTRA.fixr_target, name="orchestraTransitionV10__fixr_target", curie=FIX_ORCHESTRA.curie('fixr_target'),
                   model_uri=FIX_ORCHESTRA.orchestraTransitionV10__fixr_target, domain=None, range=str)

slots.orchestraTransportV10__fixi_address = Slot(uri=FIX_ORCHESTRA.fixi_address, name="orchestraTransportV10__fixi_address", curie=FIX_ORCHESTRA.curie('fixi_address'),
                   model_uri=FIX_ORCHESTRA.orchestraTransportV10__fixi_address, domain=None, range=Optional[str])

slots.orchestraTransportV10__fixi_message_cast = Slot(uri=FIX_ORCHESTRA.fixi_message_cast, name="orchestraTransportV10__fixi_message_cast", curie=FIX_ORCHESTRA.curie('fixi_message_cast'),
                   model_uri=FIX_ORCHESTRA.orchestraTransportV10__fixi_message_cast, domain=None, range=Optional[Union[str, "OrchestraMessageCast"]])

slots.orchestraTransportV10__fixi_use = Slot(uri=FIX_ORCHESTRA.fixi_use, name="orchestraTransportV10__fixi_use", curie=FIX_ORCHESTRA.curie('fixi_use'),
                   model_uri=FIX_ORCHESTRA.orchestraTransportV10__fixi_use, domain=None, range=Optional[Union[str, "OrchestraTransportUse"]])

slots.orchestraTransportV10__fixi_other_attributes = Slot(uri=FIX_ORCHESTRA.fixi_other_attributes, name="orchestraTransportV10__fixi_other_attributes", curie=FIX_ORCHESTRA.curie('fixi_other_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraTransportV10__fixi_other_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraTriggerV10__fixr_state_machine = Slot(uri=FIX_ORCHESTRA.fixr_state_machine, name="orchestraTriggerV10__fixr_state_machine", curie=FIX_ORCHESTRA.curie('fixr_state_machine'),
                   model_uri=FIX_ORCHESTRA.orchestraTriggerV10__fixr_state_machine, domain=None, range=str)

slots.orchestraTriggerV10__fixr_actor = Slot(uri=FIX_ORCHESTRA.fixr_actor, name="orchestraTriggerV10__fixr_actor", curie=FIX_ORCHESTRA.curie('fixr_actor'),
                   model_uri=FIX_ORCHESTRA.orchestraTriggerV10__fixr_actor, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraTriggerV10__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraTriggerV10__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraTriggerV10__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,255}$)(([A-Z]|[a-z])([0-9]|[A-Z]|[a-z]|_)*)$'))

slots.orchestraUniqueV10__fixr_field_ref = Slot(uri=FIX_ORCHESTRA.fixr_field_ref, name="orchestraUniqueV10__fixr_field_ref", curie=FIX_ORCHESTRA.curie('fixr_field_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraUniqueV10__fixr_field_ref, domain=None, range=Optional[Union[Union[dict, OrchestraFieldRefV10], list[Union[dict, OrchestraFieldRefV10]]]])

slots.orchestraActionParameterV11__fixr_field = Slot(uri=FIX_ORCHESTRA.fixr_field, name="orchestraActionParameterV11__fixr_field", curie=FIX_ORCHESTRA.curie('fixr_field'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV11__fixr_field, domain=None, range=Optional[Union[dict, OrchestraFieldV11]])

slots.orchestraActionParameterV11__fixr_field_ref = Slot(uri=FIX_ORCHESTRA.fixr_field_ref, name="orchestraActionParameterV11__fixr_field_ref", curie=FIX_ORCHESTRA.curie('fixr_field_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV11__fixr_field_ref, domain=None, range=Optional[Union[dict, OrchestraFieldRefV11]])

slots.orchestraActionParameterV11__fixr_component = Slot(uri=FIX_ORCHESTRA.fixr_component, name="orchestraActionParameterV11__fixr_component", curie=FIX_ORCHESTRA.curie('fixr_component'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV11__fixr_component, domain=None, range=Optional[Union[dict, OrchestraComponentV11]])

slots.orchestraActionParameterV11__fixr_component_ref = Slot(uri=FIX_ORCHESTRA.fixr_component_ref, name="orchestraActionParameterV11__fixr_component_ref", curie=FIX_ORCHESTRA.curie('fixr_component_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV11__fixr_component_ref, domain=None, range=Optional[Union[dict, OrchestraComponentRefV11]])

slots.orchestraActionParameterV11__fixr_group = Slot(uri=FIX_ORCHESTRA.fixr_group, name="orchestraActionParameterV11__fixr_group", curie=FIX_ORCHESTRA.curie('fixr_group'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV11__fixr_group, domain=None, range=Optional[Union[dict, OrchestraGroupV11]])

slots.orchestraActionParameterV11__fixr_group_ref = Slot(uri=FIX_ORCHESTRA.fixr_group_ref, name="orchestraActionParameterV11__fixr_group_ref", curie=FIX_ORCHESTRA.curie('fixr_group_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActionParameterV11__fixr_group_ref, domain=None, range=Optional[Union[dict, OrchestraGroupRefV11]])

slots.orchestraActionStepV11__fixr_message_ref = Slot(uri=FIX_ORCHESTRA.fixr_message_ref, name="orchestraActionStepV11__fixr_message_ref", curie=FIX_ORCHESTRA.curie('fixr_message_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActionStepV11__fixr_message_ref, domain=None, range=Optional[Union[dict, OrchestraMessageRefV11]])

slots.orchestraActionStepV11__fixr_assign = Slot(uri=FIX_ORCHESTRA.fixr_assign, name="orchestraActionStepV11__fixr_assign", curie=FIX_ORCHESTRA.curie('fixr_assign'),
                   model_uri=FIX_ORCHESTRA.orchestraActionStepV11__fixr_assign, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraActionStepV11__fixr_trigger = Slot(uri=FIX_ORCHESTRA.fixr_trigger, name="orchestraActionStepV11__fixr_trigger", curie=FIX_ORCHESTRA.curie('fixr_trigger'),
                   model_uri=FIX_ORCHESTRA.orchestraActionStepV11__fixr_trigger, domain=None, range=Optional[Union[dict, OrchestraTriggerV11]])

slots.orchestraActionStepV11__fixr_timer_schedule = Slot(uri=FIX_ORCHESTRA.fixr_timer_schedule, name="orchestraActionStepV11__fixr_timer_schedule", curie=FIX_ORCHESTRA.curie('fixr_timer_schedule'),
                   model_uri=FIX_ORCHESTRA.orchestraActionStepV11__fixr_timer_schedule, domain=None, range=Optional[Union[dict, OrchestraTimerScheduleV11]])

slots.orchestraActionV11__fixr_parameters = Slot(uri=FIX_ORCHESTRA.fixr_parameters, name="orchestraActionV11__fixr_parameters", curie=FIX_ORCHESTRA.curie('fixr_parameters'),
                   model_uri=FIX_ORCHESTRA.orchestraActionV11__fixr_parameters, domain=None, range=Optional[Union[Union[dict, OrchestraActionParameterV11], list[Union[dict, OrchestraActionParameterV11]]]])

slots.orchestraActionV11__fixr_actions = Slot(uri=FIX_ORCHESTRA.fixr_actions, name="orchestraActionV11__fixr_actions", curie=FIX_ORCHESTRA.curie('fixr_actions'),
                   model_uri=FIX_ORCHESTRA.orchestraActionV11__fixr_actions, domain=None, range=Union[Union[dict, OrchestraActionStepV11], list[Union[dict, OrchestraActionStepV11]]])

slots.orchestraActorMemberV11__fixr_field = Slot(uri=FIX_ORCHESTRA.fixr_field, name="orchestraActorMemberV11__fixr_field", curie=FIX_ORCHESTRA.curie('fixr_field'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV11__fixr_field, domain=None, range=Optional[Union[dict, OrchestraFieldV11]])

slots.orchestraActorMemberV11__fixr_field_ref = Slot(uri=FIX_ORCHESTRA.fixr_field_ref, name="orchestraActorMemberV11__fixr_field_ref", curie=FIX_ORCHESTRA.curie('fixr_field_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV11__fixr_field_ref, domain=None, range=Optional[Union[dict, OrchestraFieldRefV11]])

slots.orchestraActorMemberV11__fixr_component = Slot(uri=FIX_ORCHESTRA.fixr_component, name="orchestraActorMemberV11__fixr_component", curie=FIX_ORCHESTRA.curie('fixr_component'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV11__fixr_component, domain=None, range=Optional[Union[dict, OrchestraComponentV11]])

slots.orchestraActorMemberV11__fixr_component_ref = Slot(uri=FIX_ORCHESTRA.fixr_component_ref, name="orchestraActorMemberV11__fixr_component_ref", curie=FIX_ORCHESTRA.curie('fixr_component_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV11__fixr_component_ref, domain=None, range=Optional[Union[dict, OrchestraComponentRefV11]])

slots.orchestraActorMemberV11__fixr_group = Slot(uri=FIX_ORCHESTRA.fixr_group, name="orchestraActorMemberV11__fixr_group", curie=FIX_ORCHESTRA.curie('fixr_group'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV11__fixr_group, domain=None, range=Optional[Union[dict, OrchestraGroupV11]])

slots.orchestraActorMemberV11__fixr_group_ref = Slot(uri=FIX_ORCHESTRA.fixr_group_ref, name="orchestraActorMemberV11__fixr_group_ref", curie=FIX_ORCHESTRA.curie('fixr_group_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV11__fixr_group_ref, domain=None, range=Optional[Union[dict, OrchestraGroupRefV11]])

slots.orchestraActorMemberV11__fixr_states = Slot(uri=FIX_ORCHESTRA.fixr_states, name="orchestraActorMemberV11__fixr_states", curie=FIX_ORCHESTRA.curie('fixr_states'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV11__fixr_states, domain=None, range=Optional[Union[dict, OrchestraStateMachineV11]])

slots.orchestraActorMemberV11__fixr_timer = Slot(uri=FIX_ORCHESTRA.fixr_timer, name="orchestraActorMemberV11__fixr_timer", curie=FIX_ORCHESTRA.curie('fixr_timer'),
                   model_uri=FIX_ORCHESTRA.orchestraActorMemberV11__fixr_timer, domain=None, range=Optional[Union[dict, OrchestraTimerV11]])

slots.orchestraActorV11__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraActorV11__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraActorV11__fixr_members, domain=None, range=Optional[Union[Union[dict, OrchestraActorMemberV11], list[Union[dict, OrchestraActorMemberV11]]]])

slots.orchestraActorV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraActorV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraActorV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraActorV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraActorV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraActorV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraActorsMemberV11__fixr_actor = Slot(uri=FIX_ORCHESTRA.fixr_actor, name="orchestraActorsMemberV11__fixr_actor", curie=FIX_ORCHESTRA.curie('fixr_actor'),
                   model_uri=FIX_ORCHESTRA.orchestraActorsMemberV11__fixr_actor, domain=None, range=Optional[Union[dict, OrchestraActorV11]])

slots.orchestraActorsMemberV11__fixr_flow = Slot(uri=FIX_ORCHESTRA.fixr_flow, name="orchestraActorsMemberV11__fixr_flow", curie=FIX_ORCHESTRA.curie('fixr_flow'),
                   model_uri=FIX_ORCHESTRA.orchestraActorsMemberV11__fixr_flow, domain=None, range=Optional[Union[dict, OrchestraFlowV11]])

slots.orchestraActorsV11__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraActorsV11__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraActorsV11__fixr_members, domain=None, range=Optional[Union[Union[dict, OrchestraActorsMemberV11], list[Union[dict, OrchestraActorsMemberV11]]]])

slots.orchestraActorsV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraActorsV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraActorsV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraActorsV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraActorsV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraActorsV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraAnnotationMemberV11__fixr_documentation = Slot(uri=FIX_ORCHESTRA.fixr_documentation, name="orchestraAnnotationMemberV11__fixr_documentation", curie=FIX_ORCHESTRA.curie('fixr_documentation'),
                   model_uri=FIX_ORCHESTRA.orchestraAnnotationMemberV11__fixr_documentation, domain=None, range=Optional[Union[dict, OrchestraDocumentationV11]])

slots.orchestraAnnotationMemberV11__fixr_appinfo = Slot(uri=FIX_ORCHESTRA.fixr_appinfo, name="orchestraAnnotationMemberV11__fixr_appinfo", curie=FIX_ORCHESTRA.curie('fixr_appinfo'),
                   model_uri=FIX_ORCHESTRA.orchestraAnnotationMemberV11__fixr_appinfo, domain=None, range=Optional[Union[dict, OrchestraAppinfoV11]])

slots.orchestraAnnotationV11__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraAnnotationV11__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraAnnotationV11__fixr_members, domain=None, range=Union[Union[dict, OrchestraAnnotationMemberV11], list[Union[dict, OrchestraAnnotationMemberV11]]])

slots.orchestraAppinfoV11__fixr_text = Slot(uri=FIX_ORCHESTRA.fixr_text, name="orchestraAppinfoV11__fixr_text", curie=FIX_ORCHESTRA.curie('fixr_text'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV11__fixr_text, domain=None, range=Optional[str])

slots.orchestraAppinfoV11__fixr_any = Slot(uri=FIX_ORCHESTRA.fixr_any, name="orchestraAppinfoV11__fixr_any", curie=FIX_ORCHESTRA.curie('fixr_any'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV11__fixr_any, domain=None, range=Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]])

slots.orchestraAppinfoV11__fixr_spec_url = Slot(uri=FIX_ORCHESTRA.fixr_spec_url, name="orchestraAppinfoV11__fixr_spec_url", curie=FIX_ORCHESTRA.curie('fixr_spec_url'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV11__fixr_spec_url, domain=None, range=Optional[Union[str, URI]])

slots.orchestraAppinfoV11__fixr_lang_id = Slot(uri=FIX_ORCHESTRA.fixr_lang_id, name="orchestraAppinfoV11__fixr_lang_id", curie=FIX_ORCHESTRA.curie('fixr_lang_id'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV11__fixr_lang_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*$'))

slots.orchestraAppinfoV11__fixr_purpose = Slot(uri=FIX_ORCHESTRA.fixr_purpose, name="orchestraAppinfoV11__fixr_purpose", curie=FIX_ORCHESTRA.curie('fixr_purpose'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV11__fixr_purpose, domain=None, range=Optional[Union[str, "OrchestraPurposeV11"]])

slots.orchestraAppinfoV11__fixr_other_attributes = Slot(uri=FIX_ORCHESTRA.fixr_other_attributes, name="orchestraAppinfoV11__fixr_other_attributes", curie=FIX_ORCHESTRA.curie('fixr_other_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraAppinfoV11__fixr_other_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraBaseEncodingV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraBaseEncodingV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseEncodingV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraBaseEncodingV11__fixr_any = Slot(uri=FIX_ORCHESTRA.fixr_any, name="orchestraBaseEncodingV11__fixr_any", curie=FIX_ORCHESTRA.curie('fixr_any'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseEncodingV11__fixr_any, domain=None, range=Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]])

slots.orchestraBaseInterfaceV11__fixi_service = Slot(uri=FIX_ORCHESTRA.fixi_service, name="orchestraBaseInterfaceV11__fixi_service", curie=FIX_ORCHESTRA.curie('fixi_service'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV11__fixi_service, domain=None, range=Optional[Union[Union[dict, OrchestraServiceV11], list[Union[dict, OrchestraServiceV11]]]])

slots.orchestraBaseInterfaceV11__fixi_user_interface = Slot(uri=FIX_ORCHESTRA.fixi_user_interface, name="orchestraBaseInterfaceV11__fixi_user_interface", curie=FIX_ORCHESTRA.curie('fixi_user_interface'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV11__fixi_user_interface, domain=None, range=Optional[Union[Union[dict, OrchestraUserInterfaceV11], list[Union[dict, OrchestraUserInterfaceV11]]]])

slots.orchestraBaseInterfaceV11__fixi_encoding = Slot(uri=FIX_ORCHESTRA.fixi_encoding, name="orchestraBaseInterfaceV11__fixi_encoding", curie=FIX_ORCHESTRA.curie('fixi_encoding'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV11__fixi_encoding, domain=None, range=Optional[Union[Union[dict, OrchestraEncodingV11], list[Union[dict, OrchestraEncodingV11]]]])

slots.orchestraBaseInterfaceV11__fixi_session_protocol = Slot(uri=FIX_ORCHESTRA.fixi_session_protocol, name="orchestraBaseInterfaceV11__fixi_session_protocol", curie=FIX_ORCHESTRA.curie('fixi_session_protocol'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV11__fixi_session_protocol, domain=None, range=Optional[Union[Union[dict, OrchestraSessionProtocolV11], list[Union[dict, OrchestraSessionProtocolV11]]]])

slots.orchestraBaseInterfaceV11__fixi_protocol = Slot(uri=FIX_ORCHESTRA.fixi_protocol, name="orchestraBaseInterfaceV11__fixi_protocol", curie=FIX_ORCHESTRA.curie('fixi_protocol'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV11__fixi_protocol, domain=None, range=Optional[Union[Union[dict, OrchestraProtocolV11], list[Union[dict, OrchestraProtocolV11]]]])

slots.orchestraBaseInterfaceV11__fixi_transport = Slot(uri=FIX_ORCHESTRA.fixi_transport, name="orchestraBaseInterfaceV11__fixi_transport", curie=FIX_ORCHESTRA.curie('fixi_transport'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV11__fixi_transport, domain=None, range=Optional[Union[Union[dict, OrchestraTransportV11], list[Union[dict, OrchestraTransportV11]]]])

slots.orchestraBaseInterfaceV11__fixi_annotation = Slot(uri=FIX_ORCHESTRA.fixi_annotation, name="orchestraBaseInterfaceV11__fixi_annotation", curie=FIX_ORCHESTRA.curie('fixi_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV11__fixi_annotation, domain=None, range=Optional[Union[dict, OrchestraInterfaceAnnotationV11]])

slots.orchestraBaseInterfaceV11__fixi_name = Slot(uri=FIX_ORCHESTRA.fixi_name, name="orchestraBaseInterfaceV11__fixi_name", curie=FIX_ORCHESTRA.curie('fixi_name'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV11__fixi_name, domain=None, range=str,
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)?$'))

slots.orchestraBaseInterfaceV11__fixi_other_attributes = Slot(uri=FIX_ORCHESTRA.fixi_other_attributes, name="orchestraBaseInterfaceV11__fixi_other_attributes", curie=FIX_ORCHESTRA.curie('fixi_other_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraBaseInterfaceV11__fixi_other_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraBlockAssignmentV11__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraBlockAssignmentV11__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraBlockAssignmentV11__fixr_members, domain=None, range=Union[Union[dict, OrchestraStructureMemberV11], list[Union[dict, OrchestraStructureMemberV11]]])

slots.orchestraCategoriesV11__fixr_category = Slot(uri=FIX_ORCHESTRA.fixr_category, name="orchestraCategoriesV11__fixr_category", curie=FIX_ORCHESTRA.curie('fixr_category'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoriesV11__fixr_category, domain=None, range=Optional[Union[Union[dict, OrchestraCategoryV11], list[Union[dict, OrchestraCategoryV11]]]])

slots.orchestraCategoriesV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraCategoriesV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoriesV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraCategoriesV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraCategoriesV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoriesV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraCategoryV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraCategoryV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoryV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraCategoryV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraCategoryV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoryV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraCategoryV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraCategoryV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoryV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraCategoryV11__fixr_section = Slot(uri=FIX_ORCHESTRA.fixr_section, name="orchestraCategoryV11__fixr_section", curie=FIX_ORCHESTRA.curie('fixr_section'),
                   model_uri=FIX_ORCHESTRA.orchestraCategoryV11__fixr_section, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraCodeSetV11__fixr_code = Slot(uri=FIX_ORCHESTRA.fixr_code, name="orchestraCodeSetV11__fixr_code", curie=FIX_ORCHESTRA.curie('fixr_code'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV11__fixr_code, domain=None, range=Optional[Union[Union[dict, OrchestraCodeV11], list[Union[dict, OrchestraCodeV11]]]])

slots.orchestraCodeSetV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraCodeSetV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraCodeSetV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraCodeSetV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraCodeSetV11__fixr_type = Slot(uri=FIX_ORCHESTRA.fixr_type, name="orchestraCodeSetV11__fixr_type", curie=FIX_ORCHESTRA.curie('fixr_type'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV11__fixr_type, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraCodeSetV11__fixr_default = Slot(uri=FIX_ORCHESTRA.fixr_default, name="orchestraCodeSetV11__fixr_default", curie=FIX_ORCHESTRA.curie('fixr_default'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV11__fixr_default, domain=None, range=Optional[str])

slots.orchestraCodeSetV11__fixr_spec_url = Slot(uri=FIX_ORCHESTRA.fixr_spec_url, name="orchestraCodeSetV11__fixr_spec_url", curie=FIX_ORCHESTRA.curie('fixr_spec_url'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV11__fixr_spec_url, domain=None, range=Optional[Union[str, URI]])

slots.orchestraCodeSetV11__fixr_union_data_type = Slot(uri=FIX_ORCHESTRA.fixr_union_data_type, name="orchestraCodeSetV11__fixr_union_data_type", curie=FIX_ORCHESTRA.curie('fixr_union_data_type'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetV11__fixr_union_data_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraCodeSetsV11__fixr_code_set = Slot(uri=FIX_ORCHESTRA.fixr_code_set, name="orchestraCodeSetsV11__fixr_code_set", curie=FIX_ORCHESTRA.curie('fixr_code_set'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetsV11__fixr_code_set, domain=None, range=Optional[Union[Union[dict, OrchestraCodeSetV11], list[Union[dict, OrchestraCodeSetV11]]]])

slots.orchestraCodeSetsV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraCodeSetsV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetsV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraCodeSetsV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraCodeSetsV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetsV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraCodeSetsV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraCodeSetsV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeSetsV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraCodeV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraCodeV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraCodeV11__fixr_value = Slot(uri=FIX_ORCHESTRA.fixr_value, name="orchestraCodeV11__fixr_value", curie=FIX_ORCHESTRA.curie('fixr_value'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeV11__fixr_value, domain=None, range=str,
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)?$'))

slots.orchestraCodeV11__fixr_sort = Slot(uri=FIX_ORCHESTRA.fixr_sort, name="orchestraCodeV11__fixr_sort", curie=FIX_ORCHESTRA.curie('fixr_sort'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeV11__fixr_sort, domain=None, range=Optional[int])

slots.orchestraCodeV11__fixr_group = Slot(uri=FIX_ORCHESTRA.fixr_group, name="orchestraCodeV11__fixr_group", curie=FIX_ORCHESTRA.curie('fixr_group'),
                   model_uri=FIX_ORCHESTRA.orchestraCodeV11__fixr_group, domain=None, range=Optional[str])

slots.orchestraComponentRefV11__fixr_block_assignment = Slot(uri=FIX_ORCHESTRA.fixr_block_assignment, name="orchestraComponentRefV11__fixr_block_assignment", curie=FIX_ORCHESTRA.curie('fixr_block_assignment'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV11__fixr_block_assignment, domain=None, range=Optional[Union[Union[dict, OrchestraBlockAssignmentV11], list[Union[dict, OrchestraBlockAssignmentV11]]]])

slots.orchestraComponentRefV11__fixr_rule = Slot(uri=FIX_ORCHESTRA.fixr_rule, name="orchestraComponentRefV11__fixr_rule", curie=FIX_ORCHESTRA.curie('fixr_rule'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV11__fixr_rule, domain=None, range=Optional[Union[Union[dict, OrchestraComponentRuleV11], list[Union[dict, OrchestraComponentRuleV11]]]])

slots.orchestraComponentRefV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraComponentRefV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraComponentRefV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraComponentRefV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraComponentRefV11__fixr_presence = Slot(uri=FIX_ORCHESTRA.fixr_presence, name="orchestraComponentRefV11__fixr_presence", curie=FIX_ORCHESTRA.curie('fixr_presence'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV11__fixr_presence, domain=None, range=Optional[Union[str, "OrchestraPresence"]])

slots.orchestraComponentRefV11__fixr_instance_name = Slot(uri=FIX_ORCHESTRA.fixr_instance_name, name="orchestraComponentRefV11__fixr_instance_name", curie=FIX_ORCHESTRA.curie('fixr_instance_name'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRefV11__fixr_instance_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraComponentRuleV11__fixr_when = Slot(uri=FIX_ORCHESTRA.fixr_when, name="orchestraComponentRuleV11__fixr_when", curie=FIX_ORCHESTRA.curie('fixr_when'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRuleV11__fixr_when, domain=None, range=str,
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraComponentRuleV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraComponentRuleV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRuleV11__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraComponentRuleV11__fixr_presence = Slot(uri=FIX_ORCHESTRA.fixr_presence, name="orchestraComponentRuleV11__fixr_presence", curie=FIX_ORCHESTRA.curie('fixr_presence'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentRuleV11__fixr_presence, domain=None, range=Optional[Union[str, "OrchestraPresence"]])

slots.orchestraComponentV11__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraComponentV11__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV11__fixr_members, domain=None, range=Optional[Union[Union[dict, OrchestraStructureMemberV11], list[Union[dict, OrchestraStructureMemberV11]]]])

slots.orchestraComponentV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraComponentV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraComponentV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraComponentV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraComponentV11__fixr_category = Slot(uri=FIX_ORCHESTRA.fixr_category, name="orchestraComponentV11__fixr_category", curie=FIX_ORCHESTRA.curie('fixr_category'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV11__fixr_category, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraComponentV11__fixr_rendering = Slot(uri=FIX_ORCHESTRA.fixr_rendering, name="orchestraComponentV11__fixr_rendering", curie=FIX_ORCHESTRA.curie('fixr_rendering'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV11__fixr_rendering, domain=None, range=Optional[str])

slots.orchestraComponentV11__fixr_which = Slot(uri=FIX_ORCHESTRA.fixr_which, name="orchestraComponentV11__fixr_which", curie=FIX_ORCHESTRA.curie('fixr_which'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentV11__fixr_which, domain=None, range=Optional[Union[str, "OrchestraMemberSelection"]])

slots.orchestraComponentsV11__fixr_component = Slot(uri=FIX_ORCHESTRA.fixr_component, name="orchestraComponentsV11__fixr_component", curie=FIX_ORCHESTRA.curie('fixr_component'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentsV11__fixr_component, domain=None, range=Optional[Union[Union[dict, OrchestraComponentV11], list[Union[dict, OrchestraComponentV11]]]])

slots.orchestraComponentsV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraComponentsV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentsV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraComponentsV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraComponentsV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentsV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraComponentsV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraComponentsV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraComponentsV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraConceptMemberV11__fixr_component_ref = Slot(uri=FIX_ORCHESTRA.fixr_component_ref, name="orchestraConceptMemberV11__fixr_component_ref", curie=FIX_ORCHESTRA.curie('fixr_component_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptMemberV11__fixr_component_ref, domain=None, range=Optional[Union[dict, OrchestraComponentRefV11]])

slots.orchestraConceptMemberV11__fixr_group_ref = Slot(uri=FIX_ORCHESTRA.fixr_group_ref, name="orchestraConceptMemberV11__fixr_group_ref", curie=FIX_ORCHESTRA.curie('fixr_group_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptMemberV11__fixr_group_ref, domain=None, range=Optional[Union[dict, OrchestraGroupRefV11]])

slots.orchestraConceptMemberV11__fixr_field_ref = Slot(uri=FIX_ORCHESTRA.fixr_field_ref, name="orchestraConceptMemberV11__fixr_field_ref", curie=FIX_ORCHESTRA.curie('fixr_field_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptMemberV11__fixr_field_ref, domain=None, range=Optional[Union[dict, OrchestraFieldRefV11]])

slots.orchestraConceptMemberV11__fixr_message_ref = Slot(uri=FIX_ORCHESTRA.fixr_message_ref, name="orchestraConceptMemberV11__fixr_message_ref", curie=FIX_ORCHESTRA.curie('fixr_message_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptMemberV11__fixr_message_ref, domain=None, range=Optional[Union[dict, OrchestraMessageRefV11]])

slots.orchestraConceptV11__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraConceptV11__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptV11__fixr_members, domain=None, range=Union[Union[dict, OrchestraConceptMemberV11], list[Union[dict, OrchestraConceptMemberV11]]])

slots.orchestraConceptV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraConceptV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraConceptV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraConceptV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraConceptsV11__fixr_concept = Slot(uri=FIX_ORCHESTRA.fixr_concept, name="orchestraConceptsV11__fixr_concept", curie=FIX_ORCHESTRA.curie('fixr_concept'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptsV11__fixr_concept, domain=None, range=Optional[Union[Union[dict, OrchestraConceptV11], list[Union[dict, OrchestraConceptV11]]]])

slots.orchestraConceptsV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraConceptsV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptsV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraConceptsV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraConceptsV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraConceptsV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraDatatypeV11__fixr_mapped_datatype = Slot(uri=FIX_ORCHESTRA.fixr_mapped_datatype, name="orchestraDatatypeV11__fixr_mapped_datatype", curie=FIX_ORCHESTRA.curie('fixr_mapped_datatype'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypeV11__fixr_mapped_datatype, domain=None, range=Optional[Union[Union[dict, OrchestraMappedDatatypeV11], list[Union[dict, OrchestraMappedDatatypeV11]]]])

slots.orchestraDatatypeV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraDatatypeV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypeV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraDatatypeV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraDatatypeV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypeV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraDatatypeV11__fixr_base_type = Slot(uri=FIX_ORCHESTRA.fixr_base_type, name="orchestraDatatypeV11__fixr_base_type", curie=FIX_ORCHESTRA.curie('fixr_base_type'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypeV11__fixr_base_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraDatatypesV11__fixr_datatype = Slot(uri=FIX_ORCHESTRA.fixr_datatype, name="orchestraDatatypesV11__fixr_datatype", curie=FIX_ORCHESTRA.curie('fixr_datatype'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypesV11__fixr_datatype, domain=None, range=Optional[Union[Union[dict, OrchestraDatatypeV11], list[Union[dict, OrchestraDatatypeV11]]]])

slots.orchestraDatatypesV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraDatatypesV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypesV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraDatatypesV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraDatatypesV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraDatatypesV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraDocumentationV11__fixr_text = Slot(uri=FIX_ORCHESTRA.fixr_text, name="orchestraDocumentationV11__fixr_text", curie=FIX_ORCHESTRA.curie('fixr_text'),
                   model_uri=FIX_ORCHESTRA.orchestraDocumentationV11__fixr_text, domain=None, range=Optional[str])

slots.orchestraDocumentationV11__fixr_lang_id = Slot(uri=FIX_ORCHESTRA.fixr_lang_id, name="orchestraDocumentationV11__fixr_lang_id", curie=FIX_ORCHESTRA.curie('fixr_lang_id'),
                   model_uri=FIX_ORCHESTRA.orchestraDocumentationV11__fixr_lang_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*$'))

slots.orchestraDocumentationV11__fixr_purpose = Slot(uri=FIX_ORCHESTRA.fixr_purpose, name="orchestraDocumentationV11__fixr_purpose", curie=FIX_ORCHESTRA.curie('fixr_purpose'),
                   model_uri=FIX_ORCHESTRA.orchestraDocumentationV11__fixr_purpose, domain=None, range=Optional[Union[str, "OrchestraPurposeV11"]])

slots.orchestraDocumentationV11__fixr_content_type = Slot(uri=FIX_ORCHESTRA.fixr_content_type, name="orchestraDocumentationV11__fixr_content_type", curie=FIX_ORCHESTRA.curie('fixr_content_type'),
                   model_uri=FIX_ORCHESTRA.orchestraDocumentationV11__fixr_content_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{3,}$'))

slots.orchestraEncodingStandardV11__fixr_encoding = Slot(uri=FIX_ORCHESTRA.fixr_encoding, name="orchestraEncodingStandardV11__fixr_encoding", curie=FIX_ORCHESTRA.curie('fixr_encoding'),
                   model_uri=FIX_ORCHESTRA.orchestraEncodingStandardV11__fixr_encoding, domain=None, range=Optional[Union[dict, OrchestraUnnamedEncodingV11]])

slots.orchestraEncodingStandardV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraEncodingStandardV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraEncodingStandardV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraEncodingStandardV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraEncodingStandardV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraEncodingStandardV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraEncodingStandardV11__fixr_display_name = Slot(uri=FIX_ORCHESTRA.fixr_display_name, name="orchestraEncodingStandardV11__fixr_display_name", curie=FIX_ORCHESTRA.curie('fixr_display_name'),
                   model_uri=FIX_ORCHESTRA.orchestraEncodingStandardV11__fixr_display_name, domain=None, range=Optional[str])

slots.orchestraEncodingStandardsV11__fixr_encoding_standard = Slot(uri=FIX_ORCHESTRA.fixr_encoding_standard, name="orchestraEncodingStandardsV11__fixr_encoding_standard", curie=FIX_ORCHESTRA.curie('fixr_encoding_standard'),
                   model_uri=FIX_ORCHESTRA.orchestraEncodingStandardsV11__fixr_encoding_standard, domain=None, range=Optional[Union[Union[dict, OrchestraEncodingStandardV11], list[Union[dict, OrchestraEncodingStandardV11]]]])

slots.orchestraEncodingStandardsV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraEncodingStandardsV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraEncodingStandardsV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraEncodingsV11__fixr_encoding = Slot(uri=FIX_ORCHESTRA.fixr_encoding, name="orchestraEncodingsV11__fixr_encoding", curie=FIX_ORCHESTRA.curie('fixr_encoding'),
                   model_uri=FIX_ORCHESTRA.orchestraEncodingsV11__fixr_encoding, domain=None, range=Optional[Union[Union[dict, OrchestraNamedEncodingV11], list[Union[dict, OrchestraNamedEncodingV11]]]])

slots.orchestraFieldConstraintsV11Mixin__fixr_min_inclusive = Slot(uri=FIX_ORCHESTRA.fixr_min_inclusive, name="orchestraFieldConstraintsV11Mixin__fixr_min_inclusive", curie=FIX_ORCHESTRA.curie('fixr_min_inclusive'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV11Mixin__fixr_min_inclusive, domain=None, range=Optional[str])

slots.orchestraFieldConstraintsV11Mixin__fixr_max_inclusive = Slot(uri=FIX_ORCHESTRA.fixr_max_inclusive, name="orchestraFieldConstraintsV11Mixin__fixr_max_inclusive", curie=FIX_ORCHESTRA.curie('fixr_max_inclusive'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV11Mixin__fixr_max_inclusive, domain=None, range=Optional[str])

slots.orchestraFieldConstraintsV11Mixin__fixr_impl_length = Slot(uri=FIX_ORCHESTRA.fixr_impl_length, name="orchestraFieldConstraintsV11Mixin__fixr_impl_length", curie=FIX_ORCHESTRA.curie('fixr_impl_length'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV11Mixin__fixr_impl_length, domain=None, range=Optional[int])

slots.orchestraFieldConstraintsV11Mixin__fixr_impl_min_length = Slot(uri=FIX_ORCHESTRA.fixr_impl_min_length, name="orchestraFieldConstraintsV11Mixin__fixr_impl_min_length", curie=FIX_ORCHESTRA.curie('fixr_impl_min_length'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV11Mixin__fixr_impl_min_length, domain=None, range=Optional[int])

slots.orchestraFieldConstraintsV11Mixin__fixr_impl_max_length = Slot(uri=FIX_ORCHESTRA.fixr_impl_max_length, name="orchestraFieldConstraintsV11Mixin__fixr_impl_max_length", curie=FIX_ORCHESTRA.curie('fixr_impl_max_length'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV11Mixin__fixr_impl_max_length, domain=None, range=Optional[int])

slots.orchestraFieldConstraintsV11Mixin__fixr_presence = Slot(uri=FIX_ORCHESTRA.fixr_presence, name="orchestraFieldConstraintsV11Mixin__fixr_presence", curie=FIX_ORCHESTRA.curie('fixr_presence'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV11Mixin__fixr_presence, domain=None, range=Optional[Union[str, "OrchestraPresence"]])

slots.orchestraFieldConstraintsV11Mixin__fixr_encoding = Slot(uri=FIX_ORCHESTRA.fixr_encoding, name="orchestraFieldConstraintsV11Mixin__fixr_encoding", curie=FIX_ORCHESTRA.curie('fixr_encoding'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV11Mixin__fixr_encoding, domain=None, range=Optional[str])

slots.orchestraFieldConstraintsV11Mixin__fixr_value = Slot(uri=FIX_ORCHESTRA.fixr_value, name="orchestraFieldConstraintsV11Mixin__fixr_value", curie=FIX_ORCHESTRA.curie('fixr_value'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV11Mixin__fixr_value, domain=None, range=Optional[str])

slots.orchestraFieldConstraintsV11Mixin__fixr_rendering = Slot(uri=FIX_ORCHESTRA.fixr_rendering, name="orchestraFieldConstraintsV11Mixin__fixr_rendering", curie=FIX_ORCHESTRA.curie('fixr_rendering'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldConstraintsV11Mixin__fixr_rendering, domain=None, range=Optional[str])

slots.orchestraFieldRefV11__fixr_rule = Slot(uri=FIX_ORCHESTRA.fixr_rule, name="orchestraFieldRefV11__fixr_rule", curie=FIX_ORCHESTRA.curie('fixr_rule'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV11__fixr_rule, domain=None, range=Optional[Union[Union[dict, OrchestraFieldRuleV11], list[Union[dict, OrchestraFieldRuleV11]]]])

slots.orchestraFieldRefV11__fixr_assign = Slot(uri=FIX_ORCHESTRA.fixr_assign, name="orchestraFieldRefV11__fixr_assign", curie=FIX_ORCHESTRA.curie('fixr_assign'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV11__fixr_assign, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraFieldRefV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraFieldRefV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraFieldRefV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraFieldRefV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraFieldRefV11__fixr_length_id = Slot(uri=FIX_ORCHESTRA.fixr_length_id, name="orchestraFieldRefV11__fixr_length_id", curie=FIX_ORCHESTRA.curie('fixr_length_id'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV11__fixr_length_id, domain=None, range=Optional[int])

slots.orchestraFieldRefV11__fixr_non_encoded_field_id = Slot(uri=FIX_ORCHESTRA.fixr_non_encoded_field_id, name="orchestraFieldRefV11__fixr_non_encoded_field_id", curie=FIX_ORCHESTRA.curie('fixr_non_encoded_field_id'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV11__fixr_non_encoded_field_id, domain=None, range=Optional[int])

slots.orchestraFieldRefV11__fixr_instance_name = Slot(uri=FIX_ORCHESTRA.fixr_instance_name, name="orchestraFieldRefV11__fixr_instance_name", curie=FIX_ORCHESTRA.curie('fixr_instance_name'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRefV11__fixr_instance_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraFieldRuleV11__fixr_unique = Slot(uri=FIX_ORCHESTRA.fixr_unique, name="orchestraFieldRuleV11__fixr_unique", curie=FIX_ORCHESTRA.curie('fixr_unique'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRuleV11__fixr_unique, domain=None, range=Optional[Union[dict, OrchestraUniqueV11]])

slots.orchestraFieldRuleV11__fixr_assign = Slot(uri=FIX_ORCHESTRA.fixr_assign, name="orchestraFieldRuleV11__fixr_assign", curie=FIX_ORCHESTRA.curie('fixr_assign'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRuleV11__fixr_assign, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraFieldRuleV11__fixr_when = Slot(uri=FIX_ORCHESTRA.fixr_when, name="orchestraFieldRuleV11__fixr_when", curie=FIX_ORCHESTRA.curie('fixr_when'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRuleV11__fixr_when, domain=None, range=str,
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraFieldRuleV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraFieldRuleV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRuleV11__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraFieldRuleV11__fixr_type = Slot(uri=FIX_ORCHESTRA.fixr_type, name="orchestraFieldRuleV11__fixr_type", curie=FIX_ORCHESTRA.curie('fixr_type'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldRuleV11__fixr_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraFieldV11__fixr_rule = Slot(uri=FIX_ORCHESTRA.fixr_rule, name="orchestraFieldV11__fixr_rule", curie=FIX_ORCHESTRA.curie('fixr_rule'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_rule, domain=None, range=Optional[Union[Union[dict, OrchestraFieldRuleV11], list[Union[dict, OrchestraFieldRuleV11]]]])

slots.orchestraFieldV11__fixr_assign = Slot(uri=FIX_ORCHESTRA.fixr_assign, name="orchestraFieldV11__fixr_assign", curie=FIX_ORCHESTRA.curie('fixr_assign'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_assign, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraFieldV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraFieldV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraFieldV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraFieldV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraFieldV11__fixr_type = Slot(uri=FIX_ORCHESTRA.fixr_type, name="orchestraFieldV11__fixr_type", curie=FIX_ORCHESTRA.curie('fixr_type'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraFieldV11__fixr_code_set = Slot(uri=FIX_ORCHESTRA.fixr_code_set, name="orchestraFieldV11__fixr_code_set", curie=FIX_ORCHESTRA.curie('fixr_code_set'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_code_set, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraFieldV11__fixr_length_id = Slot(uri=FIX_ORCHESTRA.fixr_length_id, name="orchestraFieldV11__fixr_length_id", curie=FIX_ORCHESTRA.curie('fixr_length_id'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_length_id, domain=None, range=Optional[int])

slots.orchestraFieldV11__fixr_non_encoded_field_id = Slot(uri=FIX_ORCHESTRA.fixr_non_encoded_field_id, name="orchestraFieldV11__fixr_non_encoded_field_id", curie=FIX_ORCHESTRA.curie('fixr_non_encoded_field_id'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_non_encoded_field_id, domain=None, range=Optional[int])

slots.orchestraFieldV11__fixr_discriminator_id = Slot(uri=FIX_ORCHESTRA.fixr_discriminator_id, name="orchestraFieldV11__fixr_discriminator_id", curie=FIX_ORCHESTRA.curie('fixr_discriminator_id'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_discriminator_id, domain=None, range=Optional[int])

slots.orchestraFieldV11__fixr_base_category = Slot(uri=FIX_ORCHESTRA.fixr_base_category, name="orchestraFieldV11__fixr_base_category", curie=FIX_ORCHESTRA.curie('fixr_base_category'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_base_category, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraFieldV11__fixr_base_category_abbr_name = Slot(uri=FIX_ORCHESTRA.fixr_base_category_abbr_name, name="orchestraFieldV11__fixr_base_category_abbr_name", curie=FIX_ORCHESTRA.curie('fixr_base_category_abbr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_base_category_abbr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraFieldV11__fixr_union_data_type = Slot(uri=FIX_ORCHESTRA.fixr_union_data_type, name="orchestraFieldV11__fixr_union_data_type", curie=FIX_ORCHESTRA.curie('fixr_union_data_type'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldV11__fixr_union_data_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraFieldsV11__fixr_field = Slot(uri=FIX_ORCHESTRA.fixr_field, name="orchestraFieldsV11__fixr_field", curie=FIX_ORCHESTRA.curie('fixr_field'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldsV11__fixr_field, domain=None, range=Optional[Union[Union[dict, OrchestraFieldV11], list[Union[dict, OrchestraFieldV11]]]])

slots.orchestraFieldsV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraFieldsV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldsV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraFieldsV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraFieldsV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraFieldsV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraFlowV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraFlowV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraFlowV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraFlowV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraFlowV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraFlowV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraFlowV11__fixr_source = Slot(uri=FIX_ORCHESTRA.fixr_source, name="orchestraFlowV11__fixr_source", curie=FIX_ORCHESTRA.curie('fixr_source'),
                   model_uri=FIX_ORCHESTRA.orchestraFlowV11__fixr_source, domain=None, range=str)

slots.orchestraFlowV11__fixr_destination = Slot(uri=FIX_ORCHESTRA.fixr_destination, name="orchestraFlowV11__fixr_destination", curie=FIX_ORCHESTRA.curie('fixr_destination'),
                   model_uri=FIX_ORCHESTRA.orchestraFlowV11__fixr_destination, domain=None, range=str)

slots.orchestraFlowV11__fixr_reliability = Slot(uri=FIX_ORCHESTRA.fixr_reliability, name="orchestraFlowV11__fixr_reliability", curie=FIX_ORCHESTRA.curie('fixr_reliability'),
                   model_uri=FIX_ORCHESTRA.orchestraFlowV11__fixr_reliability, domain=None, range=Optional[Union[str, "OrchestraReliability"]])

slots.orchestraGroupRefV11__fixr_impl_min_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_min_occurs, name="orchestraGroupRefV11__fixr_impl_min_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_min_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupRefV11__fixr_impl_min_occurs, domain=None, range=Optional[int])

slots.orchestraGroupRefV11__fixr_impl_max_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_max_occurs, name="orchestraGroupRefV11__fixr_impl_max_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_max_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupRefV11__fixr_impl_max_occurs, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(\d+|unbounded)$'))

slots.orchestraGroupV11__fixr_num_in_group = Slot(uri=FIX_ORCHESTRA.fixr_num_in_group, name="orchestraGroupV11__fixr_num_in_group", curie=FIX_ORCHESTRA.curie('fixr_num_in_group'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV11__fixr_num_in_group, domain=None, range=Optional[Union[dict, OrchestraFieldRefV11]])

slots.orchestraGroupV11__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraGroupV11__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV11__fixr_members, domain=None, range=Optional[Union[Union[dict, OrchestraStructureMemberV11], list[Union[dict, OrchestraStructureMemberV11]]]])

slots.orchestraGroupV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraGroupV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraGroupV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraGroupV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraGroupV11__fixr_category = Slot(uri=FIX_ORCHESTRA.fixr_category, name="orchestraGroupV11__fixr_category", curie=FIX_ORCHESTRA.curie('fixr_category'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV11__fixr_category, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraGroupV11__fixr_rendering = Slot(uri=FIX_ORCHESTRA.fixr_rendering, name="orchestraGroupV11__fixr_rendering", curie=FIX_ORCHESTRA.curie('fixr_rendering'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV11__fixr_rendering, domain=None, range=Optional[str])

slots.orchestraGroupV11__fixr_impl_min_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_min_occurs, name="orchestraGroupV11__fixr_impl_min_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_min_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV11__fixr_impl_min_occurs, domain=None, range=Optional[int])

slots.orchestraGroupV11__fixr_impl_max_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_max_occurs, name="orchestraGroupV11__fixr_impl_max_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_max_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV11__fixr_impl_max_occurs, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(\d+|unbounded)$'))

slots.orchestraGroupV11__fixr_which = Slot(uri=FIX_ORCHESTRA.fixr_which, name="orchestraGroupV11__fixr_which", curie=FIX_ORCHESTRA.curie('fixr_which'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupV11__fixr_which, domain=None, range=Optional[Union[str, "OrchestraMemberSelection"]])

slots.orchestraGroupsV11__fixr_group = Slot(uri=FIX_ORCHESTRA.fixr_group, name="orchestraGroupsV11__fixr_group", curie=FIX_ORCHESTRA.curie('fixr_group'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupsV11__fixr_group, domain=None, range=Optional[Union[Union[dict, OrchestraGroupV11], list[Union[dict, OrchestraGroupV11]]]])

slots.orchestraGroupsV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraGroupsV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupsV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraGroupsV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraGroupsV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupsV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraGroupsV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraGroupsV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraGroupsV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraIdentifierV11__fixr_id = Slot(uri=FIX_ORCHESTRA.fixr_id, name="orchestraIdentifierV11__fixr_id", curie=FIX_ORCHESTRA.curie('fixr_id'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifierV11__fixr_id, domain=None, range=int)

slots.orchestraIdentifierV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraIdentifierV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifierV11__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraIdentifierV11__fixr_source_id = Slot(uri=FIX_ORCHESTRA.fixr_source_id, name="orchestraIdentifierV11__fixr_source_id", curie=FIX_ORCHESTRA.curie('fixr_source_id'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifierV11__fixr_source_id, domain=None, range=Optional[int])

slots.orchestraIdentifiersMemberV11__fixr_correlate = Slot(uri=FIX_ORCHESTRA.fixr_correlate, name="orchestraIdentifiersMemberV11__fixr_correlate", curie=FIX_ORCHESTRA.curie('fixr_correlate'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifiersMemberV11__fixr_correlate, domain=None, range=Optional[Union[dict, OrchestraIdentifierV11]])

slots.orchestraIdentifiersMemberV11__fixr_assign = Slot(uri=FIX_ORCHESTRA.fixr_assign, name="orchestraIdentifiersMemberV11__fixr_assign", curie=FIX_ORCHESTRA.curie('fixr_assign'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifiersMemberV11__fixr_assign, domain=None, range=Optional[Union[dict, OrchestraIdentifierV11]])

slots.orchestraIdentifiersV11__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraIdentifiersV11__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifiersV11__fixr_members, domain=None, range=Union[Union[dict, OrchestraIdentifiersMemberV11], list[Union[dict, OrchestraIdentifiersMemberV11]]])

slots.orchestraIdentifiersV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraIdentifiersV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentifiersV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraIdentityV11Mixin__fixr_id = Slot(uri=FIX_ORCHESTRA.fixr_id, name="orchestraIdentityV11Mixin__fixr_id", curie=FIX_ORCHESTRA.curie('fixr_id'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentityV11Mixin__fixr_id, domain=None, range=int)

slots.orchestraIdentityV11Mixin__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraIdentityV11Mixin__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentityV11Mixin__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraIdentityV11Mixin__fixr_abbr_name = Slot(uri=FIX_ORCHESTRA.fixr_abbr_name, name="orchestraIdentityV11Mixin__fixr_abbr_name", curie=FIX_ORCHESTRA.curie('fixr_abbr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentityV11Mixin__fixr_abbr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraIdentityV11Mixin__fixr_scenario = Slot(uri=FIX_ORCHESTRA.fixr_scenario, name="orchestraIdentityV11Mixin__fixr_scenario", curie=FIX_ORCHESTRA.curie('fixr_scenario'),
                   model_uri=FIX_ORCHESTRA.orchestraIdentityV11Mixin__fixr_scenario, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraInterfaceAnnotationMemberV11__fixi_documentation = Slot(uri=FIX_ORCHESTRA.fixi_documentation, name="orchestraInterfaceAnnotationMemberV11__fixi_documentation", curie=FIX_ORCHESTRA.curie('fixi_documentation'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAnnotationMemberV11__fixi_documentation, domain=None, range=Optional[Union[dict, OrchestraInterfaceDocumentationV11]])

slots.orchestraInterfaceAnnotationMemberV11__fixi_appinfo = Slot(uri=FIX_ORCHESTRA.fixi_appinfo, name="orchestraInterfaceAnnotationMemberV11__fixi_appinfo", curie=FIX_ORCHESTRA.curie('fixi_appinfo'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAnnotationMemberV11__fixi_appinfo, domain=None, range=Optional[Union[dict, OrchestraInterfaceAppinfoV11]])

slots.orchestraInterfaceAnnotationV11__fixi_members = Slot(uri=FIX_ORCHESTRA.fixi_members, name="orchestraInterfaceAnnotationV11__fixi_members", curie=FIX_ORCHESTRA.curie('fixi_members'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAnnotationV11__fixi_members, domain=None, range=Union[Union[dict, OrchestraInterfaceAnnotationMemberV11], list[Union[dict, OrchestraInterfaceAnnotationMemberV11]]])

slots.orchestraInterfaceAppinfoV11__fixi_text = Slot(uri=FIX_ORCHESTRA.fixi_text, name="orchestraInterfaceAppinfoV11__fixi_text", curie=FIX_ORCHESTRA.curie('fixi_text'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV11__fixi_text, domain=None, range=Optional[str])

slots.orchestraInterfaceAppinfoV11__fixi_any = Slot(uri=FIX_ORCHESTRA.fixi_any, name="orchestraInterfaceAppinfoV11__fixi_any", curie=FIX_ORCHESTRA.curie('fixi_any'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV11__fixi_any, domain=None, range=Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]])

slots.orchestraInterfaceAppinfoV11__fixi_spec_url = Slot(uri=FIX_ORCHESTRA.fixi_spec_url, name="orchestraInterfaceAppinfoV11__fixi_spec_url", curie=FIX_ORCHESTRA.curie('fixi_spec_url'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV11__fixi_spec_url, domain=None, range=Optional[Union[str, URI]])

slots.orchestraInterfaceAppinfoV11__fixi_lang_id = Slot(uri=FIX_ORCHESTRA.fixi_lang_id, name="orchestraInterfaceAppinfoV11__fixi_lang_id", curie=FIX_ORCHESTRA.curie('fixi_lang_id'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV11__fixi_lang_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*$'))

slots.orchestraInterfaceAppinfoV11__fixi_purpose = Slot(uri=FIX_ORCHESTRA.fixi_purpose, name="orchestraInterfaceAppinfoV11__fixi_purpose", curie=FIX_ORCHESTRA.curie('fixi_purpose'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV11__fixi_purpose, domain=None, range=Optional[Union[str, "OrchestraPurpose"]])

slots.orchestraInterfaceAppinfoV11__fixi_other_attributes = Slot(uri=FIX_ORCHESTRA.fixi_other_attributes, name="orchestraInterfaceAppinfoV11__fixi_other_attributes", curie=FIX_ORCHESTRA.curie('fixi_other_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceAppinfoV11__fixi_other_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraInterfaceDocumentationV11__fixi_text = Slot(uri=FIX_ORCHESTRA.fixi_text, name="orchestraInterfaceDocumentationV11__fixi_text", curie=FIX_ORCHESTRA.curie('fixi_text'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceDocumentationV11__fixi_text, domain=None, range=Optional[str])

slots.orchestraInterfaceDocumentationV11__fixi_any = Slot(uri=FIX_ORCHESTRA.fixi_any, name="orchestraInterfaceDocumentationV11__fixi_any", curie=FIX_ORCHESTRA.curie('fixi_any'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceDocumentationV11__fixi_any, domain=None, range=Optional[Union[Union[dict, OrchestraXmlElement], list[Union[dict, OrchestraXmlElement]]]])

slots.orchestraInterfaceDocumentationV11__fixi_lang_id = Slot(uri=FIX_ORCHESTRA.fixi_lang_id, name="orchestraInterfaceDocumentationV11__fixi_lang_id", curie=FIX_ORCHESTRA.curie('fixi_lang_id'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceDocumentationV11__fixi_lang_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z]{1,8}(-[A-Za-z0-9]{1,8})*$'))

slots.orchestraInterfaceDocumentationV11__fixi_purpose = Slot(uri=FIX_ORCHESTRA.fixi_purpose, name="orchestraInterfaceDocumentationV11__fixi_purpose", curie=FIX_ORCHESTRA.curie('fixi_purpose'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceDocumentationV11__fixi_purpose, domain=None, range=Optional[Union[str, "OrchestraPurpose"]])

slots.orchestraInterfaceDocumentationV11__fixi_content_type = Slot(uri=FIX_ORCHESTRA.fixi_content_type, name="orchestraInterfaceDocumentationV11__fixi_content_type", curie=FIX_ORCHESTRA.curie('fixi_content_type'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceDocumentationV11__fixi_content_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)?$'))

slots.orchestraInterfaceV11__fixi_sessions = Slot(uri=FIX_ORCHESTRA.fixi_sessions, name="orchestraInterfaceV11__fixi_sessions", curie=FIX_ORCHESTRA.curie('fixi_sessions'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfaceV11__fixi_sessions, domain=None, range=Optional[Union[dict, OrchestraSessionsV11]])

slots.orchestraInterfacesV11__fixi_metadata = Slot(uri=FIX_ORCHESTRA.fixi_metadata, name="orchestraInterfacesV11__fixi_metadata", curie=FIX_ORCHESTRA.curie('fixi_metadata'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfacesV11__fixi_metadata, domain=None, range=Union[dict, OrchestraMetadata])

slots.orchestraInterfacesV11__fixi_interface = Slot(uri=FIX_ORCHESTRA.fixi_interface, name="orchestraInterfacesV11__fixi_interface", curie=FIX_ORCHESTRA.curie('fixi_interface'),
                   model_uri=FIX_ORCHESTRA.orchestraInterfacesV11__fixi_interface, domain=None, range=Optional[Union[Union[dict, OrchestraInterfaceV11], list[Union[dict, OrchestraInterfaceV11]]]])

slots.orchestraMappedDatatypeV11__fixr_encoding = Slot(uri=FIX_ORCHESTRA.fixr_encoding, name="orchestraMappedDatatypeV11__fixr_encoding", curie=FIX_ORCHESTRA.curie('fixr_encoding'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_encoding, domain=None, range=Optional[Union[dict, OrchestraUnnamedEncodingV11]])

slots.orchestraMappedDatatypeV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraMappedDatatypeV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraMappedDatatypeV11__fixr_standard = Slot(uri=FIX_ORCHESTRA.fixr_standard, name="orchestraMappedDatatypeV11__fixr_standard", curie=FIX_ORCHESTRA.curie('fixr_standard'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_standard, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraMappedDatatypeV11__fixr_builtin = Slot(uri=FIX_ORCHESTRA.fixr_builtin, name="orchestraMappedDatatypeV11__fixr_builtin", curie=FIX_ORCHESTRA.curie('fixr_builtin'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_builtin, domain=None, range=Optional[Union[bool, Bool]])

slots.orchestraMappedDatatypeV11__fixr_base = Slot(uri=FIX_ORCHESTRA.fixr_base, name="orchestraMappedDatatypeV11__fixr_base", curie=FIX_ORCHESTRA.curie('fixr_base'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_base, domain=None, range=Optional[str])

slots.orchestraMappedDatatypeV11__fixr_pattern = Slot(uri=FIX_ORCHESTRA.fixr_pattern, name="orchestraMappedDatatypeV11__fixr_pattern", curie=FIX_ORCHESTRA.curie('fixr_pattern'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_pattern, domain=None, range=Optional[str])

slots.orchestraMappedDatatypeV11__fixr_element = Slot(uri=FIX_ORCHESTRA.fixr_element, name="orchestraMappedDatatypeV11__fixr_element", curie=FIX_ORCHESTRA.curie('fixr_element'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_element, domain=None, range=Optional[str])

slots.orchestraMappedDatatypeV11__fixr_size = Slot(uri=FIX_ORCHESTRA.fixr_size, name="orchestraMappedDatatypeV11__fixr_size", curie=FIX_ORCHESTRA.curie('fixr_size'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_size, domain=None, range=Optional[int])

slots.orchestraMappedDatatypeV11__fixr_parameter = Slot(uri=FIX_ORCHESTRA.fixr_parameter, name="orchestraMappedDatatypeV11__fixr_parameter", curie=FIX_ORCHESTRA.curie('fixr_parameter'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_parameter, domain=None, range=Optional[str])

slots.orchestraMappedDatatypeV11__fixr_min_inclusive = Slot(uri=FIX_ORCHESTRA.fixr_min_inclusive, name="orchestraMappedDatatypeV11__fixr_min_inclusive", curie=FIX_ORCHESTRA.curie('fixr_min_inclusive'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_min_inclusive, domain=None, range=Optional[str])

slots.orchestraMappedDatatypeV11__fixr_max_inclusive = Slot(uri=FIX_ORCHESTRA.fixr_max_inclusive, name="orchestraMappedDatatypeV11__fixr_max_inclusive", curie=FIX_ORCHESTRA.curie('fixr_max_inclusive'),
                   model_uri=FIX_ORCHESTRA.orchestraMappedDatatypeV11__fixr_max_inclusive, domain=None, range=Optional[str])

slots.orchestraMessageRefV11__fixr_identifiers = Slot(uri=FIX_ORCHESTRA.fixr_identifiers, name="orchestraMessageRefV11__fixr_identifiers", curie=FIX_ORCHESTRA.curie('fixr_identifiers'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageRefV11__fixr_identifiers, domain=None, range=Optional[Union[dict, OrchestraIdentifiersV11]])

slots.orchestraMessageRefV11__fixr_msg_type = Slot(uri=FIX_ORCHESTRA.fixr_msg_type, name="orchestraMessageRefV11__fixr_msg_type", curie=FIX_ORCHESTRA.curie('fixr_msg_type'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageRefV11__fixr_msg_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,6}$'))

slots.orchestraMessageRefV11__fixr_impl_min_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_min_occurs, name="orchestraMessageRefV11__fixr_impl_min_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_min_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageRefV11__fixr_impl_min_occurs, domain=None, range=Optional[int])

slots.orchestraMessageRefV11__fixr_impl_max_occurs = Slot(uri=FIX_ORCHESTRA.fixr_impl_max_occurs, name="orchestraMessageRefV11__fixr_impl_max_occurs", curie=FIX_ORCHESTRA.curie('fixr_impl_max_occurs'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageRefV11__fixr_impl_max_occurs, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(\d+|unbounded)$'))

slots.orchestraMessageStructureV11__fixr_members = Slot(uri=FIX_ORCHESTRA.fixr_members, name="orchestraMessageStructureV11__fixr_members", curie=FIX_ORCHESTRA.curie('fixr_members'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageStructureV11__fixr_members, domain=None, range=Optional[Union[Union[dict, OrchestraStructureMemberV11], list[Union[dict, OrchestraStructureMemberV11]]]])

slots.orchestraMessageStructureV11__fixr_which = Slot(uri=FIX_ORCHESTRA.fixr_which, name="orchestraMessageStructureV11__fixr_which", curie=FIX_ORCHESTRA.curie('fixr_which'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageStructureV11__fixr_which, domain=None, range=Optional[Union[str, "OrchestraMemberSelection"]])

slots.orchestraMessageV11__fixr_structure = Slot(uri=FIX_ORCHESTRA.fixr_structure, name="orchestraMessageV11__fixr_structure", curie=FIX_ORCHESTRA.curie('fixr_structure'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV11__fixr_structure, domain=None, range=Optional[Union[dict, OrchestraMessageStructureV11]])

slots.orchestraMessageV11__fixr_when = Slot(uri=FIX_ORCHESTRA.fixr_when, name="orchestraMessageV11__fixr_when", curie=FIX_ORCHESTRA.curie('fixr_when'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV11__fixr_when, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraMessageV11__fixr_responses = Slot(uri=FIX_ORCHESTRA.fixr_responses, name="orchestraMessageV11__fixr_responses", curie=FIX_ORCHESTRA.curie('fixr_responses'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV11__fixr_responses, domain=None, range=Optional[Union[dict, OrchestraResponsesV11]])

slots.orchestraMessageV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraMessageV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraMessageV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraMessageV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraMessageV11__fixr_msg_type = Slot(uri=FIX_ORCHESTRA.fixr_msg_type, name="orchestraMessageV11__fixr_msg_type", curie=FIX_ORCHESTRA.curie('fixr_msg_type'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV11__fixr_msg_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,6}$'))

slots.orchestraMessageV11__fixr_category = Slot(uri=FIX_ORCHESTRA.fixr_category, name="orchestraMessageV11__fixr_category", curie=FIX_ORCHESTRA.curie('fixr_category'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV11__fixr_category, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraMessageV11__fixr_flow = Slot(uri=FIX_ORCHESTRA.fixr_flow, name="orchestraMessageV11__fixr_flow", curie=FIX_ORCHESTRA.curie('fixr_flow'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV11__fixr_flow, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraMessageV11__fixr_rendering = Slot(uri=FIX_ORCHESTRA.fixr_rendering, name="orchestraMessageV11__fixr_rendering", curie=FIX_ORCHESTRA.curie('fixr_rendering'),
                   model_uri=FIX_ORCHESTRA.orchestraMessageV11__fixr_rendering, domain=None, range=Optional[str])

slots.orchestraMessagesV11__fixr_message = Slot(uri=FIX_ORCHESTRA.fixr_message, name="orchestraMessagesV11__fixr_message", curie=FIX_ORCHESTRA.curie('fixr_message'),
                   model_uri=FIX_ORCHESTRA.orchestraMessagesV11__fixr_message, domain=None, range=Optional[Union[Union[dict, OrchestraMessageV11], list[Union[dict, OrchestraMessageV11]]]])

slots.orchestraMessagesV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraMessagesV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraMessagesV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraMessagesV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraMessagesV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraMessagesV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraMessagesV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraMessagesV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraMessagesV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraNamedEncodingV11__fixr_standard = Slot(uri=FIX_ORCHESTRA.fixr_standard, name="orchestraNamedEncodingV11__fixr_standard", curie=FIX_ORCHESTRA.curie('fixr_standard'),
                   model_uri=FIX_ORCHESTRA.orchestraNamedEncodingV11__fixr_standard, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraPedigreeV11Mixin__fixr_added = Slot(uri=FIX_ORCHESTRA.fixr_added, name="orchestraPedigreeV11Mixin__fixr_added", curie=FIX_ORCHESTRA.curie('fixr_added'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_added, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraPedigreeV11Mixin__fixr_added_ep = Slot(uri=FIX_ORCHESTRA.fixr_added_ep, name="orchestraPedigreeV11Mixin__fixr_added_ep", curie=FIX_ORCHESTRA.curie('fixr_added_ep'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_added_ep, domain=None, range=Optional[int])

slots.orchestraPedigreeV11Mixin__fixr_change_type = Slot(uri=FIX_ORCHESTRA.fixr_change_type, name="orchestraPedigreeV11Mixin__fixr_change_type", curie=FIX_ORCHESTRA.curie('fixr_change_type'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_change_type, domain=None, range=Optional[Union[str, "OrchestraChangeKind"]])

slots.orchestraPedigreeV11Mixin__fixr_deprecated = Slot(uri=FIX_ORCHESTRA.fixr_deprecated, name="orchestraPedigreeV11Mixin__fixr_deprecated", curie=FIX_ORCHESTRA.curie('fixr_deprecated'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_deprecated, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraPedigreeV11Mixin__fixr_deprecated_ep = Slot(uri=FIX_ORCHESTRA.fixr_deprecated_ep, name="orchestraPedigreeV11Mixin__fixr_deprecated_ep", curie=FIX_ORCHESTRA.curie('fixr_deprecated_ep'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_deprecated_ep, domain=None, range=Optional[int])

slots.orchestraPedigreeV11Mixin__fixr_issue = Slot(uri=FIX_ORCHESTRA.fixr_issue, name="orchestraPedigreeV11Mixin__fixr_issue", curie=FIX_ORCHESTRA.curie('fixr_issue'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_issue, domain=None, range=Optional[str])

slots.orchestraPedigreeV11Mixin__fixr_last_modified = Slot(uri=FIX_ORCHESTRA.fixr_last_modified, name="orchestraPedigreeV11Mixin__fixr_last_modified", curie=FIX_ORCHESTRA.curie('fixr_last_modified'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_last_modified, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraPedigreeV11Mixin__fixr_replaced = Slot(uri=FIX_ORCHESTRA.fixr_replaced, name="orchestraPedigreeV11Mixin__fixr_replaced", curie=FIX_ORCHESTRA.curie('fixr_replaced'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_replaced, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraPedigreeV11Mixin__fixr_replaced_ep = Slot(uri=FIX_ORCHESTRA.fixr_replaced_ep, name="orchestraPedigreeV11Mixin__fixr_replaced_ep", curie=FIX_ORCHESTRA.curie('fixr_replaced_ep'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_replaced_ep, domain=None, range=Optional[int])

slots.orchestraPedigreeV11Mixin__fixr_replaced_by_field = Slot(uri=FIX_ORCHESTRA.fixr_replaced_by_field, name="orchestraPedigreeV11Mixin__fixr_replaced_by_field", curie=FIX_ORCHESTRA.curie('fixr_replaced_by_field'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_replaced_by_field, domain=None, range=Optional[int])

slots.orchestraPedigreeV11Mixin__fixr_supported = Slot(uri=FIX_ORCHESTRA.fixr_supported, name="orchestraPedigreeV11Mixin__fixr_supported", curie=FIX_ORCHESTRA.curie('fixr_supported'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_supported, domain=None, range=Optional[Union[str, "OrchestraSupport"]])

slots.orchestraPedigreeV11Mixin__fixr_updated = Slot(uri=FIX_ORCHESTRA.fixr_updated, name="orchestraPedigreeV11Mixin__fixr_updated", curie=FIX_ORCHESTRA.curie('fixr_updated'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_updated, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraPedigreeV11Mixin__fixr_updated_ep = Slot(uri=FIX_ORCHESTRA.fixr_updated_ep, name="orchestraPedigreeV11Mixin__fixr_updated_ep", curie=FIX_ORCHESTRA.curie('fixr_updated_ep'),
                   model_uri=FIX_ORCHESTRA.orchestraPedigreeV11Mixin__fixr_updated_ep, domain=None, range=Optional[int])

slots.orchestraProtocolV11__fixi_annotation = Slot(uri=FIX_ORCHESTRA.fixi_annotation, name="orchestraProtocolV11__fixi_annotation", curie=FIX_ORCHESTRA.curie('fixi_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV11__fixi_annotation, domain=None, range=Optional[Union[dict, OrchestraInterfaceAnnotationV11]])

slots.orchestraProtocolV11__fixi_name = Slot(uri=FIX_ORCHESTRA.fixi_name, name="orchestraProtocolV11__fixi_name", curie=FIX_ORCHESTRA.curie('fixi_name'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV11__fixi_name, domain=None, range=Optional[Union[str, "OrchestraProtocolName"]])

slots.orchestraProtocolV11__fixi_version = Slot(uri=FIX_ORCHESTRA.fixi_version, name="orchestraProtocolV11__fixi_version", curie=FIX_ORCHESTRA.curie('fixi_version'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV11__fixi_version, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)?$'))

slots.orchestraProtocolV11__fixi_activation_time = Slot(uri=FIX_ORCHESTRA.fixi_activation_time, name="orchestraProtocolV11__fixi_activation_time", curie=FIX_ORCHESTRA.curie('fixi_activation_time'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV11__fixi_activation_time, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?\d{4,}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$'))

slots.orchestraProtocolV11__fixi_deactivation_time = Slot(uri=FIX_ORCHESTRA.fixi_deactivation_time, name="orchestraProtocolV11__fixi_deactivation_time", curie=FIX_ORCHESTRA.curie('fixi_deactivation_time'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV11__fixi_deactivation_time, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?\d{4,}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$'))

slots.orchestraProtocolV11__fixi_deprecated = Slot(uri=FIX_ORCHESTRA.fixi_deprecated, name="orchestraProtocolV11__fixi_deprecated", curie=FIX_ORCHESTRA.curie('fixi_deprecated'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV11__fixi_deprecated, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?\d{4,}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$'))

slots.orchestraProtocolV11__fixi_layer = Slot(uri=FIX_ORCHESTRA.fixi_layer, name="orchestraProtocolV11__fixi_layer", curie=FIX_ORCHESTRA.curie('fixi_layer'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV11__fixi_layer, domain=None, range=Optional[Union[str, "OrchestraLayer"]])

slots.orchestraProtocolV11__fixi_reliability = Slot(uri=FIX_ORCHESTRA.fixi_reliability, name="orchestraProtocolV11__fixi_reliability", curie=FIX_ORCHESTRA.curie('fixi_reliability'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV11__fixi_reliability, domain=None, range=Optional[Union[str, "OrchestraReliability"]])

slots.orchestraProtocolV11__fixi_orchestration = Slot(uri=FIX_ORCHESTRA.fixi_orchestration, name="orchestraProtocolV11__fixi_orchestration", curie=FIX_ORCHESTRA.curie('fixi_orchestration'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV11__fixi_orchestration, domain=None, range=Optional[Union[str, URI]])

slots.orchestraProtocolV11__fixi_other_attributes = Slot(uri=FIX_ORCHESTRA.fixi_other_attributes, name="orchestraProtocolV11__fixi_other_attributes", curie=FIX_ORCHESTRA.curie('fixi_other_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraProtocolV11__fixi_other_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraReferenceV11Mixin__fixr_id = Slot(uri=FIX_ORCHESTRA.fixr_id, name="orchestraReferenceV11Mixin__fixr_id", curie=FIX_ORCHESTRA.curie('fixr_id'),
                   model_uri=FIX_ORCHESTRA.orchestraReferenceV11Mixin__fixr_id, domain=None, range=int)

slots.orchestraReferenceV11Mixin__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraReferenceV11Mixin__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraReferenceV11Mixin__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraReferenceV11Mixin__fixr_scenario = Slot(uri=FIX_ORCHESTRA.fixr_scenario, name="orchestraReferenceV11Mixin__fixr_scenario", curie=FIX_ORCHESTRA.curie('fixr_scenario'),
                   model_uri=FIX_ORCHESTRA.orchestraReferenceV11Mixin__fixr_scenario, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraRepositoryV11__fixr_metadata = Slot(uri=FIX_ORCHESTRA.fixr_metadata, name="orchestraRepositoryV11__fixr_metadata", curie=FIX_ORCHESTRA.curie('fixr_metadata'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_metadata, domain=None, range=Union[dict, OrchestraMetadata])

slots.orchestraRepositoryV11__fixr_categories = Slot(uri=FIX_ORCHESTRA.fixr_categories, name="orchestraRepositoryV11__fixr_categories", curie=FIX_ORCHESTRA.curie('fixr_categories'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_categories, domain=None, range=Optional[Union[dict, OrchestraCategoriesV11]])

slots.orchestraRepositoryV11__fixr_sections = Slot(uri=FIX_ORCHESTRA.fixr_sections, name="orchestraRepositoryV11__fixr_sections", curie=FIX_ORCHESTRA.curie('fixr_sections'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_sections, domain=None, range=Optional[Union[dict, OrchestraSectionsV11]])

slots.orchestraRepositoryV11__fixr_encoding_standards = Slot(uri=FIX_ORCHESTRA.fixr_encoding_standards, name="orchestraRepositoryV11__fixr_encoding_standards", curie=FIX_ORCHESTRA.curie('fixr_encoding_standards'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_encoding_standards, domain=None, range=Optional[Union[dict, OrchestraEncodingStandardsV11]])

slots.orchestraRepositoryV11__fixr_datatypes = Slot(uri=FIX_ORCHESTRA.fixr_datatypes, name="orchestraRepositoryV11__fixr_datatypes", curie=FIX_ORCHESTRA.curie('fixr_datatypes'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_datatypes, domain=None, range=Optional[Union[dict, OrchestraDatatypesV11]])

slots.orchestraRepositoryV11__fixr_code_sets = Slot(uri=FIX_ORCHESTRA.fixr_code_sets, name="orchestraRepositoryV11__fixr_code_sets", curie=FIX_ORCHESTRA.curie('fixr_code_sets'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_code_sets, domain=None, range=Optional[Union[dict, OrchestraCodeSetsV11]])

slots.orchestraRepositoryV11__fixr_fields = Slot(uri=FIX_ORCHESTRA.fixr_fields, name="orchestraRepositoryV11__fixr_fields", curie=FIX_ORCHESTRA.curie('fixr_fields'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_fields, domain=None, range=Optional[Union[dict, OrchestraFieldsV11]])

slots.orchestraRepositoryV11__fixr_actors = Slot(uri=FIX_ORCHESTRA.fixr_actors, name="orchestraRepositoryV11__fixr_actors", curie=FIX_ORCHESTRA.curie('fixr_actors'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_actors, domain=None, range=Optional[Union[dict, OrchestraActorsV11]])

slots.orchestraRepositoryV11__fixr_components = Slot(uri=FIX_ORCHESTRA.fixr_components, name="orchestraRepositoryV11__fixr_components", curie=FIX_ORCHESTRA.curie('fixr_components'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_components, domain=None, range=Optional[Union[dict, OrchestraComponentsV11]])

slots.orchestraRepositoryV11__fixr_groups = Slot(uri=FIX_ORCHESTRA.fixr_groups, name="orchestraRepositoryV11__fixr_groups", curie=FIX_ORCHESTRA.curie('fixr_groups'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_groups, domain=None, range=Optional[Union[dict, OrchestraGroupsV11]])

slots.orchestraRepositoryV11__fixr_messages = Slot(uri=FIX_ORCHESTRA.fixr_messages, name="orchestraRepositoryV11__fixr_messages", curie=FIX_ORCHESTRA.curie('fixr_messages'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_messages, domain=None, range=Optional[Union[dict, OrchestraMessagesV11]])

slots.orchestraRepositoryV11__fixr_concepts = Slot(uri=FIX_ORCHESTRA.fixr_concepts, name="orchestraRepositoryV11__fixr_concepts", curie=FIX_ORCHESTRA.curie('fixr_concepts'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_concepts, domain=None, range=Optional[Union[dict, OrchestraConceptsV11]])

slots.orchestraRepositoryV11__fixr_scenarios = Slot(uri=FIX_ORCHESTRA.fixr_scenarios, name="orchestraRepositoryV11__fixr_scenarios", curie=FIX_ORCHESTRA.curie('fixr_scenarios'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_scenarios, domain=None, range=Optional[Union[dict, OrchestraScenariosV11]])

slots.orchestraRepositoryV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraRepositoryV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraRepositoryV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraRepositoryV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_name, domain=None, range=str)

slots.orchestraRepositoryV11__fixr_version = Slot(uri=FIX_ORCHESTRA.fixr_version, name="orchestraRepositoryV11__fixr_version", curie=FIX_ORCHESTRA.curie('fixr_version'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_version, domain=None, range=str,
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraRepositoryV11__fixr_guid = Slot(uri=FIX_ORCHESTRA.fixr_guid, name="orchestraRepositoryV11__fixr_guid", curie=FIX_ORCHESTRA.curie('fixr_guid'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_guid, domain=None, range=Optional[str])

slots.orchestraRepositoryV11__fixr_spec_url = Slot(uri=FIX_ORCHESTRA.fixr_spec_url, name="orchestraRepositoryV11__fixr_spec_url", curie=FIX_ORCHESTRA.curie('fixr_spec_url'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_spec_url, domain=None, range=Optional[Union[str, URI]])

slots.orchestraRepositoryV11__fixr_namespace = Slot(uri=FIX_ORCHESTRA.fixr_namespace, name="orchestraRepositoryV11__fixr_namespace", curie=FIX_ORCHESTRA.curie('fixr_namespace'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_namespace, domain=None, range=Optional[Union[str, URI]])

slots.orchestraRepositoryV11__fixr_expression_language = Slot(uri=FIX_ORCHESTRA.fixr_expression_language, name="orchestraRepositoryV11__fixr_expression_language", curie=FIX_ORCHESTRA.curie('fixr_expression_language'),
                   model_uri=FIX_ORCHESTRA.orchestraRepositoryV11__fixr_expression_language, domain=None, range=Optional[str])

slots.orchestraResponseV11__fixr_when = Slot(uri=FIX_ORCHESTRA.fixr_when, name="orchestraResponseV11__fixr_when", curie=FIX_ORCHESTRA.curie('fixr_when'),
                   model_uri=FIX_ORCHESTRA.orchestraResponseV11__fixr_when, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraResponseV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraResponseV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraResponseV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraResponseV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraResponseV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraResponseV11__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraResponseV11__fixr_sync = Slot(uri=FIX_ORCHESTRA.fixr_sync, name="orchestraResponseV11__fixr_sync", curie=FIX_ORCHESTRA.curie('fixr_sync'),
                   model_uri=FIX_ORCHESTRA.orchestraResponseV11__fixr_sync, domain=None, range=Optional[Union[str, "OrchestraSynchronization"]])

slots.orchestraResponsesV11__fixr_response = Slot(uri=FIX_ORCHESTRA.fixr_response, name="orchestraResponsesV11__fixr_response", curie=FIX_ORCHESTRA.curie('fixr_response'),
                   model_uri=FIX_ORCHESTRA.orchestraResponsesV11__fixr_response, domain=None, range=Union[Union[dict, OrchestraResponseV11], list[Union[dict, OrchestraResponseV11]]])

slots.orchestraScenarioReferenceV11Mixin__fixr_scenario_ref_id = Slot(uri=FIX_ORCHESTRA.fixr_scenario_ref_id, name="orchestraScenarioReferenceV11Mixin__fixr_scenario_ref_id", curie=FIX_ORCHESTRA.curie('fixr_scenario_ref_id'),
                   model_uri=FIX_ORCHESTRA.orchestraScenarioReferenceV11Mixin__fixr_scenario_ref_id, domain=None, range=Optional[int])

slots.orchestraScenarioReferenceV11Mixin__fixr_scenario_ref = Slot(uri=FIX_ORCHESTRA.fixr_scenario_ref, name="orchestraScenarioReferenceV11Mixin__fixr_scenario_ref", curie=FIX_ORCHESTRA.curie('fixr_scenario_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraScenarioReferenceV11Mixin__fixr_scenario_ref, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraScenarioV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraScenarioV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraScenarioV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraScenarioV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraScenarioV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraScenarioV11__fixr_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraScenariosV11__fixr_scenario = Slot(uri=FIX_ORCHESTRA.fixr_scenario, name="orchestraScenariosV11__fixr_scenario", curie=FIX_ORCHESTRA.curie('fixr_scenario'),
                   model_uri=FIX_ORCHESTRA.orchestraScenariosV11__fixr_scenario, domain=None, range=Optional[Union[Union[dict, OrchestraScenarioV11], list[Union[dict, OrchestraScenarioV11]]]])

slots.orchestraScenariosV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraScenariosV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraScenariosV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraScenariosV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraScenariosV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraScenariosV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraSectionV11__fixr_encodings = Slot(uri=FIX_ORCHESTRA.fixr_encodings, name="orchestraSectionV11__fixr_encodings", curie=FIX_ORCHESTRA.curie('fixr_encodings'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionV11__fixr_encodings, domain=None, range=Optional[Union[dict, OrchestraEncodingsV11]])

slots.orchestraSectionV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraSectionV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraSectionV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraSectionV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraSectionV11__fixr_display_order = Slot(uri=FIX_ORCHESTRA.fixr_display_order, name="orchestraSectionV11__fixr_display_order", curie=FIX_ORCHESTRA.curie('fixr_display_order'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionV11__fixr_display_order, domain=None, range=Optional[int])

slots.orchestraSectionsV11__fixr_section = Slot(uri=FIX_ORCHESTRA.fixr_section, name="orchestraSectionsV11__fixr_section", curie=FIX_ORCHESTRA.curie('fixr_section'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionsV11__fixr_section, domain=None, range=Optional[Union[Union[dict, OrchestraSectionV11], list[Union[dict, OrchestraSectionV11]]]])

slots.orchestraSectionsV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraSectionsV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionsV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraSectionsV11__xml_base = Slot(uri=FIX_ORCHESTRA.xml_base, name="orchestraSectionsV11__xml_base", curie=FIX_ORCHESTRA.curie('xml_base'),
                   model_uri=FIX_ORCHESTRA.orchestraSectionsV11__xml_base, domain=None, range=Optional[Union[str, URI]])

slots.orchestraSessionIdentifierV11__fixi_text = Slot(uri=FIX_ORCHESTRA.fixi_text, name="orchestraSessionIdentifierV11__fixi_text", curie=FIX_ORCHESTRA.curie('fixi_text'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionIdentifierV11__fixi_text, domain=None, range=Optional[str])

slots.orchestraSessionIdentifierV11__fixi_name = Slot(uri=FIX_ORCHESTRA.fixi_name, name="orchestraSessionIdentifierV11__fixi_name", curie=FIX_ORCHESTRA.curie('fixi_name'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionIdentifierV11__fixi_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)?$'))

slots.orchestraSessionV11__fixi_identifier = Slot(uri=FIX_ORCHESTRA.fixi_identifier, name="orchestraSessionV11__fixi_identifier", curie=FIX_ORCHESTRA.curie('fixi_identifier'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionV11__fixi_identifier, domain=None, range=Optional[Union[Union[dict, OrchestraSessionIdentifierV11], list[Union[dict, OrchestraSessionIdentifierV11]]]])

slots.orchestraSessionV11__fixi_role = Slot(uri=FIX_ORCHESTRA.fixi_role, name="orchestraSessionV11__fixi_role", curie=FIX_ORCHESTRA.curie('fixi_role'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionV11__fixi_role, domain=None, range=Optional[Union[str, "OrchestraRole"]])

slots.orchestraSessionV11__fixi_security_keys = Slot(uri=FIX_ORCHESTRA.fixi_security_keys, name="orchestraSessionV11__fixi_security_keys", curie=FIX_ORCHESTRA.curie('fixi_security_keys'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionV11__fixi_security_keys, domain=None, range=Optional[str])

slots.orchestraSessionV11__fixi_activation_time = Slot(uri=FIX_ORCHESTRA.fixi_activation_time, name="orchestraSessionV11__fixi_activation_time", curie=FIX_ORCHESTRA.curie('fixi_activation_time'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionV11__fixi_activation_time, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?\d{4,}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$'))

slots.orchestraSessionV11__fixi_deactivation_time = Slot(uri=FIX_ORCHESTRA.fixi_deactivation_time, name="orchestraSessionV11__fixi_deactivation_time", curie=FIX_ORCHESTRA.curie('fixi_deactivation_time'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionV11__fixi_deactivation_time, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?\d{4,}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})?$'))

slots.orchestraSessionsV11__fixi_session = Slot(uri=FIX_ORCHESTRA.fixi_session, name="orchestraSessionsV11__fixi_session", curie=FIX_ORCHESTRA.curie('fixi_session'),
                   model_uri=FIX_ORCHESTRA.orchestraSessionsV11__fixi_session, domain=None, range=Union[Union[dict, OrchestraSessionV11], list[Union[dict, OrchestraSessionV11]]])

slots.orchestraStateMachineV11__fixr_initial = Slot(uri=FIX_ORCHESTRA.fixr_initial, name="orchestraStateMachineV11__fixr_initial", curie=FIX_ORCHESTRA.curie('fixr_initial'),
                   model_uri=FIX_ORCHESTRA.orchestraStateMachineV11__fixr_initial, domain=None, range=Union[dict, OrchestraStateV11])

slots.orchestraStateMachineV11__fixr_state = Slot(uri=FIX_ORCHESTRA.fixr_state, name="orchestraStateMachineV11__fixr_state", curie=FIX_ORCHESTRA.curie('fixr_state'),
                   model_uri=FIX_ORCHESTRA.orchestraStateMachineV11__fixr_state, domain=None, range=Union[Union[dict, OrchestraStateV11], list[Union[dict, OrchestraStateV11]]])

slots.orchestraStateMachineV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraStateMachineV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraStateMachineV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraStateMachineV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraStateMachineV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraStateMachineV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraStateV11__fixr_transition = Slot(uri=FIX_ORCHESTRA.fixr_transition, name="orchestraStateV11__fixr_transition", curie=FIX_ORCHESTRA.curie('fixr_transition'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV11__fixr_transition, domain=None, range=Optional[Union[Union[dict, OrchestraTransitionV11], list[Union[dict, OrchestraTransitionV11]]]])

slots.orchestraStateV11__fixr_onentry = Slot(uri=FIX_ORCHESTRA.fixr_onentry, name="orchestraStateV11__fixr_onentry", curie=FIX_ORCHESTRA.curie('fixr_onentry'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV11__fixr_onentry, domain=None, range=Optional[Union[dict, OrchestraActionV11]])

slots.orchestraStateV11__fixr_activity = Slot(uri=FIX_ORCHESTRA.fixr_activity, name="orchestraStateV11__fixr_activity", curie=FIX_ORCHESTRA.curie('fixr_activity'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV11__fixr_activity, domain=None, range=Optional[Union[dict, OrchestraActionV11]])

slots.orchestraStateV11__fixr_onexit = Slot(uri=FIX_ORCHESTRA.fixr_onexit, name="orchestraStateV11__fixr_onexit", curie=FIX_ORCHESTRA.curie('fixr_onexit'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV11__fixr_onexit, domain=None, range=Optional[Union[dict, OrchestraActionV11]])

slots.orchestraStateV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraStateV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraStateV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraStateV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraStateV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraStructureMemberV11__fixr_component_ref = Slot(uri=FIX_ORCHESTRA.fixr_component_ref, name="orchestraStructureMemberV11__fixr_component_ref", curie=FIX_ORCHESTRA.curie('fixr_component_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraStructureMemberV11__fixr_component_ref, domain=None, range=Optional[Union[dict, OrchestraComponentRefV11]])

slots.orchestraStructureMemberV11__fixr_group_ref = Slot(uri=FIX_ORCHESTRA.fixr_group_ref, name="orchestraStructureMemberV11__fixr_group_ref", curie=FIX_ORCHESTRA.curie('fixr_group_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraStructureMemberV11__fixr_group_ref, domain=None, range=Optional[Union[dict, OrchestraGroupRefV11]])

slots.orchestraStructureMemberV11__fixr_field_ref = Slot(uri=FIX_ORCHESTRA.fixr_field_ref, name="orchestraStructureMemberV11__fixr_field_ref", curie=FIX_ORCHESTRA.curie('fixr_field_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraStructureMemberV11__fixr_field_ref, domain=None, range=Optional[Union[dict, OrchestraFieldRefV11]])

slots.orchestraTimerScheduleV11__fixr_activity = Slot(uri=FIX_ORCHESTRA.fixr_activity, name="orchestraTimerScheduleV11__fixr_activity", curie=FIX_ORCHESTRA.curie('fixr_activity'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerScheduleV11__fixr_activity, domain=None, range=Union[dict, OrchestraActionV11])

slots.orchestraTimerScheduleV11__fixr_actor = Slot(uri=FIX_ORCHESTRA.fixr_actor, name="orchestraTimerScheduleV11__fixr_actor", curie=FIX_ORCHESTRA.curie('fixr_actor'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerScheduleV11__fixr_actor, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraTimerScheduleV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraTimerScheduleV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerScheduleV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraTimerScheduleV11__fixr_operation = Slot(uri=FIX_ORCHESTRA.fixr_operation, name="orchestraTimerScheduleV11__fixr_operation", curie=FIX_ORCHESTRA.curie('fixr_operation'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerScheduleV11__fixr_operation, domain=None, range=Union[str, "OrchestraTimerOperation"])

slots.orchestraTimerScheduleV11__fixr_interval = Slot(uri=FIX_ORCHESTRA.fixr_interval, name="orchestraTimerScheduleV11__fixr_interval", curie=FIX_ORCHESTRA.curie('fixr_interval'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerScheduleV11__fixr_interval, domain=None, range=Optional[str],
                   pattern=re.compile(r'^-?P(?=\d|T\d)(\d+Y)?(\d+M)?(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+(\.\d+)?S)?)?$'))

slots.orchestraTimerV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraTimerV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraTimerV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraTransitionV11__fixr_when = Slot(uri=FIX_ORCHESTRA.fixr_when, name="orchestraTransitionV11__fixr_when", curie=FIX_ORCHESTRA.curie('fixr_when'),
                   model_uri=FIX_ORCHESTRA.orchestraTransitionV11__fixr_when, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.orchestraTransitionV11__fixr_annotation = Slot(uri=FIX_ORCHESTRA.fixr_annotation, name="orchestraTransitionV11__fixr_annotation", curie=FIX_ORCHESTRA.curie('fixr_annotation'),
                   model_uri=FIX_ORCHESTRA.orchestraTransitionV11__fixr_annotation, domain=None, range=Optional[Union[dict, OrchestraAnnotationV11]])

slots.orchestraTransitionV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraTransitionV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraTransitionV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraTransitionV11__fixr_target = Slot(uri=FIX_ORCHESTRA.fixr_target, name="orchestraTransitionV11__fixr_target", curie=FIX_ORCHESTRA.curie('fixr_target'),
                   model_uri=FIX_ORCHESTRA.orchestraTransitionV11__fixr_target, domain=None, range=str)

slots.orchestraTransportV11__fixi_address = Slot(uri=FIX_ORCHESTRA.fixi_address, name="orchestraTransportV11__fixi_address", curie=FIX_ORCHESTRA.curie('fixi_address'),
                   model_uri=FIX_ORCHESTRA.orchestraTransportV11__fixi_address, domain=None, range=Optional[str],
                   pattern=re.compile(r'^([^ \t\r\n]+( [^ \t\r\n]+)*)?$'))

slots.orchestraTransportV11__fixi_message_cast = Slot(uri=FIX_ORCHESTRA.fixi_message_cast, name="orchestraTransportV11__fixi_message_cast", curie=FIX_ORCHESTRA.curie('fixi_message_cast'),
                   model_uri=FIX_ORCHESTRA.orchestraTransportV11__fixi_message_cast, domain=None, range=Optional[Union[str, "OrchestraMessageCast"]])

slots.orchestraTransportV11__fixi_use = Slot(uri=FIX_ORCHESTRA.fixi_use, name="orchestraTransportV11__fixi_use", curie=FIX_ORCHESTRA.curie('fixi_use'),
                   model_uri=FIX_ORCHESTRA.orchestraTransportV11__fixi_use, domain=None, range=Optional[Union[str, "OrchestraTransportUse"]])

slots.orchestraTransportV11__fixi_other_attributes = Slot(uri=FIX_ORCHESTRA.fixi_other_attributes, name="orchestraTransportV11__fixi_other_attributes", curie=FIX_ORCHESTRA.curie('fixi_other_attributes'),
                   model_uri=FIX_ORCHESTRA.orchestraTransportV11__fixi_other_attributes, domain=None, range=Optional[Union[Union[dict, OrchestraXmlAttribute], list[Union[dict, OrchestraXmlAttribute]]]])

slots.orchestraTriggerV11__fixr_state_machine = Slot(uri=FIX_ORCHESTRA.fixr_state_machine, name="orchestraTriggerV11__fixr_state_machine", curie=FIX_ORCHESTRA.curie('fixr_state_machine'),
                   model_uri=FIX_ORCHESTRA.orchestraTriggerV11__fixr_state_machine, domain=None, range=str)

slots.orchestraTriggerV11__fixr_actor = Slot(uri=FIX_ORCHESTRA.fixr_actor, name="orchestraTriggerV11__fixr_actor", curie=FIX_ORCHESTRA.curie('fixr_actor'),
                   model_uri=FIX_ORCHESTRA.orchestraTriggerV11__fixr_actor, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraTriggerV11__fixr_name = Slot(uri=FIX_ORCHESTRA.fixr_name, name="orchestraTriggerV11__fixr_name", curie=FIX_ORCHESTRA.curie('fixr_name'),
                   model_uri=FIX_ORCHESTRA.orchestraTriggerV11__fixr_name, domain=None, range=str,
                   pattern=re.compile(r'^(?=[\s\S]{1,64}$)([^ \t\r\n]+( [^ \t\r\n]+)*)$'))

slots.orchestraUniqueV11__fixr_field_ref = Slot(uri=FIX_ORCHESTRA.fixr_field_ref, name="orchestraUniqueV11__fixr_field_ref", curie=FIX_ORCHESTRA.curie('fixr_field_ref'),
                   model_uri=FIX_ORCHESTRA.orchestraUniqueV11__fixr_field_ref, domain=None, range=Optional[Union[Union[dict, OrchestraFieldRefV11], list[Union[dict, OrchestraFieldRefV11]]]])
