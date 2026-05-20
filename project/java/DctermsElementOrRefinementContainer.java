package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  This is included as a convenience for schema authors who need to define a root or container element for all of the DC elements and element refinements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DctermsElementOrRefinementContainer  {

  private String title;
  private String creator;
  private String subject;
  private String description;
  private String publisher;
  private String contributor;
  private String date;
  private String format;
  private String source;
  private String language;
  private String relation;
  private String coverage;
  private String rights;
  private String alternative;
  private String tableOfContents;
  private String abstract_;
  private String created;
  private String valid;
  private String available;
  private String issued;
  private String modified;
  private String dateAccepted;
  private String dateCopyrighted;
  private String dateSubmitted;
  private String extent;
  private String medium;
  private String isVersionOf;
  private String hasVersion;
  private String isReplacedBy;
  private String replaces;
  private String isRequiredBy;
  private String requires;
  private String isPartOf;
  private String hasPart;
  private String isReferencedBy;
  private String references;
  private String isFormatOf;
  private String hasFormat;
  private String conformsTo;
  private String spatial;
  private String temporal;
  private String audience;
  private String accrualMethod;
  private String accrualPeriodicity;
  private String accrualPolicy;
  private String instructionalMethod;
  private String provenance;
  private String rightsHolder;
  private String mediator;
  private String educationLevel;
  private String accessRights;
  private String license;
  private String bibliographicCitation;
  private String type;
  private String identifier;


}