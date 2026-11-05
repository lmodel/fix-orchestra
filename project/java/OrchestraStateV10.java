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
  One of a state machine's states, with the transitions out of it and what happens on entry, while active and on exit.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraStateV10  {

  private List<OrchestraTransitionV10> fixrTransition;
  private OrchestraActionV10 fixrOnentry;
  private OrchestraActionV10 fixrActivity;
  private OrchestraActionV10 fixrOnexit;
  private OrchestraAnnotationV10 fixrAnnotation;
  private String fixrName;


}