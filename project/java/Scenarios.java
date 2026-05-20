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
  The default scenario is id='1' name='base'.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Scenarios  {

  private List<ScenarioType> scenario;
  private Annotation annotation;
  private String base;


}