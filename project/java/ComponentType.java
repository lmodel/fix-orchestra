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
public class ComponentType  {

  private List<ComponentRefType> componentRef;
  private List<GroupRefType> groupRef;
  private List<FieldRefType> fieldRef;
  private String rendering;
  private String which;
  private Annotation annotation;
  private String category;
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
  private String abbrName;
  private String scenarioId;
  private String id;
  private String name;
  private String scenario;
  private String scenarioRefId;
  private String scenarioRef;


}