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
  A kind of party in an exchange, such as a buy-side firm or a venue, with the state it keeps: its variables, state machines and timers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraActorV11  {

  private List<OrchestraActorMemberV11> fixrMembers;
  private OrchestraAnnotationV11 fixrAnnotation;
  private String fixrName;


}