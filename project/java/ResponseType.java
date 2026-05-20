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
  Any number of action behaviors can be triggered by the same 'when' condition
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResponseType extends ActionType {

  private String when;
  private String sync;
  private Annotation annotation;
  private String name;


}