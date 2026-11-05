/**
* How far an element's latest change reaches.
*/
export enum OrchestraChangeKind {
    
    /** A change to wording only. */
    Editorial = "Editorial",
    /** A change to what the element means. */
    Definitional = "Definitional",
};
/**
* The layer of the communication stack a protocol works on.
*/
export enum OrchestraLayer {
    
    /** The application layer. */
    application = "application",
    /** The presentation layer, where encodings sit. */
    presentation = "presentation",
    /** The session layer. */
    session = "session",
    /** The transport layer. */
    transport = "transport",
};
/**
* How many of a block's members must appear.
*/
export enum OrchestraMemberSelection {
    
    /** Exactly one member appears. */
    oneOf = "oneOf",
    /** One or more members appear. */
    anyOf = "anyOf",
};
/**
* How many receivers a transport sends each message to.
*/
export enum OrchestraMessageCast {
    
    /** One receiver. */
    unicast = "unicast",
    /** A group of receivers. */
    multicast = "multicast",
    /** Every receiver. */
    broadcast = "broadcast",
};
/**
* Whether an item must, may or must not appear in a message.
*/
export enum OrchestraPresence {
    
    /** May appear; a rule can make it required. */
    optional = "optional",
    /** Must appear. */
    required = "required",
    /** Must not appear. */
    forbidden = "forbidden",
    /** May appear, and is not checked. */
    ignored = "ignored",
    /** Has a fixed value, which some encodings leave off the wire. */
    constant = "constant",
};
/**
* The FIX protocols the interfaces file names, so that they are spelled one way. A file may name another protocol.
*/
export enum OrchestraProtocolName {
    
    /** The FIX 4 session layer. */
    FIX4 = "FIX4",
    /** FIXT 1.1, the session protocol of FIX 5. */
    FIXT = "FIXT",
    /** FIXP, the FIX session protocol built for high performance. */
    FIXP = "FIXP",
    /** Classic tag=value encoding. */
    tagvalue = "tagvalue",
    /** FIX in XML. */
    FIXML = "FIXML",
    /** The FAST streaming encoding. */
    FAST = "FAST",
    /** Simple Binary Encoding. */
    SBE = "SBE",
    /** The SOFH message framing header. */
    SOFH = "SOFH",
    /** Google's protocol buffers. */
    GPB = "GPB",
    /** JSON encoding. */
    JSON = "JSON",
    /** FIX over TLS. */
    FIXS = "FIXS",
};
/**
* The kinds of purpose the standard names for a text or hint. A file may give another purpose of its own.
*/
export enum OrchestraPurpose {
    
    /** A short summary. */
    SYNOPSIS = "SYNOPSIS",
    /** A longer explanation. */
    ELABORATION = "ELABORATION",
    /** An example of use. */
    EXAMPLE = "EXAMPLE",
    /** A name to show to people in place of the element's own. */
    DISPLAY = "DISPLAY",
};
/**
* What a flow or protocol promises about delivering each message.
*/
export enum OrchestraReliability {
    
    /** No promise; any message can be lost. */
    bestEffort = "bestEffort",
    /** Each message is acted on at most once; a lost one is not sent again. */
    idempotent = "idempotent",
    /** Each message is acted on exactly once; a lost one can be sent again. */
    recoverable = "recoverable",
};
/**
* A party's role in setting up a session.
*/
export enum OrchestraRole {
    
    /** The party that opens a FIX session. */
    initiator = "initiator",
    /** The party that answers a request to open a FIX session. */
    acceptor = "acceptor",
    /** The party that connects to a server. */
    client = "client",
    /** The party that waits for clients to connect. */
    server = "server",
};
/**
* How a party treats an element of the standard.
*/
export enum OrchestraSupport {
    
    /** The party supports the element. */
    supported = "supported",
    /** The party refuses the element. */
    forbidden = "forbidden",
    /** The party accepts the element and acts on none of it. */
    ignored = "ignored",
};
/**
* How the timing of a response relates to the request it answers.
*/
export enum OrchestraSynchronization {
    
    /** The response's timing has no tie to the request's. */
    asynchronous = "asynchronous",
    /** A request waits until the one before it has its answer. */
    synchronous = "synchronous",
    /** Each response follows its request, and several requests may wait for answers at once. */
    pipelined = "pipelined",
};
/**
* What a step does to an actor's timer.
*/
export enum OrchestraTimerOperation {
    
    /** Start the timer. */
    START = "START",
    /** Stop the timer. */
    CANCEL = "CANCEL",
    /** Stop the timer and start it again. */
    RESET = "RESET",
};
/**
* The roles the interfaces file names for a transport. A file may give another role of its own.
*/
export enum OrchestraTransportUse {
    
    /** The main connection. */
    primary = "primary",
    /** The backup connection. */
    secondary = "secondary",
    /** Another connection, used in turn or by choice. */
    alternate = "alternate",
};
/**
* What a category sorts, in v1.0.
*/
export enum OrchestraCategoryContentV10 {
    
    /** The category sorts fields. */
    Field = "Field",
    /** The category sorts messages. */
    Message = "Message",
};
/**
* The shared FIXML file a category's own file includes, in v1.0.
*/
export enum OrchestraCategoryIncludeFileV10 {
    
    /** The shared file of components. */
    components = "components",
    /** The shared file of fields. */
    fields = "fields",
};
/**
* The standards v1.0 names for mapping a datatype. A file may give another standard of its own.
*/
export enum OrchestraDatatypeStandardV10 {
    
    /** The general-purpose datatypes of ISO/IEC 11404. */
    ISO11404 = "ISO11404",
    /** Google's protocol buffers. */
    GPB = "GPB",
    /** JSON Schema. */
    JSON = "JSON",
    /** Simple Binary Encoding. */
    SBE = "SBE",
    /** XML Schema, as FIXML uses it. */
    XML = "XML",
    /** The classic tag=value encoding. */
    TAG_VALUE = "TAG_VALUE",
};
/**
* The datatypes v1.0 names whose values a field may hold beside its codes.
*/
export enum OrchestraUnionDatatypeV10 {
    
    /** Quantities. */
    Qty = "Qty",
    /** Values from 100 up, kept for user-defined codes. */
    Reserved100Plus = "Reserved100Plus",
    /** Values from 1000 up, kept for user-defined codes. */
    Reserved1000Plus = "Reserved1000Plus",
    /** Values from 4000 up, kept for user-defined codes. */
    Reserved4000Plus = "Reserved4000Plus",
    /** Tenors, such as 3M. */
    Tenor = "Tenor",
};
/**
* The kinds of purpose the standard names for a text or hint. A file may give another purpose of its own.
*/
export enum OrchestraPurposeV11 {
    
    /** A short summary. */
    SYNOPSIS = "SYNOPSIS",
    /** A longer explanation. */
    ELABORATION = "ELABORATION",
    /** An example of use. */
    EXAMPLE = "EXAMPLE",
    /** A name to show to people in place of the element's own. */
    DISPLAY = "DISPLAY",
    /** A label for a table, a figure or a heading. */
    CAPTION = "CAPTION",
    /** A short hint shown when a pointer rests on the element. */
    TOOLTIP = "TOOLTIP",
    /** A formal definition in one sentence. */
    DEFINITION = "DEFINITION",
};


/**
 * The Dublin Core description at the top of a repository or interfaces file. Each key holds the values of one Dublin Core element or term.
 */
export interface OrchestraMetadata {
    /** The values the file gives for the Dublin Core element title. */
    dc_title?: string[],
    /** The values the file gives for the Dublin Core element creator. */
    dc_creator?: string[],
    /** The values the file gives for the Dublin Core element subject. */
    dc_subject?: string[],
    /** The values the file gives for the Dublin Core element description. */
    dc_description?: string[],
    /** The values the file gives for the Dublin Core element publisher. */
    dc_publisher?: string[],
    /** The values the file gives for the Dublin Core element contributor. */
    dc_contributor?: string[],
    /** The values the file gives for the Dublin Core element date. */
    dc_date?: string[],
    /** The values the file gives for the Dublin Core element type. */
    dc_type?: string[],
    /** The values the file gives for the Dublin Core element format. */
    dc_format?: string[],
    /** The values the file gives for the Dublin Core element identifier. */
    dc_identifier?: string[],
    /** The values the file gives for the Dublin Core element source. */
    dc_source?: string[],
    /** The values the file gives for the Dublin Core element language. */
    dc_language?: string[],
    /** The values the file gives for the Dublin Core element relation. */
    dc_relation?: string[],
    /** The values the file gives for the Dublin Core element coverage. */
    dc_coverage?: string[],
    /** The values the file gives for the Dublin Core element rights. */
    dc_rights?: string[],
    /** The values the file gives for the DCMI term title. */
    dcterms_title?: string[],
    /** The values the file gives for the DCMI term creator. */
    dcterms_creator?: string[],
    /** The values the file gives for the DCMI term subject. */
    dcterms_subject?: string[],
    /** The values the file gives for the DCMI term description. */
    dcterms_description?: string[],
    /** The values the file gives for the DCMI term publisher. */
    dcterms_publisher?: string[],
    /** The values the file gives for the DCMI term contributor. */
    dcterms_contributor?: string[],
    /** The values the file gives for the DCMI term date. */
    dcterms_date?: string[],
    /** The values the file gives for the DCMI term type. */
    dcterms_type?: string[],
    /** The values the file gives for the DCMI term format. */
    dcterms_format?: string[],
    /** The values the file gives for the DCMI term identifier. */
    dcterms_identifier?: string[],
    /** The values the file gives for the DCMI term source. */
    dcterms_source?: string[],
    /** The values the file gives for the DCMI term language. */
    dcterms_language?: string[],
    /** The values the file gives for the DCMI term relation. */
    dcterms_relation?: string[],
    /** The values the file gives for the DCMI term coverage. */
    dcterms_coverage?: string[],
    /** The values the file gives for the DCMI term rights. */
    dcterms_rights?: string[],
    /** The values the file gives for the DCMI term alternative. */
    dcterms_alternative?: string[],
    /** The values the file gives for the DCMI term tableOfContents. */
    dcterms_table_of_contents?: string[],
    /** The values the file gives for the DCMI term abstract. */
    dcterms_abstract?: string[],
    /** The values the file gives for the DCMI term created. */
    dcterms_created?: string[],
    /** The values the file gives for the DCMI term valid. */
    dcterms_valid?: string[],
    /** The values the file gives for the DCMI term available. */
    dcterms_available?: string[],
    /** The values the file gives for the DCMI term issued. */
    dcterms_issued?: string[],
    /** The values the file gives for the DCMI term modified. */
    dcterms_modified?: string[],
    /** The values the file gives for the DCMI term dateAccepted. */
    dcterms_date_accepted?: string[],
    /** The values the file gives for the DCMI term dateCopyrighted. */
    dcterms_date_copyrighted?: string[],
    /** The values the file gives for the DCMI term dateSubmitted. */
    dcterms_date_submitted?: string[],
    /** The values the file gives for the DCMI term extent. */
    dcterms_extent?: string[],
    /** The values the file gives for the DCMI term medium. */
    dcterms_medium?: string[],
    /** The values the file gives for the DCMI term isVersionOf. */
    dcterms_is_version_of?: string[],
    /** The values the file gives for the DCMI term hasVersion. */
    dcterms_has_version?: string[],
    /** The values the file gives for the DCMI term isReplacedBy. */
    dcterms_is_replaced_by?: string[],
    /** The values the file gives for the DCMI term replaces. */
    dcterms_replaces?: string[],
    /** The values the file gives for the DCMI term isRequiredBy. */
    dcterms_is_required_by?: string[],
    /** The values the file gives for the DCMI term requires. */
    dcterms_requires?: string[],
    /** The values the file gives for the DCMI term isPartOf. */
    dcterms_is_part_of?: string[],
    /** The values the file gives for the DCMI term hasPart. */
    dcterms_has_part?: string[],
    /** The values the file gives for the DCMI term isReferencedBy. */
    dcterms_is_referenced_by?: string[],
    /** The values the file gives for the DCMI term references. */
    dcterms_references?: string[],
    /** The values the file gives for the DCMI term isFormatOf. */
    dcterms_is_format_of?: string[],
    /** The values the file gives for the DCMI term hasFormat. */
    dcterms_has_format?: string[],
    /** The values the file gives for the DCMI term conformsTo. */
    dcterms_conforms_to?: string[],
    /** The values the file gives for the DCMI term spatial. */
    dcterms_spatial?: string[],
    /** The values the file gives for the DCMI term temporal. */
    dcterms_temporal?: string[],
    /** The values the file gives for the DCMI term audience. */
    dcterms_audience?: string[],
    /** The values the file gives for the DCMI term accrualMethod. */
    dcterms_accrual_method?: string[],
    /** The values the file gives for the DCMI term accrualPeriodicity. */
    dcterms_accrual_periodicity?: string[],
    /** The values the file gives for the DCMI term accrualPolicy. */
    dcterms_accrual_policy?: string[],
    /** The values the file gives for the DCMI term instructionalMethod. */
    dcterms_instructional_method?: string[],
    /** The values the file gives for the DCMI term provenance. */
    dcterms_provenance?: string[],
    /** The values the file gives for the DCMI term rightsHolder. */
    dcterms_rights_holder?: string[],
    /** The values the file gives for the DCMI term mediator. */
    dcterms_mediator?: string[],
    /** The values the file gives for the DCMI term educationLevel. */
    dcterms_education_level?: string[],
    /** The values the file gives for the DCMI term accessRights. */
    dcterms_access_rights?: string[],
    /** The values the file gives for the DCMI term license. */
    dcterms_license?: string[],
    /** The values the file gives for the DCMI term bibliographicCitation. */
    dcterms_bibliographic_citation?: string[],
}


/**
 * An XML element in a place where the XSDs accept any content, kept as written so that the file converts back unchanged.
 */
export interface OrchestraXmlElement {
    /** The name, with its namespace in braces when it has one. */
    xml_name: string,
    /** The element's attributes. */
    xml_attributes?: OrchestraXmlAttribute[],
    /** The text before the first child element. */
    xml_text?: string,
    /** The child elements, in order. */
    xml_children?: OrchestraXmlElement[],
    /** The text after the element and before its next sibling. */
    xml_tail?: string,
}


/**
 * An XML attribute from another namespace, kept as written.
 */
export interface OrchestraXmlAttribute {
    /** The name, with its namespace in braces when it has one. */
    xml_name: string,
    /** The attribute's value. */
    xml_value: string,
}


/**
 * One input to an action, which is a field, component or group, defined in place or named by reference. It holds exactly one of these.
 */
export interface OrchestraActionParameterV10 {
    /** A field defined in place. */
    fixr_field?: OrchestraFieldV10,
    /** A field used by reference. */
    fixr_field_ref?: OrchestraFieldRefV10,
    /** A component defined in place. */
    fixr_component?: OrchestraComponentV10,
    /** A component used by reference. */
    fixr_component_ref?: OrchestraComponentRefV10,
    /** A repeating group defined in place. */
    fixr_group?: OrchestraGroupV10,
    /** A group used by reference. */
    fixr_group_ref?: OrchestraGroupRefV10,
}


/**
 * One thing an action does: send a message, set a value, fire a transition or schedule a timer. It holds exactly one of these.
 */
export interface OrchestraActionStepV10 {
    /** A message to send. */
    fixr_message_ref?: OrchestraMessageRefV10,
    /** An expression that gives an actor's variable a value, such as $actor.variable=value. */
    fixr_assign?: string,
    /** A transition to fire. */
    fixr_trigger?: OrchestraTriggerV10,
    /** A timer to start, stop or restart. */
    fixr_timer_schedule?: OrchestraTimerScheduleV10,
}


/**
 * Things that happen together, such as when a response fires or a state is entered: messages sent, values set, transitions fired and timers scheduled, with their inputs.
 */
export interface OrchestraActionV10 {
    /** The fields, groups and components the action takes as input, in order. */
    fixr_parameters?: OrchestraActionParameterV10[],
    /** What the action does, in order: messages sent, values set, transitions fired and timers scheduled. */
    fixr_actions: OrchestraActionStepV10[],
}


/**
 * One thing an actor keeps: a variable given as a field, component or group, a state machine or a timer. It holds exactly one of these.
 */
export interface OrchestraActorMemberV10 {
    /** A variable defined in place as a field. */
    fixr_field?: OrchestraFieldV10,
    /** A variable that uses a field by its number. */
    fixr_field_ref?: OrchestraFieldRefV10,
    /** A variable defined in place as a component. */
    fixr_component?: OrchestraComponentV10,
    /** A variable that uses a component by its number. */
    fixr_component_ref?: OrchestraComponentRefV10,
    /** A variable defined in place as a repeating group. */
    fixr_group?: OrchestraGroupV10,
    /** A variable that uses a repeating group by its number. */
    fixr_group_ref?: OrchestraGroupRefV10,
    /** A state machine. */
    fixr_states?: OrchestraStateMachineV10,
    /** A timer. */
    fixr_timer?: OrchestraTimerV10,
}


/**
 * A kind of party in an exchange, such as a buy-side firm or a venue, with the state it keeps: its variables, state machines and timers.
 */
export interface OrchestraActorV10 {
    /** The actor's variables, state machines and timers, in order. */
    fixr_members?: OrchestraActorMemberV10[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The actor's name, unique among the repository's actors. */
    fixr_name: string,
}


/**
 * One entry of the actors list, an actor or a flow. It holds exactly one of these.
 */
export interface OrchestraActorsMemberV10 {
    /** An actor. */
    fixr_actor?: OrchestraActorV10,
    /** A flow. */
    fixr_flow?: OrchestraFlowV10,
}


/**
 * The parties a repository describes and the one-way flows between them.
 */
export interface OrchestraActorsV10 {
    /** The actors and flows, in order. */
    fixr_members: OrchestraActorsMemberV10[],
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * One part of an annotation, a piece of text or a hint for software. It holds exactly one of these.
 */
export interface OrchestraAnnotationMemberV10 {
    /** A piece of text. */
    fixr_documentation?: OrchestraDocumentationV10,
    /** A hint for software. */
    fixr_appinfo?: OrchestraAppinfoV10,
}


/**
 * Notes for readers and hints for software, attached to an element.
 */
export interface OrchestraAnnotationV10 extends OrchestraPedigreeV10Mixin {
    /** The texts and hints, in order. */
    fixr_members: OrchestraAnnotationMemberV10[],
}


/**
 * A hint for a particular tool or encoding, such as how FIXML renders an element, held as text and open XML.
 */
export interface OrchestraAppinfoV10 extends OrchestraPedigreeV10Mixin {
    /** The text the element holds, as written. */
    fixr_text?: string,
    /** Child elements from other namespaces, kept as written. */
    fixr_any?: OrchestraXmlElement[],
    /** The address of a document that describes the element. */
    fixr_spec_url?: string,
    /** The language of the text, as a language tag. */
    fixr_lang_id?: string,
    /** What the hint is for, such as the encoding it concerns. */
    fixr_purpose?: string,
    /** Attributes from other namespaces, kept as written. */
    fixr_other_attributes?: OrchestraXmlAttribute[],
}


/**
 * What an interface and a session share: the services, encodings and protocols of a connection, layer by layer.
 */
export interface OrchestraBaseInterfaceV10 {
    /** The application-level services offered. */
    fixi_service?: OrchestraServiceV10[],
    /** The user interfaces offered. */
    fixi_user_interface?: OrchestraUserInterfaceV10[],
    /** The encodings used. */
    fixi_encoding?: OrchestraEncodingV10[],
    /** The session-level protocols used. */
    fixi_session_protocol?: OrchestraSessionProtocolV10[],
    /** Other protocols used. */
    fixi_protocol?: OrchestraProtocolV10[],
    /** The transports used. */
    fixi_transport?: OrchestraTransportV10[],
    /** Notes for readers and hints for software. */
    fixi_annotation?: OrchestraInterfaceAnnotationV10,
    /** The interface's or session's name, unique within the file. */
    fixi_name: string,
    /** Attributes from other namespaces, kept as written. */
    fixi_other_attributes?: OrchestraXmlAttribute[],
}


/**
 * How every entry of a group, or a single use of a component, gets its values: the fields, groups and components it sets.
 */
export interface OrchestraBlockAssignmentV10 {
    /** The fields, groups and components the assignment sets, in order. */
    fixr_members: OrchestraStructureMemberV10[],
}


/**
 * The categories a repository sorts its messages and fields into.
 */
export interface OrchestraCategoriesV10 extends OrchestraContainerV10Mixin {
    /** The categories. */
    fixr_category: OrchestraCategoryV10[],
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * A business process grouping within a section, such as order handling or market data.
 */
export interface OrchestraCategoryV10 extends OrchestraPedigreeV10Mixin {
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The category's name. */
    fixr_name?: string,
    /** The FIXML schema file that holds the elements of this section or category. */
    fixr_fixml_file_name?: string,
    /** Whether the category sorts messages or fields. */
    fixr_component_type?: string,
    /** The section the category belongs to, by name. */
    fixr_section?: string,
    /** The shared FIXML file, of components or of fields, that the category's file includes. */
    fixr_include_file?: string,
}


/**
 * A named list of the values a field may take, each with a name of its own, over one underlying datatype.
 */
export interface OrchestraCodeSetV10 extends OrchestraIdentityV10Mixin, OrchestraPedigreeV10Mixin {
    /** The set's codes, in order. */
    fixr_code?: OrchestraCodeV10[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The set's datatype, by name. */
    fixr_type: string,
    /** The code a receiver assumes when none is given. */
    fixr_default?: string,
    /** The address of the outside list, such as an ISO standard, that gives the codes. */
    fixr_spec_url?: string,
}


/**
 * The code sets a repository defines.
 */
export interface OrchestraCodeSetsV10 {
    /** The code sets. */
    fixr_code_set: OrchestraCodeSetV10[],
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * One permitted value of the set, with its name and what goes on the wire.
 */
export interface OrchestraCodeV10 extends OrchestraIdentityV10Mixin, OrchestraPedigreeV10Mixin {
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The value that goes on the wire for this code. */
    fixr_value: string,
    /** A number that places the code when its set is shown. */
    fixr_sort?: string,
    /** A label that places the code with others when its set is shown. */
    fixr_group?: string,
}


/**
 * Where a message or block includes a component, by its number, with its presence and any rules that make it conditional.
 */
export interface OrchestraComponentRefV10 extends OrchestraReferenceV10Mixin, OrchestraPedigreeV10Mixin {
    /** How the component, or every entry of the group, gets its values. */
    fixr_block_assignment?: OrchestraBlockAssignmentV10[],
    /** Rules that make the component's presence depend on other values. */
    fixr_rule?: OrchestraComponentRuleV10[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** Whether the item must, may or must not appear, or has a fixed value; optional when none is given. */
    fixr_presence?: string,
    /** A name for this use of the element, so that one message or block can hold it more than once. */
    fixr_instance_name?: string,
}


/**
 * A condition that changes a component's presence, such as making it required.
 */
export interface OrchestraComponentRuleV10 {
    /** When the rule applies, written as an expression. */
    fixr_when: string,
    /** The rule's name. */
    fixr_name?: string,
    /** The presence that applies while the rule's condition holds. */
    fixr_presence?: string,
}


/**
 * A named block of fields, groups and components that messages and other blocks include by reference.
 */
export interface OrchestraComponentV10 extends OrchestraPedigreeV10Mixin, OrchestraIdentityV10Mixin {
    /** The fields, groups and components the component holds, in order. */
    fixr_members: OrchestraStructureMemberV10[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The category the component belongs to, by name. */
    fixr_category?: string,
    /** A hint for how a tool shows or reads the element, which no validator checks. */
    fixr_rendering?: string,
    /** Whether one member exactly, or one or more members, must appear. */
    fixr_which?: string,
}


/**
 * The components a repository defines.
 */
export interface OrchestraComponentsV10 extends OrchestraContainerV10Mixin {
    /** The components. */
    fixr_component: OrchestraComponentV10[],
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * One element a concept ties together, named by reference, which is a message, field, component or group. It holds exactly one of these.
 */
export interface OrchestraConceptMemberV10 {
    /** A component used by reference. */
    fixr_component_ref?: OrchestraComponentRefV10,
    /** A group used by reference. */
    fixr_group_ref?: OrchestraGroupRefV10,
    /** A field used by reference. */
    fixr_field_ref?: OrchestraFieldRefV10,
    /** A message, by reference. */
    fixr_message_ref?: OrchestraMessageRefV10,
}


/**
 * A named business idea that ties together the fields, components, groups and messages that express it.
 */
export interface OrchestraConceptV10 {
    /** The fields, components, groups and messages the concept ties together. */
    fixr_members: OrchestraConceptMemberV10[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The concept's name, unique among the repository's concepts. */
    fixr_name: string,
}


/**
 * The concepts a repository names.
 */
export interface OrchestraConceptsV10 {
    /** The concepts. */
    fixr_concept: OrchestraConceptV10[],
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * The extension pack that a list of elements is up to date with.
 */
export interface OrchestraContainerV10Mixin {
    /** The latest extension pack the list is up to date with. */
    fixr_latest_ep?: number,
}


/**
 * XML from the target standard's own schema that a datatype mapping carries.
 */
export interface OrchestraDatatypeExtensionV10 {
    /** Child elements from other namespaces, kept as written. */
    fixr_any?: OrchestraXmlElement[],
}


/**
 * A FIX datatype, such as Price or UTCTimestamp, with how it maps to the types of other standards.
 */
export interface OrchestraDatatypeV10 extends OrchestraPedigreeV10Mixin {
    /** How the datatype is written in other standards. */
    fixr_mapped_datatype?: OrchestraMappedDatatypeV10[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The datatype's name, such as Price. */
    fixr_name: string,
    /** The datatype this one narrows, such as int for Length. */
    fixr_base_type?: string,
}


/**
 * The datatypes a repository uses.
 */
export interface OrchestraDatatypesV10 extends OrchestraContainerV10Mixin {
    /** The datatypes. */
    fixr_datatype: OrchestraDatatypeV10[],
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * Text about an element, with its language, purpose and media type.
 */
export interface OrchestraDocumentationV10 extends OrchestraPedigreeV10Mixin {
    /** The text the element holds, as written. */
    fixr_text?: string,
    /** Child elements from other namespaces, kept as written. */
    fixr_any?: OrchestraXmlElement[],
    /** The language of the text, as a language tag. */
    fixr_lang_id?: string,
    /** What the text is for, such as a summary or an example. */
    fixr_purpose?: string,
    /** The media type of the text; text/plain when none is given. */
    fixr_content_type?: string,
}


/**
 * An encoding used on an interface or session, such as tag=value, FIXML or SBE.
 */
export interface OrchestraEncodingV10 extends OrchestraProtocolV10 {
}


/**
 * The limits on a field's value that a field, a use of it or a rule may set: range, length, presence, fixed or default value, character set and a display hint.
 */
export interface OrchestraFieldConstraintsV10Mixin {
    /** The smallest value allowed. */
    fixr_min_inclusive?: string,
    /** The largest value allowed. */
    fixr_max_inclusive?: string,
    /** The fixed length an implementation uses. */
    fixr_impl_length?: number,
    /** The shortest length an implementation accepts. */
    fixr_impl_min_length?: number,
    /** The longest length an implementation accepts. */
    fixr_impl_max_length?: number,
    /** Whether the item must, may or must not appear, or has a fixed value; optional when none is given. */
    fixr_presence?: string,
    /** The character set of the value, when it is not US-ASCII. */
    fixr_encoding?: string,
    /** The value a receiver assumes when an optional field is left out, or the fixed value of a constant field. */
    fixr_value?: string,
    /** A hint for how a tool shows or reads the element, which no validator checks. */
    fixr_rendering?: string,
}


/**
 * Where a message or block includes a field, by its tag number, with its presence, value limits and any rules.
 */
export interface OrchestraFieldRefV10 extends OrchestraReferenceV10Mixin, OrchestraPedigreeV10Mixin, OrchestraFieldConstraintsV10Mixin {
    /** Rules that make the element's presence or limits depend on other values. */
    fixr_rule?: OrchestraFieldRuleV10[],
    /** An expression that sets the field's value. */
    fixr_assign?: string,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The tag number of the field that gives this field's length. */
    fixr_length_id?: number,
    /** A name for this use of the element, so that one message or block can hold it more than once. */
    fixr_instance_name?: string,
}


/**
 * A condition that changes a field's presence, datatype or limits, or a check its value must pass.
 */
export interface OrchestraFieldRuleV10 extends OrchestraFieldConstraintsV10Mixin {
    /** A check that the field's value is unique. */
    fixr_unique?: OrchestraUniqueV10,
    /** Expressions that set or check values while the rule's condition holds. */
    fixr_assign?: string[],
    /** When the rule applies, written as an expression. */
    fixr_when: string,
    /** The rule's name. */
    fixr_name?: string,
    /** The datatype the field takes while the rule's condition holds. */
    fixr_type?: string,
}


/**
 * A FIX field: its tag number, its name, its datatype or its code set, and the limits on its value.
 */
export interface OrchestraFieldV10 extends OrchestraIdentityV10Mixin, OrchestraPedigreeV10Mixin, OrchestraFieldConstraintsV10Mixin {
    /** Rules that make the element's presence or limits depend on other values. */
    fixr_rule?: OrchestraFieldRuleV10[],
    /** An expression that sets the field's value. */
    fixr_assign?: string,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The field's datatype, or its code set, by name; a code set brings its own datatype. */
    fixr_type: string,
    /** The tag number of the field that gives this field's length. */
    fixr_length_id?: number,
    /** The tag number of the field whose value decides which values this field may take. */
    fixr_discriminator_id?: number,
    /** The category the field belongs to in the base specification. */
    fixr_base_category?: string,
    /** The short name the field takes within its base category in FIXML. */
    fixr_base_category_abbr_name?: string,
    /** A datatype whose values the field may hold beside its codes, such as a range kept for user-defined values. */
    fixr_union_data_type?: string,
}


/**
 * The fields a repository defines.
 */
export interface OrchestraFieldsV10 {
    /** The fields. */
    fixr_field: OrchestraFieldV10[],
    /** The latest extension pack the list is up to date with. */
    fixr_latest_ep?: number,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * Messages that travel one way, from a sending actor to a receiving one, with their delivery guarantee.
 */
export interface OrchestraFlowV10 {
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The flow's name. */
    fixr_name: string,
    /** The sending actor, by name. */
    fixr_source: string,
    /** The receiving actor, by name. */
    fixr_destination: string,
    /** How reliably the flow delivers its messages, from best effort to recoverable. */
    fixr_reliability?: string,
}


/**
 * Where a message or block includes a repeating group, by its number, with how many entries it may hold.
 */
export interface OrchestraGroupRefV10 extends OrchestraComponentRefV10 {
    /** The fewest entries an implementation accepts. */
    fixr_impl_min_occurs?: number,
    /** The most entries an implementation accepts, or unbounded. */
    fixr_impl_max_occurs?: string,
}


/**
 * A block whose entries repeat, each with the same fields, groups and components, and whose count a NumInGroup field carries.
 */
export interface OrchestraGroupV10 extends OrchestraPedigreeV10Mixin, OrchestraIdentityV10Mixin {
    /** The field that counts the group's entries. */
    fixr_num_in_group?: OrchestraFieldRefV10,
    /** The fields, groups and components that each entry holds, in order. */
    fixr_members: OrchestraStructureMemberV10[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The category the group belongs to, by name. */
    fixr_category?: string,
    /** A hint for how a tool shows or reads the element, which no validator checks. */
    fixr_rendering?: string,
    /** The fewest entries an implementation accepts. */
    fixr_impl_min_occurs?: number,
    /** The most entries an implementation accepts, or unbounded. */
    fixr_impl_max_occurs?: string,
    /** Whether one member exactly, or one or more members, must appear. */
    fixr_which?: string,
}


/**
 * The repeating groups a repository defines.
 */
export interface OrchestraGroupsV10 extends OrchestraContainerV10Mixin {
    /** The repeating groups. */
    fixr_group: OrchestraGroupV10[],
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * A field that a message sent by an action sets, or carries over from the message received, by tag number.
 */
export interface OrchestraIdentifierV10 {
    /** The tag number of the field that is set or carried over. */
    fixr_id: number,
    /** The tag number of the received message's field that the value comes from; the field's own tag number when none is given. */
    fixr_source_id?: number,
}


/**
 * One entry of a message's identifiers, a field carried over or a field set. It holds exactly one of these.
 */
export interface OrchestraIdentifiersMemberV10 {
    /** A field whose value is carried over from the message received. */
    fixr_correlate?: OrchestraIdentifierV10,
    /** A field whose value the message sent sets. */
    fixr_assign?: OrchestraIdentifierV10,
}


/**
 * The fields a message sent by an action sets or carries over.
 */
export interface OrchestraIdentifiersV10 {
    /** The fields carried over or set, in order. */
    fixr_members: OrchestraIdentifiersMemberV10[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
}


/**
 * The keys of a defined element, its number, name, short name and scenario.
 */
export interface OrchestraIdentityV10Mixin {
    /** The element's number, unique among elements of its kind; for a field, its tag number. */
    fixr_id: number,
    /** The element's name, unique among elements of its kind within one scenario. */
    fixr_name: string,
    /** A short form of the name, which FIXML uses for tags. */
    fixr_abbr_name?: string,
    /** The use case this variant of the element serves, such as a workflow or an asset class; base when none is given. */
    fixr_scenario?: string,
}


/**
 * One part of an annotation in an interfaces file, a text or a hint for software. It holds exactly one of these.
 */
export interface OrchestraInterfaceAnnotationMemberV10 {
    /** A piece of text. */
    fixi_documentation?: OrchestraInterfaceDocumentationV10,
    /** A hint for software. */
    fixi_appinfo?: OrchestraInterfaceAppinfoV10,
}


/**
 * Notes for readers and hints for software, attached to an element of an interfaces file.
 */
export interface OrchestraInterfaceAnnotationV10 {
    /** The texts and hints, in order. */
    fixi_members: OrchestraInterfaceAnnotationMemberV10[],
}


/**
 * A hint for a particular tool on an element of an interfaces file.
 */
export interface OrchestraInterfaceAppinfoV10 {
    /** The text the element holds, as written. */
    fixi_text?: string,
    /** Child elements from other namespaces, kept as written. */
    fixi_any?: OrchestraXmlElement[],
    /** The address of a document that describes the element. */
    fixi_spec_url?: string,
    /** The language of the text, as a language tag. */
    fixi_lang_id?: string,
    /** What the hint is for, such as the tool it concerns. */
    fixi_purpose?: string,
    /** Attributes from other namespaces, kept as written. */
    fixi_other_attributes?: OrchestraXmlAttribute[],
}


/**
 * Text about an element of an interfaces file.
 */
export interface OrchestraInterfaceDocumentationV10 {
    /** The text the element holds, as written. */
    fixi_text?: string,
    /** Child elements from other namespaces, kept as written. */
    fixi_any?: OrchestraXmlElement[],
    /** The language of the text, as a language tag. */
    fixi_lang_id?: string,
    /** What the text is for, such as a summary or an example. */
    fixi_purpose?: string,
    /** The media type of the text; text/plain when none is given. */
    fixi_content_type?: string,
}


/**
 * A named service offering and the sessions it carries, with the protocols on each layer.
 */
export interface OrchestraInterfaceV10 extends OrchestraBaseInterfaceV10 {
    /** The sessions the interface carries. */
    fixi_sessions?: OrchestraSessionsV10,
}


/**
 * A description of the services and sessions a party offers and how to reach them, headed by its Dublin Core metadata.
 */
export interface OrchestraInterfacesV10 {
    /** The file's Dublin Core description, such as its title, publisher and date. */
    fixi_metadata: OrchestraMetadata,
    /** The interfaces the file describes. */
    fixi_interface?: OrchestraInterfaceV10[],
}


/**
 * How a FIX datatype is written in another standard, such as XML Schema or protocol buffers.
 */
export interface OrchestraMappedDatatypeV10 {
    /** XML from the target standard's own schema. */
    fixr_extension?: OrchestraDatatypeExtensionV10,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The standard the datatype is written in, such as XML or GPB. */
    fixr_standard: string,
    /** Whether the target standard has the type built in, rather than derived. */
    fixr_builtin?: boolean,
    /** The type in the target standard that the mapping narrows or builds on. */
    fixr_base?: string,
    /** A pattern the value matches in the target standard. */
    fixr_pattern?: string,
    /** The type of each item when the target type is a list or array. */
    fixr_element?: string,
    /** A setting of the target type, such as its precision. */
    fixr_parameter?: string,
    /** The smallest value allowed. */
    fixr_min_inclusive?: string,
    /** The largest value allowed. */
    fixr_max_inclusive?: string,
}


/**
 * A message an action sends, by its number and type code, with the fields it sets or carries over.
 */
export interface OrchestraMessageRefV10 extends OrchestraReferenceV10Mixin {
    /** The fields the message sets or carries over. */
    fixr_identifiers?: OrchestraIdentifiersV10,
    /** The message sent, by name. */
    fixr_name: string,
    /** The MsgType(35) code of the message sent. */
    fixr_msg_type?: string,
    /** The fewest times the message is sent; once when none is given. */
    fixr_impl_min_occurs?: number,
    /** The most times the message is sent, or unbounded. */
    fixr_impl_max_occurs?: string,
}


/**
 * The ordered fields, groups and components of a message.
 */
export interface OrchestraMessageStructureV10 {
    /** The message's fields, groups and components, in order. */
    fixr_members: OrchestraStructureMemberV10[],
    /** Whether one member exactly, or one or more members, must appear. */
    fixr_which?: string,
}


/**
 * A FIX message: its type code, the fields, groups and components it carries in order, and the responses it can cause.
 */
export interface OrchestraMessageV10 extends OrchestraIdentityV10Mixin, OrchestraPedigreeV10Mixin {
    /** The message's fields, groups and components, in order. */
    fixr_structure: OrchestraMessageStructureV10,
    /** What can happen when the message arrives. */
    fixr_responses?: OrchestraResponsesV10,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The message's MsgType(35) code. */
    fixr_msg_type?: string,
    /** The category the message belongs to, by name. */
    fixr_category?: string,
    /** The flow that carries the message, by name. */
    fixr_flow?: string,
}


/**
 * The messages a repository defines.
 */
export interface OrchestraMessagesV10 extends OrchestraContainerV10Mixin {
    /** The messages. */
    fixr_message: OrchestraMessageV10[],
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * When an element was added, changed, deprecated or replaced, by FIX version and extension pack, and whether it is supported.
 */
export interface OrchestraPedigreeV10Mixin {
    /** The FIX version in which the element first appeared. */
    fixr_added?: string,
    /** The extension pack in which the element first appeared. */
    fixr_added_ep?: number,
    /** Whether the latest change was to wording only or to meaning. */
    fixr_change_type?: string,
    /** The FIX version from which the element is deprecated. */
    fixr_deprecated?: string,
    /** The extension pack from which the element is deprecated. */
    fixr_deprecated_ep?: number,
    /** The change request behind the element's latest change. */
    fixr_issue?: string,
    /** The FIX version in which the element last changed. */
    fixr_last_modified?: string,
    /** The FIX version in which another element took this one's place. */
    fixr_replaced?: string,
    /** The extension pack in which another element took this one's place. */
    fixr_replaced_ep?: number,
    /** The tag number of the field that takes this element's place. */
    fixr_replaced_by_field?: number,
    /** Whether a party supports, refuses or ignores the element; supported when none is given. */
    fixr_supported?: string,
    /** The FIX version of the element's latest update. */
    fixr_updated?: string,
    /** The extension pack of the element's latest update. */
    fixr_updated_ep?: number,
}


/**
 * A protocol used on one layer of an interface or session, with its version, layer and delivery guarantee.
 */
export interface OrchestraProtocolV10 {
    /** Notes for readers and hints for software. */
    fixi_annotation?: OrchestraInterfaceAnnotationV10,
    /** The protocol's name, such as FIXT or SBE, or another name of the provider's choice. */
    fixi_name?: string,
    /** The protocol's version. */
    fixi_version?: string,
    /** The layer the protocol works on. */
    fixi_layer?: string,
    /** The delivery guarantee the protocol gives, which a transport, a session or the application may provide. */
    fixi_reliability?: string,
    /** Where to find the Orchestra repository that sets out the protocol's messages and rules. */
    fixi_orchestration?: string,
    /** Attributes from other namespaces, kept as written. */
    fixi_other_attributes?: OrchestraXmlAttribute[],
}


/**
 * The keys by which a use points at a defined element: its number, its scenario and, as a convenience, its name.
 */
export interface OrchestraReferenceV10Mixin {
    /** The number of the element in use; for a field, its tag number. */
    fixr_id: number,
    /** The scenario of the element in use; base when none is given. */
    fixr_scenario?: string,
}


/**
 * A machine-readable set of rules of engagement: the datatypes, code sets, fields, components, groups and messages it defines, and the actors and workflows that use them.
 */
export interface OrchestraRepositoryV10 extends OrchestraContainerV10Mixin {
    /** The file's Dublin Core description, such as its title, publisher and date. */
    fixr_metadata: OrchestraMetadata,
    /** The repository's categories. */
    fixr_categories?: OrchestraCategoriesV10,
    /** The repository's sections. */
    fixr_sections?: OrchestraSectionsV10,
    /** The repository's datatypes. */
    fixr_datatypes: OrchestraDatatypesV10,
    /** The repository's code sets. */
    fixr_code_sets: OrchestraCodeSetsV10,
    /** The repository's fields. */
    fixr_fields: OrchestraFieldsV10,
    /** The repository's actors and flows. */
    fixr_actors?: OrchestraActorsV10,
    /** The repository's components. */
    fixr_components?: OrchestraComponentsV10,
    /** The repository's repeating groups. */
    fixr_groups?: OrchestraGroupsV10,
    /** The repository's messages. */
    fixr_messages: OrchestraMessagesV10,
    /** The repository's concepts. */
    fixr_concepts?: OrchestraConceptsV10,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The repository's name, which stays the same across its minor versions. */
    fixr_name: string,
    /** The repository's version, such as FIX.Latest_EP312. */
    fixr_version: string,
    /** An identifier of the repository, unique worldwide. */
    fixr_guid?: string,
    /** The address of a document that describes the element. */
    fixr_spec_url?: string,
    /** A namespace address that goes with the repository. */
    fixr_namespace?: string,
    /** The FIX version the repository describes, as its ApplVerID(1128) code. */
    fixr_appl_ver_id?: string,
    /** The language the conditions and assignments are written in; Score when none is given. */
    fixr_expression_language?: string,
}


/**
 * What happens when a message arrives, under an optional condition: messages sent, values set, transitions fired and timers scheduled.
 */
export interface OrchestraResponseV10 extends OrchestraActionV10 {
    /** When the response fires, written as an expression; it always fires when none is given. */
    fixr_when?: string,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The response's name. */
    fixr_name?: string,
    /** How the response's timing relates to the request it answers. */
    fixr_sync?: string,
}


/**
 * The responses a message can cause, tried one after another as given.
 */
export interface OrchestraResponsesV10 {
    /** The responses, in order. */
    fixr_response: OrchestraResponseV10[],
}


/**
 * A broad business area, such as pre-trade or post-trade, that categories fall under.
 */
export interface OrchestraSectionV10 extends OrchestraPedigreeV10Mixin {
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The section's name. */
    fixr_name?: string,
    /** Where the section comes when all sections are shown. */
    fixr_display_order?: number,
    /** The FIXML schema file that holds the elements of this section or category. */
    fixr_fixml_file_name?: string,
}


/**
 * The sections a repository defines.
 */
export interface OrchestraSectionsV10 extends OrchestraContainerV10Mixin {
    /** The sections. */
    fixr_section: OrchestraSectionV10[],
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * An application-level service an interface offers, such as order routing, with the Orchestra repository that sets out its rules.
 */
export interface OrchestraServiceV10 extends OrchestraProtocolV10 {
}


/**
 * A value, with what kind it is, that picks out a session, such as a sender or target ID.
 */
export interface OrchestraSessionIdentifierV10 {
    /** The identifier's value. */
    fixi_text?: string,
    /** What kind of identifier this is, such as SenderCompID. */
    fixi_name?: string,
}


/**
 * The session-level protocol of an interface or session, such as FIXT or FIXP.
 */
export interface OrchestraSessionProtocolV10 extends OrchestraProtocolV10 {
}


/**
 * One connection between two parties, with the identifiers, role, activation times and security keys that set it up.
 */
export interface OrchestraSessionV10 extends OrchestraBaseInterfaceV10 {
    /** The identifiers that pick out the session. */
    fixi_identifier?: OrchestraSessionIdentifierV10[],
    /** When the session takes effect. */
    fixi_activation_time?: string,
    /** When the session stops having effect. */
    fixi_deactivation_time?: string,
    /** The party's role in the session. */
    fixi_role?: string,
    /** Security keys for the session, as PEM text. */
    fixi_security_keys?: string,
}


/**
 * The sessions an interface carries.
 */
export interface OrchestraSessionsV10 {
    /** The sessions. */
    fixi_session: OrchestraSessionV10[],
}


/**
 * A named set of states that an actor moves through, from an initial state.
 */
export interface OrchestraStateMachineV10 {
    /** The state the machine starts in. */
    fixr_initial: OrchestraStateV10,
    /** The machine's other states. */
    fixr_state: OrchestraStateV10[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The state machine's name. */
    fixr_name: string,
}


/**
 * One of a state machine's states, with the transitions out of it and what happens on entry, while active and on exit.
 */
export interface OrchestraStateV10 {
    /** The moves out of this state. */
    fixr_transition?: OrchestraTransitionV10[],
    /** What happens on entering the state. */
    fixr_onentry?: OrchestraActionV10,
    /** What runs while the state is active. */
    fixr_activity?: OrchestraActionV10,
    /** What happens on leaving the state. */
    fixr_onexit?: OrchestraActionV10,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The state's name. */
    fixr_name: string,
}


/**
 * One item of an ordered structure, a component, a group or a field, by reference. It holds exactly one of these.
 */
export interface OrchestraStructureMemberV10 {
    /** A component used by reference. */
    fixr_component_ref?: OrchestraComponentRefV10,
    /** A group used by reference. */
    fixr_group_ref?: OrchestraGroupRefV10,
    /** A field used by reference. */
    fixr_field_ref?: OrchestraFieldRefV10,
}


/**
 * A step that starts, stops or restarts an actor's timer, with its interval and what to do when it runs out.
 */
export interface OrchestraTimerScheduleV10 {
    /** What happens when the timer runs out. */
    fixr_activity: OrchestraActionV10,
    /** The actor whose timer or state machine this is, by name. */
    fixr_actor: string,
    /** The timer to start, stop or restart, by name. */
    fixr_name: string,
    /** Whether to start, stop or restart the timer. */
    fixr_operation: string,
    /** How long the timer runs, as an XML Schema duration. */
    fixr_interval?: string,
}


/**
 * A named timer that an actor owns.
 */
export interface OrchestraTimerV10 {
    /** The timer's name. */
    fixr_name: string,
}


/**
 * A move from one state to a named target state, with the condition that allows it.
 */
export interface OrchestraTransitionV10 {
    /** The condition that allows the transition, written as an expression; the transition is always allowed when none is given. */
    fixr_when?: string,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV10,
    /** The transition's name. */
    fixr_name: string,
    /** The state the transition leads to, by name. */
    fixr_target: string,
}


/**
 * The transport-level protocol of an interface or session, with its address, how messages are cast and its use.
 */
export interface OrchestraTransportV10 extends OrchestraProtocolV10 {
    /** The address to connect to, such as a host and port. */
    fixi_address?: string,
    /** Whether messages go to one, some or every receiver; unicast when none is given. */
    fixi_message_cast?: string,
    /** The transport's role, such as primary or alternate. */
    fixi_use?: string,
    /** Attributes from other namespaces, kept as written. */
    fixi_other_attributes?: OrchestraXmlAttribute[],
}


/**
 * A step that fires a named transition of an actor's state machine.
 */
export interface OrchestraTriggerV10 {
    /** The state machine whose transition fires, by name. */
    fixr_state_machine: string,
    /** The actor whose timer or state machine this is, by name. */
    fixr_actor: string,
    /** The transition to fire, by name. */
    fixr_name: string,
}


/**
 * A check that a field's value is unique among the values that share the other fields it names, or among all values when it names none.
 */
export interface OrchestraUniqueV10 {
    /** The fields that scope the check, in order. */
    fixr_field_ref?: OrchestraFieldRefV10[],
}


/**
 * A user interface an interface offers, such as a trading screen, described as a protocol.
 */
export interface OrchestraUserInterfaceV10 extends OrchestraProtocolV10 {
}


/**
 * One input to an action, which is a field, component or group, defined in place or named by reference. It holds exactly one of these.
 */
export interface OrchestraActionParameterV11 {
    /** A field defined in place. */
    fixr_field?: OrchestraFieldV11,
    /** A field used by reference. */
    fixr_field_ref?: OrchestraFieldRefV11,
    /** A component defined in place. */
    fixr_component?: OrchestraComponentV11,
    /** A component used by reference. */
    fixr_component_ref?: OrchestraComponentRefV11,
    /** A repeating group defined in place. */
    fixr_group?: OrchestraGroupV11,
    /** A group used by reference. */
    fixr_group_ref?: OrchestraGroupRefV11,
}


/**
 * One thing an action does: send a message, set a value, fire a transition or schedule a timer. It holds exactly one of these.
 */
export interface OrchestraActionStepV11 {
    /** A message to send. */
    fixr_message_ref?: OrchestraMessageRefV11,
    /** An expression that gives an actor's variable a value, such as $actor.variable=value. */
    fixr_assign?: string,
    /** A transition to fire. */
    fixr_trigger?: OrchestraTriggerV11,
    /** A timer to start, stop or restart. */
    fixr_timer_schedule?: OrchestraTimerScheduleV11,
}


/**
 * Things that happen together, such as when a response fires or a state is entered: messages sent, values set, transitions fired and timers scheduled, with their inputs.
 */
export interface OrchestraActionV11 {
    /** The fields, groups and components the action takes as input, in order. */
    fixr_parameters?: OrchestraActionParameterV11[],
    /** What the action does, in order: messages sent, values set, transitions fired and timers scheduled. */
    fixr_actions: OrchestraActionStepV11[],
}


/**
 * One thing an actor keeps: a variable given as a field, component or group, a state machine or a timer. It holds exactly one of these.
 */
export interface OrchestraActorMemberV11 {
    /** A variable defined in place as a field. */
    fixr_field?: OrchestraFieldV11,
    /** A variable that uses a field by its number. */
    fixr_field_ref?: OrchestraFieldRefV11,
    /** A variable defined in place as a component. */
    fixr_component?: OrchestraComponentV11,
    /** A variable that uses a component by its number. */
    fixr_component_ref?: OrchestraComponentRefV11,
    /** A variable defined in place as a repeating group. */
    fixr_group?: OrchestraGroupV11,
    /** A variable that uses a repeating group by its number. */
    fixr_group_ref?: OrchestraGroupRefV11,
    /** A state machine. */
    fixr_states?: OrchestraStateMachineV11,
    /** A timer. */
    fixr_timer?: OrchestraTimerV11,
}


/**
 * A kind of party in an exchange, such as a buy-side firm or a venue, with the state it keeps: its variables, state machines and timers.
 */
export interface OrchestraActorV11 {
    /** The actor's variables, state machines and timers, in order. */
    fixr_members?: OrchestraActorMemberV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The actor's name, unique among the repository's actors. */
    fixr_name: string,
}


/**
 * One entry of the actors list, an actor or a flow. It holds exactly one of these.
 */
export interface OrchestraActorsMemberV11 {
    /** An actor. */
    fixr_actor?: OrchestraActorV11,
    /** A flow. */
    fixr_flow?: OrchestraFlowV11,
}


/**
 * The parties a repository describes and the one-way flows between them.
 */
export interface OrchestraActorsV11 {
    /** The actors and flows, in order. */
    fixr_members?: OrchestraActorsMemberV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * One part of an annotation, a piece of text or a hint for software. It holds exactly one of these.
 */
export interface OrchestraAnnotationMemberV11 {
    /** A piece of text. */
    fixr_documentation?: OrchestraDocumentationV11,
    /** A hint for software. */
    fixr_appinfo?: OrchestraAppinfoV11,
}


/**
 * Notes for readers and hints for software, attached to an element.
 */
export interface OrchestraAnnotationV11 extends OrchestraPedigreeV11Mixin {
    /** The texts and hints, in order. */
    fixr_members: OrchestraAnnotationMemberV11[],
}


/**
 * A hint for a particular tool or encoding, such as how FIXML renders an element, held as text and open XML.
 */
export interface OrchestraAppinfoV11 extends OrchestraPedigreeV11Mixin {
    /** The text the element holds, as written. */
    fixr_text?: string,
    /** Child elements from other namespaces, kept as written. */
    fixr_any?: OrchestraXmlElement[],
    /** The address of a document that describes the element. */
    fixr_spec_url?: string,
    /** The language of the text, as a language tag. */
    fixr_lang_id?: string,
    /** What the hint is for, such as the encoding it concerns. */
    fixr_purpose?: string,
    /** Attributes from other namespaces, kept as written. */
    fixr_other_attributes?: OrchestraXmlAttribute[],
}


/**
 * What every encoding block shares: notes, and XML in another namespace that says how an element is encoded.
 */
export interface OrchestraBaseEncodingV11 {
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** Child elements from other namespaces, kept as written. */
    fixr_any?: OrchestraXmlElement[],
}


/**
 * What an interface and a session share: the services, encodings and protocols of a connection, layer by layer.
 */
export interface OrchestraBaseInterfaceV11 {
    /** The application-level services offered. */
    fixi_service?: OrchestraServiceV11[],
    /** The user interfaces offered. */
    fixi_user_interface?: OrchestraUserInterfaceV11[],
    /** The encodings used. */
    fixi_encoding?: OrchestraEncodingV11[],
    /** The session-level protocols used. */
    fixi_session_protocol?: OrchestraSessionProtocolV11[],
    /** Other protocols used. */
    fixi_protocol?: OrchestraProtocolV11[],
    /** The transports used. */
    fixi_transport?: OrchestraTransportV11[],
    /** Notes for readers and hints for software. */
    fixi_annotation?: OrchestraInterfaceAnnotationV11,
    /** The interface's or session's name, unique within the file. */
    fixi_name: string,
    /** Attributes from other namespaces, kept as written. */
    fixi_other_attributes?: OrchestraXmlAttribute[],
}


/**
 * How every entry of a group, or a single use of a component, gets its values: the fields, groups and components it sets.
 */
export interface OrchestraBlockAssignmentV11 {
    /** The fields, groups and components the assignment sets, in order. */
    fixr_members: OrchestraStructureMemberV11[],
}


/**
 * The categories a repository sorts its messages and fields into.
 */
export interface OrchestraCategoriesV11 {
    /** The categories. */
    fixr_category?: OrchestraCategoryV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * A business process grouping within a section, such as order handling or market data.
 */
export interface OrchestraCategoryV11 extends OrchestraPedigreeV11Mixin {
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The category's name. */
    fixr_name: string,
    /** The section the category belongs to, by name. */
    fixr_section: string,
}


/**
 * A named list of the values a field may take, each with a name of its own, over one underlying datatype.
 */
export interface OrchestraCodeSetV11 extends OrchestraIdentityV11Mixin, OrchestraScenarioReferenceV11Mixin, OrchestraPedigreeV11Mixin {
    /** The set's codes, in order. */
    fixr_code?: OrchestraCodeV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** The set's datatype, by name. */
    fixr_type: string,
    /** The code a receiver assumes when none is given. */
    fixr_default?: string,
    /** The address of the outside list, such as an ISO standard, that gives the codes. */
    fixr_spec_url?: string,
    /** A datatype whose values a field of this set may hold beside its codes, such as a range kept for user-defined values. */
    fixr_union_data_type?: string,
}


/**
 * The code sets a repository defines.
 */
export interface OrchestraCodeSetsV11 {
    /** The code sets. */
    fixr_code_set?: OrchestraCodeSetV11[],
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * One permitted value of the set, with its name and what goes on the wire.
 */
export interface OrchestraCodeV11 extends OrchestraIdentityV11Mixin, OrchestraPedigreeV11Mixin {
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The value that goes on the wire for this code. */
    fixr_value: string,
    /** A number that places the code when its set is shown. */
    fixr_sort?: number,
    /** A label that places the code with others when its set is shown. */
    fixr_group?: string,
}


/**
 * Where a message or block includes a component, by its number, with its presence and any rules that make it conditional.
 */
export interface OrchestraComponentRefV11 extends OrchestraReferenceV11Mixin, OrchestraPedigreeV11Mixin {
    /** How the component, or every entry of the group, gets its values. */
    fixr_block_assignment?: OrchestraBlockAssignmentV11[],
    /** Rules that make the component's presence depend on other values. */
    fixr_rule?: OrchestraComponentRuleV11[],
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** Whether the item must, may or must not appear, or has a fixed value; optional when none is given. */
    fixr_presence?: string,
    /** A name for this use of the element, so that one message or block can hold it more than once. */
    fixr_instance_name?: string,
}


/**
 * A condition that changes a component's presence, such as making it required.
 */
export interface OrchestraComponentRuleV11 {
    /** When the rule applies, written as an expression. */
    fixr_when: string,
    /** The rule's name. */
    fixr_name?: string,
    /** The presence that applies while the rule's condition holds. */
    fixr_presence?: string,
}


/**
 * A named block of fields, groups and components that messages and other blocks include by reference.
 */
export interface OrchestraComponentV11 extends OrchestraPedigreeV11Mixin, OrchestraIdentityV11Mixin, OrchestraScenarioReferenceV11Mixin {
    /** The fields, groups and components the component holds, in order. */
    fixr_members?: OrchestraStructureMemberV11[],
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The category the component belongs to, by name. */
    fixr_category?: string,
    /** A hint for how a tool shows or reads the element, which no validator checks. */
    fixr_rendering?: string,
    /** Whether one member exactly, or one or more members, must appear. */
    fixr_which?: string,
}


/**
 * The components a repository defines.
 */
export interface OrchestraComponentsV11 {
    /** The components. */
    fixr_component?: OrchestraComponentV11[],
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * One element a concept ties together, named by reference, which is a message, field, component or group. It holds exactly one of these.
 */
export interface OrchestraConceptMemberV11 {
    /** A component used by reference. */
    fixr_component_ref?: OrchestraComponentRefV11,
    /** A group used by reference. */
    fixr_group_ref?: OrchestraGroupRefV11,
    /** A field used by reference. */
    fixr_field_ref?: OrchestraFieldRefV11,
    /** A message, by reference. */
    fixr_message_ref?: OrchestraMessageRefV11,
}


/**
 * A named business idea that ties together the fields, components, groups and messages that express it.
 */
export interface OrchestraConceptV11 {
    /** The fields, components, groups and messages the concept ties together. */
    fixr_members: OrchestraConceptMemberV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The concept's name, unique among the repository's concepts. */
    fixr_name: string,
}


/**
 * The concepts a repository names.
 */
export interface OrchestraConceptsV11 {
    /** The concepts. */
    fixr_concept?: OrchestraConceptV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * A FIX datatype, such as Price or UTCTimestamp, with how it maps to the types of other standards.
 */
export interface OrchestraDatatypeV11 extends OrchestraPedigreeV11Mixin {
    /** How the datatype is written in other standards. */
    fixr_mapped_datatype?: OrchestraMappedDatatypeV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The datatype's name, such as Price. */
    fixr_name: string,
    /** The datatype this one narrows, such as int for Length. */
    fixr_base_type?: string,
}


/**
 * The datatypes a repository uses.
 */
export interface OrchestraDatatypesV11 {
    /** The datatypes. */
    fixr_datatype?: OrchestraDatatypeV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * Text about an element, with its language, purpose and media type.
 */
export interface OrchestraDocumentationV11 extends OrchestraPedigreeV11Mixin {
    /** The text the element holds, as written. */
    fixr_text?: string,
    /** The language of the text, as a language tag. */
    fixr_lang_id?: string,
    /** What the text is for, such as a summary or an example. */
    fixr_purpose?: string,
    /** The media type of the text; text/plain when none is given. */
    fixr_content_type?: string,
}


/**
 * An encoding standard a repository uses, with a name to show and its general encoding information.
 */
export interface OrchestraEncodingStandardV11 {
    /** Encoding details that hold for the whole standard. */
    fixr_encoding?: OrchestraUnnamedEncodingV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The encoding standard's name, which encoding blocks use. */
    fixr_name: string,
    /** The standard's name as a reader sees it. */
    fixr_display_name?: string,
}


/**
 * The encoding standards that a repository's encoding blocks name.
 */
export interface OrchestraEncodingStandardsV11 {
    /** The encoding standards. */
    fixr_encoding_standard?: OrchestraEncodingStandardV11[],
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * An encoding used on an interface or session, such as tag=value, FIXML or SBE.
 */
export interface OrchestraEncodingV11 extends OrchestraProtocolV11 {
}


/**
 * The encoding blocks of one element, one for each encoding standard that needs more information about it.
 */
export interface OrchestraEncodingsV11 {
    /** The encoding blocks, one per standard. */
    fixr_encoding?: OrchestraNamedEncodingV11[],
}


/**
 * The limits on a field's value that a field, a use of it or a rule may set: range, length, presence, fixed or default value, character set and a display hint.
 */
export interface OrchestraFieldConstraintsV11Mixin {
    /** The smallest value allowed. */
    fixr_min_inclusive?: string,
    /** The largest value allowed. */
    fixr_max_inclusive?: string,
    /** The fixed length an implementation uses. */
    fixr_impl_length?: number,
    /** The shortest length an implementation accepts. */
    fixr_impl_min_length?: number,
    /** The longest length an implementation accepts. */
    fixr_impl_max_length?: number,
    /** Whether the item must, may or must not appear, or has a fixed value; optional when none is given. */
    fixr_presence?: string,
    /** The character set of the value, when it is not US-ASCII. */
    fixr_encoding?: string,
    /** The value a receiver assumes when an optional field is left out, or the fixed value of a constant field. */
    fixr_value?: string,
    /** A hint for how a tool shows or reads the element, which no validator checks. */
    fixr_rendering?: string,
}


/**
 * Where a message or block includes a field, by its tag number, with its presence, value limits and any rules.
 */
export interface OrchestraFieldRefV11 extends OrchestraReferenceV11Mixin, OrchestraPedigreeV11Mixin, OrchestraFieldConstraintsV11Mixin {
    /** Rules that make the element's presence or limits depend on other values. */
    fixr_rule?: OrchestraFieldRuleV11[],
    /** An expression that sets the field's value. */
    fixr_assign?: string,
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The tag number of the field that gives this field's length. */
    fixr_length_id?: number,
    /** The tag number of the plain field that this encoded field stands for. */
    fixr_non_encoded_field_id?: number,
    /** A name for this use of the element, so that one message or block can hold it more than once. */
    fixr_instance_name?: string,
}


/**
 * A condition that changes a field's presence, datatype or limits, or a check its value must pass.
 */
export interface OrchestraFieldRuleV11 extends OrchestraFieldConstraintsV11Mixin {
    /** A check that the field's value is unique. */
    fixr_unique?: OrchestraUniqueV11,
    /** Expressions that set or check values while the rule's condition holds. */
    fixr_assign?: string[],
    /** When the rule applies, written as an expression. */
    fixr_when: string,
    /** The rule's name. */
    fixr_name?: string,
    /** The datatype the field takes while the rule's condition holds. */
    fixr_type?: string,
}


/**
 * A FIX field: its tag number, its name, its datatype or its code set, and the limits on its value.
 */
export interface OrchestraFieldV11 extends OrchestraIdentityV11Mixin, OrchestraPedigreeV11Mixin, OrchestraFieldConstraintsV11Mixin {
    /** Rules that make the element's presence or limits depend on other values. */
    fixr_rule?: OrchestraFieldRuleV11[],
    /** An expression that sets the field's value. */
    fixr_assign?: string,
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The datatype that gives the field's values, by name, when no code set does. */
    fixr_type?: string,
    /** The field's code set, by name. */
    fixr_code_set?: string,
    /** The tag number of the field that gives this field's length. */
    fixr_length_id?: number,
    /** The tag number of the plain field that this encoded field stands for. */
    fixr_non_encoded_field_id?: number,
    /** The tag number of the field whose value decides which values this field may take. */
    fixr_discriminator_id?: number,
    /** The category the field belongs to in the base specification. */
    fixr_base_category?: string,
    /** The short name the field takes within its base category in FIXML. */
    fixr_base_category_abbr_name?: string,
    /** A datatype whose values the field may hold beside its codes, such as a range kept for user-defined values. */
    fixr_union_data_type?: string,
}


/**
 * The fields a repository defines.
 */
export interface OrchestraFieldsV11 {
    /** The fields. */
    fixr_field?: OrchestraFieldV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * Messages that travel one way, from a sending actor to a receiving one, with their delivery guarantee.
 */
export interface OrchestraFlowV11 {
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The flow's name. */
    fixr_name: string,
    /** The sending actor, by name. */
    fixr_source: string,
    /** The receiving actor, by name. */
    fixr_destination: string,
    /** How reliably the flow delivers its messages, from best effort to recoverable. */
    fixr_reliability?: string,
}


/**
 * Where a message or block includes a repeating group, by its number, with how many entries it may hold.
 */
export interface OrchestraGroupRefV11 extends OrchestraComponentRefV11 {
    /** The fewest entries an implementation accepts. */
    fixr_impl_min_occurs?: number,
    /** The most entries an implementation accepts, or unbounded. */
    fixr_impl_max_occurs?: string,
}


/**
 * A block whose entries repeat, each with the same fields, groups and components, and whose count a NumInGroup field carries.
 */
export interface OrchestraGroupV11 extends OrchestraPedigreeV11Mixin, OrchestraIdentityV11Mixin, OrchestraScenarioReferenceV11Mixin {
    /** The field that counts the group's entries. */
    fixr_num_in_group?: OrchestraFieldRefV11,
    /** The fields, groups and components that each entry holds, in order. */
    fixr_members?: OrchestraStructureMemberV11[],
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The category the group belongs to, by name. */
    fixr_category?: string,
    /** A hint for how a tool shows or reads the element, which no validator checks. */
    fixr_rendering?: string,
    /** The fewest entries an implementation accepts. */
    fixr_impl_min_occurs?: number,
    /** The most entries an implementation accepts, or unbounded. */
    fixr_impl_max_occurs?: string,
    /** Whether one member exactly, or one or more members, must appear. */
    fixr_which?: string,
}


/**
 * The repeating groups a repository defines.
 */
export interface OrchestraGroupsV11 {
    /** The repeating groups. */
    fixr_group?: OrchestraGroupV11[],
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * A field that a message sent by an action sets, or carries over from the message received, by tag number.
 */
export interface OrchestraIdentifierV11 {
    /** The tag number of the field that is set or carried over. */
    fixr_id: number,
    /** The field that is set or carried over, by name, for readability. */
    fixr_name?: string,
    /** The tag number of the received message's field that the value comes from; the field's own tag number when none is given. */
    fixr_source_id?: number,
}


/**
 * One entry of a message's identifiers, a field carried over or a field set. It holds exactly one of these.
 */
export interface OrchestraIdentifiersMemberV11 {
    /** A field whose value is carried over from the message received. */
    fixr_correlate?: OrchestraIdentifierV11,
    /** A field whose value the message sent sets. */
    fixr_assign?: OrchestraIdentifierV11,
}


/**
 * The fields a message sent by an action sets or carries over.
 */
export interface OrchestraIdentifiersV11 {
    /** The fields carried over or set, in order. */
    fixr_members: OrchestraIdentifiersMemberV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
}


/**
 * The keys of a defined element, its number, name, short name and scenario.
 */
export interface OrchestraIdentityV11Mixin {
    /** The element's number, unique among elements of its kind; for a field, its tag number. */
    fixr_id: number,
    /** The element's name, unique among elements of its kind within one scenario. */
    fixr_name: string,
    /** A short form of the name, which FIXML uses for tags. */
    fixr_abbr_name?: string,
    /** The use case this variant of the element serves, such as a workflow or an asset class; base when none is given. */
    fixr_scenario?: string,
}


/**
 * One part of an annotation in an interfaces file, a text or a hint for software. It holds exactly one of these.
 */
export interface OrchestraInterfaceAnnotationMemberV11 {
    /** A piece of text. */
    fixi_documentation?: OrchestraInterfaceDocumentationV11,
    /** A hint for software. */
    fixi_appinfo?: OrchestraInterfaceAppinfoV11,
}


/**
 * Notes for readers and hints for software, attached to an element of an interfaces file.
 */
export interface OrchestraInterfaceAnnotationV11 {
    /** The texts and hints, in order. */
    fixi_members: OrchestraInterfaceAnnotationMemberV11[],
}


/**
 * A hint for a particular tool on an element of an interfaces file.
 */
export interface OrchestraInterfaceAppinfoV11 {
    /** The text the element holds, as written. */
    fixi_text?: string,
    /** Child elements from other namespaces, kept as written. */
    fixi_any?: OrchestraXmlElement[],
    /** The address of a document that describes the element. */
    fixi_spec_url?: string,
    /** The language of the text, as a language tag. */
    fixi_lang_id?: string,
    /** What the hint is for, such as the tool it concerns. */
    fixi_purpose?: string,
    /** Attributes from other namespaces, kept as written. */
    fixi_other_attributes?: OrchestraXmlAttribute[],
}


/**
 * Text about an element of an interfaces file.
 */
export interface OrchestraInterfaceDocumentationV11 {
    /** The text the element holds, as written. */
    fixi_text?: string,
    /** Child elements from other namespaces, kept as written. */
    fixi_any?: OrchestraXmlElement[],
    /** The language of the text, as a language tag. */
    fixi_lang_id?: string,
    /** What the text is for, such as a summary or an example. */
    fixi_purpose?: string,
    /** The media type of the text; text/plain when none is given. */
    fixi_content_type?: string,
}


/**
 * A named service offering and the sessions it carries, with the protocols on each layer.
 */
export interface OrchestraInterfaceV11 extends OrchestraBaseInterfaceV11 {
    /** The sessions the interface carries. */
    fixi_sessions?: OrchestraSessionsV11,
}


/**
 * A description of the services and sessions a party offers and how to reach them, headed by its Dublin Core metadata.
 */
export interface OrchestraInterfacesV11 {
    /** The file's Dublin Core description, such as its title, publisher and date. */
    fixi_metadata: OrchestraMetadata,
    /** The interfaces the file describes. */
    fixi_interface?: OrchestraInterfaceV11[],
}


/**
 * How a FIX datatype is written in another standard, such as XML Schema or protocol buffers.
 */
export interface OrchestraMappedDatatypeV11 {
    /** Encoding information for this mapping. */
    fixr_encoding?: OrchestraUnnamedEncodingV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The standard the datatype is written in, such as XML or GPB. */
    fixr_standard: string,
    /** Whether the target standard has the type built in, rather than derived. */
    fixr_builtin?: boolean,
    /** The type in the target standard that the mapping narrows or builds on. */
    fixr_base?: string,
    /** A pattern the value matches in the target standard. */
    fixr_pattern?: string,
    /** The type of each item when the target type is a list or array. */
    fixr_element?: string,
    /** The number of items when the target type is an array. */
    fixr_size?: number,
    /** A setting of the target type, such as its precision. */
    fixr_parameter?: string,
    /** The smallest value allowed. */
    fixr_min_inclusive?: string,
    /** The largest value allowed. */
    fixr_max_inclusive?: string,
}


/**
 * A message an action sends, by its number and type code, with the fields it sets or carries over.
 */
export interface OrchestraMessageRefV11 extends OrchestraReferenceV11Mixin {
    /** The fields the message sets or carries over. */
    fixr_identifiers?: OrchestraIdentifiersV11,
    /** The MsgType(35) code of the message sent. */
    fixr_msg_type?: string,
    /** The fewest times the message is sent; once when none is given. */
    fixr_impl_min_occurs?: number,
    /** The most times the message is sent, or unbounded. */
    fixr_impl_max_occurs?: string,
}


/**
 * The ordered fields, groups and components of a message.
 */
export interface OrchestraMessageStructureV11 {
    /** The message's fields, groups and components, in order. */
    fixr_members?: OrchestraStructureMemberV11[],
    /** Whether one member exactly, or one or more members, must appear. */
    fixr_which?: string,
}


/**
 * A FIX message: its type code, the fields, groups and components it carries in order, and the responses it can cause.
 */
export interface OrchestraMessageV11 extends OrchestraIdentityV11Mixin, OrchestraScenarioReferenceV11Mixin, OrchestraPedigreeV11Mixin {
    /** The message's fields, groups and components, in order. */
    fixr_structure?: OrchestraMessageStructureV11,
    /** An expression that sets this scenario of the message apart from its others. */
    fixr_when?: string,
    /** What can happen when the message arrives. */
    fixr_responses?: OrchestraResponsesV11,
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The message's MsgType(35) code. */
    fixr_msg_type?: string,
    /** The category the message belongs to, by name. */
    fixr_category?: string,
    /** The flow that carries the message, by name. */
    fixr_flow?: string,
    /** A hint for how a tool shows or reads the element, which no validator checks. */
    fixr_rendering?: string,
}


/**
 * The messages a repository defines.
 */
export interface OrchestraMessagesV11 {
    /** The messages. */
    fixr_message?: OrchestraMessageV11[],
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * An encoding block that names the encoding standard it is for.
 */
export interface OrchestraNamedEncodingV11 extends OrchestraBaseEncodingV11 {
    /** The encoding standard this block is for, by name. */
    fixr_standard: string,
}


/**
 * When an element was added, changed, deprecated or replaced, by FIX version and extension pack, and whether it is supported.
 */
export interface OrchestraPedigreeV11Mixin {
    /** The FIX version in which the element first appeared. */
    fixr_added?: string,
    /** The extension pack in which the element first appeared. */
    fixr_added_ep?: number,
    /** Whether the latest change was to wording only or to meaning. */
    fixr_change_type?: string,
    /** The FIX version from which the element is deprecated. */
    fixr_deprecated?: string,
    /** The extension pack from which the element is deprecated. */
    fixr_deprecated_ep?: number,
    /** The change request behind the element's latest change. */
    fixr_issue?: string,
    /** The FIX version in which the element last changed. */
    fixr_last_modified?: string,
    /** The FIX version in which another element took this one's place. */
    fixr_replaced?: string,
    /** The extension pack in which another element took this one's place. */
    fixr_replaced_ep?: number,
    /** The tag number of the field that takes this element's place. */
    fixr_replaced_by_field?: number,
    /** Whether a party supports, refuses or ignores the element; supported when none is given. */
    fixr_supported?: string,
    /** The FIX version of the element's latest update. */
    fixr_updated?: string,
    /** The extension pack of the element's latest update. */
    fixr_updated_ep?: number,
}


/**
 * A protocol used on one layer of an interface or session, with its version, layer and delivery guarantee.
 */
export interface OrchestraProtocolV11 {
    /** Notes for readers and hints for software. */
    fixi_annotation?: OrchestraInterfaceAnnotationV11,
    /** The protocol's name, such as FIXT or SBE, or another name of the provider's choice. */
    fixi_name?: string,
    /** The protocol's version. */
    fixi_version?: string,
    /** When this version of the protocol takes effect. */
    fixi_activation_time?: string,
    /** When this version of the protocol stops having effect. */
    fixi_deactivation_time?: string,
    /** When this version of the protocol was deprecated. */
    fixi_deprecated?: string,
    /** The layer the protocol works on. */
    fixi_layer?: string,
    /** The delivery guarantee the protocol gives, which a transport, a session or the application may provide. */
    fixi_reliability?: string,
    /** Where to find the Orchestra repository that sets out the protocol's messages and rules. */
    fixi_orchestration?: string,
    /** Attributes from other namespaces, kept as written. */
    fixi_other_attributes?: OrchestraXmlAttribute[],
}


/**
 * The keys by which a use points at a defined element: its number, its scenario and, as a convenience, its name.
 */
export interface OrchestraReferenceV11Mixin {
    /** The number of the element in use; for a field, its tag number. */
    fixr_id: number,
    /** The element in use, by name, for readability; the number decides which element is meant. */
    fixr_name?: string,
    /** The scenario of the element in use; base when none is given. */
    fixr_scenario?: string,
}


/**
 * A machine-readable set of rules of engagement: the datatypes, code sets, fields, components, groups and messages it defines, and the actors and workflows that use them.
 */
export interface OrchestraRepositoryV11 {
    /** The file's Dublin Core description, such as its title, publisher and date. */
    fixr_metadata: OrchestraMetadata,
    /** The repository's categories. */
    fixr_categories?: OrchestraCategoriesV11,
    /** The repository's sections. */
    fixr_sections?: OrchestraSectionsV11,
    /** The encoding standards the repository's encoding blocks name. */
    fixr_encoding_standards?: OrchestraEncodingStandardsV11,
    /** The repository's datatypes. */
    fixr_datatypes?: OrchestraDatatypesV11,
    /** The repository's code sets. */
    fixr_code_sets?: OrchestraCodeSetsV11,
    /** The repository's fields. */
    fixr_fields?: OrchestraFieldsV11,
    /** The repository's actors and flows. */
    fixr_actors?: OrchestraActorsV11,
    /** The repository's components. */
    fixr_components?: OrchestraComponentsV11,
    /** The repository's repeating groups. */
    fixr_groups?: OrchestraGroupsV11,
    /** The repository's messages. */
    fixr_messages?: OrchestraMessagesV11,
    /** The repository's concepts. */
    fixr_concepts?: OrchestraConceptsV11,
    /** The repository's scenarios. */
    fixr_scenarios?: OrchestraScenariosV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The repository's name, which stays the same across its minor versions. */
    fixr_name: string,
    /** The repository's version, such as FIX.Latest_EP312. */
    fixr_version: string,
    /** An identifier of the repository, unique worldwide. */
    fixr_guid?: string,
    /** The address of a document that describes the element. */
    fixr_spec_url?: string,
    /** A namespace address that goes with the repository. */
    fixr_namespace?: string,
    /** The language the conditions and assignments are written in; Score when none is given. */
    fixr_expression_language?: string,
}


/**
 * What happens when a message arrives, under an optional condition: messages sent, values set, transitions fired and timers scheduled.
 */
export interface OrchestraResponseV11 extends OrchestraActionV11 {
    /** When the response fires, written as an expression; it always fires when none is given. */
    fixr_when?: string,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The response's name. */
    fixr_name?: string,
    /** How the response's timing relates to the request it answers. */
    fixr_sync?: string,
}


/**
 * The responses a message can cause, tried one after another as given.
 */
export interface OrchestraResponsesV11 {
    /** The responses, in order. */
    fixr_response: OrchestraResponseV11[],
}


/**
 * A pointer from an element to the scenario it belongs to, by number and, if wanted, name.
 */
export interface OrchestraScenarioReferenceV11Mixin {
    /** The scenario the element belongs to, by number. */
    fixr_scenario_ref_id?: number,
    /** The scenario the element belongs to, by name, for readability. */
    fixr_scenario_ref?: string,
}


/**
 * A named variant of elements for one use case, such as a workflow or an asset class.
 */
export interface OrchestraScenarioV11 extends OrchestraPedigreeV11Mixin {
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The scenario's name; base when none is given. */
    fixr_name?: string,
}


/**
 * The scenarios a repository defines.
 */
export interface OrchestraScenariosV11 {
    /** The scenarios. */
    fixr_scenario?: OrchestraScenarioV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * A broad business area, such as pre-trade or post-trade, that categories fall under.
 */
export interface OrchestraSectionV11 extends OrchestraPedigreeV11Mixin {
    /** More information that particular encodings need about the element. */
    fixr_encodings?: OrchestraEncodingsV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The section's name. */
    fixr_name: string,
    /** Where the section comes when all sections are shown. */
    fixr_display_order?: number,
}


/**
 * The sections a repository defines.
 */
export interface OrchestraSectionsV11 {
    /** The sections. */
    fixr_section?: OrchestraSectionV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The base address for the list's relative links, which XInclude uses. */
    xml_base?: string,
}


/**
 * An application-level service an interface offers, such as order routing, with the Orchestra repository that sets out its rules.
 */
export interface OrchestraServiceV11 extends OrchestraProtocolV11 {
}


/**
 * A value, with what kind it is, that picks out a session, such as a sender or target ID.
 */
export interface OrchestraSessionIdentifierV11 {
    /** The identifier's value. */
    fixi_text?: string,
    /** What kind of identifier this is, such as SenderCompID. */
    fixi_name?: string,
}


/**
 * The session-level protocol of an interface or session, such as FIXT or FIXP.
 */
export interface OrchestraSessionProtocolV11 extends OrchestraProtocolV11 {
}


/**
 * One connection between two parties, with the identifiers, role, activation times and security keys that set it up.
 */
export interface OrchestraSessionV11 extends OrchestraBaseInterfaceV11 {
    /** The identifiers that pick out the session. */
    fixi_identifier?: OrchestraSessionIdentifierV11[],
    /** The party's role in the session. */
    fixi_role?: string,
    /** Security keys for the session, as PEM text. */
    fixi_security_keys?: string,
    /** When the session takes effect. */
    fixi_activation_time?: string,
    /** When the session stops having effect. */
    fixi_deactivation_time?: string,
}


/**
 * The sessions an interface carries.
 */
export interface OrchestraSessionsV11 {
    /** The sessions. */
    fixi_session: OrchestraSessionV11[],
}


/**
 * A named set of states that an actor moves through, from an initial state.
 */
export interface OrchestraStateMachineV11 {
    /** The state the machine starts in. */
    fixr_initial: OrchestraStateV11,
    /** The machine's other states. */
    fixr_state: OrchestraStateV11[],
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The state machine's name. */
    fixr_name: string,
}


/**
 * One of a state machine's states, with the transitions out of it and what happens on entry, while active and on exit.
 */
export interface OrchestraStateV11 {
    /** The moves out of this state. */
    fixr_transition?: OrchestraTransitionV11[],
    /** What happens on entering the state. */
    fixr_onentry?: OrchestraActionV11,
    /** What runs while the state is active. */
    fixr_activity?: OrchestraActionV11,
    /** What happens on leaving the state. */
    fixr_onexit?: OrchestraActionV11,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The state's name. */
    fixr_name: string,
}


/**
 * One item of an ordered structure, a component, a group or a field, by reference. It holds exactly one of these.
 */
export interface OrchestraStructureMemberV11 {
    /** A component used by reference. */
    fixr_component_ref?: OrchestraComponentRefV11,
    /** A group used by reference. */
    fixr_group_ref?: OrchestraGroupRefV11,
    /** A field used by reference. */
    fixr_field_ref?: OrchestraFieldRefV11,
}


/**
 * A step that starts, stops or restarts an actor's timer, with its interval and what to do when it runs out.
 */
export interface OrchestraTimerScheduleV11 {
    /** What happens when the timer runs out. */
    fixr_activity: OrchestraActionV11,
    /** The actor whose timer or state machine this is, by name. */
    fixr_actor: string,
    /** The timer to start, stop or restart, by name. */
    fixr_name: string,
    /** Whether to start, stop or restart the timer. */
    fixr_operation: string,
    /** How long the timer runs, as an XML Schema duration. */
    fixr_interval?: string,
}


/**
 * A named timer that an actor owns.
 */
export interface OrchestraTimerV11 {
    /** The timer's name. */
    fixr_name: string,
}


/**
 * A move from one state to a named target state, with the condition that allows it.
 */
export interface OrchestraTransitionV11 {
    /** The condition that allows the transition, written as an expression; the transition is always allowed when none is given. */
    fixr_when?: string,
    /** Notes for readers and hints for software about the element. */
    fixr_annotation?: OrchestraAnnotationV11,
    /** The transition's name. */
    fixr_name: string,
    /** The state the transition leads to, by name. */
    fixr_target: string,
}


/**
 * The transport-level protocol of an interface or session, with its address, how messages are cast and its use.
 */
export interface OrchestraTransportV11 extends OrchestraProtocolV11 {
    /** The address to connect to, such as a host and port. */
    fixi_address?: string,
    /** Whether messages go to one, some or every receiver; unicast when none is given. */
    fixi_message_cast?: string,
    /** The transport's role, such as primary or alternate. */
    fixi_use?: string,
    /** Attributes from other namespaces, kept as written. */
    fixi_other_attributes?: OrchestraXmlAttribute[],
}


/**
 * A step that fires a named transition of an actor's state machine.
 */
export interface OrchestraTriggerV11 {
    /** The state machine whose transition fires, by name. */
    fixr_state_machine: string,
    /** The actor whose timer or state machine this is, by name. */
    fixr_actor: string,
    /** The transition to fire, by name. */
    fixr_name: string,
}


/**
 * A check that a field's value is unique among the values that share the other fields it names, or among all values when it names none.
 */
export interface OrchestraUniqueV11 {
    /** The fields that scope the check, in order. */
    fixr_field_ref?: OrchestraFieldRefV11[],
}


/**
 * An encoding block whose standard is clear from where it sits, so it names none.
 */
export interface OrchestraUnnamedEncodingV11 extends OrchestraBaseEncodingV11 {
}


/**
 * A user interface an interface offers, such as a trading screen, described as a protocol.
 */
export interface OrchestraUserInterfaceV11 extends OrchestraProtocolV11 {
}



