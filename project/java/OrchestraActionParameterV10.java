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
public class OrchestraActionParameterV10  {

  private OrchestraFieldV10 fixrField;
  private OrchestraFieldRefV10 fixrFieldRef;
  private OrchestraComponentV10 fixrComponent;
  private OrchestraComponentRefV10 fixrComponentRef;
  private OrchestraGroupV10 fixrGroup;
  private OrchestraGroupRefV10 fixrGroupRef;


}