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
  A named timer that an actor owns.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraTimerV11  {

  private String fixrName;


}