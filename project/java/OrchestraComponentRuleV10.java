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
  A condition that changes a component's presence, such as making it required.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraComponentRuleV10  {

  private String fixrWhen;
  private String fixrName;
  private String fixrPresence;


}