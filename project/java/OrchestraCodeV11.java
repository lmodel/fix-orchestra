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
  One permitted value in a code set, with its name and what goes on the wire.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraCodeV11  {

  private OrchestraAnnotationV11 fixrAnnotation;
  private String fixrValue;
  private Integer fixrSort;
  private String fixrGroup;
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