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
  A named service offering and the sessions it carries, with the protocols on each layer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraInterfaceV11 extends OrchestraBaseInterfaceV11 {

  private OrchestraSessionsV11 fixiSessions;


}