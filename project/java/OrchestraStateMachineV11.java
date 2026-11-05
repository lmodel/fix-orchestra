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
  A named set of states that an actor moves through, from an initial state.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraStateMachineV11  {

  private OrchestraStateV11 fixrInitial;
  private List<OrchestraStateV11> fixrState;
  private OrchestraAnnotationV11 fixrAnnotation;
  private String fixrName;


}