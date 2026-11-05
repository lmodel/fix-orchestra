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
  A FIX datatype, such as Price or UTCTimestamp, with how it maps to the types of other standards.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraDatatypeV10  {

  private List<OrchestraMappedDatatypeV10> fixrMappedDatatype;
  private OrchestraAnnotationV10 fixrAnnotation;
  private String fixrName;
  private String fixrBaseType;
  private String fixrAdded;
  private Integer fixrAddedEp;
  private String fixrChangeType;
  private String fixrDeprecated;
  private Integer fixrDeprecatedEp;
  private String fixrIssue;
  private String fixrLastModified;
  private String fixrReplaced;
  private Integer fixrReplacedEp;
  private Integer fixrReplacedByField;
  private String fixrSupported;
  private String fixrUpdated;
  private Integer fixrUpdatedEp;


}