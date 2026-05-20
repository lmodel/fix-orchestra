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
  The use case of an element, distinguished by workflow, asset class, etc.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ScenarioType  {

  private Annotation annotation;
  private String id;
  private String name;


}