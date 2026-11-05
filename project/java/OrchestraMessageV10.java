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
  A FIX message: its type code, the fields, components and groups it carries in order, and the responses it can cause.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraMessageV10  {

  private OrchestraMessageStructureV10 fixrStructure;
  private OrchestraResponsesV10 fixrResponses;
  private OrchestraAnnotationV10 fixrAnnotation;
  private String fixrMsgType;
  private String fixrCategory;
  private String fixrFlow;
  private int fixrId;
  private String fixrName;
  private String fixrAbbrName;
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