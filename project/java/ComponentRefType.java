package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

@Data
@EqualsAndHashCode(callSuper=false)
public class ComponentRefType  {

  private List<BlockAssignmentType> blockAssignment;
  private String presence;
  private List<ComponentRuleType> rule;
  private Annotation annotation;
  private String instanceName;
  private String scenarioId;
  private String id;
  private String name;
  private String scenario;
  private String added;
  private String addedEp;
  private String changeType;
  private String deprecatedEp;
  private String issue;
  private String lastModified;
  private String replaced;
  private String replacedEp;
  private String replacedByField;
  private String supported;
  private String updated;
  private String updatedEp;
  private String deprecated;


}