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
  A step that fires a named transition of an actor's state machine.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraTriggerV11  {

  private String fixrStateMachine;
  private String fixrActor;
  private String fixrName;


}