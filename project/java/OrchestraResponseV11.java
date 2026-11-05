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
  What happens when a message arrives, under an optional condition: messages sent, values set, transitions fired and timers scheduled.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraResponseV11 extends OrchestraActionV11 {

  private String fixrWhen;
  private OrchestraAnnotationV11 fixrAnnotation;
  private String fixrName;
  private String fixrSync;


}