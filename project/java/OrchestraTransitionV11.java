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
  A move from one state to a named target state, with the condition that allows it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraTransitionV11  {

  private String fixrWhen;
  private OrchestraAnnotationV11 fixrAnnotation;
  private String fixrName;
  private String fixrTarget;


}