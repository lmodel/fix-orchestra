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
  Where a message or block includes a component, by its number, with its presence and any rules that make it conditional.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraComponentRefV11  {

  private List<OrchestraBlockAssignmentV11> fixrBlockAssignment;
  private List<OrchestraComponentRuleV11> fixrRule;
  private OrchestraEncodingsV11 fixrEncodings;
  private OrchestraAnnotationV11 fixrAnnotation;
  private String fixrPresence;
  private String fixrInstanceName;
  private int fixrId;
  private String fixrName;
  private String fixrScenario;
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