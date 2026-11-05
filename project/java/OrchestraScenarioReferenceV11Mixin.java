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
  A pointer from an element to the scenario it belongs to, by number and, if wanted, name.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraScenarioReferenceV11Mixin  {

  private Integer fixrScenarioRefId;
  private String fixrScenarioRef;


}