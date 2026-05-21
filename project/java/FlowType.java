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
  A stream of messages in one direction
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FlowType  {

  private String source;
  private String destination;
  private Annotation annotation;
  private String name;
  private String reliability;


}