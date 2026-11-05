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
  A named block of fields, components and groups that messages and other blocks include by reference.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraComponentV11  {

  private List<OrchestraStructureMemberV11> fixrMembers;
  private OrchestraEncodingsV11 fixrEncodings;
  private OrchestraAnnotationV11 fixrAnnotation;
  private String fixrCategory;
  private String fixrRendering;
  private String fixrWhich;
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
  private int fixrId;
  private String fixrName;
  private String fixrAbbrName;
  private String fixrScenario;
  private Integer fixrScenarioRefId;
  private String fixrScenarioRef;


}