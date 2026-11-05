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
  One item of an ordered structure, a component, a group or a field, by reference. It holds exactly one of these.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraStructureMemberV11  {

  private OrchestraComponentRefV11 fixrComponentRef;
  private OrchestraGroupRefV11 fixrGroupRef;
  private OrchestraFieldRefV11 fixrFieldRef;


}