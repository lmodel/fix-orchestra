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
  Where a message or block includes a field, by its tag number, with its presence, value limits and any rules.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraFieldRefV10  {

  private List<OrchestraFieldRuleV10> fixrRule;
  private String fixrAssign;
  private OrchestraAnnotationV10 fixrAnnotation;
  private Integer fixrLengthId;
  private String fixrInstanceName;
  private int fixrId;
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
  private String fixrMinInclusive;
  private String fixrMaxInclusive;
  private Integer fixrImplLength;
  private Integer fixrImplMinLength;
  private Integer fixrImplMaxLength;
  private String fixrPresence;
  private String fixrEncoding;
  private String fixrValue;
  private String fixrRendering;


}