package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A reference to a scenario by its key identifiers. There are no defaults as scenario references are optional.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ScenarioRefGrp  {

  private String scenarioRefId;
  private String scenarioRef;


}