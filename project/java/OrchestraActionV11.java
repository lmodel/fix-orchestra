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
  Things that happen together, such as when a response fires or a state is entered: messages sent, values set, transitions fired and timers scheduled, with their inputs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraActionV11  {

  private List<OrchestraActionParameterV11> fixrParameters;
  private List<OrchestraActionStepV11> fixrActions;


}