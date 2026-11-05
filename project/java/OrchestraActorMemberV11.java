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
  One thing an actor keeps: a variable given as a field, component or group, a state machine or a timer. It holds exactly one of these.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraActorMemberV11  {

  private OrchestraFieldV11 fixrField;
  private OrchestraFieldRefV11 fixrFieldRef;
  private OrchestraComponentV11 fixrComponent;
  private OrchestraComponentRefV11 fixrComponentRef;
  private OrchestraGroupV11 fixrGroup;
  private OrchestraGroupRefV11 fixrGroupRef;
  private OrchestraStateMachineV11 fixrStates;
  private OrchestraTimerV11 fixrTimer;


}