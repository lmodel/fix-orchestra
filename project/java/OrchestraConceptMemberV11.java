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
  One element a concept ties together: a field, component, group or message, by reference. It holds exactly one of these.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraConceptMemberV11  {

  private OrchestraComponentRefV11 fixrComponentRef;
  private OrchestraGroupRefV11 fixrGroupRef;
  private OrchestraFieldRefV11 fixrFieldRef;
  private OrchestraMessageRefV11 fixrMessageRef;


}