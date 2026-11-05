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
  The responses a message can cause, tried one after another as given.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraResponsesV10  {

  private List<OrchestraResponseV10> fixrResponse;


}