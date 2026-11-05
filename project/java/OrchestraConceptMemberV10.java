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
public class OrchestraConceptMemberV10  {

  private OrchestraComponentRefV10 fixrComponentRef;
  private OrchestraGroupRefV10 fixrGroupRef;
  private OrchestraFieldRefV10 fixrFieldRef;
  private OrchestraMessageRefV10 fixrMessageRef;


}