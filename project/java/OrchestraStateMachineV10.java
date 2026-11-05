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
public class OrchestraStateMachineV10  {

  private OrchestraStateV10 fixrInitial;
  private List<OrchestraStateV10> fixrState;
  private OrchestraAnnotationV10 fixrAnnotation;
  private String fixrName;


}