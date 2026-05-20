/**
* Anonymous simpleType for xml:space (from xml.xsd).
*/
export enum XmlSpaceType {
    
    default = "default",
    preserve = "preserve",
};

export enum CatComponentType {
    
    Field = "Field",
    Message = "Message",
};

export enum CatIncludeFile {
    
    components = "components",
    fields = "fields",
};

export enum ChangeType {
    
    Editorial = "Editorial",
    Definitional = "Definitional",
};

export enum DatatypeStandardEnum {
    
    /** General Purpose Datatypes */
    ISO11404 = "ISO11404",
    /** Google Protocol Buffers */
    GPB = "GPB",
    /** JSON Schema */
    JSON = "JSON",
    /** Simple Binary Encoding */
    SBE = "SBE",
    /** XML Schema and FIXML */
    XML = "XML",
    /** FIX classic encoding */
    TAG_VALUE = "TAG_VALUE",
};

export enum MemberType {
    
    /** Members are mutually exclusive; exactly one must be present. */
    oneOf = "oneOf",
    /** At least one of the members must be present. */
    anyOf = "anyOf",
};

export enum Presence {
    
    /** The field or component MAY be present; it may be conditionally required based on a rule. */
    optional = "optional",
    /** The field or component MUST be present. */
    required = "required",
    /** The field or component MUST NOT be present. */
    forbidden = "forbidden",
    /** The field or component MAY be present but is not validated. */
    ignored = "ignored",
    /** The field has a constant value; in some encodings it need not be sent on the wire. */
    constant = "constant",
};
/**
* Recommended annotation purposes
*/
export enum PurposeEnum {
    
    /** Brief summary of the element, typically highlighting its key function or purpose, restricted to one paragraph for conciseness. */
    SYNOPSIS = "SYNOPSIS",
    /** Detailed explanation of the element, clarifying its usage, functionality, or background. */
    ELABORATION = "ELABORATION",
    /** Sample or illustration demonstrating how the element is used in practice. */
    EXAMPLE = "EXAMPLE",
    /** For UI when different from canonical name; may have multi-language displays. */
    DISPLAY = "DISPLAY",
    /** Descriptive label or title for the element, may be used for tables, figures, headings or brief annotations. */
    CAPTION = "CAPTION",
    /** Short message or hint that appears when hovering over the element, usually explaining its function or use. */
    TOOLTIP = "TOOLTIP",
    /** Precise and formal explanation of the element, restricted to one sentence in length to ensure brevity. */
    DEFINITION = "DEFINITION",
};
/**
* Message delivery gurantee
*/
export enum Reliability {
    
    bestEffort = "bestEffort",
    idempotent = "idempotent",
    recoverable = "recoverable",
};
/**
* Support level
*/
export enum SupportType {
    
    supported = "supported",
    forbidden = "forbidden",
    ignored = "ignored",
};

export enum Synchronization {
    
    /** Event timing is completely independent */
    asynchronous = "asynchronous",
    /** Requests in-progress block subsequent requests */
    synchronous = "synchronous",
    /** Response timing is dependent on a request, but multiple requests can be in-flight */
    pipelined = "pipelined",
};

export enum TimerOperation {
    
    START = "START",
    CANCEL = "CANCEL",
    /** Cancel and restart */
    RESET = "RESET",
};

export enum Unbounded {
    
    unbounded = "unbounded",
};
/**
* A second domain of valid values. The 'Reserved' types should only be applied Code Sets.
*/
export enum UnionDataType {
    
    Qty = "Qty",
    Reserved100Plus = "Reserved100Plus",
    Reserved1000Plus = "Reserved1000Plus",
    Reserved4000Plus = "Reserved4000Plus",
    Tenor = "Tenor",
};

export enum Layer {
    
    application = "application",
    presentation = "presentation",
    session = "session",
    transport = "transport",
};

export enum MessageCast {
    
    unicast = "unicast",
    multicast = "multicast",
    broadcast = "broadcast",
};
/**
* List of FIX protocols to standardize spelling
*/
export enum ProtocolEnum {
    
    /** FIX 4.x session layer */
    FIX4 = "FIX4",
    /** FIX Transport Session Protocol */
    FIXT = "FIXT",
    /** FIX Performance Session Layer */
    FIXP = "FIXP",
    /** Tag Value encoding (classic FIX) */
    tagvalue = "tagvalue",
    /** XML Schema */
    FIXML = "FIXML",
    /** FIX Adapted for Streaming */
    FAST = "FAST",
    /** Simple Binary Encoding */
    SBE = "SBE",
    /** Simple Open Framing Header */
    SOFH = "SOFH",
    /** Google Protocol Buffers */
    GPB = "GPB",
    /** Javascript Object Notation */
    JSON = "JSON",
    /** FIX over TLS security recommendation */
    FIXS = "FIXS",
};
/**
* Recommended annotation purposes
*/
export enum InterfacePurposeEnum {
    
    SYNOPSIS = "SYNOPSIS",
    ELABORATION = "ELABORATION",
    EXAMPLE = "EXAMPLE",
    /** For UI when different from canonical name; may have multi-language displays */
    DISPLAY = "DISPLAY",
};

export enum InterfaceReliability {
    
    bestEffort = "bestEffort",
    idempotent = "idempotent",
    recoverable = "recoverable",
};

export enum Role {
    
    initiator = "initiator",
    acceptor = "acceptor",
    client = "client",
    server = "server",
};

export enum TransportUseEnum {
    
    primary = "primary",
    secondary = "secondary",
    alternate = "alternate",
};


/**
 * This is the default type for all of the DC elements. It permits text content only with optional xml:lang attribute. Text is allowed because mixed="true", but sub-elements are disallowed because minOccurs="0" and maxOccurs="0" are on the xs:any tag. This complexType allows for restriction or extension permitting child elements.
 */
export interface DcSimpleLiteral {
    /** Mixed text content of the element. */
    value?: string,
    /** Pass-through xs:any content as raw strings. */
    content?: string[],
    lang?: string,
}


/**
 * This complexType is included as a convenience for schema authors who need to define a root or container element for all of the DC elements.
 */
export interface DcElementContainer {
    /** Free-text value of the Dublin Core element/refinement `title`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    title?: string,
    /** Free-text value of the Dublin Core element/refinement `creator`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    creator?: string,
    /** Free-text value of the Dublin Core element/refinement `subject`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    subject?: string,
    /** Free-text value of the Dublin Core element/refinement `description`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    description?: string,
    /** Free-text value of the Dublin Core element/refinement `publisher`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    publisher?: string,
    /** Free-text value of the Dublin Core element/refinement `contributor`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    contributor?: string,
    /** Free-text value of the Dublin Core element/refinement `date`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    date?: string,
    /** Free-text value of the Dublin Core element/refinement `format`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    format?: string,
    /** Free-text value of the Dublin Core element/refinement `source`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    source?: string,
    /** Free-text value of the Dublin Core element/refinement `language`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    language?: string,
    /** Free-text value of the Dublin Core element/refinement `relation`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    relation?: string,
    /** Free-text value of the Dublin Core element/refinement `coverage`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    coverage?: string,
    /** Free-text value of the Dublin Core element/refinement `rights`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    rights?: string,
    /** Free-text value of the Dublin Core element/refinement `alternative`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    alternative?: string,
    /** Free-text value of the Dublin Core element/refinement `tableOfContents`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    table_of_contents?: string,
    /** Free-text value of the Dublin Core element/refinement `abstract`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    abstract?: string,
    /** Free-text value of the Dublin Core element/refinement `created`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    created?: string,
    /** Free-text value of the Dublin Core element/refinement `valid`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    valid?: string,
    /** Free-text value of the Dublin Core element/refinement `available`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    available?: string,
    /** Free-text value of the Dublin Core element/refinement `issued`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    issued?: string,
    /** Free-text value of the Dublin Core element/refinement `modified`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    modified?: string,
    /** Free-text value of the Dublin Core element/refinement `dateAccepted`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    date_accepted?: string,
    /** Free-text value of the Dublin Core element/refinement `dateCopyrighted`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    date_copyrighted?: string,
    /** Free-text value of the Dublin Core element/refinement `dateSubmitted`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    date_submitted?: string,
    /** Free-text value of the Dublin Core element/refinement `extent`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    extent?: string,
    /** Free-text value of the Dublin Core element/refinement `medium`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    medium?: string,
    /** Free-text value of the Dublin Core element/refinement `isVersionOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_version_of?: string,
    /** Free-text value of the Dublin Core element/refinement `hasVersion`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    has_version?: string,
    /** Free-text value of the Dublin Core element/refinement `isReplacedBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_replaced_by?: string,
    /** Free-text value of the Dublin Core element/refinement `replaces`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    replaces?: string,
    /** Free-text value of the Dublin Core element/refinement `isRequiredBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_required_by?: string,
    /** Free-text value of the Dublin Core element/refinement `requires`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    requires?: string,
    /** Free-text value of the Dublin Core element/refinement `isPartOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_part_of?: string,
    /** Free-text value of the Dublin Core element/refinement `hasPart`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    has_part?: string,
    /** Free-text value of the Dublin Core element/refinement `isReferencedBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_referenced_by?: string,
    /** Free-text value of the Dublin Core element/refinement `references`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    references?: string,
    /** Free-text value of the Dublin Core element/refinement `isFormatOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_format_of?: string,
    /** Free-text value of the Dublin Core element/refinement `hasFormat`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    has_format?: string,
    /** Free-text value of the Dublin Core element/refinement `conformsTo`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    conforms_to?: string,
    /** Free-text value of the Dublin Core element/refinement `spatial`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    spatial?: string,
    /** Free-text value of the Dublin Core element/refinement `temporal`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    temporal?: string,
    /** Free-text value of the Dublin Core element/refinement `audience`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    audience?: string,
    /** Free-text value of the Dublin Core element/refinement `accrualMethod`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    accrual_method?: string,
    /** Free-text value of the Dublin Core element/refinement `accrualPeriodicity`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    accrual_periodicity?: string,
    /** Free-text value of the Dublin Core element/refinement `accrualPolicy`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    accrual_policy?: string,
    /** Free-text value of the Dublin Core element/refinement `instructionalMethod`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    instructional_method?: string,
    /** Free-text value of the Dublin Core element/refinement `provenance`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    provenance?: string,
    /** Free-text value of the Dublin Core element/refinement `rightsHolder`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    rights_holder?: string,
    /** Free-text value of the Dublin Core element/refinement `mediator`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    mediator?: string,
    /** Free-text value of the Dublin Core element/refinement `educationLevel`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    education_level?: string,
    /** Free-text value of the Dublin Core element/refinement `accessRights`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    access_rights?: string,
    /** Free-text value of the Dublin Core element/refinement `license`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    license?: string,
    /** Free-text value of the Dublin Core element/refinement `bibliographicCitation`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    bibliographic_citation?: string,
    /** Free-text value of the Dublin Core element/refinement `type`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    type?: string,
    /** Free-text value of the Dublin Core element/refinement `identifier`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    identifier?: string,
}



export interface DcAny extends DcSimpleLiteral {
}



export interface DcTitle extends DcAny {
}



export interface DcCreator extends DcAny {
}



export interface DcSubject extends DcAny {
}



export interface DcDescription extends DcAny {
}



export interface DcPublisher extends DcAny {
}



export interface DcContributor extends DcAny {
}



export interface DcDate extends DcAny {
}



export interface DcType extends DcAny {
}



export interface DcFormat extends DcAny {
}



export interface DcIdentifier extends DcAny {
}



export interface DcSource extends DcAny {
}



export interface DcLanguage extends DcAny {
}



export interface DcRelation extends DcAny {
}



export interface DcCoverage extends DcAny {
}



export interface DcRights extends DcAny {
}


/**
 * This group is included as a convenience for schema authors who need to refer to all the elements in the http://purl.org/dc/elements/1.1/ namespace.
 */
export interface DcElementsGroup {
}



export interface DctermsLCSH extends DcSimpleLiteral {
}



export interface DctermsMESH extends DcSimpleLiteral {
}



export interface DctermsDDC extends DcSimpleLiteral {
}



export interface DctermsLCC extends DcSimpleLiteral {
}



export interface DctermsUDC extends DcSimpleLiteral {
}



export interface DctermsPeriod extends DcSimpleLiteral {
}



export interface DctermsW3CDTF extends DcSimpleLiteral {
}



export interface DctermsDCMIType extends DcSimpleLiteral {
}



export interface DctermsIMT extends DcSimpleLiteral {
}



export interface DctermsURI extends DcSimpleLiteral {
}



export interface DctermsISO6392 extends DcSimpleLiteral {
}



export interface DctermsISO6393 extends DcSimpleLiteral {
}



export interface DctermsRFC1766 extends DcSimpleLiteral {
}



export interface DctermsRFC3066 extends DcSimpleLiteral {
}



export interface DctermsRFC4646 extends DcSimpleLiteral {
}



export interface DctermsPoint extends DcSimpleLiteral {
}



export interface DctermsISO3166 extends DcSimpleLiteral {
}



export interface DctermsBox extends DcSimpleLiteral {
}



export interface DctermsTGN extends DcSimpleLiteral {
}


/**
 * This is included as a convenience for schema authors who need to define a root or container element for all of the DC elements and element refinements.
 */
export interface DctermsElementOrRefinementContainer {
    /** Free-text value of the Dublin Core element/refinement `title`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    title?: string,
    /** Free-text value of the Dublin Core element/refinement `creator`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    creator?: string,
    /** Free-text value of the Dublin Core element/refinement `subject`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    subject?: string,
    /** Free-text value of the Dublin Core element/refinement `description`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    description?: string,
    /** Free-text value of the Dublin Core element/refinement `publisher`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    publisher?: string,
    /** Free-text value of the Dublin Core element/refinement `contributor`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    contributor?: string,
    /** Free-text value of the Dublin Core element/refinement `date`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    date?: string,
    /** Free-text value of the Dublin Core element/refinement `format`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    format?: string,
    /** Free-text value of the Dublin Core element/refinement `source`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    source?: string,
    /** Free-text value of the Dublin Core element/refinement `language`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    language?: string,
    /** Free-text value of the Dublin Core element/refinement `relation`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    relation?: string,
    /** Free-text value of the Dublin Core element/refinement `coverage`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    coverage?: string,
    /** Free-text value of the Dublin Core element/refinement `rights`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    rights?: string,
    /** Free-text value of the Dublin Core element/refinement `alternative`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    alternative?: string,
    /** Free-text value of the Dublin Core element/refinement `tableOfContents`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    table_of_contents?: string,
    /** Free-text value of the Dublin Core element/refinement `abstract`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    abstract?: string,
    /** Free-text value of the Dublin Core element/refinement `created`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    created?: string,
    /** Free-text value of the Dublin Core element/refinement `valid`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    valid?: string,
    /** Free-text value of the Dublin Core element/refinement `available`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    available?: string,
    /** Free-text value of the Dublin Core element/refinement `issued`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    issued?: string,
    /** Free-text value of the Dublin Core element/refinement `modified`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    modified?: string,
    /** Free-text value of the Dublin Core element/refinement `dateAccepted`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    date_accepted?: string,
    /** Free-text value of the Dublin Core element/refinement `dateCopyrighted`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    date_copyrighted?: string,
    /** Free-text value of the Dublin Core element/refinement `dateSubmitted`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    date_submitted?: string,
    /** Free-text value of the Dublin Core element/refinement `extent`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    extent?: string,
    /** Free-text value of the Dublin Core element/refinement `medium`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    medium?: string,
    /** Free-text value of the Dublin Core element/refinement `isVersionOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_version_of?: string,
    /** Free-text value of the Dublin Core element/refinement `hasVersion`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    has_version?: string,
    /** Free-text value of the Dublin Core element/refinement `isReplacedBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_replaced_by?: string,
    /** Free-text value of the Dublin Core element/refinement `replaces`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    replaces?: string,
    /** Free-text value of the Dublin Core element/refinement `isRequiredBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_required_by?: string,
    /** Free-text value of the Dublin Core element/refinement `requires`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    requires?: string,
    /** Free-text value of the Dublin Core element/refinement `isPartOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_part_of?: string,
    /** Free-text value of the Dublin Core element/refinement `hasPart`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    has_part?: string,
    /** Free-text value of the Dublin Core element/refinement `isReferencedBy`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_referenced_by?: string,
    /** Free-text value of the Dublin Core element/refinement `references`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    references?: string,
    /** Free-text value of the Dublin Core element/refinement `isFormatOf`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    is_format_of?: string,
    /** Free-text value of the Dublin Core element/refinement `hasFormat`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    has_format?: string,
    /** Free-text value of the Dublin Core element/refinement `conformsTo`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    conforms_to?: string,
    /** Free-text value of the Dublin Core element/refinement `spatial`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    spatial?: string,
    /** Free-text value of the Dublin Core element/refinement `temporal`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    temporal?: string,
    /** Free-text value of the Dublin Core element/refinement `audience`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    audience?: string,
    /** Free-text value of the Dublin Core element/refinement `accrualMethod`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    accrual_method?: string,
    /** Free-text value of the Dublin Core element/refinement `accrualPeriodicity`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    accrual_periodicity?: string,
    /** Free-text value of the Dublin Core element/refinement `accrualPolicy`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    accrual_policy?: string,
    /** Free-text value of the Dublin Core element/refinement `instructionalMethod`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    instructional_method?: string,
    /** Free-text value of the Dublin Core element/refinement `provenance`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    provenance?: string,
    /** Free-text value of the Dublin Core element/refinement `rightsHolder`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    rights_holder?: string,
    /** Free-text value of the Dublin Core element/refinement `mediator`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    mediator?: string,
    /** Free-text value of the Dublin Core element/refinement `educationLevel`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    education_level?: string,
    /** Free-text value of the Dublin Core element/refinement `accessRights`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    access_rights?: string,
    /** Free-text value of the Dublin Core element/refinement `license`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    license?: string,
    /** Free-text value of the Dublin Core element/refinement `bibliographicCitation`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    bibliographic_citation?: string,
    /** Free-text value of the Dublin Core element/refinement `type`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    type?: string,
    /** Free-text value of the Dublin Core element/refinement `identifier`. Expanded from the XSD substitutionGroup chain rooted at dc:any. */
    identifier?: string,
}



export interface DctermsTitle extends DcTitle {
}



export interface DctermsCreator extends DcCreator {
}



export interface DctermsSubject extends DcSubject {
}



export interface DctermsDescription extends DcDescription {
}



export interface DctermsPublisher extends DcPublisher {
}



export interface DctermsContributor extends DcContributor {
}



export interface DctermsDate extends DcDate {
}



export interface DctermsType extends DcType {
}



export interface DctermsFormat extends DcFormat {
}



export interface DctermsIdentifier extends DcIdentifier {
}



export interface DctermsSource extends DcSource {
}



export interface DctermsLanguage extends DcLanguage {
}



export interface DctermsRelation extends DcRelation {
}



export interface DctermsCoverage extends DcCoverage {
}



export interface DctermsRights extends DcRights {
}



export interface DctermsAlternative extends DctermsTitle {
}



export interface DctermsTableOfContents extends DctermsDescription {
}



export interface DctermsAbstract extends DctermsDescription {
}



export interface DctermsCreated extends DctermsDate {
}



export interface DctermsValid extends DctermsDate {
}



export interface DctermsAvailable extends DctermsDate {
}



export interface DctermsIssued extends DctermsDate {
}



export interface DctermsModified extends DctermsDate {
}



export interface DctermsDateAccepted extends DctermsDate {
}



export interface DctermsDateCopyrighted extends DctermsDate {
}



export interface DctermsDateSubmitted extends DctermsDate {
}



export interface DctermsExtent extends DctermsFormat {
}



export interface DctermsMedium extends DctermsFormat {
}



export interface DctermsIsVersionOf extends DctermsRelation {
}



export interface DctermsHasVersion extends DctermsRelation {
}



export interface DctermsIsReplacedBy extends DctermsRelation {
}



export interface DctermsReplaces extends DctermsRelation {
}



export interface DctermsIsRequiredBy extends DctermsRelation {
}



export interface DctermsRequires extends DctermsRelation {
}



export interface DctermsIsPartOf extends DctermsRelation {
}



export interface DctermsHasPart extends DctermsRelation {
}



export interface DctermsIsReferencedBy extends DctermsRelation {
}



export interface DctermsReferences extends DctermsRelation {
}



export interface DctermsIsFormatOf extends DctermsRelation {
}



export interface DctermsHasFormat extends DctermsRelation {
}



export interface DctermsConformsTo extends DctermsRelation {
}



export interface DctermsSpatial extends DctermsCoverage {
}



export interface DctermsTemporal extends DctermsCoverage {
}



export interface DctermsAudience extends DcAny {
}



export interface DctermsAccrualMethod extends DcAny {
}



export interface DctermsAccrualPeriodicity extends DcAny {
}



export interface DctermsAccrualPolicy extends DcAny {
}



export interface DctermsInstructionalMethod extends DcAny {
}



export interface DctermsProvenance extends DcAny {
}



export interface DctermsRightsHolder extends DcAny {
}



export interface DctermsMediator extends DctermsAudience {
}



export interface DctermsEducationLevel extends DctermsAudience {
}



export interface DctermsAccessRights extends DctermsRights {
}



export interface DctermsLicense extends DctermsRights {
}



export interface DctermsBibliographicCitation extends DctermsIdentifier {
}


/**
 * This group is included as a convenience for schema authors who need to refer to all the DC elements and element refinements in the http://purl.org/dc/elements/1.1/ and http://purl.org/dc/terms namespaces. N.B. Refinements available via substitution groups.
 */
export interface DctermsElementsAndRefinementsGroup {
}



export interface XmlSpecialAttrs {
    base?: string,
    lang?: string,
    space?: string,
    id?: string,
}


/**
 * Container for the global <xs:attribute> declarations defined in xml.xsd. Each attribute here is referenceable from other XSDs via ``ref="xml:<name>"``.
 */
export interface XmlGlobalAttributes {
    /** lang (as an attribute name) denotes an attribute whose value is a language code for the natural language of the content of any element; its value is inherited. This name is reserved by virtue of its definition in the XML specification. Notes Attempting to install the relevant ISO 2- and 3-letter codes as the enumerated possible values is probably never going to be a realistic possibility. See BCP 47 at http://www.rfc-editor.org/rfc/bcp/bcp47.txt and the IANA language subtag registry at http://www.iana.org/assignments/language-subtag-registry for further information. The union allows for the 'un-declaration' of xml:lang with the empty string. */
    lang?: string,
    /** space (as an attribute name) denotes an attribute whose value is a keyword indicating what whitespace processing discipline is intended for the content of the element; its value is inherited. This name is reserved by virtue of its definition in the XML specification. */
    space?: string,
    /** base (as an attribute name) denotes an attribute whose value provides a URI to be used as the base for interpreting any relative URIs in the scope of the element on which it appears; its value is inherited. This name is reserved by virtue of its definition in the XML Base specification. See http://www.w3.org/TR/xmlbase/ for information about this attribute. */
    base?: string,
    /** id (as an attribute name) denotes an attribute whose value should be interpreted as if declared to be of type ID. This name is reserved by virtue of its definition in the xml:id specification. See http://www.w3.org/TR/xml-id/ for information about this attribute. */
    id?: string,
}



export interface EntityAttribGrp {
    added?: string,
    added_ep?: string,
    change_type?: string,
    deprecated_ep?: string,
    issue?: string,
    last_modified?: string,
    replaced?: string,
    replaced_ep?: string,
    replaced_by_field?: string,
    supported?: string,
    updated?: string,
    updated_ep?: string,
    deprecated?: string,
}


/**
 * Attributes of a field that be overridden by a rule
 */
export interface FieldAttribGrp {
    /** Inclusive lower bound */
    min_inclusive?: string,
    /** Inclusive upper bound */
    max_inclusive?: string,
    /** Fixed length */
    impl_length?: number,
    impl_min_length?: number,
    impl_max_length?: number,
    presence?: string,
    /** If presence is optional, then it represents a default when the sender does not provide the field. If presence is constant, then it is the constant value. */
    value?: string,
    /** A hint to processes about how to interpret the element. Not validated. */
    rendering?: string,
    /** Character encoding if other than US-ASCII */
    encoding?: string,
}


/**
 * The identifiers of a message element
 */
export interface OidGrp {
    abbr_name?: string,
    /** Unique identifier of a scenario. Default is '1' for base scenario. */
    scenario_id?: string,
    /** Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag */
    id: string,
    name: string,
    /** The use case of an element, distinguished by workflow, asset class, etc. */
    scenario?: string,
}


/**
 * A reference to a message element by its key identifiers
 */
export interface RefidGrp {
    /** Unique identifier of a scenario. Default is '1' for base scenario. */
    scenario_id?: string,
    /** Numeric identifier generally must be unique within a file for an element type, e.g. unique field tag */
    id: string,
    /** The name is optional as part of a reference and only for convenience. It is not enforced by referential integrity. However, the name of the referred object is authoritative. A validator may check the consistency between the name used for the reference and the name of the referred object. */
    name?: string,
    /** The use case of an element, distinguished by workflow, asset class, etc. */
    scenario?: string,
}


/**
 * A reference to a scenario by its key identifiers. There are no defaults as scenario references are optional.
 */
export interface ScenarioRefGrp {
    /** Unique identifier of a scenario. The identifier is required when referencing another scenario. */
    scenario_ref_id?: string,
    /** Name of a scenario. The name is optional as part of a reference and only for convenience. */
    scenario_ref?: string,
}



export interface ActionType {
    field?: FieldType[],
    field_ref?: FieldRefType[],
    component?: ComponentType[],
    component_ref?: ComponentRefType[],
    group_ref?: GroupRefType[],
    /** Send a message */
    message_ref?: MessageRefType[],
    /** Trigger a state transtion in a state machine */
    trigger?: TriggerType[],
    timer_schedule?: TimerSchedule[],
    group?: GroupType[],
    /** Content of element holds an assignment expression for a state variable in the form '$actor.variable=value' */
    assign?: string[],
}


/**
 * Represents a class of participants
 */
export interface ActorType {
    field?: FieldType[],
    field_ref?: FieldRefType[],
    component?: ComponentType[],
    component_ref?: ComponentRefType[],
    group_ref?: GroupRefType[],
    states?: StateMachineType[],
    timer?: TimerType[],
    group?: GroupType[],
    annotation?: Annotation,
    name: string,
}



export interface Annotation extends EntityAttribGrp {
    documentation?: Documentation[],
    appinfo?: Appinfo[],
}


/**
 * Usage specific annotation, optionally with link to an external reference or standard
 */
export interface Appinfo extends EntityAttribGrp {
    /** Reference documentation */
    spec_url?: string,
    /** Mixed text content of the element. */
    value?: string,
    /** Pass-through xs:any content as raw strings. */
    content?: string[],
    /** Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point). */
    extra_attributes?: string[],
    lang_id?: string,
    purpose?: string,
}



export interface BlockAssignmentType {
    component_ref?: ComponentRefType[],
    group_ref?: GroupRefType[],
    field_ref?: FieldRefType[],
}



export interface CategoryType extends EntityAttribGrp {
    fixml_file_name?: string,
    component_type?: string,
    include_file?: string,
    annotation?: Annotation,
    name: string,
    section: string,
}



export interface CodeSetType extends OidGrp, ScenarioRefGrp, EntityAttribGrp {
    code?: CodeType[],
    default?: string,
    /** Reference documentation for an external code set */
    spec_url?: string,
    union_data_type?: string,
    annotation?: Annotation,
    /** Underlying FIX datatype of codes */
    type: string,
}



export interface CodeType extends OidGrp, EntityAttribGrp {
    /** The XML processor will remove line feeds, carriage returns, tabs, leading and trailing spaces, and multiple spaces. However, single internal spaces are allowed. May be further restricted by an external style. */
    value: string,
    /** Sort and group may be used to organize visualization of a code set. */
    sort?: number,
    annotation?: Annotation,
    group?: string,
}



export interface ComponentRefType extends RefidGrp, EntityAttribGrp {
    /** Specifies a how a component or each group entry is populated (optional) */
    block_assignment?: BlockAssignmentType[],
    presence?: string,
    /** Rule to tell when a conditionally require component */
    rule?: ComponentRuleType[],
    annotation?: Annotation,
    /** Override the component name for this instance, for code generation and the like. Allows more than one instance of a component in a message. */
    instance_name?: string,
}



export interface ComponentRuleType {
    when: string,
    /** Overrides presence when expression is true */
    presence?: string,
    /** Name of this rule */
    name?: string,
}



export interface ComponentType extends EntityAttribGrp, OidGrp, ScenarioRefGrp {
    component_ref?: ComponentRefType[],
    group_ref?: GroupRefType[],
    field_ref?: FieldRefType[],
    /** A hint to processes about how to interpret the element. Not validated. */
    rendering?: string,
    which?: string,
    annotation?: Annotation,
    category?: string,
}



export interface ConceptType {
    component_ref?: ComponentRefType[],
    group_ref?: GroupRefType[],
    field_ref?: FieldRefType[],
    /** Send a message */
    message_ref?: MessageRefType[],
    annotation?: Annotation,
    name: string,
}



export interface Documentation extends EntityAttribGrp {
    /** Mixed text content of the element. */
    value?: string,
    /** Pass-through xs:any content as raw strings. */
    content?: string[],
    lang_id?: string,
    purpose?: string,
    content_type?: string,
}



export interface FieldRefType extends RefidGrp, EntityAttribGrp, FieldAttribGrp {
    /** Identifies a field used as a length prefix */
    length_id?: string,
    /** Identifies a non-encoded field related to an encoded field */
    non_encoded_field_id?: string,
    /** Rule to tell when a conditionally require field is required or forbidden, to override other attributes, or perform validation. */
    rule?: FieldRuleType[],
    /** Content of element holds an assignment expression for a message field or state variable */
    assign?: string,
    annotation?: Annotation,
    /** Override the field name for this instance, for code generation and the like. Allows more than one instance of a field in a message or component. */
    instance_name?: string,
}



export interface UniqueInline {
    /** Other field or fields that scope uniqueness. If none provided, then the field value must be globally unique. */
    field_ref?: FieldRefType[],
}



export interface FieldRuleType extends FieldAttribGrp {
    unique?: UniqueInline,
    when: string,
    /** Content of element holds an assignment expression for a message field or state variable. This can be used for field validation. */
    assign?: string[],
    /** Name of this rule */
    name?: string,
    /** Overrides the type of the referenced field. */
    type?: string,
}



export interface FieldType extends OidGrp, EntityAttribGrp, FieldAttribGrp {
    /** Identifies a field used as a length prefix */
    length_id?: string,
    /** Identifies a non-encoded field related to an encoded field */
    non_encoded_field_id?: string,
    /** Identifies a field used as a discriminator for this field's domain */
    discriminator_id?: string,
    base_category?: string,
    base_category_abbr_name?: string,
    union_data_type?: string,
    /** Rule to tell when a conditionally require field is required or forbidden, to override other attributes, or perform validation. */
    rule?: FieldRuleType[],
    /** Content of element holds an assignment expression for a message field or state variable */
    assign?: string,
    annotation?: Annotation,
    /** Attribute type refers to a datatype name */
    type?: string,
    /** Attribute codeSet refers to a codeSet name */
    code_set?: string,
}


/**
 * A stream of messages in one direction
 */
export interface FlowType {
    /** Name of the actor that originates messages */
    source: string,
    /** Name of the actor that receives messages. */
    destination: string,
    annotation?: Annotation,
    name: string,
    reliability?: string,
}



export interface GroupRefType extends ComponentRefType {
    impl_min_occurs?: number,
    impl_max_occurs?: string,
}


/**
 * A repeating group. Logically, groupType is a subclass of componentType, but to make numInGroup first in the sequence, it cannot be an extension.
 */
export interface GroupType extends EntityAttribGrp, OidGrp, ScenarioRefGrp {
    num_in_group?: FieldRefType,
    component_ref?: ComponentRefType[],
    group_ref?: GroupRefType[],
    field_ref?: FieldRefType[],
    /** A hint to processes about how to interpret the element. Not validated. */
    rendering?: string,
    /** Lower bound of group instances (numInGroup) */
    impl_min_occurs?: number,
    /** Upper bound of group instances (numInGroup) */
    impl_max_occurs?: string,
    /** Member selection within each group instance */
    which?: string,
    annotation?: Annotation,
    category?: string,
}



export interface IdentifiersType {
    /** Correlated field IDs between two message types */
    correlate?: IdentifierType[],
    /** Field ID assigned */
    assign?: IdentifierType[],
    annotation?: Annotation,
}



export interface IdentifierType {
    /** Mixed text content of the element. */
    value?: string,
    name?: string,
}



export interface ExtensionInline {
    /** Pass-through xs:any content as raw strings. */
    content?: string[],
}



export interface MappedDatatype {
    /** A datatype may be mapped to an XML snippet in the native schema belonging to its encoding standard. */
    extension?: ExtensionInline,
    standard: string,
    builtin?: boolean,
    /** A lexical restriction from a base type */
    pattern?: string,
    /** Element type of an aggregate type such as an array or sequence */
    element?: string,
    /** Size of an aggregate type such as an array. That is, the number of elements. */
    size?: number,
    parameter?: string,
    /** Inclusive lower bound of values */
    min_inclusive?: string,
    /** Inclusive upper bound of values */
    max_inclusive?: string,
    annotation?: Annotation,
    /** A datatype from which a subtype is created by restriction or a derived type is created by a generator */
    base?: string,
}



export interface MessageRefType extends RefidGrp {
    identifiers?: IdentifiersType,
    msg_type?: string,
    impl_min_occurs?: number,
    /** The same message type may be sent one or more times */
    impl_max_occurs?: string,
}



export interface StructureInline {
    component_ref?: ComponentRefType[],
    group_ref?: GroupRefType[],
    field_ref?: FieldRefType[],
    which?: string,
}



export interface ResponsesInline {
    /** Responses are evaluated and triggered in the order listed */
    response: ResponseType[],
}



export interface MessageType extends OidGrp, ScenarioRefGrp, EntityAttribGrp {
    structure?: StructureInline,
    /** A condition that distinguishes when a scenario of a message type applies. It could be used to generate a decision tree to correlate an incoming message to its scenario, or to decide which scenario of a request message to send. */
    when?: string,
    responses?: ResponsesInline,
    msg_type?: string,
    /** A hint to processes about how to interpret the element. Not validated. */
    rendering?: string,
    annotation?: Annotation,
    category?: string,
    flow?: string,
}


/**
 * Any number of action behaviors can be triggered by the same 'when' condition
 */
export interface ResponseType extends ActionType {
    /** A common condition for all of the actions. If it evalutes true, then the actions are invoked. If 'when' is not present, the actions are unconditional. */
    when?: string,
    sync?: string,
    annotation?: Annotation,
    name?: string,
}


/**
 * The use case of an element, distinguished by workflow, asset class, etc.
 */
export interface ScenarioType {
    annotation?: Annotation,
    /** Unique numeric identifier. Default is '1' is for base scenario. */
    id?: string,
    /** Unique name */
    name?: string,
}



export interface SectionType extends EntityAttribGrp {
    display_order?: number,
    fixml_file_name?: string,
    annotation?: Annotation,
    name: string,
}



export interface StateMachineType {
    /** Initial state of a state machine */
    initial: StateType,
    state: StateType[],
    annotation?: Annotation,
    name: string,
}


/**
 * A state of a state machine. If it has no transitions, then it is a final state.
 */
export interface StateType {
    transition?: TransitionType[],
    /** Operation fired when entering a state. */
    onentry?: ActionType,
    /** Operation fired when entering a state and completing when exiting or earlier. */
    activity?: ActionType,
    /** Operation fired when exiting a state. */
    onexit?: ActionType,
    annotation?: Annotation,
    name: string,
}



export interface TimerSchedule {
    /** Action to take when a timer expires */
    activity: ActionType,
    operation: string,
    interval?: string,
    /** Name of the actor that owns the timer */
    actor: string,
    /** Name of the timer */
    name: string,
}



export interface TimerType {
    name: string,
}



export interface TransitionType {
    /** Optional guard condition. The transition is allowed if the condition evaluates true. If not present, the transition is unconditional. */
    when?: string,
    /** The target state of the transition */
    target: string,
    annotation?: Annotation,
    name: string,
}



export interface TriggerType {
    /** Name of the state machine */
    state_machine: string,
    /** Name of the actor that owns the state machine */
    actor: string,
    /** Name of the transition to invoke */
    name: string,
}



export interface InterfaceAnnotation {
    documentation?: InterfaceDocumentation[],
    appinfo?: InterfaceAppinfo[],
}


/**
 * Usage specific annotation, optionally with link to an external reference or standard
 */
export interface InterfaceAppinfo {
    /** Reference documentation */
    spec_url?: string,
    /** Mixed text content of the element. */
    value?: string,
    /** Pass-through xs:any content as raw strings. */
    content?: string[],
    /** Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point). */
    extra_attributes?: string[],
    lang_id?: string,
    purpose?: string,
}



export interface BaseInterfaceType {
    /** An application layer protocol with orchestration */
    service?: ServiceType[],
    user_interface?: UserInterfaceType[],
    session_protocol?: SessionProtocolType[],
    protocol?: ProtocolType[],
    transport?: TransportProtocolType[],
    /** Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point). */
    extra_attributes?: string[],
    encoding?: EncodingType[],
    annotation?: InterfaceAnnotation,
    name: string,
}



export interface InterfaceDocumentation {
    /** Mixed text content of the element. */
    value?: string,
    /** Pass-through xs:any content as raw strings. */
    content?: string[],
    lang_id?: string,
    purpose?: string,
    content_type?: string,
}



export interface EncodingType extends ProtocolType {
}



export interface SessionsInline {
    session: SessionType[],
}



export interface InterfaceType extends BaseInterfaceType {
    sessions?: SessionsInline,
}



export interface ProtocolType {
    /** When this version becomes effective */
    activation_time?: string,
    /** When this version is no longer effective */
    deactivation_time?: string,
    layer?: string,
    /** URI of Orchestra rules of engagement */
    orchestration?: string,
    /** Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point). */
    extra_attributes?: string[],
    annotation?: InterfaceAnnotation,
    name?: string,
    version?: string,
    /** When this version was deprecated; may be replaced or removed in the future */
    deprecated?: string,
    /** Reliability can be implemented at transport, session, or application layers */
    reliability?: string,
}



export interface ServiceType extends ProtocolType {
}



export interface SessionProtocolType extends ProtocolType {
}



export interface SessionType extends BaseInterfaceType {
    role?: string,
    /** Textual encoding as specified by IETF RFC 7468 */
    security_keys?: string,
    /** When this session becomes effective */
    activation_time?: string,
    /** When this session is no longer effective */
    deactivation_time?: string,
    identifier?: IdentifierType[],
}



export interface TransportProtocolType extends ProtocolType {
    address?: string,
    message_cast?: string,
    use?: string,
    /** Pass-through xs:anyAttribute values keyed by their XML attribute name (open extension point). */
    extra_attributes?: string[],
}



export interface UserInterfaceType extends ProtocolType {
}



export interface Datatype extends EntityAttribGrp {
    mapped_datatype?: MappedDatatype[],
    /** Unique identifier of a scenario. Default is '1' for base scenario. */
    scenario_id?: string,
    base_type?: string,
    annotation?: Annotation,
    name: string,
    /** The use case of a datatype by name */
    scenario?: string,
}


/**
 * Participants and the message flows between them
 */
export interface Actors {
    actor?: ActorType[],
    flow?: FlowType[],
    annotation?: Annotation,
    base?: string,
}



export interface Categories {
    /** A business process category, a subcategory of a businessArea */
    category?: CategoryType[],
    annotation?: Annotation,
    base?: string,
}



export interface CodeSets {
    code_set?: CodeSetType[],
    annotation?: Annotation,
    base?: string,
}



export interface Components {
    component?: ComponentType[],
    annotation?: Annotation,
    base?: string,
}



export interface Concepts {
    concept?: ConceptType[],
    annotation?: Annotation,
    base?: string,
}



export interface Datatypes {
    datatype?: Datatype[],
    annotation?: Annotation,
    base?: string,
}



export interface Fields {
    field?: FieldType[],
    annotation?: Annotation,
    base?: string,
}



export interface Groups {
    group?: GroupType[],
    annotation?: Annotation,
    base?: string,
}



export interface Messages {
    message?: MessageType[],
    annotation?: Annotation,
    base?: string,
}



export interface Repository {
    metadata: DctermsElementOrRefinementContainer,
    categories?: Categories,
    sections?: Sections,
    datatypes: Datatypes,
    code_sets?: CodeSets,
    fields: Fields,
    actors?: Actors,
    components?: Components,
    groups?: Groups,
    messages: Messages,
    concepts?: Concepts,
    scenarios?: Scenarios,
    guid?: string,
    /** Reference documentation */
    spec_url?: string,
    /** An associated namespace as URI */
    namespace?: string,
    /** The syntax of 'expressionType' */
    expression_language?: string,
    annotation?: Annotation,
    /** Stable name that does not change with minor version updates */
    name: string,
    version: string,
}


/**
 * The default scenario is id='1' name='base'.
 */
export interface Scenarios {
    scenario?: ScenarioType[],
    annotation?: Annotation,
    base?: string,
}



export interface Sections {
    /** A large-grained business process category */
    section?: SectionType[],
    annotation?: Annotation,
    base?: string,
}


/**
 * This represents the current state of service and session configurations. Changes to configuration can represented with patch operations. See IETF RFC 5261
 */
export interface Interfaces {
    metadata: DctermsElementOrRefinementContainer,
    interface?: InterfaceType[],
}



