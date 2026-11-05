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
  The sessions an interface carries.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraSessionsV11  {

  private List<OrchestraSessionV11> fixiSession;


}