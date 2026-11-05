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
  A business process grouping within a section, such as order handling or market data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraCategoryV10  {

  private OrchestraAnnotationV10 fixrAnnotation;
  private String fixrName;
  private String fixrFixmlFileName;
  private String fixrComponentType;
  private String fixrSection;
  private String fixrIncludeFile;
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