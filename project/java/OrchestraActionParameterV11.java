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
  One input to an action: a field, a component or a group, defined in place or named by reference. It holds exactly one of these.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraActionParameterV11  {

  private OrchestraFieldV11 fixrField;
  private OrchestraFieldRefV11 fixrFieldRef;
  private OrchestraComponentV11 fixrComponent;
  private OrchestraComponentRefV11 fixrComponentRef;
  private OrchestraGroupV11 fixrGroup;
  private OrchestraGroupRefV11 fixrGroupRef;


}