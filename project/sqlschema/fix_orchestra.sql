-- # Class: EntityAttribGrp
--     * Slot: id
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
-- # Class: FieldAttribGrp Description: Attributes of a field that be overridden by a rule
--     * Slot: id
--     * Slot: min_inclusive Description: Inclusive lower bound
--     * Slot: max_inclusive Description: Inclusive upper bound
--     * Slot: impl_length Description: Fixed length
--     * Slot: impl_min_length
--     * Slot: impl_max_length
--     * Slot: presence Description: Overrides presence when expression is true
--     * Slot: value Description: If presence is optional, then it represents a default when the sender does not provide the field. If presence is constant, then it is the constant value.
--     * Slot: rendering Description: A hint to processes about how to interpret the element. Not validated.
--     * Slot: encoding Description: Character encoding if other than US-ASCII
-- # Class: OidGrp Description: The identifiers of a message element
--     * Slot: uid
--     * Slot: abbr_name
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
-- # Class: RefidGrp Description: A reference to a message element by its key identifiers
--     * Slot: uid
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name Description: The name is optional as part of a reference and only for convenience. It is not enforced by referential integrity. However, the name of the referred object is authoritative. A validator may check the consistency between the name used for the reference and the name of the referred object.
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
-- # Class: ScenarioRefGrp Description: A reference to a scenario by its key identifiers. There are no defaults as scenario references are optional.
--     * Slot: id
--     * Slot: scenario_ref_id Description: Unique identifier of a scenario. The identifier is required when referencing another scenario.
--     * Slot: scenario_ref Description: Name of a scenario. The name is optional as part of a reference and only for convenience.
-- # Class: ActionType
--     * Slot: id
-- # Class: ActorType Description: Represents a class of participants
--     * Slot: id
--     * Slot: name
--     * Slot: Actors_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: Annotation
--     * Slot: id
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
-- # Class: Appinfo Description: Usage specific annotation, optionally with link to an external reference or standard
--     * Slot: id
--     * Slot: spec_url Description: Reference documentation
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang_id
--     * Slot: purpose
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: Annotation_id Description: Autocreated FK slot
-- # Class: BlockAssignmentType
--     * Slot: id
--     * Slot: ComponentRefType_uid Description: Autocreated FK slot
--     * Slot: GroupRefType_uid Description: Autocreated FK slot
-- # Class: CategoryType
--     * Slot: id
--     * Slot: fixml_file_name
--     * Slot: component_type
--     * Slot: include_file
--     * Slot: name
--     * Slot: section
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: Categories_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: CodeSetType
--     * Slot: uid
--     * Slot: default
--     * Slot: spec_url Description: Reference documentation for an external code set
--     * Slot: union_data_type
--     * Slot: type Description: Underlying FIX datatype of codes
--     * Slot: abbr_name
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: scenario_ref_id Description: Unique identifier of a scenario. The identifier is required when referencing another scenario.
--     * Slot: scenario_ref Description: Name of a scenario. The name is optional as part of a reference and only for convenience.
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: CodeSets_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: CodeType
--     * Slot: uid
--     * Slot: value Description: The XML processor will remove line feeds, carriage returns, tabs, leading and trailing spaces, and multiple spaces. However, single internal spaces are allowed. May be further restricted by an external style.
--     * Slot: sort Description: Sort and group may be used to organize visualization of a code set.
--     * Slot: group
--     * Slot: abbr_name
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: CodeSetType_uid Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: ComponentRefType
--     * Slot: uid
--     * Slot: presence Description: Overrides presence when expression is true
--     * Slot: instance_name Description: Override the component name for this instance, for code generation and the like. Allows more than one instance of a component in a message.
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name Description: The name is optional as part of a reference and only for convenience. It is not enforced by referential integrity. However, the name of the referred object is authoritative. A validator may check the consistency between the name used for the reference and the name of the referred object.
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: ActionType_id Description: Autocreated FK slot
--     * Slot: ActorType_id Description: Autocreated FK slot
--     * Slot: BlockAssignmentType_id Description: Autocreated FK slot
--     * Slot: ComponentType_uid Description: Autocreated FK slot
--     * Slot: ConceptType_id Description: Autocreated FK slot
--     * Slot: GroupType_uid Description: Autocreated FK slot
--     * Slot: StructureInline_id Description: Autocreated FK slot
--     * Slot: ResponseType_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: ComponentRuleType
--     * Slot: id
--     * Slot: when Description: A condition that distinguishes when a scenario of a message type applies. It could be used to generate a decision tree to correlate an incoming message to its scenario, or to decide which scenario of a request message to send.
--     * Slot: presence Description: Overrides presence when expression is true
--     * Slot: name Description: Name of this rule
--     * Slot: ComponentRefType_uid Description: Autocreated FK slot
--     * Slot: GroupRefType_uid Description: Autocreated FK slot
-- # Class: ComponentType
--     * Slot: uid
--     * Slot: rendering Description: A hint to processes about how to interpret the element. Not validated.
--     * Slot: which Description: Member selection within each group instance
--     * Slot: category
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: abbr_name
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: scenario_ref_id Description: Unique identifier of a scenario. The identifier is required when referencing another scenario.
--     * Slot: scenario_ref Description: Name of a scenario. The name is optional as part of a reference and only for convenience.
--     * Slot: ActionType_id Description: Autocreated FK slot
--     * Slot: ActorType_id Description: Autocreated FK slot
--     * Slot: ResponseType_id Description: Autocreated FK slot
--     * Slot: Components_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: ConceptType
--     * Slot: id
--     * Slot: name
--     * Slot: Concepts_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: Documentation
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang_id
--     * Slot: purpose
--     * Slot: content_type
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: Annotation_id Description: Autocreated FK slot
-- # Class: FieldRefType
--     * Slot: uid
--     * Slot: length_id Description: Identifies a field used as a length prefix
--     * Slot: non_encoded_field_id Description: Identifies a non-encoded field related to an encoded field
--     * Slot: assign Description: Content of element holds an assignment expression for a message field or state variable
--     * Slot: instance_name Description: Override the field name for this instance, for code generation and the like. Allows more than one instance of a field in a message or component.
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name Description: The name is optional as part of a reference and only for convenience. It is not enforced by referential integrity. However, the name of the referred object is authoritative. A validator may check the consistency between the name used for the reference and the name of the referred object.
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: min_inclusive Description: Inclusive lower bound
--     * Slot: max_inclusive Description: Inclusive upper bound
--     * Slot: impl_length Description: Fixed length
--     * Slot: impl_min_length
--     * Slot: impl_max_length
--     * Slot: presence Description: Overrides presence when expression is true
--     * Slot: value Description: If presence is optional, then it represents a default when the sender does not provide the field. If presence is constant, then it is the constant value.
--     * Slot: rendering Description: A hint to processes about how to interpret the element. Not validated.
--     * Slot: encoding Description: Character encoding if other than US-ASCII
--     * Slot: ActionType_id Description: Autocreated FK slot
--     * Slot: ActorType_id Description: Autocreated FK slot
--     * Slot: BlockAssignmentType_id Description: Autocreated FK slot
--     * Slot: ComponentType_uid Description: Autocreated FK slot
--     * Slot: ConceptType_id Description: Autocreated FK slot
--     * Slot: UniqueInline_id Description: Autocreated FK slot
--     * Slot: GroupType_uid Description: Autocreated FK slot
--     * Slot: StructureInline_id Description: Autocreated FK slot
--     * Slot: ResponseType_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: UniqueInline
--     * Slot: id
-- # Class: FieldRuleType
--     * Slot: id
--     * Slot: when Description: A condition that distinguishes when a scenario of a message type applies. It could be used to generate a decision tree to correlate an incoming message to its scenario, or to decide which scenario of a request message to send.
--     * Slot: name Description: Name of this rule
--     * Slot: type Description: Overrides the type of the referenced field.
--     * Slot: min_inclusive Description: Inclusive lower bound
--     * Slot: max_inclusive Description: Inclusive upper bound
--     * Slot: impl_length Description: Fixed length
--     * Slot: impl_min_length
--     * Slot: impl_max_length
--     * Slot: presence Description: Overrides presence when expression is true
--     * Slot: value Description: If presence is optional, then it represents a default when the sender does not provide the field. If presence is constant, then it is the constant value.
--     * Slot: rendering Description: A hint to processes about how to interpret the element. Not validated.
--     * Slot: encoding Description: Character encoding if other than US-ASCII
--     * Slot: FieldRefType_uid Description: Autocreated FK slot
--     * Slot: FieldType_uid Description: Autocreated FK slot
--     * Slot: unique_id
-- # Class: FieldType
--     * Slot: uid
--     * Slot: length_id Description: Identifies a field used as a length prefix
--     * Slot: non_encoded_field_id Description: Identifies a non-encoded field related to an encoded field
--     * Slot: discriminator_id Description: Identifies a field used as a discriminator for this field's domain
--     * Slot: base_category
--     * Slot: base_category_abbr_name
--     * Slot: union_data_type
--     * Slot: assign Description: Content of element holds an assignment expression for a message field or state variable
--     * Slot: type Description: Attribute type refers to a datatype name
--     * Slot: code_set Description: Attribute codeSet refers to a codeSet name
--     * Slot: abbr_name
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: min_inclusive Description: Inclusive lower bound
--     * Slot: max_inclusive Description: Inclusive upper bound
--     * Slot: impl_length Description: Fixed length
--     * Slot: impl_min_length
--     * Slot: impl_max_length
--     * Slot: presence Description: Overrides presence when expression is true
--     * Slot: value Description: If presence is optional, then it represents a default when the sender does not provide the field. If presence is constant, then it is the constant value.
--     * Slot: rendering Description: A hint to processes about how to interpret the element. Not validated.
--     * Slot: encoding Description: Character encoding if other than US-ASCII
--     * Slot: ActionType_id Description: Autocreated FK slot
--     * Slot: ActorType_id Description: Autocreated FK slot
--     * Slot: ResponseType_id Description: Autocreated FK slot
--     * Slot: Fields_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: FlowType Description: A stream of messages in one direction
--     * Slot: id
--     * Slot: source Description: Name of the actor that originates messages
--     * Slot: destination Description: Name of the actor that receives messages.
--     * Slot: name
--     * Slot: reliability
--     * Slot: Actors_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: GroupRefType
--     * Slot: uid
--     * Slot: impl_min_occurs Description: Lower bound of group instances (numInGroup)
--     * Slot: impl_max_occurs Description: Upper bound of group instances (numInGroup)
--     * Slot: presence Description: Overrides presence when expression is true
--     * Slot: instance_name Description: Override the component name for this instance, for code generation and the like. Allows more than one instance of a component in a message.
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name Description: The name is optional as part of a reference and only for convenience. It is not enforced by referential integrity. However, the name of the referred object is authoritative. A validator may check the consistency between the name used for the reference and the name of the referred object.
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: ActionType_id Description: Autocreated FK slot
--     * Slot: ActorType_id Description: Autocreated FK slot
--     * Slot: BlockAssignmentType_id Description: Autocreated FK slot
--     * Slot: ComponentType_uid Description: Autocreated FK slot
--     * Slot: ConceptType_id Description: Autocreated FK slot
--     * Slot: GroupType_uid Description: Autocreated FK slot
--     * Slot: StructureInline_id Description: Autocreated FK slot
--     * Slot: ResponseType_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: GroupType Description: A repeating group. Logically, groupType is a subclass of componentType, but to make numInGroup first in the sequence, it cannot be an extension.
--     * Slot: uid
--     * Slot: rendering Description: A hint to processes about how to interpret the element. Not validated.
--     * Slot: impl_min_occurs Description: Lower bound of group instances (numInGroup)
--     * Slot: impl_max_occurs Description: Upper bound of group instances (numInGroup)
--     * Slot: which Description: Member selection within each group instance
--     * Slot: category
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: abbr_name
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: scenario_ref_id Description: Unique identifier of a scenario. The identifier is required when referencing another scenario.
--     * Slot: scenario_ref Description: Name of a scenario. The name is optional as part of a reference and only for convenience.
--     * Slot: ActionType_id Description: Autocreated FK slot
--     * Slot: ActorType_id Description: Autocreated FK slot
--     * Slot: ResponseType_id Description: Autocreated FK slot
--     * Slot: Groups_id Description: Autocreated FK slot
--     * Slot: num_in_group_uid
--     * Slot: annotation_id
-- # Class: IdentifiersType
--     * Slot: id
--     * Slot: annotation_id
-- # Class: IdentifierType
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: name
--     * Slot: IdentifiersType_id Description: Autocreated FK slot
--     * Slot: SessionType_id Description: Autocreated FK slot
-- # Class: ExtensionInline
--     * Slot: id
-- # Class: MappedDatatype
--     * Slot: id
--     * Slot: standard
--     * Slot: builtin
--     * Slot: pattern Description: A lexical restriction from a base type
--     * Slot: element Description: Element type of an aggregate type such as an array or sequence
--     * Slot: size Description: Size of an aggregate type such as an array. That is, the number of elements.
--     * Slot: parameter
--     * Slot: min_inclusive Description: Inclusive lower bound of values
--     * Slot: max_inclusive Description: Inclusive upper bound of values
--     * Slot: base Description: A datatype from which a subtype is created by restriction or a derived type is created by a generator
--     * Slot: Datatype_id Description: Autocreated FK slot
--     * Slot: extension_id Description: A datatype may be mapped to an XML snippet in the native schema belonging to its encoding standard.
--     * Slot: annotation_id
-- # Class: MessageRefType
--     * Slot: uid
--     * Slot: msg_type
--     * Slot: impl_min_occurs Description: Lower bound of group instances (numInGroup)
--     * Slot: impl_max_occurs Description: The same message type may be sent one or more times
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name Description: The name is optional as part of a reference and only for convenience. It is not enforced by referential integrity. However, the name of the referred object is authoritative. A validator may check the consistency between the name used for the reference and the name of the referred object.
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: ActionType_id Description: Autocreated FK slot
--     * Slot: ConceptType_id Description: Autocreated FK slot
--     * Slot: ResponseType_id Description: Autocreated FK slot
--     * Slot: identifiers_id
-- # Class: StructureInline
--     * Slot: id
--     * Slot: which Description: Member selection within each group instance
-- # Class: ResponsesInline
--     * Slot: id
-- # Class: MessageType
--     * Slot: uid
--     * Slot: when Description: A condition that distinguishes when a scenario of a message type applies. It could be used to generate a decision tree to correlate an incoming message to its scenario, or to decide which scenario of a request message to send.
--     * Slot: msg_type
--     * Slot: rendering Description: A hint to processes about how to interpret the element. Not validated.
--     * Slot: category
--     * Slot: flow
--     * Slot: abbr_name
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: id Description: Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag
--     * Slot: name
--     * Slot: scenario Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: scenario_ref_id Description: Unique identifier of a scenario. The identifier is required when referencing another scenario.
--     * Slot: scenario_ref Description: Name of a scenario. The name is optional as part of a reference and only for convenience.
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: Messages_id Description: Autocreated FK slot
--     * Slot: structure_id
--     * Slot: responses_id
--     * Slot: annotation_id
-- # Class: ResponseType Description: Any number of action behaviors can be triggered by the same 'when' condition
--     * Slot: id
--     * Slot: when Description: A common condition for all of the actions. If it evalutes true, then the actions are invoked. If 'when' is not present, the actions are unconditional.
--     * Slot: sync
--     * Slot: name
--     * Slot: ResponsesInline_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: ScenarioType Description: The use case of an element, distinguished by workflow, asset class, etc.
--     * Slot: uid
--     * Slot: id Description: Unique numeric identifier. Default is '1' is for base scenario.
--     * Slot: name Description: Unique name
--     * Slot: Scenarios_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: SectionType
--     * Slot: id
--     * Slot: display_order
--     * Slot: fixml_file_name
--     * Slot: name
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: Sections_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: StateMachineType
--     * Slot: id
--     * Slot: name
--     * Slot: ActorType_id Description: Autocreated FK slot
--     * Slot: initial_id Description: Initial state of a state machine
--     * Slot: annotation_id
-- # Class: StateType Description: A state of a state machine. If it has no transitions, then it is a final state.
--     * Slot: id
--     * Slot: name
--     * Slot: StateMachineType_id Description: Autocreated FK slot
--     * Slot: onentry_id Description: Operation fired when entering a state.
--     * Slot: activity_id Description: Operation fired when entering a state and completing when exiting or earlier.
--     * Slot: onexit_id Description: Operation fired when exiting a state.
--     * Slot: annotation_id
-- # Class: TimerSchedule
--     * Slot: id
--     * Slot: operation
--     * Slot: interval
--     * Slot: actor Description: Name of the actor that owns the timer
--     * Slot: name Description: Name of the timer
--     * Slot: ActionType_id Description: Autocreated FK slot
--     * Slot: ResponseType_id Description: Autocreated FK slot
--     * Slot: activity_id Description: Action to take when a timer expires
-- # Class: TimerType
--     * Slot: id
--     * Slot: name
--     * Slot: ActorType_id Description: Autocreated FK slot
-- # Class: TransitionType
--     * Slot: id
--     * Slot: when Description: Optional guard condition. The transition is allowed if the condition evaluates true. If not present, the transition is unconditional.
--     * Slot: target Description: The target state of the transition
--     * Slot: name
--     * Slot: StateType_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: TriggerType
--     * Slot: id
--     * Slot: state_machine Description: Name of the state machine
--     * Slot: actor Description: Name of the actor that owns the state machine
--     * Slot: name Description: Name of the transition to invoke
--     * Slot: ActionType_id Description: Autocreated FK slot
--     * Slot: ResponseType_id Description: Autocreated FK slot
-- # Class: InterfaceAnnotation
--     * Slot: id
-- # Class: InterfaceAppinfo Description: Usage specific annotation, optionally with link to an external reference or standard
--     * Slot: id
--     * Slot: spec_url Description: Reference documentation
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang_id
--     * Slot: purpose
--     * Slot: InterfaceAnnotation_id Description: Autocreated FK slot
-- # Abstract Class: BaseInterfaceType
--     * Slot: id
--     * Slot: name
--     * Slot: annotation_id
-- # Class: InterfaceDocumentation
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang_id
--     * Slot: purpose
--     * Slot: content_type
--     * Slot: InterfaceAnnotation_id Description: Autocreated FK slot
-- # Class: EncodingType
--     * Slot: id
--     * Slot: activation_time Description: When this version becomes effective
--     * Slot: deactivation_time Description: When this version is no longer effective
--     * Slot: layer
--     * Slot: orchestration Description: URI of Orchestra rules of engagement
--     * Slot: name
--     * Slot: version
--     * Slot: deprecated Description: When this version was deprecated; may be replaced or removed in the future
--     * Slot: reliability Description: Reliability can be implemented at transport, session, or application layers
--     * Slot: BaseInterfaceType_id Description: Autocreated FK slot
--     * Slot: InterfaceType_id Description: Autocreated FK slot
--     * Slot: SessionType_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: SessionsInline
--     * Slot: id
-- # Class: InterfaceType
--     * Slot: id
--     * Slot: name
--     * Slot: Interfaces_id Description: Autocreated FK slot
--     * Slot: sessions_id
--     * Slot: annotation_id
-- # Class: ProtocolType
--     * Slot: id
--     * Slot: activation_time Description: When this version becomes effective
--     * Slot: deactivation_time Description: When this version is no longer effective
--     * Slot: layer
--     * Slot: orchestration Description: URI of Orchestra rules of engagement
--     * Slot: name
--     * Slot: version
--     * Slot: deprecated Description: When this version was deprecated; may be replaced or removed in the future
--     * Slot: reliability Description: Reliability can be implemented at transport, session, or application layers
--     * Slot: BaseInterfaceType_id Description: Autocreated FK slot
--     * Slot: InterfaceType_id Description: Autocreated FK slot
--     * Slot: SessionType_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: ServiceType
--     * Slot: id
--     * Slot: activation_time Description: When this version becomes effective
--     * Slot: deactivation_time Description: When this version is no longer effective
--     * Slot: layer
--     * Slot: orchestration Description: URI of Orchestra rules of engagement
--     * Slot: name
--     * Slot: version
--     * Slot: deprecated Description: When this version was deprecated; may be replaced or removed in the future
--     * Slot: reliability Description: Reliability can be implemented at transport, session, or application layers
--     * Slot: BaseInterfaceType_id Description: Autocreated FK slot
--     * Slot: InterfaceType_id Description: Autocreated FK slot
--     * Slot: SessionType_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: SessionProtocolType
--     * Slot: id
--     * Slot: activation_time Description: When this version becomes effective
--     * Slot: deactivation_time Description: When this version is no longer effective
--     * Slot: layer
--     * Slot: orchestration Description: URI of Orchestra rules of engagement
--     * Slot: name
--     * Slot: version
--     * Slot: deprecated Description: When this version was deprecated; may be replaced or removed in the future
--     * Slot: reliability Description: Reliability can be implemented at transport, session, or application layers
--     * Slot: BaseInterfaceType_id Description: Autocreated FK slot
--     * Slot: InterfaceType_id Description: Autocreated FK slot
--     * Slot: SessionType_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: SessionType
--     * Slot: id
--     * Slot: role
--     * Slot: security_keys Description: Textual encoding as specified by IETF RFC 7468
--     * Slot: activation_time Description: When this session becomes effective
--     * Slot: deactivation_time Description: When this session is no longer effective
--     * Slot: name
--     * Slot: SessionsInline_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: TransportProtocolType
--     * Slot: id
--     * Slot: address
--     * Slot: message_cast
--     * Slot: use
--     * Slot: activation_time Description: When this version becomes effective
--     * Slot: deactivation_time Description: When this version is no longer effective
--     * Slot: layer
--     * Slot: orchestration Description: URI of Orchestra rules of engagement
--     * Slot: name
--     * Slot: version
--     * Slot: deprecated Description: When this version was deprecated; may be replaced or removed in the future
--     * Slot: reliability Description: Reliability can be implemented at transport, session, or application layers
--     * Slot: BaseInterfaceType_id Description: Autocreated FK slot
--     * Slot: InterfaceType_id Description: Autocreated FK slot
--     * Slot: SessionType_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: UserInterfaceType
--     * Slot: id
--     * Slot: activation_time Description: When this version becomes effective
--     * Slot: deactivation_time Description: When this version is no longer effective
--     * Slot: layer
--     * Slot: orchestration Description: URI of Orchestra rules of engagement
--     * Slot: name
--     * Slot: version
--     * Slot: deprecated Description: When this version was deprecated; may be replaced or removed in the future
--     * Slot: reliability Description: Reliability can be implemented at transport, session, or application layers
--     * Slot: BaseInterfaceType_id Description: Autocreated FK slot
--     * Slot: InterfaceType_id Description: Autocreated FK slot
--     * Slot: SessionType_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: Datatype
--     * Slot: id
--     * Slot: scenario_id Description: Unique identifier of a scenario. Default is '1' for base scenario.
--     * Slot: base_type
--     * Slot: name
--     * Slot: scenario Description: The use case of a datatype by name
--     * Slot: added
--     * Slot: added_ep
--     * Slot: change_type
--     * Slot: deprecated_ep
--     * Slot: issue
--     * Slot: last_modified
--     * Slot: replaced
--     * Slot: replaced_ep
--     * Slot: replaced_by_field
--     * Slot: supported
--     * Slot: updated
--     * Slot: updated_ep
--     * Slot: deprecated
--     * Slot: Datatypes_id Description: Autocreated FK slot
--     * Slot: annotation_id
-- # Class: Actors Description: Participants and the message flows between them
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: Categories
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: CodeSets
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: Components
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: Concepts
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: Datatypes
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: Fields
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: Groups
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: Messages
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: Repository
--     * Slot: id
--     * Slot: guid
--     * Slot: spec_url Description: Reference documentation
--     * Slot: namespace Description: An associated namespace as URI
--     * Slot: expression_language Description: The syntax of 'expressionType'
--     * Slot: name Description: Stable name that does not change with minor version updates
--     * Slot: version
--     * Slot: metadata_id
--     * Slot: categories_id
--     * Slot: sections_id
--     * Slot: datatypes_id
--     * Slot: code_sets_id
--     * Slot: fields_id
--     * Slot: actors_id
--     * Slot: components_id
--     * Slot: groups_id
--     * Slot: messages_id
--     * Slot: concepts_id
--     * Slot: scenarios_id
--     * Slot: annotation_id
-- # Class: Scenarios Description: The default scenario is id='1' name='base'.
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: Sections
--     * Slot: id
--     * Slot: base
--     * Slot: annotation_id
-- # Class: Interfaces Description: This represents the current state of service and session configurations. Changes to configuration can represented with patch operations. See IETF RFC 5261
--     * Slot: id
--     * Slot: metadata_id
-- # Class: DcSimpleLiteral Description: This is the default type for all of the DC elements. It permits text content only with optional xml:lang attribute. Text is allowed because mixed="true", but sub-elements are disallowed because minOccurs="0" and maxOccurs="0" are on the xs:any tag. This complexType allows for restriction or extension permitting child elements.
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcElementContainer Description: This complexType is included as a convenience for schema authors who need to define a root or container element for all of the DC elements.
--     * Slot: id
--     * Slot: title Description: Free-text value of the Dublin Core element/refinement `title`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: creator Description: Free-text value of the Dublin Core element/refinement `creator`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: subject Description: Free-text value of the Dublin Core element/refinement `subject`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: description Description: Free-text value of the Dublin Core element/refinement `description`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: publisher Description: Free-text value of the Dublin Core element/refinement `publisher`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: contributor Description: Free-text value of the Dublin Core element/refinement `contributor`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: date Description: Free-text value of the Dublin Core element/refinement `date`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: format Description: Free-text value of the Dublin Core element/refinement `format`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: source Description: Free-text value of the Dublin Core element/refinement `source`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: language Description: Free-text value of the Dublin Core element/refinement `language`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: relation Description: Free-text value of the Dublin Core element/refinement `relation`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: coverage Description: Free-text value of the Dublin Core element/refinement `coverage`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: rights Description: Free-text value of the Dublin Core element/refinement `rights`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: alternative Description: Free-text value of the Dublin Core element/refinement `alternative`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: table_of_contents Description: Free-text value of the Dublin Core element/refinement `tableOfContents`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: abstract Description: Free-text value of the Dublin Core element/refinement `abstract`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: created Description: Free-text value of the Dublin Core element/refinement `created`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: valid Description: Free-text value of the Dublin Core element/refinement `valid`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: available Description: Free-text value of the Dublin Core element/refinement `available`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: issued Description: Free-text value of the Dublin Core element/refinement `issued`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: modified Description: Free-text value of the Dublin Core element/refinement `modified`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: date_accepted Description: Free-text value of the Dublin Core element/refinement `dateAccepted`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: date_copyrighted Description: Free-text value of the Dublin Core element/refinement `dateCopyrighted`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: date_submitted Description: Free-text value of the Dublin Core element/refinement `dateSubmitted`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: extent Description: Free-text value of the Dublin Core element/refinement `extent`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: medium Description: Free-text value of the Dublin Core element/refinement `medium`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_version_of Description: Free-text value of the Dublin Core element/refinement `isVersionOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: has_version Description: Free-text value of the Dublin Core element/refinement `hasVersion`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_replaced_by Description: Free-text value of the Dublin Core element/refinement `isReplacedBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: replaces Description: Free-text value of the Dublin Core element/refinement `replaces`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_required_by Description: Free-text value of the Dublin Core element/refinement `isRequiredBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: requires Description: Free-text value of the Dublin Core element/refinement `requires`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_part_of Description: Free-text value of the Dublin Core element/refinement `isPartOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: has_part Description: Free-text value of the Dublin Core element/refinement `hasPart`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_referenced_by Description: Free-text value of the Dublin Core element/refinement `isReferencedBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: references Description: Free-text value of the Dublin Core element/refinement `references`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_format_of Description: Free-text value of the Dublin Core element/refinement `isFormatOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: has_format Description: Free-text value of the Dublin Core element/refinement `hasFormat`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: conforms_to Description: Free-text value of the Dublin Core element/refinement `conformsTo`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: spatial Description: Free-text value of the Dublin Core element/refinement `spatial`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: temporal Description: Free-text value of the Dublin Core element/refinement `temporal`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: audience Description: Free-text value of the Dublin Core element/refinement `audience`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: accrual_method Description: Free-text value of the Dublin Core element/refinement `accrualMethod`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: accrual_periodicity Description: Free-text value of the Dublin Core element/refinement `accrualPeriodicity`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: accrual_policy Description: Free-text value of the Dublin Core element/refinement `accrualPolicy`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: instructional_method Description: Free-text value of the Dublin Core element/refinement `instructionalMethod`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: provenance Description: Free-text value of the Dublin Core element/refinement `provenance`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: rights_holder Description: Free-text value of the Dublin Core element/refinement `rightsHolder`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: mediator Description: Free-text value of the Dublin Core element/refinement `mediator`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: education_level Description: Free-text value of the Dublin Core element/refinement `educationLevel`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: access_rights Description: Free-text value of the Dublin Core element/refinement `accessRights`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: license Description: Free-text value of the Dublin Core element/refinement `license`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: bibliographic_citation Description: Free-text value of the Dublin Core element/refinement `bibliographicCitation`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: type Description: Free-text value of the Dublin Core element/refinement `type`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: identifier Description: Free-text value of the Dublin Core element/refinement `identifier`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
-- # Abstract Class: DcAny
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcTitle
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcCreator
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcSubject
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcDescription
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcPublisher
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcContributor
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcDate
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcType
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcFormat
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcIdentifier
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcSource
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcLanguage
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcRelation
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcCoverage
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcRights
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DcElementsGroup Description: This group is included as a convenience for schema authors who need to refer to all the elements in the http://purl.org/dc/elements/1.1/ namespace.
--     * Slot: id
-- # Class: DctermsLCSH
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsMESH
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsDDC
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsLCC
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsUDC
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsPeriod
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsW3CDTF
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsDCMIType
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsIMT
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsURI
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsISO6392
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsISO6393
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsRFC1766
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsRFC3066
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsRFC4646
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsPoint
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsISO3166
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsBox
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsTGN
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsElementOrRefinementContainer Description: This is included as a convenience for schema authors who need to define a root or container element for all of the DC elements and element refinements.
--     * Slot: id
--     * Slot: title Description: Free-text value of the Dublin Core element/refinement `title`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: creator Description: Free-text value of the Dublin Core element/refinement `creator`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: subject Description: Free-text value of the Dublin Core element/refinement `subject`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: description Description: Free-text value of the Dublin Core element/refinement `description`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: publisher Description: Free-text value of the Dublin Core element/refinement `publisher`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: contributor Description: Free-text value of the Dublin Core element/refinement `contributor`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: date Description: Free-text value of the Dublin Core element/refinement `date`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: format Description: Free-text value of the Dublin Core element/refinement `format`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: source Description: Free-text value of the Dublin Core element/refinement `source`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: language Description: Free-text value of the Dublin Core element/refinement `language`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: relation Description: Free-text value of the Dublin Core element/refinement `relation`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: coverage Description: Free-text value of the Dublin Core element/refinement `coverage`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: rights Description: Free-text value of the Dublin Core element/refinement `rights`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: alternative Description: Free-text value of the Dublin Core element/refinement `alternative`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: table_of_contents Description: Free-text value of the Dublin Core element/refinement `tableOfContents`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: abstract Description: Free-text value of the Dublin Core element/refinement `abstract`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: created Description: Free-text value of the Dublin Core element/refinement `created`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: valid Description: Free-text value of the Dublin Core element/refinement `valid`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: available Description: Free-text value of the Dublin Core element/refinement `available`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: issued Description: Free-text value of the Dublin Core element/refinement `issued`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: modified Description: Free-text value of the Dublin Core element/refinement `modified`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: date_accepted Description: Free-text value of the Dublin Core element/refinement `dateAccepted`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: date_copyrighted Description: Free-text value of the Dublin Core element/refinement `dateCopyrighted`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: date_submitted Description: Free-text value of the Dublin Core element/refinement `dateSubmitted`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: extent Description: Free-text value of the Dublin Core element/refinement `extent`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: medium Description: Free-text value of the Dublin Core element/refinement `medium`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_version_of Description: Free-text value of the Dublin Core element/refinement `isVersionOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: has_version Description: Free-text value of the Dublin Core element/refinement `hasVersion`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_replaced_by Description: Free-text value of the Dublin Core element/refinement `isReplacedBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: replaces Description: Free-text value of the Dublin Core element/refinement `replaces`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_required_by Description: Free-text value of the Dublin Core element/refinement `isRequiredBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: requires Description: Free-text value of the Dublin Core element/refinement `requires`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_part_of Description: Free-text value of the Dublin Core element/refinement `isPartOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: has_part Description: Free-text value of the Dublin Core element/refinement `hasPart`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_referenced_by Description: Free-text value of the Dublin Core element/refinement `isReferencedBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: references Description: Free-text value of the Dublin Core element/refinement `references`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: is_format_of Description: Free-text value of the Dublin Core element/refinement `isFormatOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: has_format Description: Free-text value of the Dublin Core element/refinement `hasFormat`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: conforms_to Description: Free-text value of the Dublin Core element/refinement `conformsTo`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: spatial Description: Free-text value of the Dublin Core element/refinement `spatial`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: temporal Description: Free-text value of the Dublin Core element/refinement `temporal`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: audience Description: Free-text value of the Dublin Core element/refinement `audience`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: accrual_method Description: Free-text value of the Dublin Core element/refinement `accrualMethod`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: accrual_periodicity Description: Free-text value of the Dublin Core element/refinement `accrualPeriodicity`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: accrual_policy Description: Free-text value of the Dublin Core element/refinement `accrualPolicy`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: instructional_method Description: Free-text value of the Dublin Core element/refinement `instructionalMethod`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: provenance Description: Free-text value of the Dublin Core element/refinement `provenance`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: rights_holder Description: Free-text value of the Dublin Core element/refinement `rightsHolder`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: mediator Description: Free-text value of the Dublin Core element/refinement `mediator`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: education_level Description: Free-text value of the Dublin Core element/refinement `educationLevel`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: access_rights Description: Free-text value of the Dublin Core element/refinement `accessRights`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: license Description: Free-text value of the Dublin Core element/refinement `license`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: bibliographic_citation Description: Free-text value of the Dublin Core element/refinement `bibliographicCitation`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: type Description: Free-text value of the Dublin Core element/refinement `type`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
--     * Slot: identifier Description: Free-text value of the Dublin Core element/refinement `identifier`. Expanded from the XSD substitutionGroup chain rooted at dc:any.
-- # Class: DctermsTitle
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsCreator
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsSubject
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsDescription
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsPublisher
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsContributor
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsDate
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsType
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsFormat
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsIdentifier
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsSource
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsLanguage
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsRelation
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsCoverage
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsRights
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsAlternative
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsTableOfContents
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsAbstract
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsCreated
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsValid
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsAvailable
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsIssued
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsModified
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsDateAccepted
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsDateCopyrighted
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsDateSubmitted
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsExtent
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsMedium
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsIsVersionOf
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsHasVersion
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsIsReplacedBy
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsReplaces
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsIsRequiredBy
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsRequires
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsIsPartOf
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsHasPart
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsIsReferencedBy
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsReferences
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsIsFormatOf
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsHasFormat
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsConformsTo
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsSpatial
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsTemporal
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsAudience
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsAccrualMethod
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsAccrualPeriodicity
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsAccrualPolicy
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsInstructionalMethod
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsProvenance
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsRightsHolder
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsMediator
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsEducationLevel
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsAccessRights
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsLicense
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsBibliographicCitation
--     * Slot: id
--     * Slot: value Description: Mixed text content of the element.
--     * Slot: lang
-- # Class: DctermsElementsAndRefinementsGroup Description: This group is included as a convenience for schema authors who need to refer to all the DC elements and element refinements in the http://purl.org/dc/elements/1.1/ and http://purl.org/dc/terms namespaces. N.B. Refinements available via substitution groups.
--     * Slot: id
-- # Class: XmlSpecialAttrs
--     * Slot: uid
--     * Slot: base
--     * Slot: lang
--     * Slot: space
--     * Slot: id
-- # Class: XmlGlobalAttributes Description: Container for the global <xs:attribute> declarations defined in xml.xsd. Each attribute here is referenceable from other XSDs via ``ref="xml:<name>"``.
--     * Slot: uid
--     * Slot: lang Description: lang (as an attribute name) denotes an attribute whose value is a language code for the natural language of the content of any element; its value is inherited. This name is reserved by virtue of its definition in the XML specification. Notes Attempting to install the relevant ISO 2- and 3-letter codes as the enumerated possible values is probably never going to be a realistic possibility. See BCP 47 at http://www.rfc-editor.org/rfc/bcp/bcp47.txt and the IANA language subtag registry at http://www.iana.org/assignments/language-subtag-registry for further information. The union allows for the 'un-declaration' of xml:lang with the empty string.
--     * Slot: space Description: space (as an attribute name) denotes an attribute whose value is a keyword indicating what whitespace processing discipline is intended for the content of the element; its value is inherited. This name is reserved by virtue of its definition in the XML specification.
--     * Slot: base Description: base (as an attribute name) denotes an attribute whose value provides a URI to be used as the base for interpreting any relative URIs in the scope of the element on which it appears; its value is inherited. This name is reserved by virtue of its definition in the XML Base specification. See http://www.w3.org/TR/xmlbase/ for information about this attribute.
--     * Slot: id Description: id (as an attribute name) denotes an attribute whose value should be interpreted as if declared to be of type ID. This name is reserved by virtue of its definition in the xml:id specification. See http://www.w3.org/TR/xml-id/ for information about this attribute.
-- # Class: ActionType_assign
--     * Slot: ActionType_id Description: Autocreated FK slot
--     * Slot: assign Description: Content of element holds an assignment expression for a state variable in the form '$actor.variable=value'
-- # Class: Appinfo_content
--     * Slot: Appinfo_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: Appinfo_extra_attributes
--     * Slot: Appinfo_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: Documentation_content
--     * Slot: Documentation_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: FieldRuleType_assign
--     * Slot: FieldRuleType_id Description: Autocreated FK slot
--     * Slot: assign Description: Content of element holds an assignment expression for a message field or state variable. This can be used for field validation.
-- # Class: ExtensionInline_content
--     * Slot: ExtensionInline_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: ResponseType_assign
--     * Slot: ResponseType_id Description: Autocreated FK slot
--     * Slot: assign Description: Content of element holds an assignment expression for a state variable in the form '$actor.variable=value'
-- # Class: InterfaceAppinfo_content
--     * Slot: InterfaceAppinfo_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: InterfaceAppinfo_extra_attributes
--     * Slot: InterfaceAppinfo_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: BaseInterfaceType_extra_attributes
--     * Slot: BaseInterfaceType_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: InterfaceDocumentation_content
--     * Slot: InterfaceDocumentation_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: EncodingType_extra_attributes
--     * Slot: EncodingType_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: InterfaceType_extra_attributes
--     * Slot: InterfaceType_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: ProtocolType_extra_attributes
--     * Slot: ProtocolType_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: ServiceType_extra_attributes
--     * Slot: ServiceType_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: SessionProtocolType_extra_attributes
--     * Slot: SessionProtocolType_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: SessionType_extra_attributes
--     * Slot: SessionType_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: TransportProtocolType_extra_attributes
--     * Slot: TransportProtocolType_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: UserInterfaceType_extra_attributes
--     * Slot: UserInterfaceType_id Description: Autocreated FK slot
--     * Slot: extra_attributes Description: Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point).
-- # Class: DcSimpleLiteral_content
--     * Slot: DcSimpleLiteral_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcAny_content
--     * Slot: DcAny_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcTitle_content
--     * Slot: DcTitle_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcCreator_content
--     * Slot: DcCreator_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcSubject_content
--     * Slot: DcSubject_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcDescription_content
--     * Slot: DcDescription_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcPublisher_content
--     * Slot: DcPublisher_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcContributor_content
--     * Slot: DcContributor_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcDate_content
--     * Slot: DcDate_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcType_content
--     * Slot: DcType_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcFormat_content
--     * Slot: DcFormat_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcIdentifier_content
--     * Slot: DcIdentifier_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcSource_content
--     * Slot: DcSource_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcLanguage_content
--     * Slot: DcLanguage_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcRelation_content
--     * Slot: DcRelation_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcCoverage_content
--     * Slot: DcCoverage_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DcRights_content
--     * Slot: DcRights_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsLCSH_content
--     * Slot: DctermsLCSH_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsMESH_content
--     * Slot: DctermsMESH_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsDDC_content
--     * Slot: DctermsDDC_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsLCC_content
--     * Slot: DctermsLCC_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsUDC_content
--     * Slot: DctermsUDC_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsPeriod_content
--     * Slot: DctermsPeriod_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsW3CDTF_content
--     * Slot: DctermsW3CDTF_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsDCMIType_content
--     * Slot: DctermsDCMIType_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsIMT_content
--     * Slot: DctermsIMT_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsURI_content
--     * Slot: DctermsURI_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsISO6392_content
--     * Slot: DctermsISO6392_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsISO6393_content
--     * Slot: DctermsISO6393_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsRFC1766_content
--     * Slot: DctermsRFC1766_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsRFC3066_content
--     * Slot: DctermsRFC3066_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsRFC4646_content
--     * Slot: DctermsRFC4646_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsPoint_content
--     * Slot: DctermsPoint_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsISO3166_content
--     * Slot: DctermsISO3166_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsBox_content
--     * Slot: DctermsBox_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsTGN_content
--     * Slot: DctermsTGN_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsTitle_content
--     * Slot: DctermsTitle_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsCreator_content
--     * Slot: DctermsCreator_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsSubject_content
--     * Slot: DctermsSubject_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsDescription_content
--     * Slot: DctermsDescription_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsPublisher_content
--     * Slot: DctermsPublisher_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsContributor_content
--     * Slot: DctermsContributor_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsDate_content
--     * Slot: DctermsDate_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsType_content
--     * Slot: DctermsType_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsFormat_content
--     * Slot: DctermsFormat_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsIdentifier_content
--     * Slot: DctermsIdentifier_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsSource_content
--     * Slot: DctermsSource_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsLanguage_content
--     * Slot: DctermsLanguage_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsRelation_content
--     * Slot: DctermsRelation_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsCoverage_content
--     * Slot: DctermsCoverage_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsRights_content
--     * Slot: DctermsRights_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsAlternative_content
--     * Slot: DctermsAlternative_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsTableOfContents_content
--     * Slot: DctermsTableOfContents_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsAbstract_content
--     * Slot: DctermsAbstract_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsCreated_content
--     * Slot: DctermsCreated_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsValid_content
--     * Slot: DctermsValid_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsAvailable_content
--     * Slot: DctermsAvailable_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsIssued_content
--     * Slot: DctermsIssued_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsModified_content
--     * Slot: DctermsModified_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsDateAccepted_content
--     * Slot: DctermsDateAccepted_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsDateCopyrighted_content
--     * Slot: DctermsDateCopyrighted_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsDateSubmitted_content
--     * Slot: DctermsDateSubmitted_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsExtent_content
--     * Slot: DctermsExtent_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsMedium_content
--     * Slot: DctermsMedium_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsIsVersionOf_content
--     * Slot: DctermsIsVersionOf_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsHasVersion_content
--     * Slot: DctermsHasVersion_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsIsReplacedBy_content
--     * Slot: DctermsIsReplacedBy_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsReplaces_content
--     * Slot: DctermsReplaces_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsIsRequiredBy_content
--     * Slot: DctermsIsRequiredBy_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsRequires_content
--     * Slot: DctermsRequires_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsIsPartOf_content
--     * Slot: DctermsIsPartOf_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsHasPart_content
--     * Slot: DctermsHasPart_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsIsReferencedBy_content
--     * Slot: DctermsIsReferencedBy_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsReferences_content
--     * Slot: DctermsReferences_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsIsFormatOf_content
--     * Slot: DctermsIsFormatOf_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsHasFormat_content
--     * Slot: DctermsHasFormat_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsConformsTo_content
--     * Slot: DctermsConformsTo_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsSpatial_content
--     * Slot: DctermsSpatial_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsTemporal_content
--     * Slot: DctermsTemporal_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsAudience_content
--     * Slot: DctermsAudience_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsAccrualMethod_content
--     * Slot: DctermsAccrualMethod_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsAccrualPeriodicity_content
--     * Slot: DctermsAccrualPeriodicity_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsAccrualPolicy_content
--     * Slot: DctermsAccrualPolicy_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsInstructionalMethod_content
--     * Slot: DctermsInstructionalMethod_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsProvenance_content
--     * Slot: DctermsProvenance_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsRightsHolder_content
--     * Slot: DctermsRightsHolder_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsMediator_content
--     * Slot: DctermsMediator_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsEducationLevel_content
--     * Slot: DctermsEducationLevel_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsAccessRights_content
--     * Slot: DctermsAccessRights_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsLicense_content
--     * Slot: DctermsLicense_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.
-- # Class: DctermsBibliographicCitation_content
--     * Slot: DctermsBibliographicCitation_id Description: Autocreated FK slot
--     * Slot: content Description: Pass-through xs:any content as raw strings.

CREATE TABLE "EntityAttribGrp" (
	id INTEGER NOT NULL,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_EntityAttribGrp_id" ON "EntityAttribGrp" (id);

CREATE TABLE "FieldAttribGrp" (
	id INTEGER NOT NULL,
	min_inclusive TEXT,
	max_inclusive TEXT,
	impl_length INTEGER,
	impl_min_length INTEGER,
	impl_max_length INTEGER,
	presence VARCHAR(9),
	value TEXT,
	rendering TEXT,
	encoding TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_FieldAttribGrp_id" ON "FieldAttribGrp" (id);

CREATE TABLE "OidGrp" (
	uid INTEGER NOT NULL,
	abbr_name TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	scenario TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_OidGrp_uid" ON "OidGrp" (uid);

CREATE TABLE "RefidGrp" (
	uid INTEGER NOT NULL,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT,
	scenario TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_RefidGrp_uid" ON "RefidGrp" (uid);

CREATE TABLE "ScenarioRefGrp" (
	id INTEGER NOT NULL,
	scenario_ref_id TEXT,
	scenario_ref TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ScenarioRefGrp_id" ON "ScenarioRefGrp" (id);

CREATE TABLE "ActionType" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ActionType_id" ON "ActionType" (id);

CREATE TABLE "Annotation" (
	id INTEGER NOT NULL,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Annotation_id" ON "Annotation" (id);

CREATE TABLE "BlockAssignmentType" (
	id INTEGER NOT NULL,
	"ComponentRefType_uid" INTEGER,
	"GroupRefType_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ComponentRefType_uid") REFERENCES "ComponentRefType" (uid),
	FOREIGN KEY("GroupRefType_uid") REFERENCES "GroupRefType" (uid)
);
CREATE INDEX "ix_BlockAssignmentType_id" ON "BlockAssignmentType" (id);

CREATE TABLE "ComponentRefType" (
	uid INTEGER NOT NULL,
	presence VARCHAR(9),
	instance_name TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT,
	scenario TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	"ActionType_id" INTEGER,
	"ActorType_id" INTEGER,
	"BlockAssignmentType_id" INTEGER,
	"ComponentType_uid" INTEGER,
	"ConceptType_id" INTEGER,
	"GroupType_uid" INTEGER,
	"StructureInline_id" INTEGER,
	"ResponseType_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ActionType_id") REFERENCES "ActionType" (id),
	FOREIGN KEY("ActorType_id") REFERENCES "ActorType" (id),
	FOREIGN KEY("BlockAssignmentType_id") REFERENCES "BlockAssignmentType" (id),
	FOREIGN KEY("ComponentType_uid") REFERENCES "ComponentType" (uid),
	FOREIGN KEY("ConceptType_id") REFERENCES "ConceptType" (id),
	FOREIGN KEY("GroupType_uid") REFERENCES "GroupType" (uid),
	FOREIGN KEY("StructureInline_id") REFERENCES "StructureInline" (id),
	FOREIGN KEY("ResponseType_id") REFERENCES "ResponseType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_ComponentRefType_uid" ON "ComponentRefType" (uid);

CREATE TABLE "FieldRefType" (
	uid INTEGER NOT NULL,
	length_id TEXT,
	non_encoded_field_id TEXT,
	assign TEXT,
	instance_name TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT,
	scenario TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	min_inclusive TEXT,
	max_inclusive TEXT,
	impl_length INTEGER,
	impl_min_length INTEGER,
	impl_max_length INTEGER,
	presence VARCHAR(9),
	value TEXT,
	rendering TEXT,
	encoding TEXT,
	"ActionType_id" INTEGER,
	"ActorType_id" INTEGER,
	"BlockAssignmentType_id" INTEGER,
	"ComponentType_uid" INTEGER,
	"ConceptType_id" INTEGER,
	"UniqueInline_id" INTEGER,
	"GroupType_uid" INTEGER,
	"StructureInline_id" INTEGER,
	"ResponseType_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ActionType_id") REFERENCES "ActionType" (id),
	FOREIGN KEY("ActorType_id") REFERENCES "ActorType" (id),
	FOREIGN KEY("BlockAssignmentType_id") REFERENCES "BlockAssignmentType" (id),
	FOREIGN KEY("ComponentType_uid") REFERENCES "ComponentType" (uid),
	FOREIGN KEY("ConceptType_id") REFERENCES "ConceptType" (id),
	FOREIGN KEY("UniqueInline_id") REFERENCES "UniqueInline" (id),
	FOREIGN KEY("GroupType_uid") REFERENCES "GroupType" (uid),
	FOREIGN KEY("StructureInline_id") REFERENCES "StructureInline" (id),
	FOREIGN KEY("ResponseType_id") REFERENCES "ResponseType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_FieldRefType_uid" ON "FieldRefType" (uid);

CREATE TABLE "UniqueInline" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_UniqueInline_id" ON "UniqueInline" (id);

CREATE TABLE "GroupRefType" (
	uid INTEGER NOT NULL,
	impl_min_occurs INTEGER,
	impl_max_occurs TEXT,
	presence VARCHAR(9),
	instance_name TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT,
	scenario TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	"ActionType_id" INTEGER,
	"ActorType_id" INTEGER,
	"BlockAssignmentType_id" INTEGER,
	"ComponentType_uid" INTEGER,
	"ConceptType_id" INTEGER,
	"GroupType_uid" INTEGER,
	"StructureInline_id" INTEGER,
	"ResponseType_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ActionType_id") REFERENCES "ActionType" (id),
	FOREIGN KEY("ActorType_id") REFERENCES "ActorType" (id),
	FOREIGN KEY("BlockAssignmentType_id") REFERENCES "BlockAssignmentType" (id),
	FOREIGN KEY("ComponentType_uid") REFERENCES "ComponentType" (uid),
	FOREIGN KEY("ConceptType_id") REFERENCES "ConceptType" (id),
	FOREIGN KEY("GroupType_uid") REFERENCES "GroupType" (uid),
	FOREIGN KEY("StructureInline_id") REFERENCES "StructureInline" (id),
	FOREIGN KEY("ResponseType_id") REFERENCES "ResponseType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_GroupRefType_uid" ON "GroupRefType" (uid);

CREATE TABLE "GroupType" (
	uid INTEGER NOT NULL,
	rendering TEXT,
	impl_min_occurs INTEGER,
	impl_max_occurs TEXT,
	which VARCHAR(5),
	category TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	abbr_name TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	scenario TEXT,
	scenario_ref_id TEXT,
	scenario_ref TEXT,
	"ActionType_id" INTEGER,
	"ActorType_id" INTEGER,
	"ResponseType_id" INTEGER,
	"Groups_id" INTEGER,
	num_in_group_uid INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ActionType_id") REFERENCES "ActionType" (id),
	FOREIGN KEY("ActorType_id") REFERENCES "ActorType" (id),
	FOREIGN KEY("ResponseType_id") REFERENCES "ResponseType" (id),
	FOREIGN KEY("Groups_id") REFERENCES "Groups" (id),
	FOREIGN KEY(num_in_group_uid) REFERENCES "FieldRefType" (uid),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_GroupType_uid" ON "GroupType" (uid);

CREATE TABLE "ExtensionInline" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ExtensionInline_id" ON "ExtensionInline" (id);

CREATE TABLE "StructureInline" (
	id INTEGER NOT NULL,
	which VARCHAR(5),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_StructureInline_id" ON "StructureInline" (id);

CREATE TABLE "ResponsesInline" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ResponsesInline_id" ON "ResponsesInline" (id);

CREATE TABLE "StateMachineType" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"ActorType_id" INTEGER,
	initial_id INTEGER NOT NULL,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ActorType_id") REFERENCES "ActorType" (id),
	FOREIGN KEY(initial_id) REFERENCES "StateType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_StateMachineType_id" ON "StateMachineType" (id);

CREATE TABLE "StateType" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"StateMachineType_id" INTEGER,
	onentry_id INTEGER,
	activity_id INTEGER,
	onexit_id INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("StateMachineType_id") REFERENCES "StateMachineType" (id),
	FOREIGN KEY(onentry_id) REFERENCES "ActionType" (id),
	FOREIGN KEY(activity_id) REFERENCES "ActionType" (id),
	FOREIGN KEY(onexit_id) REFERENCES "ActionType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_StateType_id" ON "StateType" (id);

CREATE TABLE "InterfaceAnnotation" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InterfaceAnnotation_id" ON "InterfaceAnnotation" (id);

CREATE TABLE "SessionsInline" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SessionsInline_id" ON "SessionsInline" (id);

CREATE TABLE "DcSimpleLiteral" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcSimpleLiteral_id" ON "DcSimpleLiteral" (id);

CREATE TABLE "DcElementContainer" (
	id INTEGER NOT NULL,
	title TEXT,
	creator TEXT,
	subject TEXT,
	description TEXT,
	publisher TEXT,
	contributor TEXT,
	date TEXT,
	format TEXT,
	source TEXT,
	language TEXT,
	relation TEXT,
	coverage TEXT,
	rights TEXT,
	alternative TEXT,
	table_of_contents TEXT,
	abstract TEXT,
	created TEXT,
	valid TEXT,
	available TEXT,
	issued TEXT,
	modified TEXT,
	date_accepted TEXT,
	date_copyrighted TEXT,
	date_submitted TEXT,
	extent TEXT,
	medium TEXT,
	is_version_of TEXT,
	has_version TEXT,
	is_replaced_by TEXT,
	replaces TEXT,
	is_required_by TEXT,
	requires TEXT,
	is_part_of TEXT,
	has_part TEXT,
	is_referenced_by TEXT,
	"references" TEXT,
	is_format_of TEXT,
	has_format TEXT,
	conforms_to TEXT,
	spatial TEXT,
	temporal TEXT,
	audience TEXT,
	accrual_method TEXT,
	accrual_periodicity TEXT,
	accrual_policy TEXT,
	instructional_method TEXT,
	provenance TEXT,
	rights_holder TEXT,
	mediator TEXT,
	education_level TEXT,
	access_rights TEXT,
	license TEXT,
	bibliographic_citation TEXT,
	type TEXT,
	identifier TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcElementContainer_id" ON "DcElementContainer" (id);

CREATE TABLE "DcAny" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcAny_id" ON "DcAny" (id);

CREATE TABLE "DcTitle" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcTitle_id" ON "DcTitle" (id);

CREATE TABLE "DcCreator" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcCreator_id" ON "DcCreator" (id);

CREATE TABLE "DcSubject" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcSubject_id" ON "DcSubject" (id);

CREATE TABLE "DcDescription" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcDescription_id" ON "DcDescription" (id);

CREATE TABLE "DcPublisher" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcPublisher_id" ON "DcPublisher" (id);

CREATE TABLE "DcContributor" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcContributor_id" ON "DcContributor" (id);

CREATE TABLE "DcDate" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcDate_id" ON "DcDate" (id);

CREATE TABLE "DcType" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcType_id" ON "DcType" (id);

CREATE TABLE "DcFormat" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcFormat_id" ON "DcFormat" (id);

CREATE TABLE "DcIdentifier" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcIdentifier_id" ON "DcIdentifier" (id);

CREATE TABLE "DcSource" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcSource_id" ON "DcSource" (id);

CREATE TABLE "DcLanguage" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcLanguage_id" ON "DcLanguage" (id);

CREATE TABLE "DcRelation" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcRelation_id" ON "DcRelation" (id);

CREATE TABLE "DcCoverage" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcCoverage_id" ON "DcCoverage" (id);

CREATE TABLE "DcRights" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcRights_id" ON "DcRights" (id);

CREATE TABLE "DcElementsGroup" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DcElementsGroup_id" ON "DcElementsGroup" (id);

CREATE TABLE "DctermsLCSH" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsLCSH_id" ON "DctermsLCSH" (id);

CREATE TABLE "DctermsMESH" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsMESH_id" ON "DctermsMESH" (id);

CREATE TABLE "DctermsDDC" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsDDC_id" ON "DctermsDDC" (id);

CREATE TABLE "DctermsLCC" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsLCC_id" ON "DctermsLCC" (id);

CREATE TABLE "DctermsUDC" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsUDC_id" ON "DctermsUDC" (id);

CREATE TABLE "DctermsPeriod" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsPeriod_id" ON "DctermsPeriod" (id);

CREATE TABLE "DctermsW3CDTF" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsW3CDTF_id" ON "DctermsW3CDTF" (id);

CREATE TABLE "DctermsDCMIType" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsDCMIType_id" ON "DctermsDCMIType" (id);

CREATE TABLE "DctermsIMT" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsIMT_id" ON "DctermsIMT" (id);

CREATE TABLE "DctermsURI" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsURI_id" ON "DctermsURI" (id);

CREATE TABLE "DctermsISO6392" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsISO6392_id" ON "DctermsISO6392" (id);

CREATE TABLE "DctermsISO6393" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsISO6393_id" ON "DctermsISO6393" (id);

CREATE TABLE "DctermsRFC1766" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsRFC1766_id" ON "DctermsRFC1766" (id);

CREATE TABLE "DctermsRFC3066" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsRFC3066_id" ON "DctermsRFC3066" (id);

CREATE TABLE "DctermsRFC4646" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsRFC4646_id" ON "DctermsRFC4646" (id);

CREATE TABLE "DctermsPoint" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsPoint_id" ON "DctermsPoint" (id);

CREATE TABLE "DctermsISO3166" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsISO3166_id" ON "DctermsISO3166" (id);

CREATE TABLE "DctermsBox" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsBox_id" ON "DctermsBox" (id);

CREATE TABLE "DctermsTGN" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsTGN_id" ON "DctermsTGN" (id);

CREATE TABLE "DctermsElementOrRefinementContainer" (
	id INTEGER NOT NULL,
	title TEXT,
	creator TEXT,
	subject TEXT,
	description TEXT,
	publisher TEXT,
	contributor TEXT,
	date TEXT,
	format TEXT,
	source TEXT,
	language TEXT,
	relation TEXT,
	coverage TEXT,
	rights TEXT,
	alternative TEXT,
	table_of_contents TEXT,
	abstract TEXT,
	created TEXT,
	valid TEXT,
	available TEXT,
	issued TEXT,
	modified TEXT,
	date_accepted TEXT,
	date_copyrighted TEXT,
	date_submitted TEXT,
	extent TEXT,
	medium TEXT,
	is_version_of TEXT,
	has_version TEXT,
	is_replaced_by TEXT,
	replaces TEXT,
	is_required_by TEXT,
	requires TEXT,
	is_part_of TEXT,
	has_part TEXT,
	is_referenced_by TEXT,
	"references" TEXT,
	is_format_of TEXT,
	has_format TEXT,
	conforms_to TEXT,
	spatial TEXT,
	temporal TEXT,
	audience TEXT,
	accrual_method TEXT,
	accrual_periodicity TEXT,
	accrual_policy TEXT,
	instructional_method TEXT,
	provenance TEXT,
	rights_holder TEXT,
	mediator TEXT,
	education_level TEXT,
	access_rights TEXT,
	license TEXT,
	bibliographic_citation TEXT,
	type TEXT,
	identifier TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsElementOrRefinementContainer_id" ON "DctermsElementOrRefinementContainer" (id);

CREATE TABLE "DctermsTitle" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsTitle_id" ON "DctermsTitle" (id);

CREATE TABLE "DctermsCreator" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsCreator_id" ON "DctermsCreator" (id);

CREATE TABLE "DctermsSubject" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsSubject_id" ON "DctermsSubject" (id);

CREATE TABLE "DctermsDescription" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsDescription_id" ON "DctermsDescription" (id);

CREATE TABLE "DctermsPublisher" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsPublisher_id" ON "DctermsPublisher" (id);

CREATE TABLE "DctermsContributor" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsContributor_id" ON "DctermsContributor" (id);

CREATE TABLE "DctermsDate" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsDate_id" ON "DctermsDate" (id);

CREATE TABLE "DctermsType" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsType_id" ON "DctermsType" (id);

CREATE TABLE "DctermsFormat" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsFormat_id" ON "DctermsFormat" (id);

CREATE TABLE "DctermsIdentifier" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsIdentifier_id" ON "DctermsIdentifier" (id);

CREATE TABLE "DctermsSource" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsSource_id" ON "DctermsSource" (id);

CREATE TABLE "DctermsLanguage" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsLanguage_id" ON "DctermsLanguage" (id);

CREATE TABLE "DctermsRelation" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsRelation_id" ON "DctermsRelation" (id);

CREATE TABLE "DctermsCoverage" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsCoverage_id" ON "DctermsCoverage" (id);

CREATE TABLE "DctermsRights" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsRights_id" ON "DctermsRights" (id);

CREATE TABLE "DctermsAlternative" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsAlternative_id" ON "DctermsAlternative" (id);

CREATE TABLE "DctermsTableOfContents" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsTableOfContents_id" ON "DctermsTableOfContents" (id);

CREATE TABLE "DctermsAbstract" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsAbstract_id" ON "DctermsAbstract" (id);

CREATE TABLE "DctermsCreated" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsCreated_id" ON "DctermsCreated" (id);

CREATE TABLE "DctermsValid" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsValid_id" ON "DctermsValid" (id);

CREATE TABLE "DctermsAvailable" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsAvailable_id" ON "DctermsAvailable" (id);

CREATE TABLE "DctermsIssued" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsIssued_id" ON "DctermsIssued" (id);

CREATE TABLE "DctermsModified" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsModified_id" ON "DctermsModified" (id);

CREATE TABLE "DctermsDateAccepted" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsDateAccepted_id" ON "DctermsDateAccepted" (id);

CREATE TABLE "DctermsDateCopyrighted" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsDateCopyrighted_id" ON "DctermsDateCopyrighted" (id);

CREATE TABLE "DctermsDateSubmitted" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsDateSubmitted_id" ON "DctermsDateSubmitted" (id);

CREATE TABLE "DctermsExtent" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsExtent_id" ON "DctermsExtent" (id);

CREATE TABLE "DctermsMedium" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsMedium_id" ON "DctermsMedium" (id);

CREATE TABLE "DctermsIsVersionOf" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsIsVersionOf_id" ON "DctermsIsVersionOf" (id);

CREATE TABLE "DctermsHasVersion" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsHasVersion_id" ON "DctermsHasVersion" (id);

CREATE TABLE "DctermsIsReplacedBy" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsIsReplacedBy_id" ON "DctermsIsReplacedBy" (id);

CREATE TABLE "DctermsReplaces" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsReplaces_id" ON "DctermsReplaces" (id);

CREATE TABLE "DctermsIsRequiredBy" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsIsRequiredBy_id" ON "DctermsIsRequiredBy" (id);

CREATE TABLE "DctermsRequires" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsRequires_id" ON "DctermsRequires" (id);

CREATE TABLE "DctermsIsPartOf" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsIsPartOf_id" ON "DctermsIsPartOf" (id);

CREATE TABLE "DctermsHasPart" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsHasPart_id" ON "DctermsHasPart" (id);

CREATE TABLE "DctermsIsReferencedBy" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsIsReferencedBy_id" ON "DctermsIsReferencedBy" (id);

CREATE TABLE "DctermsReferences" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsReferences_id" ON "DctermsReferences" (id);

CREATE TABLE "DctermsIsFormatOf" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsIsFormatOf_id" ON "DctermsIsFormatOf" (id);

CREATE TABLE "DctermsHasFormat" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsHasFormat_id" ON "DctermsHasFormat" (id);

CREATE TABLE "DctermsConformsTo" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsConformsTo_id" ON "DctermsConformsTo" (id);

CREATE TABLE "DctermsSpatial" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsSpatial_id" ON "DctermsSpatial" (id);

CREATE TABLE "DctermsTemporal" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsTemporal_id" ON "DctermsTemporal" (id);

CREATE TABLE "DctermsAudience" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsAudience_id" ON "DctermsAudience" (id);

CREATE TABLE "DctermsAccrualMethod" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsAccrualMethod_id" ON "DctermsAccrualMethod" (id);

CREATE TABLE "DctermsAccrualPeriodicity" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsAccrualPeriodicity_id" ON "DctermsAccrualPeriodicity" (id);

CREATE TABLE "DctermsAccrualPolicy" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsAccrualPolicy_id" ON "DctermsAccrualPolicy" (id);

CREATE TABLE "DctermsInstructionalMethod" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsInstructionalMethod_id" ON "DctermsInstructionalMethod" (id);

CREATE TABLE "DctermsProvenance" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsProvenance_id" ON "DctermsProvenance" (id);

CREATE TABLE "DctermsRightsHolder" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsRightsHolder_id" ON "DctermsRightsHolder" (id);

CREATE TABLE "DctermsMediator" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsMediator_id" ON "DctermsMediator" (id);

CREATE TABLE "DctermsEducationLevel" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsEducationLevel_id" ON "DctermsEducationLevel" (id);

CREATE TABLE "DctermsAccessRights" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsAccessRights_id" ON "DctermsAccessRights" (id);

CREATE TABLE "DctermsLicense" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsLicense_id" ON "DctermsLicense" (id);

CREATE TABLE "DctermsBibliographicCitation" (
	id INTEGER NOT NULL,
	value TEXT,
	lang TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsBibliographicCitation_id" ON "DctermsBibliographicCitation" (id);

CREATE TABLE "DctermsElementsAndRefinementsGroup" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_DctermsElementsAndRefinementsGroup_id" ON "DctermsElementsAndRefinementsGroup" (id);

CREATE TABLE "XmlSpecialAttrs" (
	uid INTEGER NOT NULL,
	base TEXT,
	lang TEXT,
	space TEXT,
	id TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_XmlSpecialAttrs_uid" ON "XmlSpecialAttrs" (uid);

CREATE TABLE "XmlGlobalAttributes" (
	uid INTEGER NOT NULL,
	lang TEXT,
	space VARCHAR(8),
	base TEXT,
	id TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_XmlGlobalAttributes_uid" ON "XmlGlobalAttributes" (uid);

CREATE TABLE "Appinfo" (
	id INTEGER NOT NULL,
	spec_url TEXT,
	value TEXT,
	lang_id TEXT,
	purpose TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	"Annotation_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Annotation_id") REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Appinfo_id" ON "Appinfo" (id);

CREATE TABLE "ComponentRuleType" (
	id INTEGER NOT NULL,
	"when" TEXT NOT NULL,
	presence VARCHAR(9),
	name TEXT,
	"ComponentRefType_uid" INTEGER,
	"GroupRefType_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ComponentRefType_uid") REFERENCES "ComponentRefType" (uid),
	FOREIGN KEY("GroupRefType_uid") REFERENCES "GroupRefType" (uid)
);
CREATE INDEX "ix_ComponentRuleType_id" ON "ComponentRuleType" (id);

CREATE TABLE "Documentation" (
	id INTEGER NOT NULL,
	value TEXT,
	lang_id TEXT,
	purpose TEXT,
	content_type TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	"Annotation_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Annotation_id") REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Documentation_id" ON "Documentation" (id);

CREATE TABLE "IdentifiersType" (
	id INTEGER NOT NULL,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_IdentifiersType_id" ON "IdentifiersType" (id);

CREATE TABLE "ResponseType" (
	id INTEGER NOT NULL,
	"when" TEXT,
	sync VARCHAR(12),
	name TEXT,
	"ResponsesInline_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ResponsesInline_id") REFERENCES "ResponsesInline" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_ResponseType_id" ON "ResponseType" (id);

CREATE TABLE "TransitionType" (
	id INTEGER NOT NULL,
	"when" TEXT,
	target TEXT NOT NULL,
	name TEXT NOT NULL,
	"StateType_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("StateType_id") REFERENCES "StateType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_TransitionType_id" ON "TransitionType" (id);

CREATE TABLE "InterfaceAppinfo" (
	id INTEGER NOT NULL,
	spec_url TEXT,
	value TEXT,
	lang_id TEXT,
	purpose TEXT,
	"InterfaceAnnotation_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InterfaceAnnotation_id") REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_InterfaceAppinfo_id" ON "InterfaceAppinfo" (id);

CREATE TABLE "BaseInterfaceType" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_BaseInterfaceType_id" ON "BaseInterfaceType" (id);

CREATE TABLE "InterfaceDocumentation" (
	id INTEGER NOT NULL,
	value TEXT,
	lang_id TEXT,
	purpose TEXT,
	content_type TEXT,
	"InterfaceAnnotation_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InterfaceAnnotation_id") REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_InterfaceDocumentation_id" ON "InterfaceDocumentation" (id);

CREATE TABLE "SessionType" (
	id INTEGER NOT NULL,
	role VARCHAR(9),
	security_keys TEXT,
	activation_time DATETIME,
	deactivation_time DATETIME,
	name TEXT NOT NULL,
	"SessionsInline_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("SessionsInline_id") REFERENCES "SessionsInline" (id),
	FOREIGN KEY(annotation_id) REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_SessionType_id" ON "SessionType" (id);

CREATE TABLE "Actors" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Actors_id" ON "Actors" (id);

CREATE TABLE "Categories" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Categories_id" ON "Categories" (id);

CREATE TABLE "CodeSets" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_CodeSets_id" ON "CodeSets" (id);

CREATE TABLE "Components" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Components_id" ON "Components" (id);

CREATE TABLE "Concepts" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Concepts_id" ON "Concepts" (id);

CREATE TABLE "Datatypes" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Datatypes_id" ON "Datatypes" (id);

CREATE TABLE "Fields" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Fields_id" ON "Fields" (id);

CREATE TABLE "Groups" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Groups_id" ON "Groups" (id);

CREATE TABLE "Messages" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Messages_id" ON "Messages" (id);

CREATE TABLE "Scenarios" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Scenarios_id" ON "Scenarios" (id);

CREATE TABLE "Sections" (
	id INTEGER NOT NULL,
	base TEXT,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Sections_id" ON "Sections" (id);

CREATE TABLE "Interfaces" (
	id INTEGER NOT NULL,
	metadata_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(metadata_id) REFERENCES "DctermsElementOrRefinementContainer" (id)
);
CREATE INDEX "ix_Interfaces_id" ON "Interfaces" (id);

CREATE TABLE "ActionType_assign" (
	"ActionType_id" INTEGER,
	assign TEXT,
	PRIMARY KEY ("ActionType_id", assign),
	FOREIGN KEY("ActionType_id") REFERENCES "ActionType" (id)
);
CREATE INDEX "ix_ActionType_assign_ActionType_id" ON "ActionType_assign" ("ActionType_id");
CREATE INDEX "ix_ActionType_assign_assign" ON "ActionType_assign" (assign);

CREATE TABLE "ExtensionInline_content" (
	"ExtensionInline_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("ExtensionInline_id", content),
	FOREIGN KEY("ExtensionInline_id") REFERENCES "ExtensionInline" (id)
);
CREATE INDEX "ix_ExtensionInline_content_content" ON "ExtensionInline_content" (content);
CREATE INDEX "ix_ExtensionInline_content_ExtensionInline_id" ON "ExtensionInline_content" ("ExtensionInline_id");

CREATE TABLE "DcSimpleLiteral_content" (
	"DcSimpleLiteral_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcSimpleLiteral_id", content),
	FOREIGN KEY("DcSimpleLiteral_id") REFERENCES "DcSimpleLiteral" (id)
);
CREATE INDEX "ix_DcSimpleLiteral_content_DcSimpleLiteral_id" ON "DcSimpleLiteral_content" ("DcSimpleLiteral_id");
CREATE INDEX "ix_DcSimpleLiteral_content_content" ON "DcSimpleLiteral_content" (content);

CREATE TABLE "DcAny_content" (
	"DcAny_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcAny_id", content),
	FOREIGN KEY("DcAny_id") REFERENCES "DcAny" (id)
);
CREATE INDEX "ix_DcAny_content_DcAny_id" ON "DcAny_content" ("DcAny_id");
CREATE INDEX "ix_DcAny_content_content" ON "DcAny_content" (content);

CREATE TABLE "DcTitle_content" (
	"DcTitle_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcTitle_id", content),
	FOREIGN KEY("DcTitle_id") REFERENCES "DcTitle" (id)
);
CREATE INDEX "ix_DcTitle_content_DcTitle_id" ON "DcTitle_content" ("DcTitle_id");
CREATE INDEX "ix_DcTitle_content_content" ON "DcTitle_content" (content);

CREATE TABLE "DcCreator_content" (
	"DcCreator_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcCreator_id", content),
	FOREIGN KEY("DcCreator_id") REFERENCES "DcCreator" (id)
);
CREATE INDEX "ix_DcCreator_content_DcCreator_id" ON "DcCreator_content" ("DcCreator_id");
CREATE INDEX "ix_DcCreator_content_content" ON "DcCreator_content" (content);

CREATE TABLE "DcSubject_content" (
	"DcSubject_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcSubject_id", content),
	FOREIGN KEY("DcSubject_id") REFERENCES "DcSubject" (id)
);
CREATE INDEX "ix_DcSubject_content_DcSubject_id" ON "DcSubject_content" ("DcSubject_id");
CREATE INDEX "ix_DcSubject_content_content" ON "DcSubject_content" (content);

CREATE TABLE "DcDescription_content" (
	"DcDescription_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcDescription_id", content),
	FOREIGN KEY("DcDescription_id") REFERENCES "DcDescription" (id)
);
CREATE INDEX "ix_DcDescription_content_DcDescription_id" ON "DcDescription_content" ("DcDescription_id");
CREATE INDEX "ix_DcDescription_content_content" ON "DcDescription_content" (content);

CREATE TABLE "DcPublisher_content" (
	"DcPublisher_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcPublisher_id", content),
	FOREIGN KEY("DcPublisher_id") REFERENCES "DcPublisher" (id)
);
CREATE INDEX "ix_DcPublisher_content_DcPublisher_id" ON "DcPublisher_content" ("DcPublisher_id");
CREATE INDEX "ix_DcPublisher_content_content" ON "DcPublisher_content" (content);

CREATE TABLE "DcContributor_content" (
	"DcContributor_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcContributor_id", content),
	FOREIGN KEY("DcContributor_id") REFERENCES "DcContributor" (id)
);
CREATE INDEX "ix_DcContributor_content_DcContributor_id" ON "DcContributor_content" ("DcContributor_id");
CREATE INDEX "ix_DcContributor_content_content" ON "DcContributor_content" (content);

CREATE TABLE "DcDate_content" (
	"DcDate_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcDate_id", content),
	FOREIGN KEY("DcDate_id") REFERENCES "DcDate" (id)
);
CREATE INDEX "ix_DcDate_content_DcDate_id" ON "DcDate_content" ("DcDate_id");
CREATE INDEX "ix_DcDate_content_content" ON "DcDate_content" (content);

CREATE TABLE "DcType_content" (
	"DcType_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcType_id", content),
	FOREIGN KEY("DcType_id") REFERENCES "DcType" (id)
);
CREATE INDEX "ix_DcType_content_DcType_id" ON "DcType_content" ("DcType_id");
CREATE INDEX "ix_DcType_content_content" ON "DcType_content" (content);

CREATE TABLE "DcFormat_content" (
	"DcFormat_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcFormat_id", content),
	FOREIGN KEY("DcFormat_id") REFERENCES "DcFormat" (id)
);
CREATE INDEX "ix_DcFormat_content_DcFormat_id" ON "DcFormat_content" ("DcFormat_id");
CREATE INDEX "ix_DcFormat_content_content" ON "DcFormat_content" (content);

CREATE TABLE "DcIdentifier_content" (
	"DcIdentifier_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcIdentifier_id", content),
	FOREIGN KEY("DcIdentifier_id") REFERENCES "DcIdentifier" (id)
);
CREATE INDEX "ix_DcIdentifier_content_DcIdentifier_id" ON "DcIdentifier_content" ("DcIdentifier_id");
CREATE INDEX "ix_DcIdentifier_content_content" ON "DcIdentifier_content" (content);

CREATE TABLE "DcSource_content" (
	"DcSource_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcSource_id", content),
	FOREIGN KEY("DcSource_id") REFERENCES "DcSource" (id)
);
CREATE INDEX "ix_DcSource_content_DcSource_id" ON "DcSource_content" ("DcSource_id");
CREATE INDEX "ix_DcSource_content_content" ON "DcSource_content" (content);

CREATE TABLE "DcLanguage_content" (
	"DcLanguage_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcLanguage_id", content),
	FOREIGN KEY("DcLanguage_id") REFERENCES "DcLanguage" (id)
);
CREATE INDEX "ix_DcLanguage_content_DcLanguage_id" ON "DcLanguage_content" ("DcLanguage_id");
CREATE INDEX "ix_DcLanguage_content_content" ON "DcLanguage_content" (content);

CREATE TABLE "DcRelation_content" (
	"DcRelation_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcRelation_id", content),
	FOREIGN KEY("DcRelation_id") REFERENCES "DcRelation" (id)
);
CREATE INDEX "ix_DcRelation_content_DcRelation_id" ON "DcRelation_content" ("DcRelation_id");
CREATE INDEX "ix_DcRelation_content_content" ON "DcRelation_content" (content);

CREATE TABLE "DcCoverage_content" (
	"DcCoverage_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcCoverage_id", content),
	FOREIGN KEY("DcCoverage_id") REFERENCES "DcCoverage" (id)
);
CREATE INDEX "ix_DcCoverage_content_DcCoverage_id" ON "DcCoverage_content" ("DcCoverage_id");
CREATE INDEX "ix_DcCoverage_content_content" ON "DcCoverage_content" (content);

CREATE TABLE "DcRights_content" (
	"DcRights_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DcRights_id", content),
	FOREIGN KEY("DcRights_id") REFERENCES "DcRights" (id)
);
CREATE INDEX "ix_DcRights_content_DcRights_id" ON "DcRights_content" ("DcRights_id");
CREATE INDEX "ix_DcRights_content_content" ON "DcRights_content" (content);

CREATE TABLE "DctermsLCSH_content" (
	"DctermsLCSH_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsLCSH_id", content),
	FOREIGN KEY("DctermsLCSH_id") REFERENCES "DctermsLCSH" (id)
);
CREATE INDEX "ix_DctermsLCSH_content_DctermsLCSH_id" ON "DctermsLCSH_content" ("DctermsLCSH_id");
CREATE INDEX "ix_DctermsLCSH_content_content" ON "DctermsLCSH_content" (content);

CREATE TABLE "DctermsMESH_content" (
	"DctermsMESH_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsMESH_id", content),
	FOREIGN KEY("DctermsMESH_id") REFERENCES "DctermsMESH" (id)
);
CREATE INDEX "ix_DctermsMESH_content_DctermsMESH_id" ON "DctermsMESH_content" ("DctermsMESH_id");
CREATE INDEX "ix_DctermsMESH_content_content" ON "DctermsMESH_content" (content);

CREATE TABLE "DctermsDDC_content" (
	"DctermsDDC_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsDDC_id", content),
	FOREIGN KEY("DctermsDDC_id") REFERENCES "DctermsDDC" (id)
);
CREATE INDEX "ix_DctermsDDC_content_DctermsDDC_id" ON "DctermsDDC_content" ("DctermsDDC_id");
CREATE INDEX "ix_DctermsDDC_content_content" ON "DctermsDDC_content" (content);

CREATE TABLE "DctermsLCC_content" (
	"DctermsLCC_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsLCC_id", content),
	FOREIGN KEY("DctermsLCC_id") REFERENCES "DctermsLCC" (id)
);
CREATE INDEX "ix_DctermsLCC_content_DctermsLCC_id" ON "DctermsLCC_content" ("DctermsLCC_id");
CREATE INDEX "ix_DctermsLCC_content_content" ON "DctermsLCC_content" (content);

CREATE TABLE "DctermsUDC_content" (
	"DctermsUDC_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsUDC_id", content),
	FOREIGN KEY("DctermsUDC_id") REFERENCES "DctermsUDC" (id)
);
CREATE INDEX "ix_DctermsUDC_content_DctermsUDC_id" ON "DctermsUDC_content" ("DctermsUDC_id");
CREATE INDEX "ix_DctermsUDC_content_content" ON "DctermsUDC_content" (content);

CREATE TABLE "DctermsPeriod_content" (
	"DctermsPeriod_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsPeriod_id", content),
	FOREIGN KEY("DctermsPeriod_id") REFERENCES "DctermsPeriod" (id)
);
CREATE INDEX "ix_DctermsPeriod_content_DctermsPeriod_id" ON "DctermsPeriod_content" ("DctermsPeriod_id");
CREATE INDEX "ix_DctermsPeriod_content_content" ON "DctermsPeriod_content" (content);

CREATE TABLE "DctermsW3CDTF_content" (
	"DctermsW3CDTF_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsW3CDTF_id", content),
	FOREIGN KEY("DctermsW3CDTF_id") REFERENCES "DctermsW3CDTF" (id)
);
CREATE INDEX "ix_DctermsW3CDTF_content_DctermsW3CDTF_id" ON "DctermsW3CDTF_content" ("DctermsW3CDTF_id");
CREATE INDEX "ix_DctermsW3CDTF_content_content" ON "DctermsW3CDTF_content" (content);

CREATE TABLE "DctermsDCMIType_content" (
	"DctermsDCMIType_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsDCMIType_id", content),
	FOREIGN KEY("DctermsDCMIType_id") REFERENCES "DctermsDCMIType" (id)
);
CREATE INDEX "ix_DctermsDCMIType_content_DctermsDCMIType_id" ON "DctermsDCMIType_content" ("DctermsDCMIType_id");
CREATE INDEX "ix_DctermsDCMIType_content_content" ON "DctermsDCMIType_content" (content);

CREATE TABLE "DctermsIMT_content" (
	"DctermsIMT_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsIMT_id", content),
	FOREIGN KEY("DctermsIMT_id") REFERENCES "DctermsIMT" (id)
);
CREATE INDEX "ix_DctermsIMT_content_DctermsIMT_id" ON "DctermsIMT_content" ("DctermsIMT_id");
CREATE INDEX "ix_DctermsIMT_content_content" ON "DctermsIMT_content" (content);

CREATE TABLE "DctermsURI_content" (
	"DctermsURI_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsURI_id", content),
	FOREIGN KEY("DctermsURI_id") REFERENCES "DctermsURI" (id)
);
CREATE INDEX "ix_DctermsURI_content_DctermsURI_id" ON "DctermsURI_content" ("DctermsURI_id");
CREATE INDEX "ix_DctermsURI_content_content" ON "DctermsURI_content" (content);

CREATE TABLE "DctermsISO6392_content" (
	"DctermsISO6392_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsISO6392_id", content),
	FOREIGN KEY("DctermsISO6392_id") REFERENCES "DctermsISO6392" (id)
);
CREATE INDEX "ix_DctermsISO6392_content_DctermsISO6392_id" ON "DctermsISO6392_content" ("DctermsISO6392_id");
CREATE INDEX "ix_DctermsISO6392_content_content" ON "DctermsISO6392_content" (content);

CREATE TABLE "DctermsISO6393_content" (
	"DctermsISO6393_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsISO6393_id", content),
	FOREIGN KEY("DctermsISO6393_id") REFERENCES "DctermsISO6393" (id)
);
CREATE INDEX "ix_DctermsISO6393_content_DctermsISO6393_id" ON "DctermsISO6393_content" ("DctermsISO6393_id");
CREATE INDEX "ix_DctermsISO6393_content_content" ON "DctermsISO6393_content" (content);

CREATE TABLE "DctermsRFC1766_content" (
	"DctermsRFC1766_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsRFC1766_id", content),
	FOREIGN KEY("DctermsRFC1766_id") REFERENCES "DctermsRFC1766" (id)
);
CREATE INDEX "ix_DctermsRFC1766_content_DctermsRFC1766_id" ON "DctermsRFC1766_content" ("DctermsRFC1766_id");
CREATE INDEX "ix_DctermsRFC1766_content_content" ON "DctermsRFC1766_content" (content);

CREATE TABLE "DctermsRFC3066_content" (
	"DctermsRFC3066_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsRFC3066_id", content),
	FOREIGN KEY("DctermsRFC3066_id") REFERENCES "DctermsRFC3066" (id)
);
CREATE INDEX "ix_DctermsRFC3066_content_DctermsRFC3066_id" ON "DctermsRFC3066_content" ("DctermsRFC3066_id");
CREATE INDEX "ix_DctermsRFC3066_content_content" ON "DctermsRFC3066_content" (content);

CREATE TABLE "DctermsRFC4646_content" (
	"DctermsRFC4646_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsRFC4646_id", content),
	FOREIGN KEY("DctermsRFC4646_id") REFERENCES "DctermsRFC4646" (id)
);
CREATE INDEX "ix_DctermsRFC4646_content_DctermsRFC4646_id" ON "DctermsRFC4646_content" ("DctermsRFC4646_id");
CREATE INDEX "ix_DctermsRFC4646_content_content" ON "DctermsRFC4646_content" (content);

CREATE TABLE "DctermsPoint_content" (
	"DctermsPoint_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsPoint_id", content),
	FOREIGN KEY("DctermsPoint_id") REFERENCES "DctermsPoint" (id)
);
CREATE INDEX "ix_DctermsPoint_content_DctermsPoint_id" ON "DctermsPoint_content" ("DctermsPoint_id");
CREATE INDEX "ix_DctermsPoint_content_content" ON "DctermsPoint_content" (content);

CREATE TABLE "DctermsISO3166_content" (
	"DctermsISO3166_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsISO3166_id", content),
	FOREIGN KEY("DctermsISO3166_id") REFERENCES "DctermsISO3166" (id)
);
CREATE INDEX "ix_DctermsISO3166_content_DctermsISO3166_id" ON "DctermsISO3166_content" ("DctermsISO3166_id");
CREATE INDEX "ix_DctermsISO3166_content_content" ON "DctermsISO3166_content" (content);

CREATE TABLE "DctermsBox_content" (
	"DctermsBox_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsBox_id", content),
	FOREIGN KEY("DctermsBox_id") REFERENCES "DctermsBox" (id)
);
CREATE INDEX "ix_DctermsBox_content_DctermsBox_id" ON "DctermsBox_content" ("DctermsBox_id");
CREATE INDEX "ix_DctermsBox_content_content" ON "DctermsBox_content" (content);

CREATE TABLE "DctermsTGN_content" (
	"DctermsTGN_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsTGN_id", content),
	FOREIGN KEY("DctermsTGN_id") REFERENCES "DctermsTGN" (id)
);
CREATE INDEX "ix_DctermsTGN_content_DctermsTGN_id" ON "DctermsTGN_content" ("DctermsTGN_id");
CREATE INDEX "ix_DctermsTGN_content_content" ON "DctermsTGN_content" (content);

CREATE TABLE "DctermsTitle_content" (
	"DctermsTitle_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsTitle_id", content),
	FOREIGN KEY("DctermsTitle_id") REFERENCES "DctermsTitle" (id)
);
CREATE INDEX "ix_DctermsTitle_content_DctermsTitle_id" ON "DctermsTitle_content" ("DctermsTitle_id");
CREATE INDEX "ix_DctermsTitle_content_content" ON "DctermsTitle_content" (content);

CREATE TABLE "DctermsCreator_content" (
	"DctermsCreator_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsCreator_id", content),
	FOREIGN KEY("DctermsCreator_id") REFERENCES "DctermsCreator" (id)
);
CREATE INDEX "ix_DctermsCreator_content_DctermsCreator_id" ON "DctermsCreator_content" ("DctermsCreator_id");
CREATE INDEX "ix_DctermsCreator_content_content" ON "DctermsCreator_content" (content);

CREATE TABLE "DctermsSubject_content" (
	"DctermsSubject_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsSubject_id", content),
	FOREIGN KEY("DctermsSubject_id") REFERENCES "DctermsSubject" (id)
);
CREATE INDEX "ix_DctermsSubject_content_content" ON "DctermsSubject_content" (content);
CREATE INDEX "ix_DctermsSubject_content_DctermsSubject_id" ON "DctermsSubject_content" ("DctermsSubject_id");

CREATE TABLE "DctermsDescription_content" (
	"DctermsDescription_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsDescription_id", content),
	FOREIGN KEY("DctermsDescription_id") REFERENCES "DctermsDescription" (id)
);
CREATE INDEX "ix_DctermsDescription_content_content" ON "DctermsDescription_content" (content);
CREATE INDEX "ix_DctermsDescription_content_DctermsDescription_id" ON "DctermsDescription_content" ("DctermsDescription_id");

CREATE TABLE "DctermsPublisher_content" (
	"DctermsPublisher_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsPublisher_id", content),
	FOREIGN KEY("DctermsPublisher_id") REFERENCES "DctermsPublisher" (id)
);
CREATE INDEX "ix_DctermsPublisher_content_DctermsPublisher_id" ON "DctermsPublisher_content" ("DctermsPublisher_id");
CREATE INDEX "ix_DctermsPublisher_content_content" ON "DctermsPublisher_content" (content);

CREATE TABLE "DctermsContributor_content" (
	"DctermsContributor_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsContributor_id", content),
	FOREIGN KEY("DctermsContributor_id") REFERENCES "DctermsContributor" (id)
);
CREATE INDEX "ix_DctermsContributor_content_DctermsContributor_id" ON "DctermsContributor_content" ("DctermsContributor_id");
CREATE INDEX "ix_DctermsContributor_content_content" ON "DctermsContributor_content" (content);

CREATE TABLE "DctermsDate_content" (
	"DctermsDate_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsDate_id", content),
	FOREIGN KEY("DctermsDate_id") REFERENCES "DctermsDate" (id)
);
CREATE INDEX "ix_DctermsDate_content_DctermsDate_id" ON "DctermsDate_content" ("DctermsDate_id");
CREATE INDEX "ix_DctermsDate_content_content" ON "DctermsDate_content" (content);

CREATE TABLE "DctermsType_content" (
	"DctermsType_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsType_id", content),
	FOREIGN KEY("DctermsType_id") REFERENCES "DctermsType" (id)
);
CREATE INDEX "ix_DctermsType_content_DctermsType_id" ON "DctermsType_content" ("DctermsType_id");
CREATE INDEX "ix_DctermsType_content_content" ON "DctermsType_content" (content);

CREATE TABLE "DctermsFormat_content" (
	"DctermsFormat_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsFormat_id", content),
	FOREIGN KEY("DctermsFormat_id") REFERENCES "DctermsFormat" (id)
);
CREATE INDEX "ix_DctermsFormat_content_DctermsFormat_id" ON "DctermsFormat_content" ("DctermsFormat_id");
CREATE INDEX "ix_DctermsFormat_content_content" ON "DctermsFormat_content" (content);

CREATE TABLE "DctermsIdentifier_content" (
	"DctermsIdentifier_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsIdentifier_id", content),
	FOREIGN KEY("DctermsIdentifier_id") REFERENCES "DctermsIdentifier" (id)
);
CREATE INDEX "ix_DctermsIdentifier_content_DctermsIdentifier_id" ON "DctermsIdentifier_content" ("DctermsIdentifier_id");
CREATE INDEX "ix_DctermsIdentifier_content_content" ON "DctermsIdentifier_content" (content);

CREATE TABLE "DctermsSource_content" (
	"DctermsSource_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsSource_id", content),
	FOREIGN KEY("DctermsSource_id") REFERENCES "DctermsSource" (id)
);
CREATE INDEX "ix_DctermsSource_content_DctermsSource_id" ON "DctermsSource_content" ("DctermsSource_id");
CREATE INDEX "ix_DctermsSource_content_content" ON "DctermsSource_content" (content);

CREATE TABLE "DctermsLanguage_content" (
	"DctermsLanguage_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsLanguage_id", content),
	FOREIGN KEY("DctermsLanguage_id") REFERENCES "DctermsLanguage" (id)
);
CREATE INDEX "ix_DctermsLanguage_content_DctermsLanguage_id" ON "DctermsLanguage_content" ("DctermsLanguage_id");
CREATE INDEX "ix_DctermsLanguage_content_content" ON "DctermsLanguage_content" (content);

CREATE TABLE "DctermsRelation_content" (
	"DctermsRelation_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsRelation_id", content),
	FOREIGN KEY("DctermsRelation_id") REFERENCES "DctermsRelation" (id)
);
CREATE INDEX "ix_DctermsRelation_content_DctermsRelation_id" ON "DctermsRelation_content" ("DctermsRelation_id");
CREATE INDEX "ix_DctermsRelation_content_content" ON "DctermsRelation_content" (content);

CREATE TABLE "DctermsCoverage_content" (
	"DctermsCoverage_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsCoverage_id", content),
	FOREIGN KEY("DctermsCoverage_id") REFERENCES "DctermsCoverage" (id)
);
CREATE INDEX "ix_DctermsCoverage_content_DctermsCoverage_id" ON "DctermsCoverage_content" ("DctermsCoverage_id");
CREATE INDEX "ix_DctermsCoverage_content_content" ON "DctermsCoverage_content" (content);

CREATE TABLE "DctermsRights_content" (
	"DctermsRights_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsRights_id", content),
	FOREIGN KEY("DctermsRights_id") REFERENCES "DctermsRights" (id)
);
CREATE INDEX "ix_DctermsRights_content_DctermsRights_id" ON "DctermsRights_content" ("DctermsRights_id");
CREATE INDEX "ix_DctermsRights_content_content" ON "DctermsRights_content" (content);

CREATE TABLE "DctermsAlternative_content" (
	"DctermsAlternative_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsAlternative_id", content),
	FOREIGN KEY("DctermsAlternative_id") REFERENCES "DctermsAlternative" (id)
);
CREATE INDEX "ix_DctermsAlternative_content_DctermsAlternative_id" ON "DctermsAlternative_content" ("DctermsAlternative_id");
CREATE INDEX "ix_DctermsAlternative_content_content" ON "DctermsAlternative_content" (content);

CREATE TABLE "DctermsTableOfContents_content" (
	"DctermsTableOfContents_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsTableOfContents_id", content),
	FOREIGN KEY("DctermsTableOfContents_id") REFERENCES "DctermsTableOfContents" (id)
);
CREATE INDEX "ix_DctermsTableOfContents_content_DctermsTableOfContents_id" ON "DctermsTableOfContents_content" ("DctermsTableOfContents_id");
CREATE INDEX "ix_DctermsTableOfContents_content_content" ON "DctermsTableOfContents_content" (content);

CREATE TABLE "DctermsAbstract_content" (
	"DctermsAbstract_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsAbstract_id", content),
	FOREIGN KEY("DctermsAbstract_id") REFERENCES "DctermsAbstract" (id)
);
CREATE INDEX "ix_DctermsAbstract_content_DctermsAbstract_id" ON "DctermsAbstract_content" ("DctermsAbstract_id");
CREATE INDEX "ix_DctermsAbstract_content_content" ON "DctermsAbstract_content" (content);

CREATE TABLE "DctermsCreated_content" (
	"DctermsCreated_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsCreated_id", content),
	FOREIGN KEY("DctermsCreated_id") REFERENCES "DctermsCreated" (id)
);
CREATE INDEX "ix_DctermsCreated_content_DctermsCreated_id" ON "DctermsCreated_content" ("DctermsCreated_id");
CREATE INDEX "ix_DctermsCreated_content_content" ON "DctermsCreated_content" (content);

CREATE TABLE "DctermsValid_content" (
	"DctermsValid_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsValid_id", content),
	FOREIGN KEY("DctermsValid_id") REFERENCES "DctermsValid" (id)
);
CREATE INDEX "ix_DctermsValid_content_DctermsValid_id" ON "DctermsValid_content" ("DctermsValid_id");
CREATE INDEX "ix_DctermsValid_content_content" ON "DctermsValid_content" (content);

CREATE TABLE "DctermsAvailable_content" (
	"DctermsAvailable_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsAvailable_id", content),
	FOREIGN KEY("DctermsAvailable_id") REFERENCES "DctermsAvailable" (id)
);
CREATE INDEX "ix_DctermsAvailable_content_DctermsAvailable_id" ON "DctermsAvailable_content" ("DctermsAvailable_id");
CREATE INDEX "ix_DctermsAvailable_content_content" ON "DctermsAvailable_content" (content);

CREATE TABLE "DctermsIssued_content" (
	"DctermsIssued_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsIssued_id", content),
	FOREIGN KEY("DctermsIssued_id") REFERENCES "DctermsIssued" (id)
);
CREATE INDEX "ix_DctermsIssued_content_DctermsIssued_id" ON "DctermsIssued_content" ("DctermsIssued_id");
CREATE INDEX "ix_DctermsIssued_content_content" ON "DctermsIssued_content" (content);

CREATE TABLE "DctermsModified_content" (
	"DctermsModified_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsModified_id", content),
	FOREIGN KEY("DctermsModified_id") REFERENCES "DctermsModified" (id)
);
CREATE INDEX "ix_DctermsModified_content_DctermsModified_id" ON "DctermsModified_content" ("DctermsModified_id");
CREATE INDEX "ix_DctermsModified_content_content" ON "DctermsModified_content" (content);

CREATE TABLE "DctermsDateAccepted_content" (
	"DctermsDateAccepted_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsDateAccepted_id", content),
	FOREIGN KEY("DctermsDateAccepted_id") REFERENCES "DctermsDateAccepted" (id)
);
CREATE INDEX "ix_DctermsDateAccepted_content_DctermsDateAccepted_id" ON "DctermsDateAccepted_content" ("DctermsDateAccepted_id");
CREATE INDEX "ix_DctermsDateAccepted_content_content" ON "DctermsDateAccepted_content" (content);

CREATE TABLE "DctermsDateCopyrighted_content" (
	"DctermsDateCopyrighted_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsDateCopyrighted_id", content),
	FOREIGN KEY("DctermsDateCopyrighted_id") REFERENCES "DctermsDateCopyrighted" (id)
);
CREATE INDEX "ix_DctermsDateCopyrighted_content_DctermsDateCopyrighted_id" ON "DctermsDateCopyrighted_content" ("DctermsDateCopyrighted_id");
CREATE INDEX "ix_DctermsDateCopyrighted_content_content" ON "DctermsDateCopyrighted_content" (content);

CREATE TABLE "DctermsDateSubmitted_content" (
	"DctermsDateSubmitted_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsDateSubmitted_id", content),
	FOREIGN KEY("DctermsDateSubmitted_id") REFERENCES "DctermsDateSubmitted" (id)
);
CREATE INDEX "ix_DctermsDateSubmitted_content_DctermsDateSubmitted_id" ON "DctermsDateSubmitted_content" ("DctermsDateSubmitted_id");
CREATE INDEX "ix_DctermsDateSubmitted_content_content" ON "DctermsDateSubmitted_content" (content);

CREATE TABLE "DctermsExtent_content" (
	"DctermsExtent_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsExtent_id", content),
	FOREIGN KEY("DctermsExtent_id") REFERENCES "DctermsExtent" (id)
);
CREATE INDEX "ix_DctermsExtent_content_DctermsExtent_id" ON "DctermsExtent_content" ("DctermsExtent_id");
CREATE INDEX "ix_DctermsExtent_content_content" ON "DctermsExtent_content" (content);

CREATE TABLE "DctermsMedium_content" (
	"DctermsMedium_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsMedium_id", content),
	FOREIGN KEY("DctermsMedium_id") REFERENCES "DctermsMedium" (id)
);
CREATE INDEX "ix_DctermsMedium_content_DctermsMedium_id" ON "DctermsMedium_content" ("DctermsMedium_id");
CREATE INDEX "ix_DctermsMedium_content_content" ON "DctermsMedium_content" (content);

CREATE TABLE "DctermsIsVersionOf_content" (
	"DctermsIsVersionOf_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsIsVersionOf_id", content),
	FOREIGN KEY("DctermsIsVersionOf_id") REFERENCES "DctermsIsVersionOf" (id)
);
CREATE INDEX "ix_DctermsIsVersionOf_content_DctermsIsVersionOf_id" ON "DctermsIsVersionOf_content" ("DctermsIsVersionOf_id");
CREATE INDEX "ix_DctermsIsVersionOf_content_content" ON "DctermsIsVersionOf_content" (content);

CREATE TABLE "DctermsHasVersion_content" (
	"DctermsHasVersion_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsHasVersion_id", content),
	FOREIGN KEY("DctermsHasVersion_id") REFERENCES "DctermsHasVersion" (id)
);
CREATE INDEX "ix_DctermsHasVersion_content_DctermsHasVersion_id" ON "DctermsHasVersion_content" ("DctermsHasVersion_id");
CREATE INDEX "ix_DctermsHasVersion_content_content" ON "DctermsHasVersion_content" (content);

CREATE TABLE "DctermsIsReplacedBy_content" (
	"DctermsIsReplacedBy_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsIsReplacedBy_id", content),
	FOREIGN KEY("DctermsIsReplacedBy_id") REFERENCES "DctermsIsReplacedBy" (id)
);
CREATE INDEX "ix_DctermsIsReplacedBy_content_DctermsIsReplacedBy_id" ON "DctermsIsReplacedBy_content" ("DctermsIsReplacedBy_id");
CREATE INDEX "ix_DctermsIsReplacedBy_content_content" ON "DctermsIsReplacedBy_content" (content);

CREATE TABLE "DctermsReplaces_content" (
	"DctermsReplaces_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsReplaces_id", content),
	FOREIGN KEY("DctermsReplaces_id") REFERENCES "DctermsReplaces" (id)
);
CREATE INDEX "ix_DctermsReplaces_content_DctermsReplaces_id" ON "DctermsReplaces_content" ("DctermsReplaces_id");
CREATE INDEX "ix_DctermsReplaces_content_content" ON "DctermsReplaces_content" (content);

CREATE TABLE "DctermsIsRequiredBy_content" (
	"DctermsIsRequiredBy_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsIsRequiredBy_id", content),
	FOREIGN KEY("DctermsIsRequiredBy_id") REFERENCES "DctermsIsRequiredBy" (id)
);
CREATE INDEX "ix_DctermsIsRequiredBy_content_DctermsIsRequiredBy_id" ON "DctermsIsRequiredBy_content" ("DctermsIsRequiredBy_id");
CREATE INDEX "ix_DctermsIsRequiredBy_content_content" ON "DctermsIsRequiredBy_content" (content);

CREATE TABLE "DctermsRequires_content" (
	"DctermsRequires_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsRequires_id", content),
	FOREIGN KEY("DctermsRequires_id") REFERENCES "DctermsRequires" (id)
);
CREATE INDEX "ix_DctermsRequires_content_DctermsRequires_id" ON "DctermsRequires_content" ("DctermsRequires_id");
CREATE INDEX "ix_DctermsRequires_content_content" ON "DctermsRequires_content" (content);

CREATE TABLE "DctermsIsPartOf_content" (
	"DctermsIsPartOf_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsIsPartOf_id", content),
	FOREIGN KEY("DctermsIsPartOf_id") REFERENCES "DctermsIsPartOf" (id)
);
CREATE INDEX "ix_DctermsIsPartOf_content_DctermsIsPartOf_id" ON "DctermsIsPartOf_content" ("DctermsIsPartOf_id");
CREATE INDEX "ix_DctermsIsPartOf_content_content" ON "DctermsIsPartOf_content" (content);

CREATE TABLE "DctermsHasPart_content" (
	"DctermsHasPart_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsHasPart_id", content),
	FOREIGN KEY("DctermsHasPart_id") REFERENCES "DctermsHasPart" (id)
);
CREATE INDEX "ix_DctermsHasPart_content_DctermsHasPart_id" ON "DctermsHasPart_content" ("DctermsHasPart_id");
CREATE INDEX "ix_DctermsHasPart_content_content" ON "DctermsHasPart_content" (content);

CREATE TABLE "DctermsIsReferencedBy_content" (
	"DctermsIsReferencedBy_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsIsReferencedBy_id", content),
	FOREIGN KEY("DctermsIsReferencedBy_id") REFERENCES "DctermsIsReferencedBy" (id)
);
CREATE INDEX "ix_DctermsIsReferencedBy_content_DctermsIsReferencedBy_id" ON "DctermsIsReferencedBy_content" ("DctermsIsReferencedBy_id");
CREATE INDEX "ix_DctermsIsReferencedBy_content_content" ON "DctermsIsReferencedBy_content" (content);

CREATE TABLE "DctermsReferences_content" (
	"DctermsReferences_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsReferences_id", content),
	FOREIGN KEY("DctermsReferences_id") REFERENCES "DctermsReferences" (id)
);
CREATE INDEX "ix_DctermsReferences_content_DctermsReferences_id" ON "DctermsReferences_content" ("DctermsReferences_id");
CREATE INDEX "ix_DctermsReferences_content_content" ON "DctermsReferences_content" (content);

CREATE TABLE "DctermsIsFormatOf_content" (
	"DctermsIsFormatOf_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsIsFormatOf_id", content),
	FOREIGN KEY("DctermsIsFormatOf_id") REFERENCES "DctermsIsFormatOf" (id)
);
CREATE INDEX "ix_DctermsIsFormatOf_content_DctermsIsFormatOf_id" ON "DctermsIsFormatOf_content" ("DctermsIsFormatOf_id");
CREATE INDEX "ix_DctermsIsFormatOf_content_content" ON "DctermsIsFormatOf_content" (content);

CREATE TABLE "DctermsHasFormat_content" (
	"DctermsHasFormat_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsHasFormat_id", content),
	FOREIGN KEY("DctermsHasFormat_id") REFERENCES "DctermsHasFormat" (id)
);
CREATE INDEX "ix_DctermsHasFormat_content_DctermsHasFormat_id" ON "DctermsHasFormat_content" ("DctermsHasFormat_id");
CREATE INDEX "ix_DctermsHasFormat_content_content" ON "DctermsHasFormat_content" (content);

CREATE TABLE "DctermsConformsTo_content" (
	"DctermsConformsTo_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsConformsTo_id", content),
	FOREIGN KEY("DctermsConformsTo_id") REFERENCES "DctermsConformsTo" (id)
);
CREATE INDEX "ix_DctermsConformsTo_content_DctermsConformsTo_id" ON "DctermsConformsTo_content" ("DctermsConformsTo_id");
CREATE INDEX "ix_DctermsConformsTo_content_content" ON "DctermsConformsTo_content" (content);

CREATE TABLE "DctermsSpatial_content" (
	"DctermsSpatial_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsSpatial_id", content),
	FOREIGN KEY("DctermsSpatial_id") REFERENCES "DctermsSpatial" (id)
);
CREATE INDEX "ix_DctermsSpatial_content_DctermsSpatial_id" ON "DctermsSpatial_content" ("DctermsSpatial_id");
CREATE INDEX "ix_DctermsSpatial_content_content" ON "DctermsSpatial_content" (content);

CREATE TABLE "DctermsTemporal_content" (
	"DctermsTemporal_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsTemporal_id", content),
	FOREIGN KEY("DctermsTemporal_id") REFERENCES "DctermsTemporal" (id)
);
CREATE INDEX "ix_DctermsTemporal_content_DctermsTemporal_id" ON "DctermsTemporal_content" ("DctermsTemporal_id");
CREATE INDEX "ix_DctermsTemporal_content_content" ON "DctermsTemporal_content" (content);

CREATE TABLE "DctermsAudience_content" (
	"DctermsAudience_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsAudience_id", content),
	FOREIGN KEY("DctermsAudience_id") REFERENCES "DctermsAudience" (id)
);
CREATE INDEX "ix_DctermsAudience_content_DctermsAudience_id" ON "DctermsAudience_content" ("DctermsAudience_id");
CREATE INDEX "ix_DctermsAudience_content_content" ON "DctermsAudience_content" (content);

CREATE TABLE "DctermsAccrualMethod_content" (
	"DctermsAccrualMethod_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsAccrualMethod_id", content),
	FOREIGN KEY("DctermsAccrualMethod_id") REFERENCES "DctermsAccrualMethod" (id)
);
CREATE INDEX "ix_DctermsAccrualMethod_content_DctermsAccrualMethod_id" ON "DctermsAccrualMethod_content" ("DctermsAccrualMethod_id");
CREATE INDEX "ix_DctermsAccrualMethod_content_content" ON "DctermsAccrualMethod_content" (content);

CREATE TABLE "DctermsAccrualPeriodicity_content" (
	"DctermsAccrualPeriodicity_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsAccrualPeriodicity_id", content),
	FOREIGN KEY("DctermsAccrualPeriodicity_id") REFERENCES "DctermsAccrualPeriodicity" (id)
);
CREATE INDEX "ix_DctermsAccrualPeriodicity_content_DctermsAccrualPeriodicity_id" ON "DctermsAccrualPeriodicity_content" ("DctermsAccrualPeriodicity_id");
CREATE INDEX "ix_DctermsAccrualPeriodicity_content_content" ON "DctermsAccrualPeriodicity_content" (content);

CREATE TABLE "DctermsAccrualPolicy_content" (
	"DctermsAccrualPolicy_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsAccrualPolicy_id", content),
	FOREIGN KEY("DctermsAccrualPolicy_id") REFERENCES "DctermsAccrualPolicy" (id)
);
CREATE INDEX "ix_DctermsAccrualPolicy_content_DctermsAccrualPolicy_id" ON "DctermsAccrualPolicy_content" ("DctermsAccrualPolicy_id");
CREATE INDEX "ix_DctermsAccrualPolicy_content_content" ON "DctermsAccrualPolicy_content" (content);

CREATE TABLE "DctermsInstructionalMethod_content" (
	"DctermsInstructionalMethod_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsInstructionalMethod_id", content),
	FOREIGN KEY("DctermsInstructionalMethod_id") REFERENCES "DctermsInstructionalMethod" (id)
);
CREATE INDEX "ix_DctermsInstructionalMethod_content_DctermsInstructionalMethod_id" ON "DctermsInstructionalMethod_content" ("DctermsInstructionalMethod_id");
CREATE INDEX "ix_DctermsInstructionalMethod_content_content" ON "DctermsInstructionalMethod_content" (content);

CREATE TABLE "DctermsProvenance_content" (
	"DctermsProvenance_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsProvenance_id", content),
	FOREIGN KEY("DctermsProvenance_id") REFERENCES "DctermsProvenance" (id)
);
CREATE INDEX "ix_DctermsProvenance_content_content" ON "DctermsProvenance_content" (content);
CREATE INDEX "ix_DctermsProvenance_content_DctermsProvenance_id" ON "DctermsProvenance_content" ("DctermsProvenance_id");

CREATE TABLE "DctermsRightsHolder_content" (
	"DctermsRightsHolder_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsRightsHolder_id", content),
	FOREIGN KEY("DctermsRightsHolder_id") REFERENCES "DctermsRightsHolder" (id)
);
CREATE INDEX "ix_DctermsRightsHolder_content_content" ON "DctermsRightsHolder_content" (content);
CREATE INDEX "ix_DctermsRightsHolder_content_DctermsRightsHolder_id" ON "DctermsRightsHolder_content" ("DctermsRightsHolder_id");

CREATE TABLE "DctermsMediator_content" (
	"DctermsMediator_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsMediator_id", content),
	FOREIGN KEY("DctermsMediator_id") REFERENCES "DctermsMediator" (id)
);
CREATE INDEX "ix_DctermsMediator_content_DctermsMediator_id" ON "DctermsMediator_content" ("DctermsMediator_id");
CREATE INDEX "ix_DctermsMediator_content_content" ON "DctermsMediator_content" (content);

CREATE TABLE "DctermsEducationLevel_content" (
	"DctermsEducationLevel_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsEducationLevel_id", content),
	FOREIGN KEY("DctermsEducationLevel_id") REFERENCES "DctermsEducationLevel" (id)
);
CREATE INDEX "ix_DctermsEducationLevel_content_DctermsEducationLevel_id" ON "DctermsEducationLevel_content" ("DctermsEducationLevel_id");
CREATE INDEX "ix_DctermsEducationLevel_content_content" ON "DctermsEducationLevel_content" (content);

CREATE TABLE "DctermsAccessRights_content" (
	"DctermsAccessRights_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsAccessRights_id", content),
	FOREIGN KEY("DctermsAccessRights_id") REFERENCES "DctermsAccessRights" (id)
);
CREATE INDEX "ix_DctermsAccessRights_content_DctermsAccessRights_id" ON "DctermsAccessRights_content" ("DctermsAccessRights_id");
CREATE INDEX "ix_DctermsAccessRights_content_content" ON "DctermsAccessRights_content" (content);

CREATE TABLE "DctermsLicense_content" (
	"DctermsLicense_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsLicense_id", content),
	FOREIGN KEY("DctermsLicense_id") REFERENCES "DctermsLicense" (id)
);
CREATE INDEX "ix_DctermsLicense_content_DctermsLicense_id" ON "DctermsLicense_content" ("DctermsLicense_id");
CREATE INDEX "ix_DctermsLicense_content_content" ON "DctermsLicense_content" (content);

CREATE TABLE "DctermsBibliographicCitation_content" (
	"DctermsBibliographicCitation_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("DctermsBibliographicCitation_id", content),
	FOREIGN KEY("DctermsBibliographicCitation_id") REFERENCES "DctermsBibliographicCitation" (id)
);
CREATE INDEX "ix_DctermsBibliographicCitation_content_DctermsBibliographicCitation_id" ON "DctermsBibliographicCitation_content" ("DctermsBibliographicCitation_id");
CREATE INDEX "ix_DctermsBibliographicCitation_content_content" ON "DctermsBibliographicCitation_content" (content);

CREATE TABLE "ActorType" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"Actors_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Actors_id") REFERENCES "Actors" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_ActorType_id" ON "ActorType" (id);

CREATE TABLE "CategoryType" (
	id INTEGER NOT NULL,
	fixml_file_name TEXT,
	component_type VARCHAR(7),
	include_file VARCHAR(10),
	name TEXT NOT NULL,
	section TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	"Categories_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Categories_id") REFERENCES "Categories" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_CategoryType_id" ON "CategoryType" (id);

CREATE TABLE "CodeSetType" (
	uid INTEGER NOT NULL,
	"default" TEXT,
	spec_url TEXT,
	union_data_type VARCHAR(16),
	type TEXT NOT NULL,
	abbr_name TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	scenario TEXT,
	scenario_ref_id TEXT,
	scenario_ref TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	"CodeSets_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("CodeSets_id") REFERENCES "CodeSets" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_CodeSetType_uid" ON "CodeSetType" (uid);

CREATE TABLE "ConceptType" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"Concepts_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Concepts_id") REFERENCES "Concepts" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_ConceptType_id" ON "ConceptType" (id);

CREATE TABLE "FlowType" (
	id INTEGER NOT NULL,
	source TEXT NOT NULL,
	destination TEXT NOT NULL,
	name TEXT NOT NULL,
	reliability VARCHAR(11),
	"Actors_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Actors_id") REFERENCES "Actors" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_FlowType_id" ON "FlowType" (id);

CREATE TABLE "IdentifierType" (
	id INTEGER NOT NULL,
	value TEXT,
	name TEXT,
	"IdentifiersType_id" INTEGER,
	"SessionType_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("IdentifiersType_id") REFERENCES "IdentifiersType" (id),
	FOREIGN KEY("SessionType_id") REFERENCES "SessionType" (id)
);
CREATE INDEX "ix_IdentifierType_id" ON "IdentifierType" (id);

CREATE TABLE "MessageType" (
	uid INTEGER NOT NULL,
	"when" TEXT,
	msg_type TEXT,
	rendering TEXT,
	category TEXT,
	flow TEXT,
	abbr_name TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	scenario TEXT,
	scenario_ref_id TEXT,
	scenario_ref TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	"Messages_id" INTEGER,
	structure_id INTEGER,
	responses_id INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Messages_id") REFERENCES "Messages" (id),
	FOREIGN KEY(structure_id) REFERENCES "StructureInline" (id),
	FOREIGN KEY(responses_id) REFERENCES "ResponsesInline" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_MessageType_uid" ON "MessageType" (uid);

CREATE TABLE "ScenarioType" (
	uid INTEGER NOT NULL,
	id TEXT,
	name TEXT,
	"Scenarios_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Scenarios_id") REFERENCES "Scenarios" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_ScenarioType_uid" ON "ScenarioType" (uid);

CREATE TABLE "SectionType" (
	id INTEGER NOT NULL,
	display_order INTEGER,
	fixml_file_name TEXT,
	name TEXT NOT NULL,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	"Sections_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sections_id") REFERENCES "Sections" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_SectionType_id" ON "SectionType" (id);

CREATE TABLE "TimerSchedule" (
	id INTEGER NOT NULL,
	operation VARCHAR(6) NOT NULL,
	interval TEXT,
	actor TEXT NOT NULL,
	name TEXT NOT NULL,
	"ActionType_id" INTEGER,
	"ResponseType_id" INTEGER,
	activity_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("ActionType_id") REFERENCES "ActionType" (id),
	FOREIGN KEY("ResponseType_id") REFERENCES "ResponseType" (id),
	FOREIGN KEY(activity_id) REFERENCES "ActionType" (id)
);
CREATE INDEX "ix_TimerSchedule_id" ON "TimerSchedule" (id);

CREATE TABLE "TriggerType" (
	id INTEGER NOT NULL,
	state_machine TEXT NOT NULL,
	actor TEXT NOT NULL,
	name TEXT NOT NULL,
	"ActionType_id" INTEGER,
	"ResponseType_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ActionType_id") REFERENCES "ActionType" (id),
	FOREIGN KEY("ResponseType_id") REFERENCES "ResponseType" (id)
);
CREATE INDEX "ix_TriggerType_id" ON "TriggerType" (id);

CREATE TABLE "InterfaceType" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"Interfaces_id" INTEGER,
	sessions_id INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Interfaces_id") REFERENCES "Interfaces" (id),
	FOREIGN KEY(sessions_id) REFERENCES "SessionsInline" (id),
	FOREIGN KEY(annotation_id) REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_InterfaceType_id" ON "InterfaceType" (id);

CREATE TABLE "Datatype" (
	id INTEGER NOT NULL,
	scenario_id TEXT,
	base_type TEXT,
	name TEXT NOT NULL,
	scenario TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	"Datatypes_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Datatypes_id") REFERENCES "Datatypes" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_Datatype_id" ON "Datatype" (id);

CREATE TABLE "Repository" (
	id INTEGER NOT NULL,
	guid TEXT,
	spec_url TEXT,
	namespace TEXT,
	expression_language TEXT,
	name TEXT NOT NULL,
	version TEXT NOT NULL,
	metadata_id INTEGER NOT NULL,
	categories_id INTEGER,
	sections_id INTEGER,
	datatypes_id INTEGER NOT NULL,
	code_sets_id INTEGER,
	fields_id INTEGER NOT NULL,
	actors_id INTEGER,
	components_id INTEGER,
	groups_id INTEGER,
	messages_id INTEGER NOT NULL,
	concepts_id INTEGER,
	scenarios_id INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	UNIQUE (name),
	UNIQUE (id),
	FOREIGN KEY(metadata_id) REFERENCES "DctermsElementOrRefinementContainer" (id),
	FOREIGN KEY(categories_id) REFERENCES "Categories" (id),
	FOREIGN KEY(sections_id) REFERENCES "Sections" (id),
	FOREIGN KEY(datatypes_id) REFERENCES "Datatypes" (id),
	FOREIGN KEY(code_sets_id) REFERENCES "CodeSets" (id),
	FOREIGN KEY(fields_id) REFERENCES "Fields" (id),
	FOREIGN KEY(actors_id) REFERENCES "Actors" (id),
	FOREIGN KEY(components_id) REFERENCES "Components" (id),
	FOREIGN KEY(groups_id) REFERENCES "Groups" (id),
	FOREIGN KEY(messages_id) REFERENCES "Messages" (id),
	FOREIGN KEY(concepts_id) REFERENCES "Concepts" (id),
	FOREIGN KEY(scenarios_id) REFERENCES "Scenarios" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "Repository_id_idx" ON "Repository" (id);
CREATE INDEX "Repository_name_idx" ON "Repository" (name);
CREATE INDEX "ix_Repository_id" ON "Repository" (id);

CREATE TABLE "Appinfo_content" (
	"Appinfo_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("Appinfo_id", content),
	FOREIGN KEY("Appinfo_id") REFERENCES "Appinfo" (id)
);
CREATE INDEX "ix_Appinfo_content_content" ON "Appinfo_content" (content);
CREATE INDEX "ix_Appinfo_content_Appinfo_id" ON "Appinfo_content" ("Appinfo_id");

CREATE TABLE "Appinfo_extra_attributes" (
	"Appinfo_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("Appinfo_id", extra_attributes),
	FOREIGN KEY("Appinfo_id") REFERENCES "Appinfo" (id)
);
CREATE INDEX "ix_Appinfo_extra_attributes_Appinfo_id" ON "Appinfo_extra_attributes" ("Appinfo_id");
CREATE INDEX "ix_Appinfo_extra_attributes_extra_attributes" ON "Appinfo_extra_attributes" (extra_attributes);

CREATE TABLE "Documentation_content" (
	"Documentation_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("Documentation_id", content),
	FOREIGN KEY("Documentation_id") REFERENCES "Documentation" (id)
);
CREATE INDEX "ix_Documentation_content_Documentation_id" ON "Documentation_content" ("Documentation_id");
CREATE INDEX "ix_Documentation_content_content" ON "Documentation_content" (content);

CREATE TABLE "ResponseType_assign" (
	"ResponseType_id" INTEGER,
	assign TEXT,
	PRIMARY KEY ("ResponseType_id", assign),
	FOREIGN KEY("ResponseType_id") REFERENCES "ResponseType" (id)
);
CREATE INDEX "ix_ResponseType_assign_ResponseType_id" ON "ResponseType_assign" ("ResponseType_id");
CREATE INDEX "ix_ResponseType_assign_assign" ON "ResponseType_assign" (assign);

CREATE TABLE "InterfaceAppinfo_content" (
	"InterfaceAppinfo_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("InterfaceAppinfo_id", content),
	FOREIGN KEY("InterfaceAppinfo_id") REFERENCES "InterfaceAppinfo" (id)
);
CREATE INDEX "ix_InterfaceAppinfo_content_InterfaceAppinfo_id" ON "InterfaceAppinfo_content" ("InterfaceAppinfo_id");
CREATE INDEX "ix_InterfaceAppinfo_content_content" ON "InterfaceAppinfo_content" (content);

CREATE TABLE "InterfaceAppinfo_extra_attributes" (
	"InterfaceAppinfo_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("InterfaceAppinfo_id", extra_attributes),
	FOREIGN KEY("InterfaceAppinfo_id") REFERENCES "InterfaceAppinfo" (id)
);
CREATE INDEX "ix_InterfaceAppinfo_extra_attributes_InterfaceAppinfo_id" ON "InterfaceAppinfo_extra_attributes" ("InterfaceAppinfo_id");
CREATE INDEX "ix_InterfaceAppinfo_extra_attributes_extra_attributes" ON "InterfaceAppinfo_extra_attributes" (extra_attributes);

CREATE TABLE "BaseInterfaceType_extra_attributes" (
	"BaseInterfaceType_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("BaseInterfaceType_id", extra_attributes),
	FOREIGN KEY("BaseInterfaceType_id") REFERENCES "BaseInterfaceType" (id)
);
CREATE INDEX "ix_BaseInterfaceType_extra_attributes_BaseInterfaceType_id" ON "BaseInterfaceType_extra_attributes" ("BaseInterfaceType_id");
CREATE INDEX "ix_BaseInterfaceType_extra_attributes_extra_attributes" ON "BaseInterfaceType_extra_attributes" (extra_attributes);

CREATE TABLE "InterfaceDocumentation_content" (
	"InterfaceDocumentation_id" INTEGER,
	content TEXT,
	PRIMARY KEY ("InterfaceDocumentation_id", content),
	FOREIGN KEY("InterfaceDocumentation_id") REFERENCES "InterfaceDocumentation" (id)
);
CREATE INDEX "ix_InterfaceDocumentation_content_InterfaceDocumentation_id" ON "InterfaceDocumentation_content" ("InterfaceDocumentation_id");
CREATE INDEX "ix_InterfaceDocumentation_content_content" ON "InterfaceDocumentation_content" (content);

CREATE TABLE "SessionType_extra_attributes" (
	"SessionType_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("SessionType_id", extra_attributes),
	FOREIGN KEY("SessionType_id") REFERENCES "SessionType" (id)
);
CREATE INDEX "ix_SessionType_extra_attributes_SessionType_id" ON "SessionType_extra_attributes" ("SessionType_id");
CREATE INDEX "ix_SessionType_extra_attributes_extra_attributes" ON "SessionType_extra_attributes" (extra_attributes);

CREATE TABLE "CodeType" (
	uid INTEGER NOT NULL,
	value TEXT NOT NULL,
	sort INTEGER,
	"group" TEXT,
	abbr_name TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	scenario TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	"CodeSetType_uid" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("CodeSetType_uid") REFERENCES "CodeSetType" (uid),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_CodeType_uid" ON "CodeType" (uid);

CREATE TABLE "ComponentType" (
	uid INTEGER NOT NULL,
	rendering TEXT,
	which VARCHAR(5),
	category TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	abbr_name TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	scenario TEXT,
	scenario_ref_id TEXT,
	scenario_ref TEXT,
	"ActionType_id" INTEGER,
	"ActorType_id" INTEGER,
	"ResponseType_id" INTEGER,
	"Components_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ActionType_id") REFERENCES "ActionType" (id),
	FOREIGN KEY("ActorType_id") REFERENCES "ActorType" (id),
	FOREIGN KEY("ResponseType_id") REFERENCES "ResponseType" (id),
	FOREIGN KEY("Components_id") REFERENCES "Components" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_ComponentType_uid" ON "ComponentType" (uid);

CREATE TABLE "FieldType" (
	uid INTEGER NOT NULL,
	length_id TEXT,
	non_encoded_field_id TEXT,
	discriminator_id TEXT,
	base_category TEXT,
	base_category_abbr_name TEXT,
	union_data_type VARCHAR(16),
	assign TEXT,
	type TEXT,
	code_set TEXT,
	abbr_name TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	scenario TEXT,
	added TEXT,
	added_ep TEXT,
	change_type VARCHAR(12),
	deprecated_ep TEXT,
	issue TEXT,
	last_modified TEXT,
	replaced TEXT,
	replaced_ep TEXT,
	replaced_by_field TEXT,
	supported VARCHAR(9),
	updated TEXT,
	updated_ep TEXT,
	deprecated TEXT,
	min_inclusive TEXT,
	max_inclusive TEXT,
	impl_length INTEGER,
	impl_min_length INTEGER,
	impl_max_length INTEGER,
	presence VARCHAR(9),
	value TEXT,
	rendering TEXT,
	encoding TEXT,
	"ActionType_id" INTEGER,
	"ActorType_id" INTEGER,
	"ResponseType_id" INTEGER,
	"Fields_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ActionType_id") REFERENCES "ActionType" (id),
	FOREIGN KEY("ActorType_id") REFERENCES "ActorType" (id),
	FOREIGN KEY("ResponseType_id") REFERENCES "ResponseType" (id),
	FOREIGN KEY("Fields_id") REFERENCES "Fields" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_FieldType_uid" ON "FieldType" (uid);

CREATE TABLE "MappedDatatype" (
	id INTEGER NOT NULL,
	standard TEXT NOT NULL,
	builtin BOOLEAN,
	pattern TEXT,
	element TEXT,
	size INTEGER,
	parameter TEXT,
	min_inclusive TEXT,
	max_inclusive TEXT,
	base TEXT,
	"Datatype_id" INTEGER,
	extension_id INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Datatype_id") REFERENCES "Datatype" (id),
	FOREIGN KEY(extension_id) REFERENCES "ExtensionInline" (id),
	FOREIGN KEY(annotation_id) REFERENCES "Annotation" (id)
);
CREATE INDEX "ix_MappedDatatype_id" ON "MappedDatatype" (id);

CREATE TABLE "MessageRefType" (
	uid INTEGER NOT NULL,
	msg_type TEXT,
	impl_min_occurs INTEGER,
	impl_max_occurs TEXT,
	scenario_id TEXT,
	id TEXT NOT NULL,
	name TEXT,
	scenario TEXT,
	"ActionType_id" INTEGER,
	"ConceptType_id" INTEGER,
	"ResponseType_id" INTEGER,
	identifiers_id INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ActionType_id") REFERENCES "ActionType" (id),
	FOREIGN KEY("ConceptType_id") REFERENCES "ConceptType" (id),
	FOREIGN KEY("ResponseType_id") REFERENCES "ResponseType" (id),
	FOREIGN KEY(identifiers_id) REFERENCES "IdentifiersType" (id)
);
CREATE INDEX "ix_MessageRefType_uid" ON "MessageRefType" (uid);

CREATE TABLE "TimerType" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"ActorType_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ActorType_id") REFERENCES "ActorType" (id)
);
CREATE INDEX "ix_TimerType_id" ON "TimerType" (id);

CREATE TABLE "EncodingType" (
	id INTEGER NOT NULL,
	activation_time DATETIME,
	deactivation_time DATETIME,
	layer VARCHAR(12),
	orchestration TEXT,
	name TEXT,
	version TEXT,
	deprecated DATETIME,
	reliability VARCHAR(11),
	"BaseInterfaceType_id" INTEGER,
	"InterfaceType_id" INTEGER,
	"SessionType_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BaseInterfaceType_id") REFERENCES "BaseInterfaceType" (id),
	FOREIGN KEY("InterfaceType_id") REFERENCES "InterfaceType" (id),
	FOREIGN KEY("SessionType_id") REFERENCES "SessionType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_EncodingType_id" ON "EncodingType" (id);

CREATE TABLE "ProtocolType" (
	id INTEGER NOT NULL,
	activation_time DATETIME,
	deactivation_time DATETIME,
	layer VARCHAR(12),
	orchestration TEXT,
	name TEXT,
	version TEXT,
	deprecated DATETIME,
	reliability VARCHAR(11),
	"BaseInterfaceType_id" INTEGER,
	"InterfaceType_id" INTEGER,
	"SessionType_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BaseInterfaceType_id") REFERENCES "BaseInterfaceType" (id),
	FOREIGN KEY("InterfaceType_id") REFERENCES "InterfaceType" (id),
	FOREIGN KEY("SessionType_id") REFERENCES "SessionType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_ProtocolType_id" ON "ProtocolType" (id);

CREATE TABLE "ServiceType" (
	id INTEGER NOT NULL,
	activation_time DATETIME,
	deactivation_time DATETIME,
	layer VARCHAR(12),
	orchestration TEXT,
	name TEXT,
	version TEXT,
	deprecated DATETIME,
	reliability VARCHAR(11),
	"BaseInterfaceType_id" INTEGER,
	"InterfaceType_id" INTEGER,
	"SessionType_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BaseInterfaceType_id") REFERENCES "BaseInterfaceType" (id),
	FOREIGN KEY("InterfaceType_id") REFERENCES "InterfaceType" (id),
	FOREIGN KEY("SessionType_id") REFERENCES "SessionType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_ServiceType_id" ON "ServiceType" (id);

CREATE TABLE "SessionProtocolType" (
	id INTEGER NOT NULL,
	activation_time DATETIME,
	deactivation_time DATETIME,
	layer VARCHAR(12),
	orchestration TEXT,
	name TEXT,
	version TEXT,
	deprecated DATETIME,
	reliability VARCHAR(11),
	"BaseInterfaceType_id" INTEGER,
	"InterfaceType_id" INTEGER,
	"SessionType_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BaseInterfaceType_id") REFERENCES "BaseInterfaceType" (id),
	FOREIGN KEY("InterfaceType_id") REFERENCES "InterfaceType" (id),
	FOREIGN KEY("SessionType_id") REFERENCES "SessionType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_SessionProtocolType_id" ON "SessionProtocolType" (id);

CREATE TABLE "TransportProtocolType" (
	id INTEGER NOT NULL,
	address TEXT,
	message_cast VARCHAR(9),
	use TEXT,
	activation_time DATETIME,
	deactivation_time DATETIME,
	layer VARCHAR(12),
	orchestration TEXT,
	name TEXT,
	version TEXT,
	deprecated DATETIME,
	reliability VARCHAR(11),
	"BaseInterfaceType_id" INTEGER,
	"InterfaceType_id" INTEGER,
	"SessionType_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BaseInterfaceType_id") REFERENCES "BaseInterfaceType" (id),
	FOREIGN KEY("InterfaceType_id") REFERENCES "InterfaceType" (id),
	FOREIGN KEY("SessionType_id") REFERENCES "SessionType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_TransportProtocolType_id" ON "TransportProtocolType" (id);

CREATE TABLE "UserInterfaceType" (
	id INTEGER NOT NULL,
	activation_time DATETIME,
	deactivation_time DATETIME,
	layer VARCHAR(12),
	orchestration TEXT,
	name TEXT,
	version TEXT,
	deprecated DATETIME,
	reliability VARCHAR(11),
	"BaseInterfaceType_id" INTEGER,
	"InterfaceType_id" INTEGER,
	"SessionType_id" INTEGER,
	annotation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BaseInterfaceType_id") REFERENCES "BaseInterfaceType" (id),
	FOREIGN KEY("InterfaceType_id") REFERENCES "InterfaceType" (id),
	FOREIGN KEY("SessionType_id") REFERENCES "SessionType" (id),
	FOREIGN KEY(annotation_id) REFERENCES "InterfaceAnnotation" (id)
);
CREATE INDEX "ix_UserInterfaceType_id" ON "UserInterfaceType" (id);

CREATE TABLE "InterfaceType_extra_attributes" (
	"InterfaceType_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("InterfaceType_id", extra_attributes),
	FOREIGN KEY("InterfaceType_id") REFERENCES "InterfaceType" (id)
);
CREATE INDEX "ix_InterfaceType_extra_attributes_extra_attributes" ON "InterfaceType_extra_attributes" (extra_attributes);
CREATE INDEX "ix_InterfaceType_extra_attributes_InterfaceType_id" ON "InterfaceType_extra_attributes" ("InterfaceType_id");

CREATE TABLE "FieldRuleType" (
	id INTEGER NOT NULL,
	"when" TEXT NOT NULL,
	name TEXT,
	type TEXT,
	min_inclusive TEXT,
	max_inclusive TEXT,
	impl_length INTEGER,
	impl_min_length INTEGER,
	impl_max_length INTEGER,
	presence VARCHAR(9),
	value TEXT,
	rendering TEXT,
	encoding TEXT,
	"FieldRefType_uid" INTEGER,
	"FieldType_uid" INTEGER,
	unique_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FieldRefType_uid") REFERENCES "FieldRefType" (uid),
	FOREIGN KEY("FieldType_uid") REFERENCES "FieldType" (uid),
	FOREIGN KEY(unique_id) REFERENCES "UniqueInline" (id)
);
CREATE INDEX "ix_FieldRuleType_id" ON "FieldRuleType" (id);

CREATE TABLE "EncodingType_extra_attributes" (
	"EncodingType_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("EncodingType_id", extra_attributes),
	FOREIGN KEY("EncodingType_id") REFERENCES "EncodingType" (id)
);
CREATE INDEX "ix_EncodingType_extra_attributes_extra_attributes" ON "EncodingType_extra_attributes" (extra_attributes);
CREATE INDEX "ix_EncodingType_extra_attributes_EncodingType_id" ON "EncodingType_extra_attributes" ("EncodingType_id");

CREATE TABLE "ProtocolType_extra_attributes" (
	"ProtocolType_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("ProtocolType_id", extra_attributes),
	FOREIGN KEY("ProtocolType_id") REFERENCES "ProtocolType" (id)
);
CREATE INDEX "ix_ProtocolType_extra_attributes_ProtocolType_id" ON "ProtocolType_extra_attributes" ("ProtocolType_id");
CREATE INDEX "ix_ProtocolType_extra_attributes_extra_attributes" ON "ProtocolType_extra_attributes" (extra_attributes);

CREATE TABLE "ServiceType_extra_attributes" (
	"ServiceType_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("ServiceType_id", extra_attributes),
	FOREIGN KEY("ServiceType_id") REFERENCES "ServiceType" (id)
);
CREATE INDEX "ix_ServiceType_extra_attributes_ServiceType_id" ON "ServiceType_extra_attributes" ("ServiceType_id");
CREATE INDEX "ix_ServiceType_extra_attributes_extra_attributes" ON "ServiceType_extra_attributes" (extra_attributes);

CREATE TABLE "SessionProtocolType_extra_attributes" (
	"SessionProtocolType_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("SessionProtocolType_id", extra_attributes),
	FOREIGN KEY("SessionProtocolType_id") REFERENCES "SessionProtocolType" (id)
);
CREATE INDEX "ix_SessionProtocolType_extra_attributes_SessionProtocolType_id" ON "SessionProtocolType_extra_attributes" ("SessionProtocolType_id");
CREATE INDEX "ix_SessionProtocolType_extra_attributes_extra_attributes" ON "SessionProtocolType_extra_attributes" (extra_attributes);

CREATE TABLE "TransportProtocolType_extra_attributes" (
	"TransportProtocolType_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("TransportProtocolType_id", extra_attributes),
	FOREIGN KEY("TransportProtocolType_id") REFERENCES "TransportProtocolType" (id)
);
CREATE INDEX "ix_TransportProtocolType_extra_attributes_TransportProtocolType_id" ON "TransportProtocolType_extra_attributes" ("TransportProtocolType_id");
CREATE INDEX "ix_TransportProtocolType_extra_attributes_extra_attributes" ON "TransportProtocolType_extra_attributes" (extra_attributes);

CREATE TABLE "UserInterfaceType_extra_attributes" (
	"UserInterfaceType_id" INTEGER,
	extra_attributes TEXT,
	PRIMARY KEY ("UserInterfaceType_id", extra_attributes),
	FOREIGN KEY("UserInterfaceType_id") REFERENCES "UserInterfaceType" (id)
);
CREATE INDEX "ix_UserInterfaceType_extra_attributes_UserInterfaceType_id" ON "UserInterfaceType_extra_attributes" ("UserInterfaceType_id");
CREATE INDEX "ix_UserInterfaceType_extra_attributes_extra_attributes" ON "UserInterfaceType_extra_attributes" (extra_attributes);

CREATE TABLE "FieldRuleType_assign" (
	"FieldRuleType_id" INTEGER,
	assign TEXT,
	PRIMARY KEY ("FieldRuleType_id", assign),
	FOREIGN KEY("FieldRuleType_id") REFERENCES "FieldRuleType" (id)
);
CREATE INDEX "ix_FieldRuleType_assign_assign" ON "FieldRuleType_assign" (assign);
CREATE INDEX "ix_FieldRuleType_assign_FieldRuleType_id" ON "FieldRuleType_assign" ("FieldRuleType_id");
