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
  A named list of the values a field may take, each with a name of its own, over one underlying datatype.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraCodeSetV11  {

  private List<OrchestraCodeV11> fixrCode;
  private OrchestraAnnotationV11 fixrAnnotation;
  private OrchestraEncodingsV11 fixrEncodings;
  private String fixrType;
  private String fixrDefault;
  private URI fixrSpecUrl;
  private String fixrUnionDataType;
  private int fixrId;
  private String fixrName;
  private String fixrAbbrName;
  private String fixrScenario;
  private Integer fixrScenarioRefId;
  private String fixrScenarioRef;
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