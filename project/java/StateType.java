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
  A state of a state machine. If it has no transitions, then it is a final state.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StateType  {

  private List<TransitionType> transition;
  private ActionType onentry;
  private ActionType activity;
  private ActionType onexit;
  private Annotation annotation;
  private String name;


}