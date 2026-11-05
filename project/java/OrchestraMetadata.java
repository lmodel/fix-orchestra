package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The Dublin Core description at the head of an Orchestra file. Each key holds the values of one Dublin Core element or term.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraMetadata  {

  private List<String> dcTitle;
  private List<String> dcCreator;
  private List<String> dcSubject;
  private List<String> dcDescription;
  private List<String> dcPublisher;
  private List<String> dcContributor;
  private List<String> dcDate;
  private List<String> dcType;
  private List<String> dcFormat;
  private List<String> dcIdentifier;
  private List<String> dcSource;
  private List<String> dcLanguage;
  private List<String> dcRelation;
  private List<String> dcCoverage;
  private List<String> dcRights;
  private List<String> dctermsTitle;
  private List<String> dctermsCreator;
  private List<String> dctermsSubject;
  private List<String> dctermsDescription;
  private List<String> dctermsPublisher;
  private List<String> dctermsContributor;
  private List<String> dctermsDate;
  private List<String> dctermsType;
  private List<String> dctermsFormat;
  private List<String> dctermsIdentifier;
  private List<String> dctermsSource;
  private List<String> dctermsLanguage;
  private List<String> dctermsRelation;
  private List<String> dctermsCoverage;
  private List<String> dctermsRights;
  private List<String> dctermsAlternative;
  private List<String> dctermsTableOfContents;
  private List<String> dctermsAbstract;
  private List<String> dctermsCreated;
  private List<String> dctermsValid;
  private List<String> dctermsAvailable;
  private List<String> dctermsIssued;
  private List<String> dctermsModified;
  private List<String> dctermsDateAccepted;
  private List<String> dctermsDateCopyrighted;
  private List<String> dctermsDateSubmitted;
  private List<String> dctermsExtent;
  private List<String> dctermsMedium;
  private List<String> dctermsIsVersionOf;
  private List<String> dctermsHasVersion;
  private List<String> dctermsIsReplacedBy;
  private List<String> dctermsReplaces;
  private List<String> dctermsIsRequiredBy;
  private List<String> dctermsRequires;
  private List<String> dctermsIsPartOf;
  private List<String> dctermsHasPart;
  private List<String> dctermsIsReferencedBy;
  private List<String> dctermsReferences;
  private List<String> dctermsIsFormatOf;
  private List<String> dctermsHasFormat;
  private List<String> dctermsConformsTo;
  private List<String> dctermsSpatial;
  private List<String> dctermsTemporal;
  private List<String> dctermsAudience;
  private List<String> dctermsAccrualMethod;
  private List<String> dctermsAccrualPeriodicity;
  private List<String> dctermsAccrualPolicy;
  private List<String> dctermsInstructionalMethod;
  private List<String> dctermsProvenance;
  private List<String> dctermsRightsHolder;
  private List<String> dctermsMediator;
  private List<String> dctermsEducationLevel;
  private List<String> dctermsAccessRights;
  private List<String> dctermsLicense;
  private List<String> dctermsBibliographicCitation;


}